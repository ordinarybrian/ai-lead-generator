# Nicholas Ries, initial email v2 (2026-08-31)

Status: **SENT 2026-08-31** to nicholasries@compassproductionamdg.com. Supersedes v1
(2026-08-26), which was drafted but never sent.

Angle change from v1: v1 opened by quoting his "No hosting markup. No forced
subscriptions." line and attributing it to "your pricing page." Brian flagged that there
is no pricing page in the site's navigation (the tier pages `/launch-site/`,
`/business-site/`, `/growth-site/` are reachable only via the sitemap, and the page at
`/pricing/` is password-protected). The quote itself is accurate and still live on
`/launch-site/` as of 2026-08-31, but the "your pricing page says" framing was wrong.

v2 drops the quote entirely and reframes the pitch per Brian's direction (2026-08-31):
instead of "call me when hosting breaks," position Inland Elite as a managed local
hosting and domain option Nicholas can offer clients who don't want to set up their own
Hostinger/SiteGround account. Still a plain referral/handoff angle, not white-label
(no white-label or Agency Hosting language, consistent with `people/nicholas-ries.md`).
"Premium" was deliberately not used as a label per email-writing-rules.md's "Never
Oversell What You're Offering"; the offering is described concretely instead (local,
managed, covers the domain).

Location line: Nicholas is in Post Falls, so per PROJECT.md's Working Style rule the only
location claim is "out of Hayden." No other location claim stacked on top.

No manual signature block, per `email-rules/signature.md` (normal email, client appends
the standard signature on send).

---

**To:** nicholasries@compassproductionamdg.com (verified via `mailto:` link in raw HTML
on both the homepage and /contact page; see `leads/compass-production-llc/leadership.md`)
**Subject:** hosting for the clients who don't want to set it up themselves

### As sent (Brian's wording)

Hi Nicholas,

Right now when someone hires you for a site, they set up their own Hostinger or SiteGround account and own it themselves. That keeps things clean for your, but it also leaves the client who doesn't want to deal with that side of it doing it anyway, right?

I run Inland Elite Hosting out of Hayden. Managed WordPress hosting, plus the domain side and the upkeep after a site launches. For the clients who'd rather hand that part to someone local, I could be the option you point them to instead of a self-serve host. You keep building the sites. I keep them running.

When a client doesn't want to manage their own hosting, what do you do now?

### Brian's edits to the v2 draft

- "That keeps things clean" -> "That keeps things clean for your" (typo for "for you";
  recorded as sent, not corrected in this log).
- "...doing it anyway." -> "...doing it anyway, right?" (softening tag question added).
- No other changes from the drafted v2.

---

## QA result (of the drafted v2, before Brian's edits)

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

Notes:

- **Fact & Consent (Test 0):** `do_not_contact` blank on the Compass Production LLC row.
  `last_verified` 2026-08-20; the opening fact was re-confirmed live on 2026-08-31 via a
  fresh fetch of `https://compassproductionamdg.com/launch-site/` ("hosting and domain
  registration are purchased separately through your own account"; recommends Hostinger
  and SiteGround). "You build on WordPress" traces to the generator meta tags in
  `organization.md`. No claim that Nicholas dislikes his current setup; the sentence
  about the client "doing it anyway" is about a subset of his clients, framed as a
  conditional the email then offers to solve, per "Don't Invent Their Pain."
- **One Idea (Test 9):** single point: Inland Elite could be the managed local hosting
  (and domain) option he offers clients who don't want to DIY a self-serve host. No
  white-label, pricing, or meeting ask.
- **CTA (Test 10):** "When a client doesn't want to manage their own hosting, what do
  you do now?" invites him to describe his current process. Low-pressure.
- **Counts:** ~105 words. "Could" count: 1. Em dashes: 0.
- **Personalization (Test 8):** built on his own currently-live hosting model (clients
  self-serve Hostinger/SiteGround, client-owned accounts). Could not be sent unchanged
  to another lead.

- **Brian's edits (per [[feedback_qa_gate_flags_on_user_edits]]):** the "for your" typo
  is the only QA-relevant item, and it's a plain typo in an already-sent email, not a
  gate issue. The ", right?" tag question is conversational and consistent with Gate 1.
  Nothing to action; noted for a faithful record.
