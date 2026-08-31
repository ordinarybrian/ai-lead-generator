# Nicholas Ries, initial email v1 (2026-08-26)

Status: SUPERSEDED, NEVER SENT. Replaced by `2026-08-31-initial-email-v2.md` (sent
2026-08-31). Brian flagged that the "your pricing page says it plainly" framing here was
wrong: there is no pricing page in the site nav, and the quoted line lives on the
unlinked `/launch-site/` tier page. v2 drops the quote and reframes around offering a
managed local hosting/domain option to his clients.

---

**To:** nicholasries@compassproductionamdg.com (verified via `mailto:` link in raw HTML on both the homepage and /contact page; see `leads/compass-production-llc/leadership.md`. Displayed on-page with a capital "N" as a cosmetic artifact; local part of an email address is case-insensitive in practice, so lowercase is used here.)
**Subject:** your "no hosting markup" line

Hi Nicholas,

Your pricing page says it plainly: "No hosting markup. No forced subscriptions." That line's on the $150 launch tier and the bigger builds too. You're building all of it in WordPress and Elementor.

I run Inland Elite Hosting out of Hayden, managed WordPress hosting for other designers around North Idaho. If a client of yours ever wants more than a self-serve host, that's the part I could handle. You'd keep the design work, I'd just be the one they call if hosting breaks.

Who do you usually send people to for hosting once a site's live?

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

- **Fact & Consent (Test 0):** `do_not_contact` is blank on the Compass Production LLC row in `lead-index.csv` (14th column, empty). `last_verified` is 2026-08-20, six days before this draft, current for a solo freelancer's site content. Every fact referenced traces to a source:
  - The quote "No hosting markup. No forced subscriptions." is a direct, partial quote (first two of three sentences on his own site) sourced to `leads/compass-production-llc/organization.md` and `sources.md`, both citing `https://compassproductionamdg.com/launch-site/`, retrieved 2026-08-20. The third sentence on the actual page ("No hidden upsells.") was deliberately omitted from the quote to avoid assembling a three-item list in the email (see Gate 4 note below), not because it's inaccurate.
  - "$150 launch tier" matches the Launch Site price in `organization.md` and `sources.md` ("$150 one-time").
  - "the bigger builds too" refers to the Business Site ($500-$1,000) and Growth Site ($1,000-$3,000) tiers, both confirmed in `organization.md`/`sources.md` to carry the same no-bundled-hosting language ("Client-Owned Hosting," "hosting and domain registration are not bundled").
  - "You're building all of it in WordPress and Elementor" is sourced to the generator meta tags independently confirmed via curl on the raw HTML (`organization.md`: "WordPress 7.0.4," "Elementor 4.1.4," "WooCommerce 10.9.1"), not just marketing copy.
  - "self-serve host" characterizes the Hostinger/SiteGround recommendation and "Client-Owned Hosting" framing from the three pricing-tier pages, not an invented detail.
  - No claim that Nicholas or his clients dislike, struggle with, or want to stop handling hosting. The email frames Inland Elite as a conditional option ("If a client of yours ever wants more...") rather than an assumed pain point, per "Don't Invent Their Pain" in `email-writing-rules.md`.
  - No partnership terms, commission, pricing, or white-label language mentioned or implied. This is a plain referral/handoff pitch consistent with PROJECT.md's guidance for a solo, ~2-year-old freelance practice ("standard freelancer-handoff pitch, not the white-label/Agency Hosting angle," per `people/nicholas-ries.md`).

- **Location personalization:** Nicholas is in Post Falls, so the only location line used is "I run Inland Elite Hosting out of Hayden," per PROJECT.md's Working Style rule for recipients in CDA/Post Falls/Hayden. No other location claim is stacked on top of it (his own service-area list from `organization.md` was deliberately not repeated back at him, to keep to a single location claim).

- **Human Gates (Test 1):**
  - Gate 1 (Text-a-Friend): every sentence reads like something said out loud, not written for an essay.
  - Gate 2 (Reflection-Sentence): no sentence narrates how the observation was arrived at (no "It occurred to me," "I noticed," etc. used as a framing device). The email states the observed fact directly in the first sentence.
  - Gate 3 (Universal-Claim): no sentence opens with a generalization about "everyone" or "most people."
  - Gate 4 (Rule-of-Three): the one colon in the email ("says it plainly: ...") introduces a direct two-sentence quote from Nicholas's own site, not a curated list I assembled to unpack a claim. The third clause of his actual on-site statement ("No hidden upsells.") was deliberately left out specifically so the quote wouldn't read as a triplet. No other colon-plus-list construction appears anywhere in the draft.
  - Gate 5 (One-Read): sentences are short and single-clause or two-clause at most; read aloud at talking speed without needing a second pass.
  - Gate 6 (Stranger-at-a-Bar): each line is something Brian could plausibly say out loud to someone he just met, including the closing question.

- **AI / Buzzwords (Tests 2-3):** no phrases from the "Never Sound Like AI" or "Avoid Corporate Buzzwords" lists, or close paraphrases of them, appear anywhere in the draft.

- **Sales Tone (Test 4):** no "I'd love to," "we're offering," or similar sales phrasing. The email explicitly disclaims any interest in his design work ("You'd keep the design work, I'd just be the one they call if hosting breaks"), directly following "Don't Position Inland Elite as a Competitor."

- **Personalization (Test 8):** could not be sent unchanged to another lead. It quotes Nicholas's exact pricing-page language, cites his specific $150 launch-tier price point, and names his specific tech stack (WordPress/Elementor). The angle (plain handoff/referral pitch, no white-label mention) matches the solo-freelancer lead type per `email-writing-rules.md`'s "Match the Outreach to the Lead Type" and the specific guidance in `people/nicholas-ries.md`.

- **One Idea (Test 9):** single point, statable in one sentence: "Since you already tell clients you won't mark up their hosting, I could be the option you point them to when they want more than a self-serve host." No second idea (no white-label pitch, no pricing, no meeting ask) is introduced.

- **CTA (Test 10):** "Who do you usually send people to for hosting once a site's live?" is a small, low-pressure question inviting him to describe his current process. No meeting, sale, or pricing ask.

- **Word count / "Could" count / Em dashes:** 103 words total including greeting and signature (verified via `wc -w`), consistent with the two prior passing initial-email drafts in this project (509 Designs v1 at 116 words, v3 at 102 words), both of which sit below the 120-220 "ideal" band but were judged PASS on Length since Test 15's only explicit FAIL condition is exceeding 250. One use of "could" (well under the 3+ FAIL threshold). Zero em dashes.

- **Final Gate:** pictured against this project's actual top prospects (Valik Rudd, Heather Valencia, Kevin Raverty) as the standard for "would Brian confidently send this exactly as written" — yes. It matches the tone and structure of the Kevin Raverty (509 Designs) initial email that already shipped and drew a comparison well, applied to research specific to Compass Production LLC.

- **Caution carried forward from `people/nicholas-ries.md`:** the site's contact form displays a "No soliciting, Clients only" notice. This email is sent directly to his verified personal address rather than through that form, and is short, specific, and clearly written for his business rather than a mass pitch, consistent with the file's guidance that this is standard freelancer boilerplate aimed at spam rather than a hard signal against genuine local-partnership outreach.
