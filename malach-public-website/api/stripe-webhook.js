import { sendJson, methodNotAllowed, readRaw } from './_lib/http.js';
import { verifyStripeSignature, stripeRequest } from './_lib/stripe.js';
import { syncEntitlement } from './_lib/entitlements.js';

export const config = { api: { bodyParser: false } };

async function subscriptionRecord(event) {
  const object = event.data.object;
  let subscription = object;
  const subscriptionId = object.id?.startsWith('sub_') ? object.id : object.subscription;
  if (subscriptionId && !object.id?.startsWith('sub_')) {
    subscription = await stripeRequest(`/subscriptions/${encodeURIComponent(subscriptionId)}`, {}, 'GET');
  }
  const metadata = subscription.metadata || object.metadata || {};
  return {
    source: 'stripe',
    event_id: event.id,
    event_type: event.type,
    stripe_customer_id: String(subscription.customer || object.customer || ''),
    stripe_subscription_id: String(subscription.id?.startsWith('sub_') ? subscription.id : object.subscription || ''),
    plan: metadata.plan || 'unknown',
    interval: metadata.interval || 'unknown',
    status: subscription.status || (event.type === 'checkout.session.completed' ? 'active' : 'unknown'),
    billing_email: object.customer_details?.email || object.customer_email || '',
    current_period_end: subscription.current_period_end || null,
    cancel_at_period_end: Boolean(subscription.cancel_at_period_end),
    updated_at: new Date().toISOString()
  };
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return methodNotAllowed(res, ['POST']);
  try {
    const raw = await readRaw(req);
    const signature = req.headers['stripe-signature'];
    if (!verifyStripeSignature(raw, signature, process.env.STRIPE_WEBHOOK_SECRET)) {
      return sendJson(res, 400, { error: 'Invalid signature' });
    }
    const event = JSON.parse(raw.toString('utf8'));
    const handled = new Set([
      'checkout.session.completed',
      'customer.subscription.created',
      'customer.subscription.updated',
      'customer.subscription.deleted',
      'invoice.payment_failed',
      'invoice.paid'
    ]);
    if (handled.has(event.type)) {
      const record = await subscriptionRecord(event);
      await syncEntitlement(record);
    }
    sendJson(res, 200, { received: true });
  } catch (error) {
    console.error('stripe_webhook_failed', { message: error.message });
    sendJson(res, 500, { error: 'Webhook processing failed' });
  }
}
