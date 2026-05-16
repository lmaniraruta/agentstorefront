"""SDK client. Wraps the REST API for AI agents."""
from __future__ import annotations
import httpx
from typing import Optional, List, Any
from dataclasses import dataclass

DEFAULT_BASE = "https://agentstorefront-production.up.railway.app"


class AgentStorefrontError(Exception):
    """Raised when the API returns a non-2xx response."""

    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"[{status_code}] {detail}")


@dataclass
class Service:
    id: int
    name: str
    description: str
    category: Optional[str]
    endpoint_url: str
    pricing_model: str
    price_cents: int
    currency: str
    tags: List[str]

    @property
    def price_usd(self) -> float:
        return self.price_cents / 100

    @classmethod
    def from_dict(cls, d: dict) -> "Service":
        return cls(
            id=d["id"],
            name=d["name"],
            description=d["description"],
            category=d.get("category"),
            endpoint_url=d["endpoint_url"],
            pricing_model=d["pricing_model"],
            price_cents=d["price_cents"],
            currency=d.get("currency", "usd"),
            tags=d.get("tags", []),
        )


@dataclass
class Subscription:
    id: int
    agent_id: int
    service_id: int
    status: str
    stripe_subscription_id: Optional[str]


class Agent:
    """High-level agent client."""

    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE, timeout: float = 30.0):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self._http = httpx.Client(
            base_url=self.base_url,
            timeout=timeout,
            headers={"Authorization": f"Bearer {api_key}"},
        )

    # ---- factory ----
    @classmethod
    def register(
        cls,
        name: str,
        owner_email: Optional[str] = None,
        base_url: str = DEFAULT_BASE,
    ) -> "Agent":
        """Create a new agent identity. Returns Agent with api_key set.

        IMPORTANT: store agent.api_key — shown once.
        """
        with httpx.Client(base_url=base_url, timeout=30.0) as c:
            r = c.post("/agents", json={"name": name, "owner_email": owner_email})
            cls._raise(r)
            data = r.json()
        return cls(api_key=data["api_key"], base_url=base_url)

    # ---- discovery ----
    def discover(
        self,
        query: str,
        max_price_cents: Optional[int] = None,
        pricing_model: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 10,
    ) -> List[Service]:
        payload = {"q": query, "limit": limit}
        if max_price_cents is not None:
            payload["max_price_cents"] = max_price_cents
        if pricing_model:
            payload["pricing_model"] = pricing_model
        if category:
            payload["category"] = category
        r = self._http.post("/discover", json=payload)
        self._raise(r)
        data = r.json()
        return [Service.from_dict(s) for s in data["services"]]

    # ---- subscription ----
    def subscribe(self, service_id: int) -> Subscription:
        r = self._http.post("/subscribe", json={"service_id": service_id})
        self._raise(r)
        d = r.json()
        return Subscription(
            id=d["id"],
            agent_id=d["agent_id"],
            service_id=d["service_id"],
            status=d["status"],
            stripe_subscription_id=d.get("stripe_subscription_id"),
        )

    # ---- direct call (transparent proxy to seller endpoint) ----
    def call(self, service_id: int, payload: Any = None) -> dict:
        """Fetch the service definition then forward the payload to its endpoint."""
        r = self._http.get(f"/services/{service_id}")
        self._raise(r)
        svc = r.json()
        target = svc["endpoint_url"]
        # MVP: agent's API key is forwarded as bearer; sellers can ignore or validate via webhook
        with httpx.Client(timeout=30.0) as c:
            resp = c.post(
                target,
                json=payload or {},
                headers={"X-AgentStorefront-Key": self.api_key},
            )
            try:
                return resp.json()
            except Exception:
                return {"raw": resp.text, "status": resp.status_code}

    # ---- helpers ----
    def me(self) -> dict:
        r = self._http.get("/agents/me")
        self._raise(r)
        return r.json()

    @staticmethod
    def _raise(r: httpx.Response):
        if r.status_code >= 400:
            try:
                detail = r.json().get("detail", r.text)
            except Exception:
                detail = r.text
            raise AgentStorefrontError(r.status_code, detail)

    def close(self):
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()
