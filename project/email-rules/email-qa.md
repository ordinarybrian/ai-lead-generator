# EMAIL_QA.md

# Lead-Generation Outreach
## Email Pass / Fail Checklist

Every outbound email must pass every section below.

If any item fails, rewrite the email.

This file audits a finished draft. It assumes `email-writing-rules.md` as the source of truth for phrase lists, banned words, and the Pass/Fail Gate definitions — those are not repeated here in full. Where a test below checks against a list defined in the rules file, go read that list fresh each time rather than relying on memory of it; the rules file is what gets updated when a new AI-tell is discovered, not this one.

---

# Test 0 — Fact & Consent Check

Run this before any of the tone/style tests below. A perfectly-written email built on a
stale fact or sent to a suppressed contact is still a FAIL, and no amount of gate-passing
prose fixes that.

Check the lead's row in `leads/lead-index.csv` and its `leads/<organization-slug>/`
files:

1. Is `do_not_contact` set to `TRUE` for this lead? If so, stop — do not send or keep
   drafting. Flag it instead of proceeding.
2. Does every fact the draft references about the recipient (title, company, a recent
   event or initiative) match the current lead record, and is it traceable to
   `leads/<organization-slug>/sources.md`?
3. Is `last_verified` on the lead row recent enough to trust? If it's stale, re-verify
   the fact before sending — don't ship a draft built on an assumption that the contact
   still holds that title or that company detail is still accurate.
4. Does the draft claim or imply that the prospect dislikes, struggles with, or wants to stop handling hosting or technical support? If so, is that claim actually supported by the research? If not, rewrite it as an option rather than an assumed pain point.
5. Does the draft offer or imply any partnership terms that have not been explicitly defined in `PROJECT.md`? If so, FAIL.

PASS

`do_not_contact` is not set, and every fact referenced in the draft is current and
traceable to a source.

FAIL

`do_not_contact` is `TRUE`, or any referenced fact is stale, unverified, or untraceable.
Re-verify or rewrite before continuing to the tests below.

---

# Test 1 — Gate Check (Human Test)

Run the draft against all six Pass/Fail Gates defined in `email-writing-rules.md`, sentence by sentence. Not a skim — check every sentence against every gate.

1. Text-a-Friend Gate
2. Reflection-Sentence Gate
3. Universal-Claim Gate
4. Rule-of-Three Gate
5. One-Read Gate
6. Stranger-at-a-Bar Gate

Full definitions, FAIL examples, and a worked before/after rewrite are in `email-writing-rules.md` under "Pass/Fail Gates" — read them there, don't rely on the one-line summaries above.

PASS

All six gates clear on every sentence.

FAIL

Any single gate fails on any single sentence. Note which gate(s) failed and on which sentence when reporting the result — "fails Gate 2" is a more useful note than "sounds off."

---

# Test 2 — AI Test

Check every sentence against the "Never Sound Like AI" phrase list in `email-writing-rules.md`.

FAIL if any listed phrase appears, or a close paraphrase of one — a rewording that does the same job as a banned phrase is still a Gate 2 failure (see Test 1), even if the exact words differ.

PASS

None of those phrases, or functional equivalents of them, appear.

---

# Test 3 — Corporate Buzzword Test

Check every sentence against the "Avoid Corporate Buzzwords" list in `email-writing-rules.md`.

If more than ONE listed buzzword appears...

FAIL

---

# Test 4 — Sales Test

Question:

Does this sound like someone trying to sell something?

See "Never Sound Like Sales" and "Don't Sell" in `email-writing-rules.md`.

PASS

Feels like sharing an idea.

FAIL

Feels like a pitch.

For designers, developers, and agencies, also ask:

Could this email reasonably make the recipient think Inland Elite wants to compete for
their existing design, development, marketing, or creative relationship?

If yes...

FAIL

---

# Test 5 — Executive Test

Imagine the recipient opens this between meetings.

Would they read to the end?

PASS

Likely yes.

FAIL

Too long.

Too polished.

Too much explanation.

---

# Test 6 — Curiosity Test

Question:

Does the email create curiosity?

PASS

The reader wants to know more.

FAIL

The email explains everything.

---

# Test 7 — Vision Test

Question:

Can the recipient imagine what's being offered actually working for them?

See "Show, Don't Tell" in `email-writing-rules.md` — a single vivid image passes; a curated list of examples fails Gate 4 instead.

PASS

The language is such that at a 7th grade reading level the recipient can understand how Inland Elite might fit into their existing client workflow without requiring a lengthy explanation. A concrete example may be used when it helps, but isn't mandatory.

FAIL

The email only talks about the thing itself, not what it enables.

---

# Test 8 — Personalization Test

Question:

Could I replace the company name with another company and send the same email?

If yes...

FAIL

Does the outreach angle make sense for this lead's `lead_type`, while still being based
on organization-specific research?

A freelancer, creative studio, marketing agency, and MSP should not receive the same
underlying pitch with names swapped.

If the angle comes only from the lead type and not from research about this specific
organization...

FAIL

The email must clearly be written for THIS organization.

---

# Test 9 — One Idea Test

Question:

What is the single point?

If you cannot answer in one sentence...

FAIL

---

# Test 10 — CTA Test

Question:

Is the ask small?

PASS

Reply.

Conversation.

Referral.

Thoughts.

FAIL

Meeting.

Sale.

Pricing.

Negotiation.

---

# Test 11 — Adjective Test

Highlight every adjective. See "Don't Stack Adjectives" in `email-writing-rules.md`.

If there are more than about one adjective every two sentences...

FAIL

---

# Test 12 — "Could" Test

Count the word "could." See "Don't Repeat 'Could'" in `email-writing-rules.md`.

0–2

PASS

3+

Rewrite.

---

# Test 13 — Reading Level

The email should read around:

8th–10th grade.

If it sounds like Harvard Business Review...

FAIL

---

# Test 14 — Paragraph Test

Maximum paragraph length:

4 lines.

If larger...

FAIL

---

# Test 15 — Word Count

Ideal:

120–220 words

Maximum:

250

Over 250

FAIL

---

# Test 16 — Rewrite Test

Delete the first paragraph.

Is the email better?

If yes...

The first paragraph was unnecessary.

Rewrite.

---

# Test 17 — Remove One Sentence

Delete one random sentence.

Does the email still work?

If yes...

That sentence wasn't needed.

Rewrite.

---

# Test 18 — Forward Test

Question:

Would the recipient comfortably forward this internally?

PASS

FAIL

---

# Test 19 — Memory Test

After reading, close the email.

Can you summarize it in ONE sentence?

If not...

FAIL

---

# Test 20 — "Why Them?" Test

Finish this sentence:

"I emailed this company because..."

If you can't answer in one sentence...

FAIL

---

# Test 21, Em Dash Test

Search the draft for "—". See "Never Use Em Dashes" in `email-writing-rules.md`.

PASS

Zero em dashes.

FAIL

One or more. Rewrite the sentence with a period, a comma, or a parenthetical instead.

---

# Final Gate

Imagine the recipient is one of this project's actual top prospects.

**Replace the placeholder names below with this project's current top prospects from
`leads/lead-index.csv` / `PROJECT.md` before running QA** — the gate only works if you
picture a real, specific person.

- Valik Rudd, Owner / Senior Web Developer of Timber Web Design
- Heather Valencia, Owner & Business Manager of Ravenous Raven Design
- Kevin Raverty, Owner of 509 Designs

Would you confidently send this email exactly as written?

YES

PASS

Anything else

FAIL

Rewrite.

---

# Final Principle

The email should feel like one intelligent person sharing one interesting idea with another intelligent person.

Not marketing.

Not AI.

Not sales.

Just an idea worth considering.

## Review Overview

Once the review is complete, output the judgement using the following syntax:

EMAIL QA

Fact & Consent........... PASS
Human Gates.............. PASS
AI / Buzzwords........... PASS
Sales Tone............... PASS
Personalization.......... PASS
One Idea................. PASS
CTA...................... PASS
Readability.............. PASS
Length................... PASS
Em Dashes................ PASS
Final Send Test.......... PASS

Overall: PASS

Failures:
None.

Reason for failure:
The phrase "strategic opportunity" makes the email sound like a pitch. Rewrite without that phrase.
