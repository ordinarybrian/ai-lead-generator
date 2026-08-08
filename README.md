# Lead-Generation Framework

A file-based, AI-agent-driven framework for finding leads, researching them, and
drafting personalized outreach — for any use case where you need to reach the right
person at the right organization with a message that doesn't sound like a mass email.

## What this is

There's no hosted app, no database, no build step. Leads and outreach live as plain
markdown and CSV files in this repository. An AI coding agent — Claude Code, or any
other agent that reads an `AGENTS.md`-style instructions file — reads those files,
researches organizations and people, updates the pipeline CSV, and drafts outreach that
it runs through a Pass/Fail QA checklist before handing it to you. The agent never sends
anything automatically; drafting is not authorization to contact anyone.

## When to use it

This template is deliberately generic. Example use cases:

- **Selling an asset** — a domain, a piece of equipment, a business — to organizations
  that could plausibly use it.
- **B2B sales prospecting** — finding companies with a specific need and reaching the
  right buyer.
- **Job search outreach** — finding target companies and reaching a hiring manager
  directly, alongside a normal application.
- **Partnership or fundraising outreach** — finding organizations or funders aligned
  with a specific ask and reaching the right decision-maker.

## Repository structure

| Path | Purpose |
|---|---|
| `AGENTS.md` | Governs how an AI agent works in this repo: context routing, research rules, outreach boundaries. Rarely needs editing. |
| `PROJECT.md` | The one file you fill in to define your specific use case — what's being offered, target categories, contact priority, optional commercial terms, cadence. |
| `leads/` | The lead pipeline: `lead-index.csv` plus one folder per organization with research files. Ships empty (header/template only). |
| `outreach/` | Drafted outreach and QA results, one folder per organization/person. Ships empty. |
| `email-rules/` | The writing rules (Pass/Fail Gates, banned-phrase lists) and the QA checklist every draft must pass. Domain-agnostic; rarely needs editing. |
| `examples/sample-domain-brokerage/` | A fully worked reference example — a real, populated instance of this framework from the project it was built for. |
| `.claude/` | Claude Code permission settings. Already generic; no changes needed. |

## Getting started

1. Clone or copy this repository.
2. Fill in `PROJECT.md` with your specific use case: what you're offering or seeking,
   your primary goal, positioning, target lead categories, contact-selection priority
   order, an optional commercial-terms section (delete it if you don't need one), and
   your outreach cadence.
3. Open `leads/lead-index.csv` and adjust the header if your use case needs different
   columns (see the note in `leads/README.md` for examples — a job search might swap
   in `role_title`, `application_status`, `referral_source`, and so on). The two
   placeholder rows are there to show the expected format; delete them once you add
   real leads. The shipped columns already separate email confidence from delivery
   status, track a `last_verified` date and a `do_not_contact` flag, and split
   `next_action_date` out from the free-text `next_action` — see the column reference
   in `leads/README.md` before you change them.
4. Skim `email-rules/`. The Pass/Fail Gates and QA checklist themselves rarely need
   changes — but swap the worked examples for something closer to your own pitch if you
   want, and replace the placeholder names in the "Final Gate" section of
   `email-rules/email-qa.md` with your project's actual top prospects.
5. Open the project in Claude Code (or another coding agent that reads `AGENTS.md`) and
   give it a first task — for example: *"research Acme Corp as a potential lead and
   create its leads/ folder."*
6. Look at `examples/sample-domain-brokerage/` for a fully worked reference showing what
   a populated project looks like end to end, from a researched lead through a QA'd
   outreach draft.

## How the agent workflow works

Work proceeds in four phases:

1. **Find and grade leads** — populate and prioritize `leads/lead-index.csv`.
2. **Research the organization** — `leads/<organization-slug>/organization.md`,
   `leadership.md`, `sources.md`.
3. **Research the people** — `leads/<organization-slug>/people/<person-slug>.md`.
4. **Draft and QA outreach** — a draft under `outreach/<organization-slug>/<person-slug>/`,
   checked against `email-rules/email-writing-rules.md` and `email-rules/email-qa.md`.
   QA starts with a fact-and-consent check (is the lead's `do_not_contact` flag clear,
   are the facts in the draft still current) before any of the tone/style tests run.

There's also a standing fifth task worth asking for periodically: a **pipeline health
check**, defined in `AGENTS.md`, that scans `leads/lead-index.csv` for overdue
follow-ups, stale verification dates, missing email-confidence labels, duplicate
organizations, and `do_not_contact` violations — without touching any other file.

`AGENTS.md` defines a **context-routing** table so the agent only reads the files
relevant to the current objective — it doesn't load the whole project tree for every
task.

## Conventions

- **Slugs**: lowercase, hyphenated (`acme-corp`, not `AcmeCorp` or `acme_corp`).
- **Status/priority vocab** in the CSV: adapt as needed, but keep values consistent
  within a project (e.g., `Researching` → `Ready for Outreach` → `Initial Email Sent` →
  `Follow-up 1 Sent` → `Replied` / `No Response` → `Closed Won` / `Closed Lost`; priority
  tiers like `A+`, `A`, `B`, `C`).
- **Never use a sentinel value (`FALSE`, `N/A`, `TBD`) to mean "no value yet"** in a date
  or status cell — leave it genuinely blank, so the field stays trustworthy for sorting
  or scripting later.
- **Dates are ISO (`YYYY-MM-DD`)**, including `last_verified` and `next_action_date` —
  this is what makes "what's overdue" or "what needs re-verifying" answerable by
  scanning the CSV instead of re-reading every row's notes.
- **Outreach is drafted, never sent automatically.** A file under `outreach/` is a
  draft, not a record of contact. `leads/lead-index.csv` is only updated with an
  outreach status once an action is actually authorized and completed.

## Customization notes

To adapt this framework to a new use case, you need to touch:

1. **`PROJECT.md`** — your use case, positioning, targets, and cadence.
2. **`leads/lead-index.csv` header** — only if your use case needs different columns.
3. **`email-rules/` worked examples** (optional) — swap in examples relevant to your
   pitch; the gates and checklist structure itself rarely needs to change.

You should generally **not** need to touch:

- `AGENTS.md`'s context-routing logic and research/data rules.
- The Pass/Fail Gate mechanics and QA checklist structure in `email-rules/`.
- The folder structure (`leads/<org>/{organization,leadership,sources}.md`,
  `leads/<org>/people/`, `outreach/<org>/<person>/`).
