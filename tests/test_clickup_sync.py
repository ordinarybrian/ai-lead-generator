from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from zoneinfo import ZoneInfo


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "clickup_sync.py"
SPEC = importlib.util.spec_from_file_location("clickup_sync", SCRIPT)
assert SPEC and SPEC.loader
clickup_sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clickup_sync)


class ClickUpSyncTests(unittest.TestCase):
    def test_normalize_matches_common_field_names(self) -> None:
        self.assertEqual(clickup_sync.normalize("LinkedIn_URL"), "linkedin url")

    def test_date_round_trip_uses_workspace_calendar_date(self) -> None:
        timezone = ZoneInfo("America/Los_Angeles")
        epoch = clickup_sync.to_epoch_ms("2026-10-12", timezone)
        self.assertEqual(clickup_sync.epoch_ms_to_date(epoch, timezone), "2026-10-12")

    def test_dropdown_value_resolves_to_clickup_option_id(self) -> None:
        field = {
            "type": "drop_down",
            "name": "Priority tier",
            "type_config": {"options": [{"id": "priority-a", "name": "A"}]},
        }
        self.assertEqual(
            clickup_sync.resolve_custom_field_value(field, "a", ZoneInfo("UTC")),
            "priority-a",
        )

    def test_build_task_payload_keeps_native_values_out_of_custom_fields(self) -> None:
        row = {
            "organization": "Example Org",
            "outreach_status": "Researching",
            "next_action_date": "2026-10-12",
            "priority": "A",
            "email": "person@example.com",
            "notes": "Verify title",
        }
        custom_fields = [{"id": "email-id", "name": "Email", "type": "email"}]
        payload, custom_values, unmapped, unmatched = clickup_sync.build_task_payload(
            row,
            custom_fields,
            [{"status": "Researching"}],
            "notes",
            ZoneInfo("UTC"),
        )
        self.assertEqual(payload["status"], "Researching")
        self.assertEqual(payload["priority"], 1)
        self.assertEqual(payload["description"], "Verify title")
        self.assertEqual(custom_values, [{"id": "email-id", "value": "person@example.com"}])
        self.assertEqual(unmapped, [])
        self.assertIsNone(unmatched)


if __name__ == "__main__":
    unittest.main()
