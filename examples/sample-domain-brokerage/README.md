# Sample: Domain Brokerage (SeniorCenter.com)

This is a fully worked reference example, archived from the project this framework was
originally built for: brokering the sale of the domain `SeniorCenter.com` to organizations
that could plausibly build a national consumer-facing resource on it.

It is here so you can see what a populated project looks like end to end — a filled-out
`project/leads/lead-index.csv`, several complete organization folders (`organization.md`,
`leadership.md`, `sources.md`, `people/`), and real outreach drafts under
`project/outreach/<organization-slug>/<person-slug>/` — before you start filling in your own.

## What's in here

- `project/leads/lead-index.csv` — a fully populated pipeline CSV, including researched
  rows, bare "to research" rows, and the full set of status/priority values in use.
- `project/leads/<organization-slug>/` — twelve researched organizations (AARP, A Place
  for Mom, Brookdale, Humana, UnitedHealthcare, USAging, and others), each with
  `organization.md`, `leadership.md`, `sources.md`, and `people/<person-slug>.md`.
- `project/outreach/<organization-slug>/<person-slug>/` — real drafted outreach emails
  (initial contact and follow-ups) for several of those organizations, including one
  QA'd example under `project/outreach/aarp/anna-banks/README.md`.
- `homepage-mockup-aarp.png` — a visual concept asset used as a follow-up attachment
  in outreach, referenced from the AARP drafts.

## How to use this example

Don't copy this data into your own `project/leads/` or `project/outreach/` directories —
it's specific to a domain-sale pitch and won't fit a job search, B2B sales, or
partnership project. Instead, read it side by side with the empty `project/leads/` and
`project/outreach/` folders and your own `project/PROJECT.md` to see:

- how a `lead-index.csv` row looks once fully researched vs. still pending,
- what level of detail belongs in `organization.md` vs. `leadership.md` vs. `sources.md`,
- how confidence labels (verified / pattern-based guess / unverified) show up in practice,
- what a drafted, QA'd outreach email and its follow-ups actually look like.

The commercial terms (asking price, minimum offer, commission) referenced in these
files are specific to this archived example and are not part of the generalized
framework — see `project/PROJECT.md` for where a new project defines its own optional
commercial terms, if any.