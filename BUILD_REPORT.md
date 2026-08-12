# Malach Public Website Build Report

## Scope completed

- 16 public routes
- premium dark and light design system
- responsive mobile, tablet, laptop and desktop layouts
- official Malach logo variants with safe padding
- interactive Agent Canvas
- interactive financial chart with multi-series selection and trend comparison
- Advantage research-browser demonstration with source provenance
- Attribution, Voice, Chat, Evolution, multi-store and authority demonstrations
- data-driven pricing structure
- Stripe Checkout, Customer Portal and signed-webhook serverless endpoints
- optional subscription entitlement forwarding
- privacy, terms, security and support routes
- SEO, Open Graph, sitemap, robots and web manifest
- Vercel configuration and security headers
- GitHub validation workflow

## Validation performed

```text
Static route and asset validation: PASS
JavaScript syntax validation: PASS
Stripe price allowlist test: PASS
Stripe webhook signature test: PASS
Browser render smoke: PASS — 14 primary routes
Desktop horizontal overflow: PASS
Mobile horizontal overflow: PASS
Theme interaction: PASS
Command palette: PASS
Mobile navigation: PASS
Agent Canvas tabs: PASS
Financial series toggles: PASS
Pricing interval toggle: PASS
Duplicate HTML ID check: PASS
Image alt-attribute check: PASS
Credential-pattern scan: PASS
```

## Public-launch dependencies still required

- final approved pricing and Stripe price IDs
- live Stripe keys and webhook secret
- a verified Malach subscription-entitlement endpoint or Supabase schema
- support-delivery webhook or active support@malach.app mailbox
- legal review of Privacy and Terms
- live domain and browser acceptance on malach.app
- Google OAuth brand/domain verification
- final Safari and real-device tests

The website does not claim that coming-soon features are currently available and does not claim unsupported security certifications.
