# EMAIL_QA.md

# Employment Outreach
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
4. If the draft references an advertised opening, is the posting current, is the role
   still accepting applications, and does the draft represent its responsibilities
   accurately?
5. If no current opening is known, does the draft avoid implying that the organization
   is hiring?
6. Is every claim about Brian supported by a user-approved résumé, portfolio, work
   sample, or experience record? If no authoritative candidate source is available,
   flag the claim instead of inventing or strengthening it.
7. Do any statements about location, relocation, remote work, or compensation match the
   current instructions in `PROJECT.md`?

PASS

`do_not_contact` is not set, every organization/contact fact is current and traceable,
every candidate claim is supported, and the draft describes the employment situation
accurately.

FAIL

`do_not_contact` is `TRUE`, or any referenced fact, opening, candidate claim, or project
constraint is stale, unsupported, inaccurate, or untraceable. Re-verify or rewrite
before continuing to the tests below.

---

# Test 1 — Gate Check (Human Test)

Run the draft against all six Pass/Fail Gates defined in `email-writing-rules.md`, sentence by sentence. Not a skim — check every sentence against every gate.

1. Natural-Email Gate
2. Reflection-Sentence Gate
3. Universal-Claim Gate
4. Rule-of-Three Gate
5. One-Read Gate
6. Professional-Introduction Gate

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

# Test 4 — Generic Application / Self-Promotion Test

Question:

Does this sound like a generic cover letter, résumé summary, or exaggerated candidate
pitch?

See "Never Sound Like a Generic Job Application" and "Don't Oversell" in
`email-writing-rules.md`.

PASS

Feels like a capable person making a specific, supported connection between the
organization's need and his experience.

FAIL

Feels generic, inflated, overly eager, or centered on claims rather than evidence.

---

# Test 5 — Recipient & Skimmability Test

Imagine the actual recipient — hiring manager, agency owner, technical leader, or
recruiter — opens this between other tasks.

Would they read to the end?

PASS

Likely yes.

FAIL

Too long.

Too polished.

Too much explanation.

---

# Test 6 — Relevance & Interest Test

Question:

Does the recipient immediately understand why Brian may be relevant and want to see a
reply, résumé, portfolio, or next conversation?

PASS

The connection is clear, specific, and interesting enough to continue.

FAIL

The email is vague, generic, confusing, or tells Brian's whole career story.

---

# Test 7 — Role-Fit Evidence Test

Question:

Can the recipient imagine Brian handling one relevant responsibility based on evidence
in the email?

See "Show, Don't Tell" in `email-writing-rules.md`. Use one supported example; a curated
list of examples fails Gate 4 instead.

PASS

The email connects a real need or responsibility to supported experience.

FAIL

The email makes broad fit claims, recites skills, or leaves the recipient to infer why
the experience matters.

---

# Test 8 — Personalization Test

Question:

Could I replace the company name with another company and send the same email?

If yes...

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

Application review.

Brief call or meeting.

FAIL

Demanding an interview.

Multiple asks.

An open-ended request for the recipient's time.

Negotiation.

---

# Test 11 — Adjective Test

Highlight every adjective. See "Don't Stack Adjectives" in `email-writing-rules.md`.

PASS

The adjectives are specific, necessary, and supported.

FAIL

Adjectives are stacked, vague, self-congratulatory, or unsupported. Do not fail a useful
draft merely because it crosses an arbitrary adjective count.

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

Ideal for most first-contact employment outreach:

80–160 words

Practical maximum:

200 words

Over 200 without a clear reason

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

Remove each sentence in turn.

If removing a sentence loses no relevant fact, evidence, context, or part of the ask,
that sentence probably is not needed. Cut it or justify why it remains.

PASS

Every remaining sentence contributes relevant information or necessary context.

FAIL

One or more sentences can be removed with no meaningful loss.

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

# Final Gate

Name the actual intended recipient, current title, organization, and outreach mode for
this draft. Do not substitute a generic persona or a permanent list of top prospects.

- Recipient: [ACTUAL RECIPIENT NAME]
- Current title and organization: [TITLE], [ORGANIZATION]
- Mode: [ADVERTISED OPENING / PROACTIVE OUTREACH / FOLLOW-UP OR REFERRAL]

Would you confidently send this email exactly as written?

YES

PASS

Anything else

FAIL

Rewrite.

---

# Final Principle

The email should feel like one experienced professional starting a useful conversation
with a possible manager, colleague, owner, or recruiter.

Not marketing.

Not AI.

Not a mass application.

Just a clear, credible reason to consider a possible fit.

## Review Overview

Once the review is complete, output the judgement using the following syntax:

EMAIL QA

Recipient / Mode...................... [NAME / MODE]
Fact & Consent Check.................. PASS
Gate Check (Human Test)............... PASS
AI Test............................... PASS
Corporate Buzzword Test............... PASS
Generic Application Test.............. PASS
Recipient & Skimmability Test......... PASS
Relevance & Interest Test............. PASS
Role-Fit Evidence Test................ PASS
Personalization Test.................. PASS
One Idea Test......................... PASS
CTA Test.............................. PASS
Adjective Test........................ PASS
"Could" Test.......................... PASS
Reading Level......................... PASS
Paragraph Test........................ PASS
Word Count............................ PASS
Rewrite Test.......................... PASS
Remove One Sentence Test.............. PASS
Forward Test.......................... PASS
Memory Test........................... PASS
"Why Them?" Test...................... PASS
Final Gate............................ PASS

Overall: PASS

Required changes:
None.

If any test fails, set `Overall` to `FAIL`, name the failed test and sentence, and list
the smallest changes required. Do not use a numeric score: every required test must pass.
