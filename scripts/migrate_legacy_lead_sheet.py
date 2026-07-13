#!/usr/bin/env python3
"""One-time, loss-conscious migration of the legacy lead Sheet schema."""

from __future__ import annotations

import csv
import os
from datetime import datetime
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "leads" / "lead-index.csv"
BACKUPS = ROOT / "leads" / "backups"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
NEW_HEADER = [
    "organization", "website", "organization_type", "market_or_audience",
    "primary_contact", "contact_title", "linkedin_url", "email", "email_status",
    "backup_contact", "strategic_story", "priority", "outreach_status",
    "last_contact_date", "next_action", "notes",
]
OLD_HEADER = [
    "Company", "Industry", "website", "contact", "contact phone", "contact email",
    "LinkedIn", "Priority (A/B/C)", "Contacted", "Follow-up 1", "Follow-up 2",
    "Status", "Notes",
]


def combine_notes(row: dict[str, str]) -> str:
    parts: list[str] = []
    if row.get("Notes", "").strip():
        parts.append(row["Notes"].strip())
    for label, column in (
        ("Contact phone", "contact phone"),
        ("Follow-up 1", "Follow-up 1"),
        ("Follow-up 2", "Follow-up 2"),
    ):
        value = row.get(column, "").strip()
        if value:
            parts.append(f"{label}: {value}")
    return " | ".join(parts)


def migrate(values: list[list[str]]) -> list[list[str]]:
    if not values or values[0] != OLD_HEADER:
        raise RuntimeError("Remote header does not match the reviewed legacy schema.")
    migrated = [NEW_HEADER]
    for raw in values[1:]:
        padded = (raw + [""] * len(OLD_HEADER))[: len(OLD_HEADER)]
        row = dict(zip(OLD_HEADER, padded))
        # Skip only completely empty spreadsheet rows.
        if not any(cell.strip() for cell in padded):
            continue
        email = row["contact email"].strip()
        migrated.append([
            row["Company"].strip(),
            row["website"].strip(),
            row["Industry"].strip(),
            "",
            row["contact"].strip(),
            "",
            row["LinkedIn"].strip(),
            email,
            "unverified" if email else "",
            "",
            "",
            row["Priority (A/B/C)"].strip(),
            row["Status"].strip(),
            row["Contacted"].strip(),
            "",
            combine_notes(row),
        ])
    return migrated


def write_csv(path: Path, rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle, lineterminator="\n").writerows(rows)


def main() -> None:
    spreadsheet_id = os.environ["LEAD_INDEX_SPREADSHEET_ID"]
    tab_name = os.environ.get("LEAD_INDEX_WORKSHEET", "Sheet1")
    credentials = Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"], scopes=SCOPES
    )
    sheet = gspread.authorize(credentials).open_by_key(spreadsheet_id).worksheet(tab_name)
    remote = sheet.get_all_values()
    migrated = migrate(remote)

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    remote_backup = BACKUPS / f"lead-index-google-sheet-before-migration-{stamp}.csv"
    local_backup = BACKUPS / f"lead-index-local-before-migration-{stamp}.csv"
    write_csv(remote_backup, remote)
    write_csv(local_backup, list(csv.reader(TARGET.open(newline="", encoding="utf-8-sig"))))
    write_csv(TARGET, migrated)

    sheet.clear()
    sheet.update(migrated, "A1", value_input_option="RAW")
    sheet.freeze(rows=1)
    print(f"Migrated {len(migrated) - 1} non-empty lead rows.")
    print(f"Remote backup: {remote_backup.relative_to(ROOT)}")
    print(f"Local backup: {local_backup.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
