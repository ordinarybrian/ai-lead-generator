# Leads

This folder contains the lead pipeline and detailed research for individual organizations
(or, depending on your use case, roles, individuals, or partners — see `project/PROJECT.md`).

## Workflow

1. Add or update the organization in `lead-index.csv`.
2. Create one lowercase, hyphenated organization folder, such as `<organization-slug>/`.
3. Keep organization facts in `organization.md`, leadership notes in `leadership.md`, and source links in `sources.md`.
4. Keep individual decision-maker research in `people/<person-slug>.md`.
5. Store generated outreach outside this folder under `project/outreach/<organization-slug>/<person-slug>/`.

Do not create a detailed folder until the organization is a plausible prospect. Preserve uncertainty and verify current facts before outreach.

## Adapting the CSV schema

`lead-index.csv` ships with a minimal, universal header. Adapt the columns to fit your
use case — for example, a job search might swap `organization` framing toward
`role_title`, and add `application_status` or `referral_source` columns; a fundraising
project might add `ask_amount` or `gift_capacity`. Preserve whatever columns you add
once real data is in them, and avoid removing columns other than the two placeholder
rows shipped in the template.

See `examples/sample-domain-brokerage/project/leads/` for a fully populated reference
example (with additional columns such as `organization_type`, `market_or_audience`, and
`strategic_story` that were specific to that project).

If you sync this CSV to ClickUp via `scripts/clickup_sync.py`, most column renames need
no code changes — the script maps any column to a same-named ClickUp custom field
automatically. The exception is five columns the script special-cases by literal name:
`organization` (task name), `next_action_date` (native due date), `outreach_status`
(native status), `priority` (via a hardcoded `PRIORITY_MAP`), and `notes` (task
description). Renaming or removing any of those requires editing the corresponding
string literal(s) in the script — see its module docstring and `NATIVE_COLUMNS`.

## Column reference

This branch's `lead-index.csv` has grown past the shipped template (see "Adapting the CSV
schema" above) — this table reflects the columns actually in use here, in header order.
The "ClickUp Field Type" column is what to create on the target List in
`scripts/clickup_sync.py`'s Setup step 1/2 (see that script's docstring); columns
marked "Native" are handled by ClickUp's built-in task attributes, not a custom field.

| Column | Purpose | ClickUp Field Type |
|---|---|---|
| `organization` | Organization (or role/target) name. | Native — Task Name |
| `website` | Primary URL. | URL |
| `lead_type` | Short category/role description for the lead (e.g. `Freelance Web Developer`, `Small Marketing Agency`). | Text |
| `primary_contact` | Name of the first-choice contact, per `project/PROJECT.md`'s priority order. | Text |
| `contact_title` | Their title, as currently verified. | Text |
| `linkedin_url` | Contact's LinkedIn profile, if found. | URL |
| `email` | Contact's email address, if any is known or guessed. | Email |
| `email_confidence` | How sure you are the address is real: `verified` \| `possible` \| `pattern-based` \| `unverified`. Never mark `verified` without evidence. | Drop Down: `verified`, `possible`, `pattern-based`, `unverified` |
| `email_delivery_status` | What's actually happened when it's been used: blank (not sent yet) \| `sent - no bounce` \| `bounced` \| `confirmed valid` \| `replied`. Kept separate from `email_confidence` — a guess can be confirmed by a clean send, and a "verified" address can still bounce. | Drop Down: `sent - no bounce`, `bounced`, `confirmed valid`, `replied` |
| `backup_contact_name` | An alternate contact's name at the same organization. Leave blank if none identified. | Text |
| `backup_contact_title` | The backup contact's title. | Text |
| `backup_contact_email` | The backup contact's email address. | Email |
| `last_verified` | ISO date (`YYYY-MM-DD`) the contact's title/employment was last checked. Titles and jobs change — re-check before outreach if this is stale. | Date |
| `do_not_contact` | Leave blank normally. Set to `TRUE` if this lead should never be contacted again (explicit opt-out, bounced permanently, etc.). Always check this before drafting or sending. | Checkbox |
| `priority` | This project's priority tier (e.g. `A+`, `A`, `B`, `C`). | Native — Priority (lossy: `A+` and `A` both map to ClickUp's single "Urgent" tier) |
| `qualification_status` | Research verdict on whether this lead is worth pursuing, e.g. `qualified`, `disqualified`. | Drop Down: `qualified`, `disqualified` (add options as new verdicts appear) |
| `fit_reason` | Free-text explanation of why the lead is (or isn't) a good fit — the evidence behind `qualification_status`. | Text |
| `outreach_status` | Pipeline stage (e.g. `Researching`, `Ready for Outreach`, `Initial Email Sent`, `Follow-up 1 Sent`, `On Hold`, `Replied`, `No Response`, `Closed Won`, `Closed Lost`). | Native — Status (must exactly match a List Status, added via ClickUp's List settings — see `scripts/clickup_sync.py`'s docstring) |
| `contact_attempts` | Running count of outreach attempts made so far. | Number |
| `last_contact_date` | ISO date of the most recent actual contact attempt. | Date |
| `next_action` | Free-text description of what to do next. | Text |
| `next_action_date` | ISO date the next action is due — kept separate from `next_action` so due/overdue items can be sorted or queried instead of parsed out of prose. | Native — Due Date |
| `notes` | Anything else worth recording. | Native — Description |

## CSV hygiene rules

- **Never write a sentinel value (`FALSE`, `N/A`, `TBD`) into a date or status cell to
  mean "no value yet."** Leave the cell genuinely blank. A literal `"FALSE"` string in a
  date field is indistinguishable from real data to anything that later reads the CSV.
- **Check for duplicate organizations before adding a row.** Search the CSV for the
  organization name (and obvious variants) first — a duplicate row with divergent data
  is worse than no row, because it's unclear which one is current.
- **Re-verify before outreach, not just before first contact.** If `last_verified` is
  more than a few weeks old, confirm the contact's title and employment are still
  current before drafting or sending anything.
- **Respect `do_not_contact`.** Never draft or send outreach to a row where it's `TRUE`,
  regardless of priority or how long it's been.
- See `AGENTS.md`'s "Pipeline health check" section for the periodic scan an agent can
  run across this file (stale next-actions, missing verification, duplicates, `do_not_contact` violations).
