# Project Context

This is the one file you edit to stand up a new lead-generation project on this framework.
Fill in every bracketed placeholder. Delete a section only if it truly doesn't apply — the
"Optional commercial terms" section is the one most likely to be skippable.

Each section below includes a short inline example showing how it might be filled in for
a domain sale, a job search, and a B2B partnership push, so the pattern is clear even
though your project is probably none of those three exactly.

---

## What Is Being Offered or Sought

One paragraph. What is this project trying to place with someone else — a product, an
asset, a candidate's labor, a partnership, a donation ask? State it plainly.

> [WHAT YOU'RE OFFERING OR SEEKING]

<!--
Example (domain sale): "This project is for selling the domain ExampleAsset.com to an
organization that could build a consumer-facing product on it."

Example (job search): "This project is for finding and applying to senior product
management roles at mid-size B2B SaaS companies, and reaching the hiring manager or
team lead directly rather than relying solely on the applicant tracking system."

Example (B2B partnership): "This project is for identifying mid-market logistics
companies that could integrate with our API, and reaching a technical or partnerships
lead who could sponsor a pilot."
-->

## Primary Goal

What does this project exist to accomplish, and what does "success" look like at the end
of it — a signed deal, an accepted offer, a scheduled pilot, a grant awarded?

> [PRIMARY GOAL AND DEFINITION OF SUCCESS]

<!--
Example (domain sale): "Success is a signed purchase agreement at or above the minimum
acceptable offer, closed through escrow."

Example (job search): "Success is an accepted offer for a role that matches the target
criteria below, ideally within 90 days."

Example (B2B partnership): "Success is a signed pilot agreement with at least one
mid-market logistics company within the quarter."
-->

## Positioning / Pitch Angle

How should this be framed to a prospect? What's the core idea a recipient should walk
away with after one read?

> [POSITIONING / PITCH ANGLE]

<!--
Example (domain sale): "Position the domain as a possible national consumer-facing
identity and destination — not as a keyword or SEO asset. The strongest pitch is what
the organization could build with it, not the domain's inherent value."

Example (job search): "Position the candidate as someone who has already solved a
version of this company's current problem, not as a generic applicant. Lead with a
specific, relevant accomplishment."

Example (B2B partnership): "Position the integration as solving a specific operational
pain point this company already has in public — not as a generic 'let's partner'
outreach."
-->

## Target Categories

Who counts as a qualified lead for this project? List the categories worth researching,
roughly in priority order.

> [TARGET CATEGORY 1]
> [TARGET CATEGORY 2]
> [TARGET CATEGORY 3]
> ...

<!--
Example (domain sale): consumer platforms in the relevant space; large nonprofits with
a matching mission; companies with existing but fragmented offerings in the category.

Example (job search): companies of a target size/stage, in a target industry, with a
public need matching the candidate's specialty (e.g., recent job postings, funding
announcements, public statements about the relevant problem).

Example (B2B partnership): companies with the technical prerequisites for integration,
a public need for the capability being offered, and a partnerships or BD function that
can actually sponsor a pilot.
-->

## Contact-Selection Priority Order

For a typical target organization, who should be contacted first? List roles in priority
order. Note any small-organization exception (e.g., go straight to the CEO when no other
role exists).

1. [ROLE 1]
2. [ROLE 2]
3. [ROLE 3]
4. ...

<!--
Example (domain sale): CMO -> Chief Growth Officer -> Chief Digital Officer -> VP
Marketing/Brand/Growth -> Strategic Partnerships lead -> CEO (small orgs only).

Example (job search): hiring manager for the specific role -> a peer already on the
team -> a recruiter or talent partner -> a more senior leader only as a last resort.

Example (B2B partnership): Head of Partnerships/BD -> a relevant technical lead ->
VP of Product -> CEO (small orgs only).
-->

## Optional: Commercial Terms

**OPTIONAL — delete this section entirely if the project has no price, budget, salary,
or compensation component (e.g., most job searches, many partnership or fundraising
projects).**

> [PRICE / BUDGET / COMPENSATION FIGURES, IF ANY]
> [MINIMUM ACCEPTABLE OUTCOME, IF ANY — e.g., floor price, minimum acceptable salary]
> [ANY FIGURE THAT MUST STAY CONFIDENTIAL AND NEVER BE DISCLOSED OR INFERRED]

<!--
Example (domain sale): "Asking price: $X. Minimum acceptable offer: $Y. Broker
commission: Z%. The seller's absolute floor is private and must never be disclosed
or inferred from the stated minimum."

Example (B2B partnership): "No fixed pricing yet — the goal of first contact is a
scoping conversation, not a quote."
-->

## Outreach Cadence

> Day 0: [INITIAL CONTACT]
> Day [N]: [FIRST FOLLOW-UP]
> Day [N]: [SECOND FOLLOW-UP]
> Day [N]: [FINAL TOUCH OR ALTERNATE-CONTACT OUTREACH]

<!--
Example (domain sale): Day 0 initial email; Day 4-5 first follow-up; Day 10-12 second
follow-up; Day 21 final light follow-up or alternate contact.

Example (job search): Day 0 application + direct outreach to hiring manager; Day 5
follow-up referencing the application; Day 14 final check-in or pivot to a different
role/contact at the same company.
-->

Do not contact multiple people at the same organization on the same day. Log every
contact attempt in `leads/lead-index.csv`, including a `next_action_date` for whatever
comes next so due and overdue follow-ups can be found without re-reading every row.

If a contact asks not to be contacted again, set `do_not_contact` to `TRUE` on their row
immediately — see `leads/README.md` and `AGENTS.md` for how that's enforced.

## Language and Tone

The detailed anti-AI-tell rules (Pass/Fail Gates, banned-phrase lists) live in
`email-rules/email-writing-rules.md` and the QA checklist lives in
`email-rules/email-qa.md` — read those before drafting or reviewing outreach. They are
domain-agnostic and rarely need project-specific edits.

The one thing worth customizing per project is the **Final Gate** reviewer list in
`email-rules/email-qa.md` — replace the placeholder names there with this project's
actual top prospects, so the QA step imagines the real recipients.

---

## Working Style

- Make the smallest well-supported change needed and summarize what changed.
- Ask before sending outreach, publishing content, changing live systems, disclosing
  confidential information, or materially changing pricing/compensation/negotiation
  strategy.
- If uncertainty remains, label it plainly instead of filling gaps with assumptions.
