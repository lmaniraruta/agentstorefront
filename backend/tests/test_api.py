"""End-to-end test: register seller → list service → agent discovers → subscribes."""
import os
import tempfile
import sys
from pathlib import Path

# Use a temp file DB so connections share state (sqlite :memory: doesn't share across conns)
_tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_tmp.close()
os.environ["DATABASE_PATH"] = _tmp.name

sys.path.insert(0, str(Path(__file__).parent.parent))

# Reload db module to pick up env var
import db
db.DB_PATH = _tmp.name

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def setup_module():
    db.init_db()


def teardown_module():
    try:
        os.unlink(_tmp.name)
    except OSError:
        pass


def test_happy_path():
    # 1. Seller signs up
    r = client.post("/sellers", json={"email": "dev@example.com"})
    assert r.status_code == 201, r.text
    seller = r.json()
    assert seller["id"] > 0

    # 2. Seller lists service
    r = client.post(
        f"/services?seller_id={seller['id']}",
        json={
            "name": "Crypto Signal Pro",
            "description": "Real-time crypto trading signals for AI agents. BTC, ETH, SOL coverage.",
            "category": "signals",
            "endpoint_url": "https://example.com/api/signals",
            "pricing_model": "subscription",
            "price_cents": 2900,
            "tags": ["crypto", "trading", "signals"],
        },
    )
    assert r.status_code == 201, r.text
    svc = r.json()
    assert svc["price_cents"] == 2900

    # 3. Agent registers
    r = client.post("/agents", json={"name": "TradingBotV1", "owner_email": "bot@example.com"})
    assert r.status_code == 201, r.text
    agent = r.json()
    api_key = agent["api_key"]
    assert api_key.startswith("as_")

    # 4. Verify identity
    r = client.get("/agents/me", headers={"Authorization": f"Bearer {api_key}"})
    assert r.status_code == 200
    assert r.json()["name"] == "TradingBotV1"

    # 5. Agent discovers services
    r = client.post(
        "/discover",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"q": "crypto trading signals", "max_price_cents": 5000},
    )
    assert r.status_code == 200, r.text
    results = r.json()
    assert results["count"] >= 1
    assert results["services"][0]["name"] == "Crypto Signal Pro"

    # 6. Agent subscribes
    r = client.post(
        "/subscribe",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"service_id": svc["id"]},
    )
    assert r.status_code == 201, r.text
    sub = r.json()
    assert sub["status"] == "active"


def test_auth_required():
    r = client.post("/discover", json={"q": "anything"})
    assert r.status_code == 401

    r = client.get("/agents/me")
    assert r.status_code == 401

    r = client.get("/agents/me", headers={"Authorization": "Bearer invalid_key"})
    assert r.status_code == 401
