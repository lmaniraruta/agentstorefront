"""Pydantic schemas. Machine-readable for agent consumption."""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal, List
from datetime import datetime


# --- Sellers ---
class SellerCreate(BaseModel):
    email: EmailStr


class Seller(BaseModel):
    id: int
    email: str
    stripe_account_id: Optional[str] = None
    created_at: datetime


# --- Agents ---
class AgentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=80)
    owner_email: Optional[EmailStr] = None


class AgentKey(BaseModel):
    id: int
    name: str
    api_key: str  # only returned at creation
    owner_email: Optional[str] = None


# --- Services ---
class ServiceCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    description: str = Field(..., min_length=20, max_length=2000)
    category: str = Field(..., examples=["data", "signals", "compute", "writing", "auth", "search"])
    endpoint_url: str
    pricing_model: Literal["per_call", "subscription", "usage"]
    price_cents: int = Field(..., ge=0)
    currency: str = "usd"
    machine_spec: Optional[dict] = None  # JSON Schema for input/output
    tags: List[str] = []


class Service(BaseModel):
    id: int
    seller_id: int
    name: str
    description: str
    category: Optional[str]
    endpoint_url: str
    pricing_model: str
    price_cents: int
    currency: str
    machine_spec: Optional[dict] = None
    tags: List[str] = []
    active: bool
    created_at: datetime


# --- Discover ---
class DiscoverQuery(BaseModel):
    """Agents send natural-language or structured queries."""
    q: str = Field(..., description="Natural language: 'find a service that does X'")
    max_price_cents: Optional[int] = None
    pricing_model: Optional[Literal["per_call", "subscription", "usage"]] = None
    category: Optional[str] = None
    limit: int = 10


class DiscoverResult(BaseModel):
    services: List[Service]
    count: int


# --- Subscribe ---
class SubscribeRequest(BaseModel):
    service_id: int


class Subscription(BaseModel):
    id: int
    agent_id: int
    service_id: int
    status: str
    stripe_subscription_id: Optional[str] = None
    created_at: datetime
