# Lead-generation framework

This workspace is a portable, file-based framework for AI-agent-driven lead generation
and outreach. Work proceeds in phases: find and grade leads, research a selected
organization, research its relevant people, then prepare and QA personalized outreach.

The specific use case (what's being offered, who's being targeted, positioning, cadence,
and optional commercial terms) is defined in `project/PROJECT.md` — read it before doing
project-specific work.

## Context routing

Read only the files relevant to the current objective. Always read this file first.

- Lead discovery or grading: `project/leads/README.md`, then `project/leads/lead-index.csv`; read an organization folder only when evaluating that organization.
- Organization research: `project/leads/<organization-slug>/organization.md`, `leadership.md`, and `sources.md` as needed.
- Person research: the relevant file under `project/leads/<organization-slug>/people/` and only the sources needed to verify it.
- Email drafting: the relevant organization and person files, `project/email-rules/email-writing-rules.md`, and any specifically requested asset.
- Email QA: `project/email-rules/email-qa.md`, the draft under `project/outreach/<organization-slug>/<person-slug>/`, and no unrelated lead files.
- Positioning, targeting, commercial terms, or project-wide strategy: read `project/PROJECT.md`.
- Pipeline health check: `project/leads/lead-index.csv` only — see "Pipeline health check" below.
- Do not read every lead, every source, or the full project tree by default.

## Project structure

- `project/PROJECT.md` is the single file that defines this project's specific use case — edit it before starting a new project.
- `project/leads/lead-index.csv` is the pipeline source of truth for organization/contact status.
- `project/leads/<organization-slug>/` contains research for one organization only.
- `project/leads/<organization-slug>/people/` contains research for individual decision-makers.
- `project/outreach/<organization-slug>/<person-slug>/` contains drafts and QA results for one person.
- `project/email-rules/` contains the writing boundaries and QA checklist; these are the authoritative email rules.
- `examples/` contains reference assets, including `examples/sample-domain-brokerage/` — a fully worked example project, not live lead records.

## Research and data rules

- Preserve existing research and distinguish sourced facts, inferences, pattern-based guesses, and verified information.
- Never invent contacts, email addresses, company facts, budgets, priorities, or mission statements. Label `email_confidence` as verified, possible, pattern-based, or unverified — and keep `email_delivery_status` (what actually happened when it was used) separate from that confidence label.
- Record supporting URLs where practical and verify current titles and contact details before outreach.
- Inspect the CSV schema before editing it. Preserve columns and existing research, avoid duplicates, and back up the CSV before broad changes.
- Never write a sentinel value (`FALSE`, `N/A`, `TBD`) into a date or status cell to mean "no value yet" — leave it genuinely blank. See `project/leads/README.md`'s CSV hygiene rules.
- Before adding a new organization row, check for an existing row with the same or a near-identical name. Do not create duplicate rows with divergent data.
- Grade leads on strategic fit, practical use, budget or likelihood-to-act, contact authority, explainability, internal sponsorship, and response likelihood—not organization size alone.
- Contact facts decay: titles change, people leave, people go on leave. Treat `last_verified` on a lead row as an expiration date, not a formality — re-verify the contact's title and employment before drafting or sending anything if it's more than a few weeks stale, and update `last_verified` after re-checking.

## Strategy and outreach boundaries

- Favor direct, highly personalized outreach over marketplaces or mass email.
- Follow the positioning and target-category guidance in `project/PROJECT.md` for what's being offered and who qualifies as a lead.
- Prioritize contacts per the priority order defined in `project/PROJECT.md`.
- Emails should be short, specific, conversational, curious, low-pressure, and easy to forward. Follow `project/email-rules/email-writing-rules.md` exactly.
- Do not include price, compensation, or other commercial terms in a first-contact email unless explicitly requested. Do not attach supporting visual/media assets unless requested.
- Never draft or send outreach to a lead whose `do_not_contact` column is `TRUE`, regardless of priority, staleness, or how long it's been since the opt-out.
- Do not send outreach automatically. Drafting does not authorize external contact.

## Pipeline health check

Run this as a discrete task when asked to check on the pipeline, or periodically on a
project with an active lead list. Read only `project/leads/lead-index.csv` for this — no
organization folders needed. Scan for:

- **Overdue next actions**: rows where `next_action_date` is in the past but
  `outreach_status` hasn't moved.
- **Stale verification**: rows with `priority` of the top tier(s) where `last_verified`
  is missing or old, especially if `outreach_status` suggests outreach is imminent.
- **Missing confidence labels**: rows with an `email` value but no `email_confidence`.
- **Duplicate organizations**: repeated or near-identical `organization` values with
  different data in other columns.
- **`do_not_contact` violations**: any row marked `TRUE` with an `outreach_status` or
  `next_action` that implies further contact is planned.

Report findings as a short list grouped by category — don't silently fix the CSV unless
asked to.

## Commercial confidentiality (if applicable)

Only relevant if this project has a commercial-terms section in `project/PROJECT.md`
(price, budget, compensation, commission). Skip this section entirely for projects
without one.

- Treat any stated minimum/floor/budget figure in `project/PROJECT.md` as confidential. Never disclose it, infer it beyond what's stated, or call a stated minimum the floor if a separate private floor exists.
- Never accept an offer, make a binding commitment, or represent approval without explicit authorization.
- Keep commercial terms and negotiation details confidential.

## Working style

- Make the smallest well-supported change needed and summarize what changed.
- Ask before sending outreach, publishing content, changing live systems, disclosing confidential information, or materially changing pricing, compensation, or negotiation strategy.
- If uncertainty remains, label it plainly instead of filling gaps with assumptions.
