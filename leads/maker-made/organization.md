# Maker + Made

## Organization

- Organization: Maker + Made (branding/creative agency; small team, not a solo shop)
- Website: https://www.maker--made.com/
- Organization type: "Strategy-first creative agency" — brand identity, website design/development, packaging & print, product photography, content, environmental/merch design.
- Founded in early 2019 by two co-founders/best friends, Millie Schnebly and Brittany Stodgell. Per the site's own `/studio` page, founding-story language ("founded in 2019 by two best friends") appears without naming them on that page directly, but the names are corroborated by search-indexed team-page content and by RocketReach/SignalHire listings (see `sources.md`).
- **Physically based in Spokane, WA** — 304 W Pacific Ave, #290, Spokane, WA 99201 (confirmed footer/contact address). This corrects the initial CSV framing as a "Sandpoint studio": the site has SEO-oriented `/locations-sandpoint` and `/locations-spokane` landing pages targeting several North Idaho/Inland Northwest markets, but Sandpoint is a service area, not a physical office. Sandpoint, Bonner County, Ponderay, Sagle, Dover, Hope, and Priest River are named as part of the service area on `/locations-sandpoint`.
- Team (per `/studio` page, retrieved 2026-08-10): Millie Schnebly (Managing Partner), Brittany Stodgell (Creative Partner), Jazmin Ely (Senior Project Manager), Sarina McKenna (Lead Digital Designer), Brennah Schmelzer (Graphic Designer), Aimee Skaer (Graphic Designer). A separate fetch of the `/hire-us` page returned a slightly different title/name set for some support-staff roles (e.g., "Sarina Horn" as Lead Digital Designer instead of "Sarina McKenna," and Millie described as "Project Manager" rather than "Managing Partner") — likely either a fetch/summarization inconsistency or the page having changed between visits. Treat the co-founder identities and top-level titles (Millie Schnebly / Brittany Stodgell as owners) as solid since they're corroborated by multiple independent sources; treat the exact junior-staff roster as lower-confidence.

## Services and positioning

- Core services: brand identity/strategy, website design + development, packaging and print design, product photography, content creation, environmental design, merchandise design, naming/messaging, Amazon A+ content.
- **Website platforms offered, per the agency's own `/locations-spokane` page (retrieved 2026-08-10): "Custom Shopify Development" and "Custom Squarespace Development."** No WordPress offering is mentioned anywhere found on the site. The same page describes their process as "discovery, strategy, user experience planning, design, development, testing, and launch support" with no ongoing website maintenance, hosting, or retainer-based technical support service found — their retained/ongoing offering is oriented toward marketing and content, not site upkeep.
- The studio's own site (maker--made.com) itself runs on Squarespace (squarespace-cdn.com asset URLs).

## THE KEY QUESTION: are client sites WordPress-based? — No, confirmed otherwise

This was the single highest-priority open question for this lead. It is now answered with reasonable-to-high confidence: **client sites are Squarespace or Shopify, not WordPress.**

Evidence:

1. **Primary-source statement of service**: Maker + Made's own `/locations-spokane` page explicitly advertises "Custom Shopify Development" and "Custom Squarespace Development" as their two website platforms — no WordPress option listed.
2. **Direct inspection of 5 live client sites**, checked for platform-identifying markers (CDN asset URLs, e.g. `images.squarespace-cdn.com`, or Shopify `myshopify.com`/`/collections/` URL patterns) on 2026-08-10:
   - Nook Interiors (nookinteriors.com) — **Squarespace**. Footer explicitly reads "Site design by Maker and Made," directly confirming this as their own client work.
   - Bernardo Wills Architects (bernardowills.com) — **Squarespace**.
   - Mac & Jack's Brewing Co. (macandjacks.com) — **Squarespace**.
   - Indaba Coffee (indabacoffee.com) — **Squarespace** for the main site, with a separate Shopify subdomain (`indaba-coffee.myshopify.com`) for e-commerce.
   - Araza Beauty (arazabeauty.com) — **Shopify** (URL structure `/collections/...` is a Shopify signature).
3. Zero of the 5 sites checked showed any WordPress signature (`wp-content`, `wp-json`, `wp-includes`).

This is a sample of 5 out of roughly 12 case studies listed on the `/projects` page (Coppa Butchery, Roo Gardening, Roast House Coffee, Mountain Madness Soap Co., Honey & Soul, Zona Blanca/Lime Fish Salt, and The Light Factory were not individually platform-checked), so this is not exhaustive — but combined with the agency's own explicit "Squarespace / Shopify" service description, the pattern is consistent and coherent rather than a coincidence, and there's no contrary signal anywhere.

**Practical implication for Inland Elite's core offer (managed WordPress hosting):** Squarespace and Shopify are both fully-hosted, closed platforms — there is no separate hosting layer to hand off, no WordPress core/plugin maintenance, and no migration/infrastructure work of the kind Inland Elite specializes in. This isn't just "wrong CMS, ask them to switch" — it's a structural mismatch: their clients' sites don't have an external hosting need at all. The white-label/referral pitch built around WordPress hosting and maintenance has no natural entry point here.

## Why this is (or isn't) a good fit

- Positive: Legitimate, established small agency (7 years old, small team, real named clients) actively serving the North Idaho/Inland Northwest region from Spokane — matches PROJECT.md's "small branding and creative studios" category in general shape.
- Negative (significant): No WordPress in their toolkit and no hosting/maintenance offering of their own to hand off — the core hosting-partnership value proposition doesn't map cleanly onto Squarespace/Shopify client work. A partnership conversation here would need to be reframed (e.g., asking whether any legacy/inherited clients run WordPress, or whether they'd ever refer clients who need something Squarespace/Shopify can't do) rather than the standard "we'll take hosting/maintenance off your plate for the WordPress sites you build" pitch.

## Research status

- Website (`/`, `/studio`, `/locations-sandpoint`, `/locations-spokane`, `/hire-us`, `/projects`, and several individual case-study pages) reviewed via fetch on 2026-08-10.
- 5 live client websites independently checked for CMS platform signatures on 2026-08-10 (see above).
- Washington Secretary of State business-entity search (ccfs.sos.wa.gov) attempted but not completed — the search tool is a JavaScript single-page app that could not be queried via simple page fetch. Co-founder names/titles are corroborated through the site's own team page plus multiple independent third-party listings instead (see `sources.md`).
