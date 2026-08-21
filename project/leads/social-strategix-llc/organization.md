# Social Strategix LLC

## Organization

- Organization: Social Strategix LLC
- Website: https://www.socialstrategix.com/
- Organization type: Solo freelance web design business run by Jordan Quast — the only named person anywhere on the site.
- Address: Coeur d'Alene, ID 83815 (per site content; no street address published in reviewed pages).
- Phone: (208) 691-1588 — consistent across the company's own site and search-aggregator listings.
- Contact email domain differs slightly from the website domain: the site is socialstrategix.com, but the confirmed contact email is at socialstrategixllc.com. Both resolve to the same business (site content, phone number, and Jordan Quast's name all match); not treated as a red flag, just noted.

## Services and positioning

- Per the site: "professional, functional, and affordable websites for small businesses," emphasizing speed — "LAUNCH YOUR NEW WEBSITE IN AS LITTLE AS 1 WEEK!" — versus a stated 60–90 day industry-typical timeline.
- Sales model is a "free design demo" — the site is built and shown before any payment is required ("we are willing to design your site for free. If you don't love it, you pay nothing"), with a stated policy that all payments are final and non-refundable once accepted.
- No specific mention of WordPress anywhere in reviewed content. Technical inspection of the site's own raw HTML (retrieved 2026-08-20) found **no WordPress markers** (`wp-content`, `wp-includes`, or a WordPress generator tag are all absent), and no markers for Wix, Squarespace, Shopify, or similar common builders either. The asset file paths use a fingerprinted `/assets/application-[hash].js` / `/assets/modernizr-[hash].js` pattern characteristic of a Ruby-on-Rails-style asset pipeline, not a WordPress or typical no-code-builder site. This strongly suggests Social Strategix's own site — and by extension the client sites it produces, which are plausibly built on the same underlying platform — run on a custom or shared proprietary platform, not WordPress. Not confirmed with full certainty (the specific platform/vendor was not identified), but the WordPress mismatch itself is reasonably well supported by direct technical inspection.

## Hosting posture — critical fit finding

**Social Strategix LLC sells its own bundled hosting/maintenance product as a standard, disclosed part of every engagement — a direct, monetized overlap with Inland Elite's core offering.**

- Pricing page (socialstrategix.com/pricing, retrieved 2026-08-20): **$999 one-time** setup fee (first 5 pages; additional pages $100 each) plus **$99/month** recurring fee described as "Worry-Free Cloud Hosting," covering hosting, SSL certificate, traffic analytics, and "update support."
- This is not an optional add-on or pass-through recommendation (contrast with Crisp Web Services' informal SiteGround referral) — it is priced, named as a specific product ("Worry-Free Cloud Hosting"), and appears to be the standard ongoing offering for every client, not an occasional upsell.
- Combined with the non-WordPress platform signal above, this closely parallels the AllerGale Design disqualification pattern (own hosting product + non-WordPress/proprietary-leaning platform) rather than the softer Crisp Web Services or Ever Marketing "existing retainer on a WordPress stack" pattern.

## Why this is not a good fit

- A referral/partnership pitch would ask Jordan Quast to send clients to a hosting provider that competes directly with a specifically named, monthly-billed product ("Worry-Free Cloud Hosting") that is already central to how the business is priced and marketed — this is the harder, structural-competitor form of overlap PROJECT.md flags as a poor fit, not the softer "hasn't formalized hosting" case.
- The platform-mismatch signal (no WordPress markers found; Rails-style asset pipeline) adds a second complicating factor on top of the hosting overlap, though this is somewhat less certain than the pricing-page hosting finding, which is a direct first-party confirmation.
- The standing white-label/Agency Hosting option (PROJECT.md's commercial-terms section) is the only angle that could make sense here, similar to Enleaf — but Social Strategix appears to be a single-operator freelance business (not an agency running 10+ sites), so the Agency Hosting tier's 10-site minimum is unlikely to be a natural fit at this stage. A pure referral pitch is not recommended.

## Research status

- Site pages fetched/reviewed 2026-08-20: /contact-us, homepage, /pricing.
- Raw HTML independently checked via curl (2026-08-20) for platform markers (none found for WordPress/Wix/Squarespace/Shopify/Duda/Webflow/GoHighLevel) and for `mailto:` links.
- Naming-collision check (important — see leadership.md for detail): several similarly-named but **unrelated** businesses and domains exist — social-strategix.com (a placeholder/template site with Lorem Ipsum content and fake DC contact info, unrelated), strategixsocial.net (a different social-media agency run by "George Farris," unrelated), plus unrelated BBB-listed companies "Social Strategy Group," "Social Strategies," and "Social Impact Strategies Group LLC." The confirmed entity for this lead is specifically **socialstrategix.com**, matching the (208) 691-1588 phone number and Jordan Quast's name.
- Not completed: BBB profile (none found in search results for this specific business), Idaho Secretary of State entity lookup, and confirmation of the exact underlying website-builder platform/vendor.
- See `sources.md` for the full citation list and `leadership.md`/`people/` for contact research.
