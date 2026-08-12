# Public Launch Checklist

## Brand and content

- [ ] Confirm final homepage copy.
- [ ] Confirm official logo safe zones on desktop and mobile.
- [ ] Replace private-launch pricing when approved.
- [ ] Create support@malach.app.
- [ ] Review every “coming soon” label.
- [ ] Confirm no development or candidate terminology is visible.

## Legal

- [ ] Counsel reviews Privacy Policy.
- [ ] Counsel reviews Terms of Service.
- [ ] Confirm legal entity and governing-law language if required.
- [ ] Publish support and account-deletion process.

## Domain and OAuth

- [ ] `malach.app` resolves to the public website.
- [ ] `app.malach.app` resolves to Malach application.
- [ ] HTTPS certificates are active.
- [ ] Google Auth Platform branding says Malach.
- [ ] Homepage, Privacy, Terms and Support URLs are registered.
- [ ] `https://app.malach.app/api/oauth/google/callback` passes OAuth.
- [ ] Legacy callbacks remain during rollback window.

## Stripe

- [ ] Test products and prices created.
- [ ] Test-mode Checkout passes.
- [ ] Webhook signature verification passes.
- [ ] Entitlement activation passes.
- [ ] Failed-payment handling passes.
- [ ] Cancellation handling passes.
- [ ] Customer Portal passes.
- [ ] Live-mode products and prices created.
- [ ] Live webhook configured.

## Quality

- [ ] `npm test` passes.
- [ ] `python3 scripts/browser_smoke.py` passes.
- [ ] Chrome desktop and mobile pass.
- [ ] Safari desktop and mobile pass.
- [ ] Keyboard navigation passes.
- [ ] Reduced-motion mode passes.
- [ ] No horizontal overflow.
- [ ] No console errors.
- [ ] 404 page works.
- [ ] All external links work.
- [ ] Core Web Vitals reviewed.

## Operations

- [ ] Error monitoring configured.
- [ ] Contact delivery configured.
- [ ] Analytics configured with privacy review.
- [ ] Rollback procedure tested.
- [ ] Prior deployment retained.
