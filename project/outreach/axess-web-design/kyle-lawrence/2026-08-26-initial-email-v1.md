# Kyle Lawrence, initial email v1 (2026-08-26)

Status: DRAFTED, NOT SENT. Awaiting Brian's approval before sending.

---

**To:** axesswebdesign@gmail.com
**Subject:** Who hosts your WordPress sites?

Hi Kyle,

Your FAQ page recommends WordPress for SEO-heavy or growing sites. That's exactly the kind of site where hosting quality shows up in load time and search rankings.

I run Inland Elite Hosting locally in Hayden. Mostly managed WordPress hosting and the upkeep that keeps a site fast after launch.

You work directly with clients with no agency handoffs. I run things pretty much the same way. For the WordPress builds specifically, that's something I could handle behind the scenes while you keep the design and SEO work.

How are you handling hosting on your WordPress sites right now?

Brian Clark
Inland Elite Hosting

---

## QA result

EMAIL QA

Fact & Consent........... PASS
Human Gates.............. PASS
AI / Buzzwords........... PASS
Sales Tone............... PASS
Personalization.......... PASS
One Idea.................. PASS
CTA...................... PASS
Readability.............. PASS
Length................... PASS
Em Dashes................ PASS
Final Send Test.......... PASS

Overall: PASS

Failures:
None.

Notes:

- **Test 0 (Fact & Consent):** `do_not_contact` is blank on the Axess Web Design row in `project/leads/lead-index.csv` (column confirmed empty, not TRUE). `last_verified` is 2026-08-20, six days before this draft, not stale. Every fact used is traceable:
  - "Your FAQ page recommends WordPress for SEO-heavy or growing sites" — direct paraphrase of `organization.md` line 21 / `sources.md` line 9, quoting axesswebdesign.com/web-design-faq/ (retrieved 2026-08-20): "WordPress offers the most flexibility and is best for SEO-heavy or growing sites."
  - "You work directly with clients with no agency handoffs" — paraphrase of `organization.md` line 14, quoting axesswebdesign.com/about/: "You work directly with Kyle — no agency overhead, no project handoffs, no runaround."
  - "Brian runs Inland Elite Hosting locally in Hayden" — per `PROJECT.md` Working Style location-personalization rule: recipient is in Post Falls (`organization.md` line 7, `sources.md` line 5), so "Brian runs the business out of Hayden" is the one allowed location line. No other location claim is stacked (Post Falls, CDA, Spokane are not mentioned about Brian).
  - No claim that any specific named client site runs on WordPress — per the task constraint and `people/kyle-lawrence.md` line 26 ("Do not assume all of his client sites are WordPress — confirm before referencing 'your WordPress sites' broadly... frame around WordPress specifically"), the email frames WordPress as a category/question ("your WordPress sites," "the WordPress builds specifically") rather than inventing or naming a specific project, since no research file names one.
  - No mention of the $99/mo Care Package — the email stays on hosting/infrastructure only, which `organization.md` line 23 and `kyle-lawrence.md` line 19 identify as the non-competing angle (a maintenance-framed pitch would overlap the Care Package; a hosting-framed one does not).
  - No partnership terms, pricing, or white-label language offered — this is a first-contact plain referral pitch per the task constraint, consistent with `email-writing-rules.md` "Don't Invent Partnership Terms."
- **Human Gates (Test 1):** checked sentence by sentence against all six gates. No sentence narrates how the idea arose (Gate 2) — the FAQ observation and the "no agency handoffs" parallel are both stated as direct facts, not "it occurred to me" framing. No universal claims (Gate 3). No colon-plus-list construction anywhere (Gate 4). Longest sentence ("For the WordPress builds specifically, that's something I could handle behind the scenes while you keep the design and SEO work") mirrors the structure of the closing offer sentence in the 509 Designs v3 email that already passed QA, and reads fine at talking speed (Gate 5). Every sentence would plausibly be said out loud to someone (Gate 6).
- **AI/Buzzwords (Test 2/3):** no phrases from the "Never Sound Like AI" list, no corporate buzzwords.
- **Sales Tone (Test 4):** no sales-language phrases from the banned list. The email explicitly frames the offer around hosting/infrastructure only ("while you keep the design and SEO work"), so it should not read as Inland Elite trying to take over Kyle's design or SEO relationship with clients — follows "Don't Position Inland Elite as a Competitor."
- **Personalization (Test 8):** built entirely from two facts unique to Axess's own site copy (the FAQ's WordPress recommendation, and the "no agency handoffs" positioning line). Could not be sent unchanged to another lead — those two lines don't apply to, say, a multi-person agency or a lead whose site doesn't make that specific FAQ claim.
- **One Idea (Test 9):** the single point is "Brian could host the WordPress sites Kyle builds while Kyle keeps the design/SEO relationship." Nothing else is introduced.
- **CTA (Test 10):** closing question ("How are you handling hosting on your WordPress sites right now?") asks him to explain his current setup — a reply/conversation-starter question, not a meeting, sale, or pricing ask.
- **Don't Invent Their Pain:** the email does not claim Kyle dislikes or struggles with hosting. It offers the option ("that's something I could handle") and asks a neutral, open question about his current process, rather than assuming he currently self-hosts anything or wants to stop. This was a deliberate judgment call — an earlier draft considered a conditional "if hosting isn't something you want to keep managing yourself" clause, but that was cut because `organization.md` line 22 indicates Axess defers hosting/domain questions to "your CMS provider," meaning there's no confirmed evidence Kyle currently hosts anything himself to be relieved of. Assuming that would have been an invented pain point.
- **Word count:** 100 words (including the "Hi Kyle," greeting; signature not counted), which is below the 120-220 ideal band but well under the 250 max. Flagging this rather than treating it as an automatic pass: the 509 Designs v3 draft (`outreach/509-designs/kevin-raverty/2026-08-08-initial-email-v3.md`) passed QA at a similarly short 102 words with the same three-idea structure (observation, offer, question), so a tight, skimmable length under the ideal band has precedent as acceptable rather than a defect, especially given the Executive Test favors brevity. "Could" count: 1. Zero em dashes.
- **Paragraph length:** four short paragraphs (2, 2, 3, and 1 sentences) plus the closing question, none exceeding roughly 3 lines at normal wrap width — kept intentionally short and varied in rhythm rather than one longer block, per "Avoid Perfect Structure."
- **Final Gate:** imagined this landing with Valik Rudd, Heather Valencia, or Kevin Raverty (the placeholder reviewers in `email-qa.md`) as well as with Kyle Lawrence specifically — reads as a short, specific, low-pressure note from one solo operator to another, not a form pitch. Would send as written.
