#!/usr/bin/env python3
"""Sync project/leads/lead-index.csv into a ClickUp List, one task per organization.

Setup
-----
1. In ClickUp, create a List for this project. For each CSV column you want tracked
   as its own field (beyond the ones handled natively below), add a matching Custom
   Field to the List with the *same name* (case/spacing-insensitive, e.g. a
   "linkedin_url" column matches a "LinkedIn URL" field). Columns with no matching
   field are reported as unmapped and skipped -- nothing is dropped silently.
2. For `outreach_status` to land as the task's native Status (so you get a working
   board view), add matching Statuses to the List (e.g. "Researching", "Ready for
   Outreach", "Initial Email Sent", ...) -- exact text match required (case-insensitive).
   A List that only has ClickUp's generic defaults ("to do", "in progress", ...) will
   never match any real pipeline stage; every task silently keeps the default status
   instead. Non-matching values are reported to stderr, same as unmapped columns.
3. Set CLICKUP_API_TOKEN and CLICKUP_LIST_ID, either as real env vars or in a
   `.env` file at the repo root (already gitignored):
       CLICKUP_API_TOKEN=pk_...
       CLICKUP_LIST_ID=901234567

Usage
-----
    python3 scripts/clickup_sync.py --dry-run   # preview, no API calls that write
    python3 scripts/clickup_sync.py             # create/update tasks for real
    python3 scripts/clickup_sync.py --pull --dry-run   # preview pulling ClickUp -> CSV
    python3 scripts/clickup_sync.py --pull             # write ClickUp changes into the CSV
    python3 scripts/clickup_sync.py --native-only       # push only status/priority/due
                                                          # date/description -- skips all
                                                          # per-field Custom Field API
                                                          # calls, which count against
                                                          # ClickUp's plan-limited,
                                                          # non-resetting Custom Field
                                                          # "uses" quota (Free plan: 60
                                                          # total, ever -- see
                                                          # https://help.clickup.com/hc/en-us/articles/10993484102167).
                                                          # Once that quota is exhausted,
                                                          # use --native-only for routine
                                                          # updates and reserve a full
                                                          # sync for after a plan upgrade.

Matching existing tasks to CSV rows is done by exact task-name == organization-name
match (fetched fresh from the List each run) -- there is no local id-mapping file to
keep in sync or go stale. Re-running is safe: it converges the List to match the CSV.

--pull reverses the direction: it reads each matched task's native fields and custom
fields and writes them back into the CSV row, for cases like dragging a task to a new
status on ClickUp's board view. It only overwrites a cell when ClickUp actually holds a
non-blank value that differs from the CSV -- an unset ClickUp field never blanks out
existing CSV data. Note `priority` is lossy in this direction: ClickUp has no "A+" tier
distinct from "A", so both collapse to `A` on pull.

This project's CSV schema is intentionally adaptable (see project/leads/README.md), so
this script does not hardcode a fixed column list -- it maps whatever columns are
present.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "project" / "leads" / "lead-index.csv"
API_BASE = "https://api.clickup.com/api/v2"

# organization -> task name; next_action_date -> native due date; outreach_status ->
# native status (falls back to a custom field, see resolve_status). Handled specially,
# never treated as a generic custom field.
NATIVE_COLUMNS = {"organization", "next_action_date", "outreach_status"}

PRIORITY_MAP = {"A+": 1, "A": 1, "B": 2, "C": 3, "D": 4}
REVERSE_PRIORITY_MAP = {1: "A", 2: "B", 3: "C", 4: "D"}
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


def get_task(token: str, task_id: str) -> dict:
    return api_request(token, "GET", f"/task/{task_id}")


def get_workspace_timezone(token: str) -> ZoneInfo:
    # ClickUp normalizes due_date_time=false dates to 4am in the *workspace's* local
    # timezone -- encoding as UTC midnight lands on the wrong side of that boundary for
    # any timezone behind UTC, silently shifting the stored date back a day. Local noon
    # keeps the encoded instant safely inside the intended calendar day.
    name = api_request(token, "GET", "/user").get("user", {}).get("timezone")
    try:
        return ZoneInfo(name) if name else ZoneInfo("UTC")
    except Exception:
        return ZoneInfo("UTC")


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


def to_epoch_ms(date_str: str, tz: ZoneInfo) -> int | None:
    date_str = date_str.strip()
    if not date_str:
        return None
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=12, tzinfo=tz)
    return int(dt.timestamp() * 1000)


def epoch_ms_to_date(value, tz: ZoneInfo) -> str:
    if not value:
        return ""
    dt = datetime.fromtimestamp(int(value) / 1000, tz=timezone.utc).astimezone(tz)
    return dt.strftime("%Y-%m-%d")


def resolve_status(value: str, list_statuses: list[dict]) -> str | None:
    value = value.strip()
    if not value:
        return None
    for status in list_statuses:
        if status["status"].lower() == value.lower():
            return status["status"]
    return None


def resolve_custom_field_value(field: dict, raw_value: str, tz: ZoneInfo):
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
        return to_epoch_ms(value, tz)
    if field_type == "number":
        try:
            return float(value) if "." in value else int(value)
        except ValueError:
            return None
    return value  # text, short_text, url, email, phone, ...


def reverse_custom_field_value(field: dict, value, tz: ZoneInfo) -> str:
    if value in (None, "", []):
        return ""
    field_type = field["type"]
    if field_type == "drop_down":
        options = field.get("type_config", {}).get("options", [])
        for opt in options:
            if opt["id"] == value:
                return opt["name"]
        return ""
    if field_type == "labels":
        options = field.get("type_config", {}).get("options", [])
        names = [opt["name"] for opt in options if opt["id"] in value]
        return ", ".join(names)
    if field_type == "checkbox":
        return "TRUE" if value else ""
    if field_type == "date":
        return epoch_ms_to_date(value, tz)
    if field_type == "number":
        return str(value)
    return str(value)  # text, short_text, url, email, phone, ...


def build_task_payload(row: dict, custom_fields: list[dict], list_statuses: list[dict],
                        description_column: str | None,
                        tz: ZoneInfo) -> tuple[dict, list[dict], list[str], str | None]:
    payload: dict = {}
    unmapped: list[str] = []
    unmatched_status: str | None = None

    if description_column and row.get(description_column, "").strip():
        payload["description"] = row[description_column]

    if "next_action_date" in row:
        due = to_epoch_ms(row["next_action_date"], tz)
        if due is not None:
            payload["due_date"] = due
            payload["due_date_time"] = False

    if "outreach_status" in row and row["outreach_status"].strip():
        status = resolve_status(row["outreach_status"], list_statuses)
        if status:
            payload["status"] = status
        else:
            unmatched_status = row["outreach_status"].strip()

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
        value = resolve_custom_field_value(field, raw_value, tz)
        if value is not None:
            resolved_custom_fields.append({"id": field["id"], "value": value})

    return payload, resolved_custom_fields, unmapped, unmatched_status


def sync(csv_path: Path, token: str, list_id: str, dry_run: bool,
         native_only: bool = False) -> None:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    tz = get_workspace_timezone(token)
    list_meta = get_list_meta(token, list_id)
    list_statuses = list_meta.get("statuses", [])
    custom_fields = get_custom_fields(token, list_id)
    existing_tasks = get_existing_tasks(token, list_id)

    all_unmapped: set[str] = set()
    unmatched_statuses: dict[str, list[str]] = {}
    description_column = "notes" if rows and "notes" in rows[0] else None

    for row in rows:
        org = row.get("organization", "").strip()
        if not org:
            continue
        payload, custom_field_values, unmapped, unmatched_status = build_task_payload(
            row, custom_fields, list_statuses, description_column, tz)
        if native_only:
            custom_field_values = []
        else:
            all_unmapped.update(unmapped)
        if unmatched_status:
            unmatched_statuses.setdefault(unmatched_status, []).append(org)

        task_id = existing_tasks.get(org)
        if task_id:
            action = f"UPDATE {org} ({task_id})"
            method, path = "PUT", f"/task/{task_id}"
        else:
            action = f"CREATE {org}"
            method, path = "POST", f"/list/{list_id}/task"
            payload = {"name": org, **payload}

        if dry_run:
            print(f"[dry-run] {action}: "
                  f"{json.dumps({**payload, 'custom_fields': custom_field_values}, indent=2)}")
            continue

        resp = api_request(token, method, path, payload)
        if not task_id:
            task_id = resp["id"]
        # Custom Fields go through the dedicated per-field endpoint, not the bulk
        # `custom_fields` array on Create/Update Task -- ClickUp's bulk array silently
        # drops values for at least the "text" (long text) field type, with no error.
        # Each call here permanently consumes one of the Workspace's Custom Field
        # "uses" (plan-limited, e.g. 60 total on Free, never reset -- see --native-only
        # above), so this loop is skipped entirely in that mode.
        for cf in custom_field_values:
            api_request(token, "POST", f"/task/{task_id}/field/{cf['id']}",
                        {"value": cf["value"]})
        print(action)

    if all_unmapped:
        print("\nColumns with no matching ClickUp custom field (data not synced):",
              file=sys.stderr)
        for col in sorted(all_unmapped):
            print(f"  - {col}", file=sys.stderr)

    if unmatched_statuses:
        print("\noutreach_status values with no matching List Status (native status not "
              "set -- add a matching Status to the List, e.g. via ClickUp's List "
              "settings):", file=sys.stderr)
        for status, orgs in sorted(unmatched_statuses.items()):
            print(f"  - {status!r}: {', '.join(sorted(orgs))}", file=sys.stderr)


def pull(csv_path: Path, token: str, list_id: str, dry_run: bool) -> None:
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    tz = get_workspace_timezone(token)
    custom_fields = get_custom_fields(token, list_id)
    fields_by_name = {normalize(f["name"]): f for f in custom_fields}
    existing_tasks = get_existing_tasks(token, list_id)

    description_column = "notes" if fieldnames and "notes" in fieldnames else None
    changed_count = 0

    for row in rows:
        org = row.get("organization", "").strip()
        if not org:
            continue
        task_id = existing_tasks.get(org)
        if not task_id:
            print(f"warning: no ClickUp task found for {org!r}; skipping", file=sys.stderr)
            continue

        task = get_task(token, task_id)
        changes: dict[str, tuple[str, str]] = {}

        if "outreach_status" in row:
            new_value = task.get("status", {}).get("status", "")
            if new_value and new_value != row["outreach_status"]:
                changes["outreach_status"] = (row["outreach_status"], new_value)

        if "priority" in row and task.get("priority"):
            raw_priority = task["priority"].get("id")
            new_value = REVERSE_PRIORITY_MAP.get(int(raw_priority)) if raw_priority else None
            if new_value and new_value != row["priority"]:
                changes["priority"] = (row["priority"], new_value)

        if "next_action_date" in row:
            new_value = epoch_ms_to_date(task.get("due_date"), tz)
            if new_value and new_value != row["next_action_date"]:
                changes["next_action_date"] = (row["next_action_date"], new_value)

        if description_column:
            new_value = task.get("description", "") or ""
            if new_value and new_value != row.get(description_column, ""):
                changes[description_column] = (row.get(description_column, ""), new_value)

        for cf in task.get("custom_fields", []):
            column = next(
                (col for col in fieldnames
                 if col not in NATIVE_COLUMNS and col != description_column
                 and col != "priority" and normalize(col) == normalize(cf["name"])),
                None,
            )
            field_def = fields_by_name.get(normalize(cf["name"])) if column else None
            if not column or not field_def:
                continue
            new_value = reverse_custom_field_value(field_def, cf.get("value"), tz)
            if new_value and new_value != row.get(column, ""):
                changes[column] = (row.get(column, ""), new_value)

        if not changes:
            continue

        changed_count += 1
        if dry_run:
            print(f"[dry-run] UPDATE {org}:")
            for col, (old, new) in changes.items():
                print(f"    {col}: {old!r} -> {new!r}")
            continue

        for col, (_, new) in changes.items():
            row[col] = new
        print(f"UPDATE {org}: {', '.join(changes)}")

    if dry_run:
        print(f"\n[dry-run] {changed_count} row(s) would be updated. No files written.")
        return

    if changed_count == 0:
        print("No changes pulled from ClickUp.")
        return

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nUpdated {changed_count} row(s) in {csv_path}.")


def main() -> None:
    load_dotenv(REPO_ROOT / ".env")

    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--list-id", default=os.environ.get("CLICKUP_LIST_ID"))
    parser.add_argument("--dry-run", action="store_true",
                         help="Print planned changes without writing to ClickUp or the CSV")
    parser.add_argument("--pull", action="store_true",
                         help="Pull changes from ClickUp back into the CSV, instead of "
                              "pushing the CSV to ClickUp")
    parser.add_argument("--native-only", action="store_true",
                         help="Push only status/priority/due-date/description; skip all "
                              "per-field Custom Field API calls (see usage note above)")
    args = parser.parse_args()

    token = os.environ.get("CLICKUP_API_TOKEN")
    if not token:
        parser.error("CLICKUP_API_TOKEN is not set (env var or .env file)")
    if not args.list_id:
        parser.error("--list-id or CLICKUP_LIST_ID is required")
    if not args.csv.exists():
        parser.error(f"CSV not found: {args.csv}")

    if args.pull:
        if args.native_only:
            parser.error("--native-only has no effect with --pull (reading is free; "
                          "only writing Custom Field values consumes the quota)")
        pull(args.csv, token, args.list_id, args.dry_run)
    else:
        sync(args.csv, token, args.list_id, args.dry_run, args.native_only)


if __name__ == "__main__":
    main()
