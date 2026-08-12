# Deployment Guide

## 1. Push to GitHub

```bash
git init
git add .
git commit -m "Launch Malach public website"
git branch -M main
git remote add origin git@github.com:YOUR_ACCOUNT/malach-website.git
git push -u origin main
```

## 2. Deploy to Vercel

1. Sign in to Vercel.
2. Select **Add New → Project**.
3. Import the GitHub repository.
4. Framework preset: **Other**.
5. Build command: leave empty.
6. Output directory: leave empty.
7. Deploy.

Vercel will serve the static files and automatically expose the functions in `/api`.

## 3. Add environment variables

Copy the required values from `.env.example` into Vercel Project Settings → Environment Variables.

Use separate values for Preview and Production where appropriate.

## 4. Add the domain

In Vercel Project Settings → Domains, add:

```text
malach.app
www.malach.app
```

Redirect `www.malach.app` to `malach.app`.

Do not point `app.malach.app` at this website project. That hostname belongs to the Malach application load balancer.

## 5. Verify production pages

Check:

```text
https://malach.app/
https://malach.app/pricing/
https://malach.app/security/
https://malach.app/privacy/
https://malach.app/terms/
https://malach.app/support/
```

## 6. Configure OAuth branding

Google Auth Platform should use:

```text
Homepage: https://malach.app
Privacy:  https://malach.app/privacy/
Terms:    https://malach.app/terms/
Support:  https://malach.app/support/
App URL:  https://app.malach.app
Callback: https://app.malach.app/api/oauth/google/callback
```

Keep old Cloud Run callbacks until the branded callback passes live acceptance.

## 7. Rollback

Vercel retains previous deployments. Roll back from the Deployments tab by promoting a previous known-good deployment.
