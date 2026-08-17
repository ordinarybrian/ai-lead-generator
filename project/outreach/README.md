# Outreach outputs

Store drafts and QA results by organization and person:

`<organization-slug>/<person-slug>/`

Example: `<organization-slug>/<person-slug>/first-contact.md` and `first-contact.qa.md`.

Do not send messages automatically. A draft is not a record of contact; update `project/leads/lead-index.csv` only when an outreach action is actually authorized and completed.

Before drafting or sending, run the lead through Test 0 in `project/email-rules/email-qa.md`:
check `do_not_contact` on the lead's row in `project/leads/lead-index.csv`, and confirm any
fact referenced in the draft is still current per `last_verified`. Once an outreach
action is logged, also update `next_action_date` so the follow-up cadence stays
queryable.

Also mirror the QA'd draft into the lead row's `email_draft` column (`To:` / `Subject:` /
`Body:`) so it's visible from the pipeline view (including in ClickUp, if synced). After
that email is actually sent, overwrite `email_draft` with the next follow-up's draft —
see "Email draft rotation" in `project/leads/README.md`.

See `examples/sample-domain-brokerage/project/outreach/` for a fully worked reference
example, including a QA'd draft under `aarp/anna-banks/`.
