"""Service registry: sellers list, agents discover."""
import json
from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models import ServiceCreate, Service
from db import cursor

router = APIRouter(prefix="/services", tags=["services"])


def _row_to_service(row: dict) -> Service:
    return Service(
        id=row["id"],
        seller_id=row["seller_id"],
        name=row["name"],
        description=row["description"],
        category=row["category"],
        endpoint_url=row["endpoint_url"],
        pricing_model=row["pricing_model"],
        price_cents=row["price_cents"],
        currency=row["currency"],
        machine_spec=json.loads(row["machine_spec"]) if row["machine_spec"] else None,
        tags=row["tags"].split(",") if row["tags"] else [],
        active=bool(row["active"]),
        created_at=row["created_at"],
    )


@router.post("", response_model=Service, status_code=201)
def list_service(body: ServiceCreate, seller_id: int = Query(...)):
    """Seller registers a service. seller_id in query for MVP — replace with auth later."""
    with cursor() as c:
        c.execute("SELECT id FROM sellers WHERE id = ?", (seller_id,))
        if not c.fetchone():
            raise HTTPException(404, f"Seller {seller_id} not found")
        c.execute(
            """INSERT INTO services
               (seller_id, name, description, category, endpoint_url,
                pricing_model, price_cents, currency, machine_spec, tags)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                seller_id,
                body.name,
                body.description,
                body.category,
                body.endpoint_url,
                body.pricing_model,
                body.price_cents,
                body.currency,
                json.dumps(body.machine_spec) if body.machine_spec else None,
                ",".join(body.tags),
            ),
        )
        sid = c.lastrowid
        c.execute("SELECT * FROM services WHERE id = ?", (sid,))
        row = dict(c.fetchone())
    return _row_to_service(row)


@router.get("", response_model=List[Service])
def list_all_services(active_only: bool = True, limit: int = 50):
    with cursor() as c:
        if active_only:
            c.execute("SELECT * FROM services WHERE active = 1 ORDER BY id DESC LIMIT ?", (limit,))
        else:
            c.execute("SELECT * FROM services ORDER BY id DESC LIMIT ?", (limit,))
        rows = [dict(r) for r in c.fetchall()]
    return [_row_to_service(r) for r in rows]


@router.get("/{service_id}", response_model=Service)
def get_service(service_id: int):
    with cursor() as c:
        c.execute("SELECT * FROM services WHERE id = ?", (service_id,))
        row = c.fetchone()
        if not row:
            raise HTTPException(404, "Service not found")
    return _row_to_service(dict(row))
