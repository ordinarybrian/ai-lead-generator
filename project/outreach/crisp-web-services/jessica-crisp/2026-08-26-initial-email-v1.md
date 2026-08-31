# Jessica Crisp, initial email v1 (2026-08-26)

Status: **SENT 2026-08-31** to jessicacrisp@crispwebservices.com, with Brian's edits (see
"As sent" below).

Angle: plain referral/behind-the-scenes pitch, not white-label -- Crisp Web Services has
no branded, monetized hosting product of its own to protect (see
`leads/crisp-web-services/organization.md`'s "Hosting posture" section), just an informal
offer to arrange SiteGround hosting for clients who ask. Per this lead's `next_action` in
`lead-index.csv`, the draft acknowledges that informal arrangement without assuming she
resents it or wants to stop doing it -- it asks rather than asserts, per
"Don't Invent Their Pain" in `email-rules/email-writing-rules.md`.

Location line: Jessica is in Spokane Valley, so per PROJECT.md's Working Style rule for
Spokane recipients, the only location claim used is the general regional phrase ("I run
Inland Elite Hosting out of North Idaho"), not the Hayden-specific phrasing reserved for
CDA/Post Falls/Hayden recipients. No other location claim is stacked on top of it.

No manual signature block included -- per `email-rules/signature.md`, this is a normal
email (not a contact form or other non-email channel), so Brian's email client appends
the standard signature automatically on send.

---

**To:** jessicacrisp@crispwebservices.com (confirmed via `mailto:` link in raw HTML on
both her /about and /contact pages -- see `leads/crisp-web-services/people/jessica-crisp.md`)
**Subject:** the SiteGround line on your FAQ page

Hi Jessica,

Your FAQ page mentions that clients can go through you for hosting, and you'll buy and manage the SiteGround account for them.

I run Inland Elite Hosting out of North Idaho. Mostly managed WordPress hosting, plus the migrations and maintenance that come with keeping a site running after launch. Since you build exclusively on WordPress, that's pretty much all I do.

If it'd help to have somewhere local to send those hosting requests, that's something I could take on. You wouldn't be the one holding the account. Design and marketing stay entirely yours. I'd just be the hosting behind it.

Is that something you end up managing for most clients who ask, or is it more of an occasional thing?

---

## As sent (2026-08-31, Brian's wording)

Hi Jessica,

Your FAQ page mentions that clients can go through you for hosting, and you'll buy and manage the SiteGround account for them.

I run Inland Elite Hosting out of North Idaho. Mostly managed WordPress hosting, plus the migrations and maintenance that come with keeping a site running after launch. Since you build exclusively on WordPress, that's pretty much what I do.

If it'd help to have somewhere local to send those hosting requests, that's something I could take on. You wouldn't be the one holding the account. Design and marketing stay entirely yours. I'd just be the hosting behind it. You could send clients over or white-label the hosting yourself.

Is that something you end up managing for most clients who ask, or is it more of an occasional thing?

### Brian's edits to the draft

- "that's pretty much all I do" -> "that's pretty much what I do."
- Added: "You could send clients over or white-label the hosting yourself."

### Note on the white-label addition (per [[feedback_qa_gate_flags_on_user_edits]])

The added sentence introduces white-label, which the draft had deliberately left out
since Crisp has no branded hosting product to protect. Two QA-relevant points, neither
blocking (email already sent):

- **One Idea (Test 9):** the email now carries two options instead of one (send clients
  over, or white-label). Mild "One Good Idea" stretch, not a hard fail.
- **Don't Invent Partnership Terms / PROJECT.md:** white-label is a real standing option
  in PROJECT.md's Commercial Terms and is explicitly allowed to be "raised as a
  possibility" with freelancers, with no rates attached. Brian's sentence does exactly
  that (no pricing, framed as "yourself"), so it stays within the established
  positioning. Also now bumps "could" to 2 uses (still under the 3+ threshold).

---

## QA result (of the original draft, before Brian's edits)

EMAIL QA

Fact & Consent........... PASS
Human Gates............... PASS
AI / Buzzwords............ PASS
Sales Tone................ PASS
Personalization........... PASS
One Idea.................. PASS
CTA....................... PASS
Readability............... PASS
Length.................... PASS
Em Dashes................. PASS
Final Send Test........... PASS

Overall: PASS

Failures:
None.

Notes:

- **Fact & Consent (Test 0):** `do_not_contact` is blank on the Crisp Web Services row in
  `lead-index.csv`, and `last_verified` is 2026-08-20, the same date the underlying facts
  were fetched. Every claim in the draft is traceable:
  - "Your FAQ page mentions that clients can go through you for hosting, and you'll buy
    and manage the SiteGround account for them" paraphrases the FAQ's own words ("You can
    also choose to go through us to get a hosting package. We will purchase and manage
    everything for you"), sourced in `organization.md`'s "Hosting posture" section and
    `sources.md`.
  - "Since you build exclusively on WordPress" paraphrases the FAQ's own statement ("We
    exclusively use Word Press to build our websites"), same source.
  - The email does not claim or imply Jessica dislikes or wants to stop the informal
    SiteGround arrangement -- it's offered as a conditional ("if it'd help") and closed
    with an open question about how often it comes up, not an assumed pain point.
  - No partnership terms, referral commission, or white-label language appears anywhere.
    This is framed as a plain "I could take this piece on" offer, consistent with the
    task instruction that this lead gets a referral pitch (not white-label), since she
    has no branded/monetized hosting product to protect.

- **Human Gates (Test 1):** Read sentence by sentence.
  - Opening sentence states the specific FAQ fact directly, no reflection framing ("It
    occurred to me..." etc.) -- passes Gate 2.
  - No "everyone/most people" framing anywhere -- passes Gate 3.
  - "Mostly managed WordPress hosting, plus the migrations and maintenance that come with
    keeping a site running after launch" pairs two items with "and," not a curated
    three-item list -- passes Gate 4 (mirrors the style-reference email's "Mostly managed
    WordPress hosting and the maintenance that keeps a site fast after launch").
  - No stacked colon/em-dash/list constructions in any sentence -- passes Gate 5 (One-Read).
    The closing paragraph was deliberately split into four short sentences instead of one
    longer compound sentence for this reason.
  - Every sentence reads like something said out loud to a new acquaintance, not essay
    prose -- passes Gates 1 and 6.

- **Personalization (Test 8):** Built entirely on Crisp Web Services' own FAQ page
  wording (the SiteGround pass-through offer, the WordPress-exclusive claim) plus the
  Spokane-specific location phrasing. This could not be sent unchanged to another lead --
  the opening sentence names a specific offer only Crisp Web Services makes on its own
  site, and the location line is the Spokane-specific phrase, not the Hayden phrase used
  for CDA/Post Falls/Hayden leads.

- **Sales Tone / Not a Competitor (Test 4):** "Design and marketing stay entirely yours.
  I'd just be the hosting behind it" directly disclaims any interest in her design or
  marketing work, per "Don't Position Inland Elite as a Competitor."

- **One Idea (Test 9):** Single point -- Inland Elite could take the SiteGround
  hosting/account-management piece off her plate, if that'd be useful, leaving her design
  and marketing work untouched.

- **CTA (Test 10):** Closing question ("Is that something you end up managing for most
  clients who ask, or is it more of an occasional thing?") asks her to describe her
  current process. Small, low-pressure, not a meeting or pricing ask.

- **Counts:** 122 words (within the 120-220 ideal band). "Could" count: 1. Em dash count:
  0. Longest paragraph is 4 short sentences, well under a 4-line wrap at normal email
  width.

- **Final Gate:** Pictured this going to Jessica Crisp herself, the actual intended
  recipient, and cross-checked the bar against this project's other current top
  prospects (Valik Rudd, Heather Valencia, Kevin Raverty) per the placeholder list in
  `email-qa.md`. Confidently sendable as written -- specific, low-pressure, doesn't
  overclaim, and doesn't assume she wants to stop doing the informal SiteGround
  arrangement, just asks about it.
