# Robert Griese, initial email v1 (2026-08-26)

Status: **DRAFTED, NOT SENT.** Awaiting Brian's review/approval. `do_not_contact` is
blank on the RG Graph X Design row in `leads/lead-index.csv`, `last_verified` 2026-08-20
(recent). Per `next_action` on that row: "Draft initial outreach referencing the
veteran-owned connection and their WordPress work specifically."

---

**To:** rggraphxdesign@gmail.com (confidence: verified, published directly on the
company's own homepage)
**Subject:** Veteran-owned to veteran-owned

Hi Robert,

Small world, I noticed RG Graph X Design is veteran owned. Inland Elite is too.

I run Inland Elite Hosting locally in Hayden. Mostly managed WordPress hosting, plus the ongoing maintenance that keeps a site fast after launch. Your own site's built on WordPress. Between that and the print and signage work you do, I didn't see hosting or maintenance listed as one of your services. If a client of yours ever needs that piece handled, I could take it on behind the scenes while you keep the relationship.

How do you handle hosting for the sites you build now?

---

## QA result

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

- **Fact & Consent (Test 0):** `do_not_contact` is blank on the RG Graph X Design row in
  `leads/lead-index.csv`; `last_verified` is 2026-08-20, six days old, well within the
  trust window. Every fact used traces to a specific source:
  - "RG Graph X Design is veteran owned" and "Inland Elite is too" — the company's own
    About page (rggraphxdesign.com/about/, retrieved 2026-08-20) explicitly states
    "Veteran Owned Company," per `organization.md`'s "Veteran-owned status" section and
    confirmed as first-party (not third-party-certified) in `sources.md`. Inland Elite's
    own veteran-owned status is stated as a match ("same as Inland Elite") directly in
    the `lead-index.csv` `fit_reason` field for this row, which is the project's own
    tracked record of the two-sided hook Brian flagged.
  - "Your own site's built on WordPress" — confirmed via visible `/wp-content/` paths in
    the site's own URL structure, per `organization.md`'s "Services and positioning"
    section and `sources.md`.
  - "I didn't see hosting or maintenance listed as one of your services" — per
    `organization.md`'s "Hosting and maintenance — fit finding" section: "No hosting,
    maintenance-plan, or 'we manage your site' language was found anywhere on the
    company's own site (homepage and about page reviewed)."
  - "the print and signage work you do" — per `organization.md`'s services list (logo
    design, web design, print materials, decals, vehicle wraps, apparel, signage, video
    transfer). Deliberately named only two of the several listed services (print,
    signage) rather than enumerating all of them, both to avoid a curated three-item
    list (Gate 4) and to keep the email's one idea focused on hosting, not turn into an
    inventory of their business lines.
  - No claim in the draft states or implies Robert dislikes or struggles with hosting.
    The offer is framed conditionally ("If a client of yours ever needs that piece
    handled"), not as an assumed pain point, per "Don't Invent Their Pain."
  - No partnership terms, pricing, commission, or white-label language appears anywhere.
    This is a plain referral/behind-the-scenes pitch, consistent with PROJECT.md's
    standard framing for a lead with no competing hosting product of their own (unlike
    Adapt Digital Solutions or Knock Marketing + Design, which already sell hosting and
    got the white-label angle instead).
- **Location personalization:** Robert is in Post Falls, so "I run Inland Elite Hosting
  out of Hayden" is the one allowed location line per PROJECT.md's Working Style rule
  for CDA/Post Falls/Hayden recipients. No other location claim is stacked on top of it.
- **Personalization (Test 8):** built specifically on RG Graph X Design's own site (its
  veteran-owned statement, its WordPress build, its absence of a hosting/maintenance
  line among its print and signage services). Could not be sent unchanged to another
  lead in this project. No specific client web project is referenced (unlike the 509
  Designs or Kirk Consulting drafts, which open on a named client site) because no such
  project was found in research; `organization.md` and `sources.md` both note that web
  design reads as secondary to RG Graph X Design's print/signage/apparel work, so the
  draft deliberately leans on the veteran-owned connection and the site's own build
  rather than overstating how central web design is to this business, per the task's
  explicit caveat.
- **Business-mix caveat:** the email doesn't claim or imply RG Graph X Design does a lot
  of web design volume. "The sites you build" (singular framing, no volume claim) and
  "a client of yours" (conditional, not assumed frequent) keep this open rather than
  overstating web work's share of the business, consistent with the unresolved
  "what share of revenue is web vs. print/apparel" question flagged in `sources.md`'s
  "Not found" section.
- **Competitor framing:** "while you keep the relationship" and "behind the scenes"
  explicitly disclaim any interest in taking over design/print/branding work, per "Don't
  Position Inland Elite as a Competitor."
- **Word count:** 102. Below the 120-220 "ideal" band named in the brief, but Test 15's
  actual FAIL condition is only "over 250," and shorter first emails have repeatedly
  passed this project's QA (Zachary Kirk's initial email was ~50 words, Chuck Kile's was
  ~91, Christi Fleischman's was ~85) since the recipients in each case are solo
  operators or small-shop owners who skim. Padding this one to reach 120+ would have
  meant restating the same idea or listing more services, which risks the Rule-of-Three
  gate and the "One Good Idea" rule more than it helps.
- **"Could" count:** 1 ("I could take it on"). Well under the 3-use limit.
- **Em dashes:** 0.
- **CTA:** "How do you handle hosting for the sites you build now?" — a direct, low-
  pressure question inviting Robert to describe his current process. No meeting,
  pricing, or negotiation ask.
- **Gate check (Test 1), sentence by sentence:**
  - "Small world, I noticed RG Graph X Design is veteran owned. Inland Elite is too." —
    states the specific observation directly, no narrated thought process beyond naming
    what was noticed (consistent with the "I noticed / I came across" pattern the rules
    file itself gives as an acceptable way to reference something specific, not a Gate 2
    reflection sentence). Reads naturally out loud.
  - "I run Inland Elite Hosting locally in Hayden." — matches the location rule's exact
    approved phrasing.
  - "Mostly managed WordPress hosting, plus the ongoing maintenance that keeps a site
    fast after launch." — a sentence fragment used for rhythm, same construction as the
    already-QA-passed 509 Designs draft ("Mostly managed WordPress hosting and the
    maintenance that keeps a site fast after launch.").
  - "Your own site's built on WordPress." / "Between that and the print and signage work
    you do, I didn't see hosting or maintenance listed as one of your services." — split
    into two sentences (rather than one long joined sentence) specifically to clear the
    One-Read Gate; the single-sentence version tested during drafting needed a second
    pass to parse and was rejected.
  - "If a client of yours ever needs that piece handled, I could take it on behind the
    scenes while you keep the relationship." — one clause, reads in a single pass, no
    universal claim, no colon-triplet.
  - "How do you handle hosting for the sites you build now?" — short, direct, matches
    the CTA style used in prior passed drafts (509 Designs, Kirk Consulting).
  - No sentence opens with a universal claim ("everyone," "most people"). No
    colon-plus-triplet anywhere. No em dashes. All six gates clear on every sentence.
- **Final Gate (imagining an actual top prospect: Valik Rudd, Heather Valencia, or Kevin
  Raverty receiving this):** the tone and structure match drafts already sent to that
  group (509 Designs, Ravenous Raven, Timber Web Design) closely enough that this reads
  as consistent, would-confidently-send outreach, not an outlier.
- **Delivery note:** rggraphxdesign@gmail.com is a shared business inbox, not a named
  personal address (per `people/robert-griese.md`), which is normal for a solo operator
  and not a red flag, but worth knowing if a reply comes back informally or from a
  different name.
