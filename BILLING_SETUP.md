# Stripe Billing Setup

The repository includes:

- `POST /api/create-checkout-session`
- `POST /api/create-portal-session`
- `POST /api/stripe-webhook`
- `GET /api/public-config`

## 1. Create Stripe products and prices

Create products for:

- Malach Core
- Malach Autonomous
- Malach Portfolio, if sold through self-service checkout

Create monthly and annual recurring prices as needed.

Do not paste price amounts into JavaScript. Store Stripe price IDs in environment variables.

## 2. Configure environment variables

See `.env.example`.

At minimum:

```text
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
STRIPE_PRICE_CORE_MONTHLY
STRIPE_PRICE_AUTONOMOUS_MONTHLY
MALACH_ENTITLEMENT_WEBHOOK_URL
MALACH_ENTITLEMENT_WEBHOOK_TOKEN
```

Public display amounts are optional:

```text
PUBLIC_PRICE_CORE_MONTHLY=$---
```

These strings are display-only. Stripe remains the authority for the actual amount charged.

## 3. Create the webhook endpoint

In Stripe Workbench / Developers → Webhooks, create:

```text
https://malach.app/api/stripe-webhook
```

Subscribe to:

- `checkout.session.completed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `invoice.paid`
- `invoice.payment_failed`

Store the signing secret as `STRIPE_WEBHOOK_SECRET`.

## 4. Entitlement destination

A successful Checkout page is not proof of payment. The verified webhook updates entitlement state.

The webhook can send a normalized subscription record to:

```text
MALACH_ENTITLEMENT_WEBHOOK_URL
```

The Malach application should authenticate this request, store subscription state and activate the corresponding plan.

Optional Supabase mirroring is also supported if these are configured:

```text
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY
```

Create a `subscriptions` table with a unique `stripe_subscription_id` column before enabling the mirror.

## 5. Customer Portal

`/api/create-portal-session` is intentionally protected by `MALACH_PORTAL_API_TOKEN`. The authenticated Malach application should call this endpoint server-to-server and redirect the user to the returned URL.

## 6. Test mode acceptance

Test all of these before using live keys:

- successful Checkout
- canceled Checkout
- failed card payment
- subscription update
- cancellation at period end
- immediate cancellation
- webhook retry
- duplicate webhook delivery
- Customer Portal invoice access
- plan upgrade and downgrade, if enabled
- application entitlement activation and removal

## 7. Live mode

Use separate live price IDs, webhook secret and secret key. Never copy test IDs into production.
