# H2 AgentStorefront

Parent: A.I C.E.O. Status: BUILDING (was QUEUED). Bucket: HARD. Composite 8.25/10.

## TLDR
App Store for AI agents. Devs list services machine-readable. Agents discover + pay autonomously. Stripe Connect 12% cut.

## Why now
- Visa/MC/OpenAI/Google shipped agentic payment rails Q1 2026
- McKinsey: $3-5T agentic commerce by 2030
- Rails exist. Marketplace doesn't. We build the storefront layer.
- Bridges from E2 (GPTs/Projects already shipping — they list themselves first)

## Scope (MVP)
- POST /services — devs list (name, desc, pricing, endpoint, API key)
- GET /discover — agents query "find service does X under $Y/mo"
- POST /auth/agent — issue API key for agent identity
- POST /subscribe — agent subscribes, Stripe Connect charge
- Seller dashboard: Next.js, view subs + earnings
- Agent SDK: Python first, JS later

## Stack
- Backend: FastAPI + SQLite MVP → Supabase pgvector at scale
- Payments: Stripe Connect (marketplace, 12% fee)
- Auth: API keys + JWT
- Frontend: Next.js + Tailwind, Vercel
- Hosting: Railway (backend) + Vercel (frontend)
- SDK: pip install agentstorefront

## Files (this dir)
- CLAUDE.md (you here)
- README.md — public-facing
- BLUEPRINT.md — full 12-section plan
- backend/ — FastAPI app
- sdk-python/ — pip package
- landing/ — Next.js site
- DISTRIBUTION.md — HN/Reddit/X/DM copy
- FIDELE_5_PERCENT.md — manual steps only Fidele can do
- LAUNCH_METRICS.md — track signups, GMV, fees

## Revenue model
12% of every transaction. Pure platform cut. No fulfillment.

- Mo3: 20 sellers, $600 MRR cut
- Mo6: 100 sellers, $8K MRR
- Mo12: 300 sellers, $50K+ MRR
- Ceiling: $2M-$10M/yr

## Build order
1. ✅ CLAUDE.md + folder linked
2. FastAPI scaffold + SQLite + 3 endpoints (services / discover / auth)
3. Agent SDK Python
4. Landing page + seller form
5. Stripe Connect integration (Fidele activates Connect in dashboard)
6. Distribution drop (HN, Reddit, 25 DMs)
7. Seed supply: list E1 + E2 + RoutineOS + MendAI as own services
8. First 20 external sellers — 0% fee 6 mo

## Distribution
- HN Show post day 1
- r/LocalLLaMA + r/MachineLearning posts
- 25 DM list AI agent builders (LangChain, AutoGen, CrewAI maintainers)
- Build-in-public X thread
- GitHub repo public (open SDK) — stars = signal

## Risks
- Chicken-egg: seed supply w/ own products + free 6mo
- Google/OpenAI builds competitor: ship faster, 6mo head start
- Agent fraud: Stripe fraud + rate limit + key scoping
- Too early: rails already shipped Q1 2026, demand exists

## Banned
- Don't compete with rails — build ON TOP
- Don't human-first UX — agent API first, dashboard is afterthought
- Don't gate-keep — open SDK, low fees
- Don't add features till 20 sellers live

## Tool routing
- Code → backend, SDK, landing
- Cowork → domain, Railway, Vercel, Stripe Connect, GitHub
- Chat → strategy, distribution copy
- Design → logo, OG image, social cards

## Success metrics
- M1: 20 sellers, 5 paying agent subs
- M3: 100 sellers, $1K platform fees
- M6: first seller earning $1K+/mo passively
- WIN: agents subscribing zero human involvement
- KILL: <10 sellers after 60d active outreach

## Session start
1. Read this file
2. TaskList check
3. Pick top pending
4. Cook 95%, ask Fidele only for 5%
