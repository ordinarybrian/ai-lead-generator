---
name: pipeline-management
description: Inspect or update the lead pipeline CSV, including health checks and CSV hygiene. Use for pipeline status, overdue actions, duplicate detection, or lead-index edits.
---

Treat `project/leads/lead-index.csv` as the pipeline source of truth.

- Inspect the CSV schema before editing; preserve existing columns and research.
- For a health check, read only the CSV. Report overdue next actions, stale verification, missing email confidence, duplicate organizations, and do-not-contact violations. Do not silently repair findings.
- Leave unknown dates and statuses blank; never use `FALSE`, `N/A`, or `TBD` as a sentinel value.
- Never plan, draft, or send outreach for a row whose `do_not_contact` is `TRUE`.
- ClickUp is not configured for this implementation. Do not invoke `scripts/clickup_sync.py` or attempt an external synchronization unless the user explicitly asks to opt in.
