import crypto from 'node:crypto';
import { verifyStripeSignature, priceMap } from '../api/_lib/stripe.js';

process.env.STRIPE_PRICE_CORE_MONTHLY = 'price_core_monthly';
const prices = priceMap();
if (prices.core.monthly !== 'price_core_monthly') throw new Error('Stripe price mapping failed');

const payload = Buffer.from(JSON.stringify({ id: 'evt_test', type: 'checkout.session.completed' }));
const secret = 'whsec_test_only';
const timestamp = Math.floor(Date.now() / 1000);
const digest = crypto.createHmac('sha256', secret).update(`${timestamp}.${payload.toString('utf8')}`).digest('hex');
const header = `t=${timestamp},v1=${digest}`;
if (!verifyStripeSignature(payload, header, secret)) throw new Error('Stripe signature verification failed');
if (verifyStripeSignature(payload, `t=${timestamp},v1=${'0'.repeat(64)}`, secret)) throw new Error('Invalid Stripe signature was accepted');
console.log('API smoke passed: price allowlist and webhook signature verification.');
