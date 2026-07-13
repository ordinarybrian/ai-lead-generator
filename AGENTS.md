# SeniorCenter.com brokerage project

This workspace supports Brian Clark's brokerage of the `SeniorCenter.com` domain. Work proceeds in phases: find and grade leads, research a selected organization, research its relevant leadership, then prepare and QA personalized outreach.

## Context routing

Read only the files relevant to the current objective. Always read this file first.

- Lead discovery or grading: `leads/README.md`, then `leads/lead-index.csv`; read an organization folder only when evaluating that organization.
- Organization research: `leads/<organization-slug>/organization.md`, `leadership.md`, and `sources.md` as needed.
- Person research: the relevant file under `leads/<organization-slug>/people/` and only the sources needed to verify it.
- Email drafting: the relevant organization and person files, `email-rules/email-writing-rules.md`, and any specifically requested asset.
- Email QA: `email-rules/email-qa.md`, the draft under `outreach/<organization-slug>/<person-slug>/`, and no unrelated lead files.
- Pricing, negotiation, brokerage authority, or project-wide strategy: read `SENIORCENTER_BROKERAGE_CONTEXT.md`.
- Do not read every lead, every source, or the full project tree by default.

## Project structure

- `leads/lead-index.csv` is the pipeline source of truth for organization/contact status.
- `leads/<organization-slug>/` contains research for one organization only.
- `leads/<organization-slug>/people/` contains research for individual decision-makers.
- `outreach/<organization-slug>/<person-slug>/` contains drafts and QA results for one person.
- `email-rules/` contains the writing boundaries and QA checklist; these are the authoritative email rules.
- `examples/` contains visual or other reference assets, not lead records.

## Research and data rules

- Preserve existing research and distinguish sourced facts, inferences, pattern-based guesses, and verified information.
- Never invent contacts, email addresses, company facts, budgets, priorities, or mission statements. Label email status as verified, possible, pattern-based, or unverified.
- Record supporting URLs where practical and verify current titles and contact details before outreach.
- Inspect the CSV schema before editing it. Preserve columns and existing research, avoid duplicates, and back up the CSV before broad changes.
- Grade leads on strategic fit, practical use, budget likelihood, contact authority, explainability, internal sponsorship, and response likelihood—not company size alone.

## Strategy and outreach boundaries

- Favor direct, highly personalized outreach over marketplaces or mass email.
- Position SeniorCenter.com as a possible national consumer resource for senior centers, programs, events, services, caregivers, and community information.
- Prioritize marketing, growth, digital, brand, commercial, or strategic-partnership leaders where appropriate.
- Emails should be short, specific, conversational, curious, low-pressure, and easy to forward. Follow `email-rules/email-writing-rules.md` exactly.
- Do not include price in a first-contact email unless Brian requests it. Do not attach the homepage concept unless Brian requests it.
- Do not send outreach automatically. Drafting does not authorize external contact.

## Commercial confidentiality

- Asking price: **$149,000 USD**; stated minimum acceptable offer: **$75,000 USD**; broker commission: **15%**.
- The seller's absolute floor is private. Never disclose it, infer it, or call the stated minimum the floor.
- Never accept an offer, make a binding commitment, or represent seller approval without explicit authorization.
- Keep seller information, brokerage terms, and negotiation details confidential.

## Working style

- Make the smallest well-supported change needed and summarize what changed.
- Ask before sending outreach, publishing content, changing live systems, disclosing confidential information, or materially changing pricing or negotiation strategy.
- If uncertainty remains, label it plainly instead of filling gaps with assumptions.
