# Fidele 5% — manual moves only you can do

Claude handled the 95%. These 8 steps need your hands. Total ~30 min.

---

## 1. Domain (~3 min, $12-15)

- Go to porkbun.com or namecheap.com
- Buy: `agentstorefront.com` (preferred) — fall back to `agentstorefront.ai` or `agentstore.dev`
- Use Stripe-linked card

**Paste me back the domain you got.**

---

## 2. GitHub repo (~2 min, free)

- New public repo: `lfidele/agentstorefront`
- Description: "App Store for AI agents — discover, subscribe, pay autonomously."
- Initialize empty (no README, no license — I have those)
- Copy the SSH or HTTPS URL

I'll handle the push w/ skill `push-folder-to-github`.

---

## 3. GitHub push 2FA (~1 min)

When I run the push, approve the 2FA prompt.

---

## 4. Railway backend deploy (~5 min, free tier)

- railway.app → sign in w/ GitHub
- New project → Deploy from GitHub → pick agentstorefront repo
- Root dir: `backend/`
- Set env vars (Settings → Variables):
  - `PLATFORM_FEE_PCT=12`
  - `ALLOWED_ORIGINS=https://agentstorefront.com,http://localhost:3000`
  - (skip Stripe keys until step 6)
- Click Deploy
- Custom Domain: `api.agentstorefront.com` → copy CNAME, add to porkbun DNS

**Paste me back the railway URL.**

---

## 5. Vercel landing deploy (~3 min, free)

- vercel.com → sign in w/ GitHub
- Import agentstorefront repo
- Root dir: `landing/`
- Framework preset: Other
- Deploy
- Custom Domain: `agentstorefront.com` → add A/CNAME at porkbun

---

## 6. Stripe Connect activation (~5 min, free until first sale)

- stripe.com → sign up if needed (use lmaniraruta@gmail.com)
- Dashboard → Connect → "Get started"
- Platform profile → fill in (you can leave most defaults)
- Get **Connect Client ID** (`ca_...`) — Settings → Connect
- Get **Secret Key** (`sk_test_...`) — Developers → API keys
- Add to Railway env vars:
  - `STRIPE_SECRET_KEY=sk_test_...`
  - `STRIPE_CONNECT_CLIENT_ID=ca_...`

---

## 7. Formspree (or skip — keep form as-is)

- formspree.io → sign up, free tier
- New form → "AgentStorefront Sellers"
- Get form ID like `xyzabc123`
- I'll wire into `landing/index.html`

---

## 8. Post HN + Reddit + X thread (~5 min)

When I say go:
- Paste `DISTRIBUTION.md` § 1 into news.ycombinator.com/submit
- Paste § 2 into r/LocalLLaMA
- Tweet § 4 thread from your X account

---

## Quick paste form (fill once, send back)

```
DOMAIN: agentstorefront.com (or _____)
GITHUB URL: https://github.com/lfidele/agentstorefront
RAILWAY URL: https://_____.up.railway.app
VERCEL URL: https://_____.vercel.app
STRIPE SECRET KEY: sk_test_____ (paste in Railway env, not here)
STRIPE CONNECT CLIENT ID: ca_____
FORMSPREE ID (optional): _____
```

When that's filled, I'll patch the SDK base URL, landing page links, and CORS in 60 sec.
