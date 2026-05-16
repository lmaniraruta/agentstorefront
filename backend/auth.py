"""API key issuance + verification for agents."""
import secrets
import hashlib
import os
from fastapi import Header, HTTPException, status
from typing import Optional

API_KEY_PREFIX = os.getenv("API_KEY_PREFIX", "as_")


def issue_api_key() -> tuple[str, str]:
    """Returns (plaintext_key, hashed_key). Show plaintext once."""
    raw = secrets.token_urlsafe(32)
    plaintext = f"{API_KEY_PREFIX}{raw}"
    hashed = hashlib.sha256(plaintext.encode()).hexdigest()
    return plaintext, hashed


def hash_key(plaintext: str) -> str:
    return hashlib.sha256(plaintext.encode()).hexdigest()


def get_agent_from_key(authorization: Optional[str] = Header(None)) -> dict:
    """Dep injection for protected routes."""
    from db import cursor

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or malformed Authorization header. Use 'Bearer <api_key>'",
        )
    key = authorization.replace("Bearer ", "").strip()
    if not key.startswith(API_KEY_PREFIX):
        raise HTTPException(status_code=401, detail="Invalid API key format")

    hashed = hash_key(key)
    with cursor() as c:
        c.execute("SELECT id, name, owner_email FROM agents WHERE api_key_hash = ?", (hashed,))
        row = c.fetchone()
        if not row:
            raise HTTPException(status_code=401, detail="Invalid API key")
        return dict(row)
