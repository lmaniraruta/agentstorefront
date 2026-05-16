# Distribution — Launch Week

Goal: 20 sellers + 100 GitHub stars in first 14 days.

---

## 1. Hacker News — Show HN

**When:** Tue or Wed, 8-10am ET. Avoid weekends.

**Title:**
> Show HN: AgentStorefront – an App Store for AI agents to buy services from

**Body:**
```
Hi HN,

I built AgentStorefront — a marketplace where AI agents discover, subscribe to, and pay for services autonomously. Devs list their APIs once. Agents find and buy them via a discovery API. No human in the loop.

Why: Visa, Mastercard, OpenAI, and Google all shipped agent payment rails this quarter. The rails exist. The storefront didn't. McKinsey says $3–5T in agentic commerce by 2030, and right now there's nowhere indie devs can list a service for machine buyers and earn passively.

How it works:
- Devs POST a service spec (name, desc, pricing, endpoint URL)
- Agents GET /discover with natural-language queries
- Agents POST /subscribe; Stripe Connect handles the charge; we take 12%
- The Python SDK is one import: pip install agentstorefront

What's live in this MVP:
- FastAPI backend (open source, self-hostable)
- Python SDK with discover / subscribe / call
- Stripe Connect integration for marketplace payments
- Seller signup form

What's next:
- pgvector-backed semantic discovery
- JS/TS SDK
- Usage-based billing meter
- 0% platform fee for first 50 sellers (6 months) to seed supply

Repo: https://github.com/lfidele/agentstorefront
Site: https://agentstorefront.com

Would love feedback — especially from anyone building agents who has a service they'd want to monetize, or from anyone running into the "where do my agents shop?" problem.
```

---

## 2. Reddit — r/LocalLLaMA

**Subject:**
> I built a marketplace where your LangChain/AutoGen agents can buy tools autonomously [open source]

**Body:**
```
TLDR: pip install agentstorefront, your agent gets a discover() + subscribe() + call() interface to a growing catalog of paid APIs. 12% platform fee, Stripe Connect handles payouts to sellers.

Why I made it: I have a few small APIs I want to monetize but I don't want a sales pipeline. I wanted my agents to be able to FIND and BUY services without me writing custom integrations.

Code is open: https://github.com/lfidele/agentstorefront
Live: https://agentstorefront.com

Currently in seed-supply mode — 0% fee for the first 50 listings. If you have an API gathering dust, list it.

Feedback welcome. Especially: what's the worst part of the agent discovery flow? What service would you actually pay your agent to subscribe to?
```

---

## 3. Reddit — r/MachineLearning (be careful — strict rules)

**Subject:**
> [P] Open-source marketplace for AI agents to buy paid APIs (FastAPI + Stripe Connect + Python SDK)

**Body:**
```
Project link: https://github.com/lfidele/agentstorefront

Built this because the payment rails for agentic commerce shipped this quarter (Stripe ACP, Google UCP, Visa AP) but no one built the storefront layer on top. This is an MVP — backend in FastAPI, SQLite for now (pgvector next), Python SDK ships discover/subscribe/call.

Looking for:
- API providers to list (first 50 are fee-free for 6 months)
- Feedback on the discovery interface (currently keyword scoring; planning embedding similarity)
- Anyone interested in collaborating on the JS SDK

Happy to answer questions about the design.
```

**Banned moves:** no DM-bait, no link in title, no salesy tone. r/ML kills marketing fast.

---

## 4. X Thread (5 tweets)

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
- a crypto data feed
- a knowledge API
- a scheduling tool

…you write a custom integration. Every. Single. Time.

Sellers have no way to list. Agents have no way to discover. The agentic economy can't compound.
```

**Tweet 3 (solution):**
```
AgentStorefront = the App Store for AI agents.

Devs list services with machine-readable specs.
Agents discover via natural-language API.
Stripe Connect handles autonomous payments.
12% platform fee. No fulfillment work.

It's a flywheel:
sellers → agents → sellers → ...
```

**Tweet 4 (proof):**
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
Open source: github.com/lfidele/agentstorefront
Site: agentstorefront.com

First 50 sellers = 0% fee for 6 months.

If you have an API, list it. If you build agents, install the SDK. RTs help me find the early adopters.
```

---

## 5. DM List — 25 AI Agent Builders

| Handle / Platform | Hook |
|---|---|
| LangChain core maintainers | "your agents need a runtime tool-discovery layer — built this" |
| AutoGen authors | "self-extending agents need a marketplace — here's the supply side" |
| CrewAI Discord owners | "crewai + agentstorefront = agents that bid for their own tools" |
| Stripe DevRel | "built on top of ACP — would love feedback on the marketplace layer" |
| Anthropic DevRel | "tool use in Claude + paid services catalog — opening the marketplace" |
| Top 10 RapidAPI sellers | "list your API once for AI agents — 0% fee 6 months" |
| Top 10 Replit AI builders | "your agents can now buy tools at runtime" |

Use `outbound-dm-engine` skill for personalization on each.

---

## 6. Build-in-Public Cadence (daily, 14 days)

| Day | Post |
|---|---|
| 1 | Show HN post + screenshot of dashboard |
| 2 | "First agent subscribed autonomously — here's the log" (proof) |
| 3 | Architecture diagram (FastAPI + SQLite + Stripe Connect) |
| 4 | "Why I'm not competing with OpenAI's protocol — I'm building on top" |
| 5 | First seller spotlight + their MRR |
| 6 | Demo video: agent finds + uses a service in real-time |
| 7 | Friday review: stars / sellers / GMV |
| 8 | Open question: should categories be folksonomy or curated? |
| 9 | Lesson learned post |
| 10 | Seller earnings screenshot (anonymous) |
| 11 | "Building the JS SDK live — code stream" |
| 12 | Roadmap reveal |
| 13 | "Agents bought $X this week without humans" |
| 14 | 2-week recap post + ask for sellers |

---

## Success bars

- 14d: 100 GH stars, 10 sellers, 50 agent registrations
- 30d: 20 sellers, $600 platform MRR
- 60d: 50 sellers, first organic agent subscription (no Fidele-seeded)
