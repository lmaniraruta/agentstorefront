# AgentStorefront — Backend

FastAPI service registry + discovery + Stripe Connect payments.

## Run local

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # edit if you have Stripe keys
python db.py          # init SQLite
uvicorn main:app --reload
```

Open http://localhost:8000/docs for Swagger.

## Test

```bash
pytest tests/ -v
```

## Endpoints

| Method | Path | Auth | Purpose |
|---|---|---|---|
| POST | /sellers | none | seller signup |
| POST | /services?seller_id=N | (seller_id query — MVP) | list a service |
| GET | /services | none | browse services |
| POST | /agents | none | register agent, get API key |
| GET | /agents/me | Bearer | verify identity |
| POST | /discover | Bearer | search services |
| POST | /subscribe | Bearer | subscribe + charge |

## Deploy → Railway

1. `railway init`
2. `railway up`
3. Set env vars: `STRIPE_SECRET_KEY`, `PLATFORM_FEE_PCT=12`, `ALLOWED_ORIGINS=https://agentstorefront.com`
4. Custom domain → CNAME to railway-generated URL

## Phase 2

- Swap SQLite → Supabase + pgvector (semantic search)
- Stripe Connect onboarding flow for sellers
- Webhooks for transaction confirmation
- Rate limiting per agent key
- Service health probes
- Usage-based billing meter
