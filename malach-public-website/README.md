# Malach Public Website

Production-oriented public website for **Malach — Autonomous Commerce Intelligence**.

The repository is deliberately dependency-light: the marketing experience is static HTML, CSS and native JavaScript, while billing and contact endpoints run as serverless Node functions. This keeps the site fast, portable and easy to audit.


## Preview

![Malach homepage — dark](previews/home-dark.png)

![Malach homepage — light](previews/home-light.png)

![Malach homepage — mobile](previews/home-mobile-dark.png)

## Included

- Premium dark/light glass design system
- Public routes for Product, Auto Agent, Intelligence, Advantage, Attribution, Voice, Security, Pricing, About, Support, Privacy, Terms and Login
- Interactive Agent Canvas demo
- Multi-series financial chart with Shared Dollar and Compare Trends modes
- Advantage research-browser demo with source provenance
- Attribution, Voice, Chat, Evolution, multi-store and control demonstrations
- Coming-soon roadmap with explicit labels
- Stripe Checkout, Billing Portal and webhook endpoints
- Optional entitlement forwarding to the Malach application and/or Supabase
- SEO metadata, Open Graph image, sitemap, robots, web manifest and favicons
- Vercel security headers
- Route, asset and JavaScript validation
- Browser smoke-test script for desktop and mobile layouts

## Quick preview

```bash
npm run dev
```

Open:

```text
http://127.0.0.1:3000
```

Run static validation:

```bash
npm test
```

Run the optional Chromium smoke suite:

```bash
python3 scripts/browser_smoke.py
```

## Recommended deployment

1. Create a private GitHub repository.
2. Upload this project to the repository root.
3. Import the repository into Vercel.
4. Add the environment variables from `.env.example`.
5. Attach `malach.app` to the Vercel project.
6. Keep `app.malach.app` pointed at the Malach application load balancer.

GitHub is the source repository. Vercel is recommended for the public site because the included Stripe and contact endpoints require a serverless runtime. GitHub Pages can host the static pages, but it cannot run the billing APIs.

## Domain layout

```text
https://malach.app          public website
https://app.malach.app      Malach application
```

The intended OAuth callback remains:

```text
https://app.malach.app/api/oauth/google/callback
```

## Billing state

The website does not invent launch prices. If Stripe price IDs are absent, pricing buttons become **Request access** or **Contact sales**. Once Stripe environment variables are configured, eligible buttons automatically start Checkout.

See [BILLING_SETUP.md](BILLING_SETUP.md).

## Content configuration

Primary public URLs and emails are used consistently throughout the generated pages. Edit:

- `scripts/generate_site.py` for copy and page structure
- `assets/css/styles.css` for design tokens and layouts
- `assets/data/plans.json` for plan features
- `assets/data/coming-soon.json` for roadmap items

After changing generated-page content, run:

```bash
npm run generate
npm test
```

## Important launch work

Before launch:

- Replace any placeholder display prices with approved pricing.
- Create `support@malach.app`.
- Have counsel review Privacy and Terms.
- Configure Stripe test mode, then live mode.
- Configure a verified entitlement destination for webhooks.
- Confirm `malach.app`, `app.malach.app`, Privacy, Terms and Support in Google Auth Platform.
- Test every checkout, cancellation, failed-payment and portal path.
- Run the browser smoke suite on Chrome and Safari.

See [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md).

## Logo assets

The supplied official Malach logo is used directly. Separate safe-zone assets are included for:

- full lockup
- mark
- wordmark
- favicon
- Apple touch icon
- social preview

Do not crop the right wing, upper points, lower center or copper outer edges.

## Security

- No secret values belong in the repository.
- Stripe and entitlement credentials are read only from environment variables.
- Raw card information is handled by Stripe Checkout, not the Malach website.
- The public-config endpoint returns only safe display values and enabled/disabled state.
- The Billing Portal endpoint requires a private bearer token and is intended to be called from the authenticated Malach application.

See [SECURITY.md](SECURITY.md).
