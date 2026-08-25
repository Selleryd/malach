# Deployment

## Validate

```bash
npm test
python3 scripts/browser_smoke.py
git diff --check
```

## GitHub

The canonical repository is configured with `CNAME` set to `malach.app`.

Do not commit `.env` files or secret values. Use repository/deployment environment variables for Stripe, contact delivery and entitlement synchronization.

## Production acceptance

Verify:

- `/`
- `/product/`
- `/pricing/`
- `/security/`
- `/status/`
- `/support/`
- `/privacy/`
- `/terms/`
- Sign-in and Start free CTAs
- Mobile navigation and dropdowns
- Stripe Checkout, webhook and portal endpoints

## Status health source

Set `MALACH_APP_HEALTH_URL` to a JSON health endpoint for the Malach application. The public Status page calls the same-origin `/api/health` proxy; it does not infer application health from the marketing website itself.
