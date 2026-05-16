# AgentStorefront — Landing

Single-page static site. Tailwind via CDN. Zero build.

## Deploy → Vercel (90 seconds)

```bash
cd landing
npx vercel
```

Or via Vercel dashboard: drag `landing/` folder into "New Project" → set framework to "Other" → deploy.

Custom domain: `agentstorefront.com` → CNAME to vercel.

## Form

The `#sellerForm` currently just shows a "thanks" modal. Hook it up:

**Option A — Formspree (fastest):**
1. Sign up formspree.io
2. Get form ID
3. Replace `onsubmit=...` with `action="https://formspree.io/f/YOUR_ID" method="POST"`

**Option B — Backend /sellers endpoint:**
```js
fetch('https://api.agentstorefront.com/sellers', {
  method: 'POST',
  body: JSON.stringify({ email })
})
```

## What to swap before launch

- [ ] Replace `https://github.com/lfidele/agentstorefront` w/ real repo URL
- [ ] Replace `https://x.com/fidele07` w/ active X handle
- [ ] Hook form to Formspree or backend
- [ ] Add OG image (`og.png` 1200x630)
