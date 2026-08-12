# Website Security Notes

## Secrets

Never commit:

- Stripe secret keys
- webhook secrets
- OAuth secrets
- Supabase service-role keys
- Malach entitlement tokens
- contact-webhook tokens

Use Vercel environment variables or another approved secret manager.

## Billing

The public browser never receives `STRIPE_SECRET_KEY`. Checkout sessions are created server-side. Stripe collects card data on Stripe-hosted Checkout.

Webhook signatures are verified before subscription state is accepted.

## Content Security Policy

`vercel.json` includes a conservative CSP and related headers. Review the policy before adding analytics, videos, third-party chat widgets or new external resources.

## Contact endpoint

The contact endpoint requires an external delivery webhook. Apply rate limiting at the webhook destination or with a Vercel/edge security layer before a high-volume launch.

## Legal and compliance

The site makes no claim of SOC 2, ISO 27001, HIPAA or other certification. Add such claims only after they are actually obtained and approved.

## Application security boundary

The public website is separate from the Malach application at `app.malach.app`. Marketing-site analytics must never receive private advertising metrics, API keys, OAuth tokens or commerce data.
