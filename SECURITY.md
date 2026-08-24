# Website Security

- No secret values belong in the repository.
- Stripe card data is collected by Stripe-hosted Checkout.
- Stripe webhook signatures are verified before billing state is trusted.
- Contact delivery tokens and entitlement tokens are environment variables.
- The marketing site is separate from private Malach workspace data.
- Content Security Policy permits only the Malach application health endpoint in addition to same-origin requests.
- Do not claim certifications that have not been obtained.
