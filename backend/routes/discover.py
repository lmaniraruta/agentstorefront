"""Discovery: agents query for services in machine-readable form.

MVP uses keyword + filter scoring. Phase 2 swaps to pgvector semantic search.
"""
import json
from fastapi import APIRouter, Depends
from models import DiscoverQuery, DiscoverResult
from auth import get_agent_from_key
from routes.services import _row_to_service
from db import cursor

router = APIRouter(prefix="/discover", tags=["discover"])


def _score(query: str, name: str, description: str, tags: str) -> float:
    """Naive scoring: token overlap. Replace with embedding similarity Phase 2."""
    q_tokens = set(query.lower().split())
    if not q_tokens:
        return 0.0
    text = f"{name} {description} {tags}".lower()
    hits = sum(1 for t in q_tokens if t in text)
    return hits / len(q_tokens)


@router.post("", response_model=DiscoverResult)
def discover(body: DiscoverQuery, agent=Depends(get_agent_from_key)):
    """
    Agent-side discovery. Authenticated.

    Returns ranked services matching natural-language query + filters.
    """
    with cursor() as c:
        sql = "SELECT * FROM services WHERE active = 1"
        params = []
        if body.category:
            sql += " AND category = ?"
            params.append(body.category)
        if body.pricing_model:
            sql += " AND pricing_model = ?"
            params.append(body.pricing_model)
        if body.max_price_cents is not None:
            sql += " AND price_cents <= ?"
            params.append(body.max_price_cents)
        c.execute(sql, params)
        rows = [dict(r) for r in c.fetchall()]

    scored = []
    for r in rows:
        s = _score(body.q, r["name"], r["description"], r["tags"] or "")
        if s > 0:
            scored.append((s, r))
    scored.sort(key=lambda x: -x[0])
    top = [r for _, r in scored[: body.limit]]
    return DiscoverResult(
        services=[_row_to_service(r) for r in top],
        count=len(top),
    )
