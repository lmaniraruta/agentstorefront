# AgentStorefront

**The App Store for AI agents.** Devs list services with machine-readable specs. AI agents discover, subscribe, and pay autonomously. 12% platform fee via Stripe Connect.

🌐 Live: [agentstorefront.app](https://agentstorefront.app)
📦 SDK: `pip install agentstorefront`
🐙 Repo: [github.com/lmaniraruta/agentstorefront](https://github.com/lmaniraruta/agentstorefront)

---

## Why

Q1 2026 — Visa, Mastercard, OpenAI, and Google all shipped payment rails so AI agents can buy things autonomously. McKinsey: $3-5T in agentic commerce by 2030.

The rails exist. The marketplace didn't. This is the storefront layer.

## Repo structure

```
backend/        FastAPI service registry + discovery + Stripe Connect (Railway deploy)
sdk-python/     pip-installable Agent SDK
landing/        Static landing page (Vercel deploy)
DISTRIBUTION.md HN/Reddit/X launch copy + 25 DM targets
VERIFY_LOG.md   Test proof
CLAUDE.md       Operator memory (caveman)
```

## 60-sec agent quickstart

```python
from agentstorefront import Agent

agent = Agent.register(name="MyTradingBot")
print("SAVE THIS:", agent.api_key)

results = agent.discover("crypto trading signals", max_price_cents=3000)
agent.subscribe(service_id=results[0].id)
data = agent.call(service_id=results[0].id, payload={"symbol": "BTC"})
```

## For sellers

[List your service](https://agentstorefront.app/#sell). First 50 sellers: **0% fee for 6 months**. We're seeding supply.

## Stack

FastAPI · SQLite (→ Supabase pgvector at scale) · Stripe Connect · Tailwind · Vercel · Railway

## Status

MVP shipped 2026-05-15. Backend tests passing. Awaiting first seller listings.

## License

MIT.
