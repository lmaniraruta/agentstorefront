"""Subscription + transaction routes. Stripe Connect wired in when keys present."""
import os
from fastapi import APIRouter, HTTPException, Depends
from models import SubscribeRequest, Subscription
from auth import get_agent_from_key
from db import cursor

router = APIRouter(prefix="/subscribe", tags=["subscribe"])

PLATFORM_FEE_PCT = int(os.getenv("PLATFORM_FEE_PCT", "12"))
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY", "")

try:
    import stripe
    if STRIPE_KEY:
        stripe.api_key = STRIPE_KEY
except ImportError:
    stripe = None


@router.post("", response_model=Subscription, status_code=201)
def subscribe(body: SubscribeRequest, agent=Depends(get_agent_from_key)):
    """Agent subscribes to a service. Creates Stripe Connect charge if keys set."""
    with cursor() as c:
        c.execute("SELECT * FROM services WHERE id = ? AND active = 1", (body.service_id,))
        svc = c.fetchone()
        if not svc:
            raise HTTPException(404, "Service not found or inactive")
        svc = dict(svc)

        # Check existing sub
        c.execute(
            "SELECT * FROM subscriptions WHERE agent_id = ? AND service_id = ? AND status = 'active'",
            (agent["id"], body.service_id),
        )
        if c.fetchone():
            raise HTTPException(409, "Already subscribed")

        # MVP: skip Stripe if no key set; record sub locally
        stripe_sub_id = None
        if stripe and STRIPE_KEY:
            try:
                c.execute("SELECT stripe_account_id FROM sellers WHERE id = ?", (svc["seller_id"],))
                seller = c.fetchone()
                if seller and seller["stripe_account_id"]:
                    fee_cents = (svc["price_cents"] * PLATFORM_FEE_PCT) // 100
                    charge = stripe.PaymentIntent.create(
                        amount=svc["price_cents"],
                        currency=svc["currency"],
                        application_fee_amount=fee_cents,
                        stripe_account=seller["stripe_account_id"],
                        metadata={"agent_id": agent["id"], "service_id": svc["id"]},
                    )
                    stripe_sub_id = charge.id
            except Exception as e:
                raise HTTPException(502, f"Stripe error: {e}")

        c.execute(
            """INSERT INTO subscriptions (agent_id, service_id, stripe_subscription_id, status)
               VALUES (?, ?, ?, 'active')""",
            (agent["id"], body.service_id, stripe_sub_id),
        )
        sub_id = c.lastrowid

        # record transaction
        fee = (svc["price_cents"] * PLATFORM_FEE_PCT) // 100
        c.execute(
            """INSERT INTO transactions
               (agent_id, service_id, amount_cents, platform_fee_cents, stripe_charge_id, status)
               VALUES (?, ?, ?, ?, ?, 'completed')""",
            (agent["id"], svc["id"], svc["price_cents"], fee, stripe_sub_id),
        )

        c.execute("SELECT * FROM subscriptions WHERE id = ?", (sub_id,))
        row = dict(c.fetchone())
    return Subscription(**row)
