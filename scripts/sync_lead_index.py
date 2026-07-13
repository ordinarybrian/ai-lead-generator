#!/usr/bin/env python3
"""Conflict-safe two-way sync between lead-index.csv and Google Sheets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "leads" / "lead-index.csv"
STATE_PATH = ROOT / ".sync" / "lead-index-state.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def normalize(rows: list[list[str]]) -> list[list[str]]:
    """Match CSV semantics when Sheets omits trailing empty cells."""
    if not rows:
        return []
    width = len(rows[0])
    return [([str(cell) for cell in row] + [""] * width)[:width] for row in rows]


def table_hash(rows: list[list[str]]) -> str:
    normalized = normalize(rows)
    return hashlib.sha256(
        json.dumps(normalized, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()


def read_csv() -> list[list[str]]:
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.reader(handle))


def write_csv(rows: list[list[str]]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = CSV_PATH.with_suffix(".csv.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle, lineterminator="\n").writerows(normalize(rows))
    temporary.replace(CSV_PATH)


def load_state() -> dict[str, str]:
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(content_hash: str) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps({"synced_hash": content_hash}, indent=2) + "\n", encoding="utf-8"
    )


def worksheet():
    spreadsheet_id = os.environ.get("LEAD_INDEX_SPREADSHEET_ID")
    credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    tab_name = os.environ.get("LEAD_INDEX_WORKSHEET", "Leads")
    if not spreadsheet_id or not credentials_path:
        raise RuntimeError(
            "Set LEAD_INDEX_SPREADSHEET_ID and GOOGLE_APPLICATION_CREDENTIALS."
        )
    credentials = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
    book = gspread.authorize(credentials).open_by_key(spreadsheet_id)
    try:
        return book.worksheet(tab_name)
    except gspread.WorksheetNotFound:
        return book.add_worksheet(title=tab_name, rows=1000, cols=30)


def push(sheet, rows: list[list[str]]) -> None:
    sheet.clear()
    if rows:
        sheet.update(rows, "A1", value_input_option="RAW")
        sheet.freeze(rows=1)


def sync(prefer: str | None = None) -> str:
    local = read_csv()
    sheet = worksheet()
    remote = sheet.get_all_values()
    state = load_state().get("synced_hash")
    local_hash, remote_hash = table_hash(local), table_hash(remote)

    if local_hash == remote_hash:
        save_state(local_hash)
        return "already in sync"

    if prefer == "local":
        push(sheet, local)
        save_state(local_hash)
        return "pushed local CSV (forced)"
    if prefer == "sheet":
        if not remote:
            raise RuntimeError("Cannot replace the CSV with an empty Sheet.")
        write_csv(remote)
        save_state(remote_hash)
        return "pulled Google Sheet (forced)"

    if state:
        local_changed = local_hash != state
        remote_changed = remote_hash != state
        if local_changed and not remote_changed:
            push(sheet, local)
            save_state(local_hash)
            return "pushed local CSV"
        if remote_changed and not local_changed:
            if not remote:
                raise RuntimeError("Google Sheet is empty; refusing to erase the CSV.")
            write_csv(remote)
            save_state(remote_hash)
            return "pulled Google Sheet"
        raise RuntimeError(
            "Sync conflict: both files changed. Re-run with --prefer local or --prefer sheet."
        )

    # Safe first-run behavior: an empty/new Sheet receives the CSV; a populated
    # Sheet replaces a header-only CSV. Any other mismatch needs a human choice.
    if not remote:
        push(sheet, local)
        save_state(local_hash)
        return "initialized Google Sheet from local CSV"
    if len(local) == 1 and len(remote) > 1 and local[0] == remote[0]:
        write_csv(remote)
        save_state(remote_hash)
        return "initialized local CSV from Google Sheet"
    raise RuntimeError(
        "First-sync conflict: both sides contain different data. "
        "Re-run with --prefer local or --prefer sheet."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="sync repeatedly")
    parser.add_argument("--interval", type=int, default=60, help="watch interval in seconds")
    parser.add_argument("--prefer", choices=("local", "sheet"))
    args = parser.parse_args()
    while True:
        try:
            print(f"lead-index: {sync(args.prefer)}", flush=True)
        except Exception as exc:
            print(f"lead-index sync error: {exc}", file=sys.stderr, flush=True)
            if not args.watch:
                return 1
        if not args.watch:
            return 0
        args.prefer = None
        time.sleep(max(args.interval, 10))


if __name__ == "__main__":
    raise SystemExit(main())
