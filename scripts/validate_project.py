#!/usr/bin/env python3
"""Validate the local lead-generation project without using external services."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECT_FILE = REPO_ROOT / "project" / "PROJECT.md"
LEADS_FILE = REPO_ROOT / "project" / "leads" / "lead-index.csv"
QA_FILE = REPO_ROOT / "project" / "email-rules" / "email-qa.md"
REQUIRED_COLUMNS = {
    "organization",
    "email_confidence",
    "do_not_contact",
    "last_verified",
    "next_action_date",
    "outreach_status",
}


def bracketed_placeholders(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if re.match(r"^>\s*\[[^]]+\]$", line.strip())]


def validate(template: bool) -> list[str]:
    errors: list[str] = []
    for path in (PROJECT_FILE, LEADS_FILE, QA_FILE):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(REPO_ROOT)}")
    if errors:
        return errors

    with LEADS_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = set(reader.fieldnames or [])
        rows = list(reader)
    missing_columns = REQUIRED_COLUMNS - fieldnames
    if missing_columns:
        errors.append("lead-index.csv is missing required columns: " +
                      ", ".join(sorted(missing_columns)))
    for row_number, row in enumerate(rows, start=2):
        organization = (row.get("organization") or "").strip()
        if not organization:
            errors.append(f"lead-index.csv row {row_number} has no organization")
        if not template and "delete before use" in organization.lower():
            errors.append(f"lead-index.csv row {row_number} is still a template row")

    if not template:
        placeholders = bracketed_placeholders(PROJECT_FILE)
        if placeholders:
            errors.append("PROJECT.md still has placeholders: " + ", ".join(placeholders))
        qa_text = QA_FILE.read_text(encoding="utf-8")
        if "[PROSPECT 1 NAME]" in qa_text:
            errors.append("email-qa.md still has Final Gate prospect placeholders")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", action="store_true",
                        help="Validate the shipped framework while allowing its placeholders")
    args = parser.parse_args()
    errors = validate(args.template)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    mode = "template" if args.template else "configured project"
    print(f"PASS: {mode} validation completed without external services.")


if __name__ == "__main__":
    main()
