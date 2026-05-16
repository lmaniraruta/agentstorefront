# Distribution — Launch Night (2026-05-16)

**Live URLs:**
- Landing: https://agentstorefront.app
- API: https://api.agentstorefront.app
- Docs (Swagger UI): https://api.agentstorefront.app/docs
- GitHub: https://github.com/lmaniraruta/agentstorefront
- SDK: `pip install agentstorefront`

Goal — first 14 days:
- 100 GitHub stars
- 20 sellers signed up
- 50 agent registrations
- First organic agent subscription (no Fidele-seeded)

DNS still propagating? Use Railway URLs as fallback in copy: `https://agentstorefront-production.up.railway.app`.

---

## 1. 🟠 Hacker News — Show HN

**When:** Tue or Wed, 8-10am ET. Avoid weekends. (If launching tonight, ship it — perfect is enemy of done.)

**Submit at:** https://news.ycombinator.com/submit

**Title (max 80 chars):**
```
Show HN: AgentStorefront – an App Store for AI agents to buy services from
```

**URL field:**
```
https://agentstorefront.app
```

**Text field (paste the entire block below):**
```
Hi HN — I built AgentStorefront, a marketplace where AI agents discover, subscribe to, and pay for services autonomously. Devs list APIs once. Agents find and buy them via a discovery API. No human in the loop.

Why: Visa, Mastercard, OpenAI, and Google all shipped agent payment rails this quarter. McKinsey says $3–5T in agentic commerce by 2030. The rails exist — but there was no marketplace where indie devs could list services for machine buyers and earn passively.

What's live:
- FastAPI backend, open source: github.com/lmaniraruta/agentstorefront
- Python SDK: `pip install agentstorefront`
- Stripe Connect integration (12% platform fee, sellers keep 88%)
- 5 services already listed (my own to seed supply)
- Working agent flow: register → discover → subscribe → call

What's next:
- pgvector-backed semantic discovery
- JS/TS SDK
- Usage-based billing meter
- 0% platform fee for first 50 sellers (6 months) to seed supply

Try the Swagger explorer: https://api.agentstorefront.app/docs

Would love feedback — especially from anyone building agents who has a service they'd want to monetize, or who's run into the "where do my agents shop?" problem.
```

---

## 2. 🔵 Reddit — r/LocalLLaMA

**Submit at:** https://www.reddit.com/r/LocalLLaMA/submit?type=LINK (or TEXT)

**Title:**
```
I built a marketplace where your LangChain/AutoGen agents can buy tools autonomously [open source]
```

**Body:**
```
TLDR: `pip install agentstorefront` — your agent gets discover(), subscribe(), call() against a growing catalog of paid APIs. 12% platform fee, Stripe Connect handles payouts to sellers.

Why I made it: I have a few small APIs I want to monetize but don't want a sales pipeline. I wanted my agents to FIND and BUY services without me writing custom integrations every time.

```python
from agentstorefront import Agent

agent = Agent.register(name="MyBot")
hits = agent.discover("crypto trading signals", max_price_cents=3000)
agent.subscribe(service_id=hits[0].id)
data = agent.call(service_id=hits[0].id, payload={"sym": "BTC"})
```

Repo: https://github.com/lmaniraruta/agentstorefront
Site: https://agentstorefront.app
API explorer: https://api.agentstorefront.app/docs

Currently in seed-supply mode — 0% fee for first 50 listings. If you have an API gathering dust, list it.

Feedback welcome. Especially: what's the worst part of the agent discovery flow? What service would you actually pay your agent to subscribe to?
```

---

## 3. 🔵 Reddit — r/MachineLearning [careful, strict rules]

**Submit at:** https://www.reddit.com/r/MachineLearning/submit

**Title (must be tagged):**
```
[P] Open-source marketplace for AI agents to buy paid APIs (FastAPI + Stripe Connect + Python SDK)
```

**Body:**
```
Project link: https://github.com/lmaniraruta/agentstorefront
Live site: https://agentstorefront.app

Built this because the payment rails for agentic commerce shipped this quarter (Stripe ACP, Google UCP, Visa AP) but no one built the storefront layer on top. This is an MVP — FastAPI backend, SQLite for now (pgvector next), Python SDK ships discover/subscribe/call.

Looking for:
- API providers to list (first 50 are fee-free for 6 months)
- Feedback on the discovery interface (currently keyword scoring; planning embedding similarity in v0.2)
- Anyone interested in collaborating on the JS SDK

Happy to answer questions about the design.
```

**Banned moves:** no DM-bait, no marketing tone, no link in title. r/ML kills self-promo fast.

---

## 4. ⚫ X Thread (5 tweets) — post from @fidele07

**Tweet 1 (hook):**
```
Visa, Mastercard, OpenAI, and Google all shipped agent payment rails this quarter.

McKinsey says $3–5 trillion in agentic commerce by 2030.

But there's no marketplace where the agents actually shop.

So I built one. 🧵
```

**Tweet 2 (problem):**
```
Today if your AI agent needs:
• crypto data feed
• knowledge API
• scheduling tool

…you write a custom integration. Every. Single. Time.

Sellers have no way to list.
Agents have no way to discover.
The agentic economy can't compound.
```

**Tweet 3 (solution):**
```
AgentStorefront = the App Store for AI agents.

Devs list services with machine-readable specs.
Agents discover via natural-language API.
Stripe Connect handles autonomous payments.
12% platform fee. No fulfillment.

Flywheel:
sellers → agents → sellers → ∞
```

**Tweet 4 (proof in code):**
```
Your agent in 12 lines of Python:

```py
from agentstorefront import Agent
a = Agent.register(name="MyBot")
hits = a.discover("crypto signals under $30")
a.subscribe(hits[0].id)
data = a.call(hits[0].id, {"sym": "BTC"})
```

That's it. The agent just bought a service.
```

**Tweet 5 (CTA):**
```
🟢 Open source: github.com/lmaniraruta/agentstorefront
🟢 Site: agentstorefront.app
🟢 Docs: api.agentstorefront.app/docs

First 50 sellers = 0% fee for 6 months.

If you have an API, list it.
If you build agents, install the SDK.

RTs help me find early adopters 🙏
```

---

## 5. 💼 LinkedIn Post — from your personal profile

```
I just shipped AgentStorefront — the App Store for AI agents.

In Q1 2026, Visa, Mastercard, OpenAI, and Google all launched payment rails so AI agents can buy things autonomously. McKinsey is calling $3-5T in agentic commerce by 2030.

But until tonight, there was nowhere indie devs could list a service for machine buyers.

So I built it.

→ Devs list APIs with machine-readable specs
→ AI agents discover, subscribe, and pay autonomously
→ Stripe Connect handles the marketplace economics (12% platform fee)
→ Sellers keep 88%, zero fulfillment work

It's open source. The first 50 sellers pay 0% fees for 6 months.

If you've got an API you've been sitting on — even a small one — list it tonight: agentstorefront.app

If you build agents — try the SDK: pip install agentstorefront

I'm hunting for early adopters who want to be the first sellers on a marketplace before the AI-buys-stuff explosion compounds.

DM me if you want to talk about it.
```

---

## 6. 📨 DM Templates — 25 AI Agent Builders

### Generic opener (personalize hook line per target):

```
Hey [Name] — saw your work on [PROJECT] (the [SPECIFIC THING] post specifically — [GENUINE OBSERVATION]).

I just shipped something I think your community might want to look at: AgentStorefront — a marketplace where AI agents can discover and subscribe to paid APIs autonomously.

It's open source, Python SDK is `pip install agentstorefront`, and I'm offering 0% platform fees for the first 50 sellers (6 months).

Three reasons I'm pinging you specifically:
1. [Project] users would benefit from runtime service discovery
2. You probably have a perspective on what's missing in the agentic stack
3. If you want to be one of the first 5 listed services, I'll personally onboard you

Not asking for an endorsement — just want eyes on it and brutal feedback.

Site: agentstorefront.app
Repo: github.com/lmaniraruta/agentstorefront

— Fidele
```

### Target list (research each, personalize, send):

| # | Handle / Platform | Why | Hook |
|---|---|---|---|
| 1 | LangChain Discord mods | Tool-discovery layer is missing | "your agents need a runtime tool-discovery layer" |
| 2 | AutoGen / Microsoft folks | Multi-agent systems | "self-extending agents need a marketplace" |
| 3 | CrewAI Discord owners | Crew → service collaboration | "crewai + AS = agents that bid for their own tools" |
| 4 | Stripe DevRel (any) | Built on top of ACP | "built on top of ACP — would love feedback" |
| 5 | Anthropic DevRel | Claude tool use | "tool use in Claude + paid services catalog" |
| 6-15 | Top 10 RapidAPI sellers | Easy supply-side | "list your API once for AI agents — 0% fee 6mo" |
| 16-25 | Top 10 Replit AI builders / Cursor power users | Build agents daily | "your agents can buy tools at runtime now" |

Run the `outbound-dm-engine` skill to research and personalize each one.

---

## 7. 📅 Build-in-Public Cadence (14 days, 1 post min)

| Day | Channel | Post idea |
|---|---|---|
| 1 (tonight) | X | Show HN linked + the 5-tweet thread |
| 2 | LinkedIn | Long-form "why I built this" |
| 3 | X | Screenshot — first organic agent subscription log |
| 4 | LinkedIn | Architecture diagram (FastAPI + Stripe Connect + Vercel + Railway) |
| 5 | Reddit r/SaaS | "How I shipped a marketplace in one session" |
| 6 | X | Demo video — agent finds + uses a service in real time |
| 7 | Friday Review (chat) | Stars / sellers / GMV tally |
| 8 | X | Open question: folksonomy vs curated categories? |
| 9 | LinkedIn | Lessons-learned post |
| 10 | X | First seller MRR screenshot (anonymous) |
| 11 | X | "Building the JS SDK live" — stream link or replay |
| 12 | LinkedIn | Roadmap reveal |
| 13 | X | "Agents bought $X this week with zero human involvement" |
| 14 | Everywhere | 2-week recap post + new seller CTA |

---

## Success bars

- 14d: 100 GH stars · 10 sellers · 50 agent registrations
- 30d: 20 sellers · $600 platform MRR
- 60d: 50 sellers · first organic agent subscription
- 90d: KILL or scale decision

---

## Ready-to-go checklist (tonight)

- [ ] HN Show post (section 1)
- [ ] r/LocalLLaMA post (section 2)
- [ ] X thread, 5 tweets, post from @fidele07 (section 4)
- [ ] LinkedIn post (section 5)
- [ ] First 5 DMs from target list (section 6) — pick the 5 with strongest hooks
- [ ] Reply to ALL HN comments within 1 hour for first 4 hours

If you ship even half of this, you'll wake up to stars + seller signups. Go.
