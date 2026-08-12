import { sendJson, methodNotAllowed, readJson } from './_lib/http.js';
import { priceMap, stripeRequest } from './_lib/stripe.js';

const allowedPlans = new Set(['core', 'autonomous', 'portfolio']);
const allowedIntervals = new Set(['monthly', 'annual']);

export default async function handler(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const body = await readJson(req);
    const planId = String(body.planId || '');
    const interval = String(body.interval || 'monthly');
    if (!allowedPlans.has(planId) || !allowedIntervals.has(interval)) return sendJson(res, 400, { error: 'Invalid plan selection' });
    const priceId = priceMap()?.[planId]?.[interval];
    if (!priceId) return sendJson(res, 503, { error: 'This plan is not available for online checkout yet.' });

    const siteUrl = (process.env.SITE_URL || 'https://malach.app').replace(/\/$/, '');
    const appUrl = (process.env.APP_URL || 'https://app.malach.app').replace(/\/$/, '');
    const params = {
      mode: 'subscription',
      'line_items[0][price]': priceId,
      'line_items[0][quantity]': 1,
      success_url: `${appUrl}/onboarding?checkout=success&session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${siteUrl}/pricing/?checkout=canceled`,
      allow_promotion_codes: 'true',
      billing_address_collection: 'auto',
      client_reference_id: body.clientReferenceId || undefined,
      customer_email: body.email || undefined,
      'metadata[plan]': planId,
      'metadata[interval]': interval,
      'subscription_data[metadata][plan]': planId,
      'subscription_data[metadata][interval]': interval
    };
    if (process.env.STRIPE_AUTOMATIC_TAX === 'true') params['automatic_tax[enabled]'] = 'true';
    const session = await stripeRequest('/checkout/sessions', params);
    sendJson(res, 200, { id: session.id, url: session.url });
  } catch (error) {
    console.error('checkout_session_failed', { message: error.message, code: error.code });
    sendJson(res, 500, { error: 'Secure checkout could not be started. Please contact support.' });
  }
}
