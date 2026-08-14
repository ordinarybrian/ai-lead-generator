#!/usr/bin/env python3
"""Sync leads/lead-index.csv into a ClickUp List, one task per organization.

Setup
-----
1. In ClickUp, create a List for this project. For each CSV column you want tracked
   as its own field (beyond the ones handled natively below), add a matching Custom
   Field to the List with the *same name* (case/spacing-insensitive, e.g. a
   "linkedin_url" column matches a "LinkedIn URL" field). Columns with no matching
   field are reported as unmapped and skipped -- nothing is dropped silently.
2. For `outreach_status` to land as the task's native Status (so you get a working
   board view), add matching Statuses to the List (e.g. "Researching", "Ready for
   Outreach", "Initial Email Sent", ...). Values that don't match an existing List
   status are left as a plain custom field instead, if one exists, else skipped.
3. Set CLICKUP_API_TOKEN and CLICKUP_LIST_ID, either as real env vars or in a
   `.env` file at the repo root (already gitignored):
       CLICKUP_API_TOKEN=pk_...
       CLICKUP_LIST_ID=901234567

Usage
-----
    python3 scripts/clickup_sync.py --dry-run   # preview, no API calls that write
    python3 scripts/clickup_sync.py             # create/update tasks for real

Matching existing tasks to CSV rows is done by exact task-name == organization-name
match (fetched fresh from the List each run) -- there is no local id-mapping file to
keep in sync or go stale. Re-running is safe: it converges the List to match the CSV.

This project's CSV schema is intentionally adaptable (see leads/README.md), so this
script does not hardcode a fixed column list -- it maps whatever columns are present.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "leads" / "lead-index.csv"
API_BASE = "https://api.clickup.com/api/v2"

# organization -> task name; next_action_date -> native due date; outreach_status ->
# native status (falls back to a custom field, see resolve_status). Handled specially,
# never treated as a generic custom field.
NATIVE_COLUMNS = {"organization", "next_action_date", "outreach_status"}

PRIORITY_MAP = {"A+": 1, "A": 1, "B": 2, "C": 3, "D": 4}
TRUE_VALUES = {"true", "yes", "1"}


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def api_request(token: str, method: str, path: str, body: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", token)
    req.add_header("Content-Type", "application/json")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 4:
                time.sleep(int(e.headers.get("Retry-After", "5")))
                continue
            raise RuntimeError(f"{method} {path} failed: {e.code} {e.read().decode()}") from e
    raise RuntimeError(f"{method} {path} failed after retries")


def get_list_meta(token: str, list_id: str) -> dict:
    return api_request(token, "GET", f"/list/{list_id}")


def get_custom_fields(token: str, list_id: str) -> list[dict]:
    return api_request(token, "GET", f"/list/{list_id}/field")["fields"]


def get_existing_tasks(token: str, list_id: str) -> dict[str, str]:
    tasks_by_name: dict[str, str] = {}
    page = 0
    while True:
        resp = api_request(
            token, "GET", f"/list/{list_id}/task?include_closed=true&page={page}"
        )
        for task in resp.get("tasks", []):
            if task["name"] in tasks_by_name:
                print(f"warning: duplicate task name in ClickUp list: {task['name']!r} "
                      f"(keeping {tasks_by_name[task['name']]}, ignoring {task['id']})",
                      file=sys.stderr)
                continue
            tasks_by_name[task["name"]] = task["id"]
        if resp.get("last_page", True):
            break
        page += 1
    return tasks_by_name


def normalize(name: str) -> str:
    return name.strip().lower().replace("_", " ").replace("-", " ")


def to_epoch_ms(date_str: str) -> int | None:
    date_str = date_str.strip()
    if not date_str:
        return None
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def to_e164(value: str, field_name: str) -> str | None:
    """ClickUp's phone field rejects anything without a leading '+<country code>'.
    Assumes unmarked 10/11-digit numbers are US/Canada (+1)."""
    digits = re.sub(r"\D", "", value)
    if value.startswith("+") and digits:
        return f"+{digits}"
    if len(digits) == 10:
        return f"+1{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    print(f"warning: {value!r} in field {field_name!r} doesn't look like a valid "
          f"phone number; skipping", file=sys.stderr)
    return None


def resolve_status(value: str, list_statuses: list[dict]) -> str | None:
    value = value.strip()
    if not value:
        return None
    for status in list_statuses:
        if status["status"].lower() == value.lower():
            return status["status"]
    return None


def resolve_custom_field_value(field: dict, raw_value: str):
    value = raw_value.strip()
    if not value:
        return None
    field_type = field["type"]
    if field_type in ("drop_down", "labels"):
        options = field.get("type_config", {}).get("options", [])
        for opt in options:
            if opt["name"].lower() == value.lower():
                return opt["id"] if field_type == "drop_down" else [opt["id"]]
        print(f"warning: {value!r} is not a defined option on custom field "
              f"{field['name']!r}; skipping", file=sys.stderr)
        return None
    if field_type == "checkbox":
        return value.lower() in TRUE_VALUES
    if field_type == "date":
        return to_epoch_ms(value)
    if field_type == "number":
        try:
            return float(value) if "." in value else int(value)
        except ValueError:
            return None
    if field_type == "phone":
        return to_e164(value, field["name"])
    return value  # text, short_text, url, email, ...


def build_task_payload(row: dict, custom_fields: list[dict], list_statuses: list[dict],
                        description_column: str | None) -> tuple[dict, list[str]]:
    payload: dict = {}
    unmapped: list[str] = []

    if description_column and row.get(description_column, "").strip():
        payload["description"] = row[description_column]

    if "next_action_date" in row:
        due = to_epoch_ms(row["next_action_date"])
        if due is not None:
            payload["due_date"] = due
            payload["due_date_time"] = False

    if "outreach_status" in row:
        status = resolve_status(row["outreach_status"], list_statuses)
        if status:
            payload["status"] = status

    if "priority" in row:
        priority = PRIORITY_MAP.get(row["priority"].strip().upper())
        if priority:
            payload["priority"] = priority

    fields_by_name = {normalize(f["name"]): f for f in custom_fields}
    resolved_custom_fields = []
    for column, raw_value in row.items():
        if column in NATIVE_COLUMNS or column == description_column or column == "priority":
            continue
        field = fields_by_name.get(normalize(column))
        if not field:
            if raw_value.strip():
                unmapped.append(column)
            continue
        value = resolve_custom_field_value(field, raw_value)
        if value is not None:
            resolved_custom_fields.append({"id": field["id"], "value": value})
    if resolved_custom_fields:
        payload["custom_fields"] = resolved_custom_fields

    return payload, unmapped


def sync(csv_path: Path, token: str, list_id: str, dry_run: bool) -> None:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    list_meta = get_list_meta(token, list_id)
    list_statuses = list_meta.get("statuses", [])
    custom_fields = get_custom_fields(token, list_id)
    existing_tasks = get_existing_tasks(token, list_id)

    all_unmapped: set[str] = set()
    description_column = "notes" if rows and "notes" in rows[0] else None

    for row in rows:
        org = row.get("organization", "").strip()
        if not org:
            continue
        payload, unmapped = build_task_payload(row, custom_fields, list_statuses,
                                                description_column)
        all_unmapped.update(unmapped)

        task_id = existing_tasks.get(org)
        if task_id:
            action = f"UPDATE {org} ({task_id})"
            method, path = "PUT", f"/task/{task_id}"
        else:
            action = f"CREATE {org}"
            method, path = "POST", f"/list/{list_id}/task"
            payload = {"name": org, **payload}

        if dry_run:
            print(f"[dry-run] {action}: {json.dumps(payload, indent=2)}")
            continue

        api_request(token, method, path, payload)
        print(action)

    if all_unmapped:
        print("\nColumns with no matching ClickUp custom field (data not synced):",
              file=sys.stderr)
        for col in sorted(all_unmapped):
            print(f"  - {col}", file=sys.stderr)


def main() -> None:
    load_dotenv(REPO_ROOT / ".env")

    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--list-id", default=os.environ.get("CLICKUP_LIST_ID"))
    parser.add_argument("--dry-run", action="store_true",
                         help="Print planned create/update calls without writing to ClickUp")
    args = parser.parse_args()

    token = os.environ.get("CLICKUP_API_TOKEN")
    if not token:
        parser.error("CLICKUP_API_TOKEN is not set (env var or .env file)")
    if not args.list_id:
        parser.error("--list-id or CLICKUP_LIST_ID is required")
    if not args.csv.exists():
        parser.error(f"CSV not found: {args.csv}")

    sync(args.csv, token, args.list_id, args.dry_run)


if __name__ == "__main__":
    main()
