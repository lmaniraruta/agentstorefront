"""Agent identity + API keys."""
import json
from fastapi import APIRouter, HTTPException, Depends
from models import AgentCreate, AgentKey
from auth import issue_api_key, get_agent_from_key
from db import cursor

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("", response_model=AgentKey, status_code=201)
def create_agent(body: AgentCreate):
    """Issue an API key. Plaintext returned ONCE — agent must store it."""
    plaintext, hashed = issue_api_key()
    with cursor() as c:
        c.execute(
            "INSERT INTO agents (name, api_key_hash, owner_email) VALUES (?, ?, ?)",
            (body.name, hashed, body.owner_email),
        )
        agent_id = c.lastrowid
    return AgentKey(
        id=agent_id,
        name=body.name,
        api_key=plaintext,
        owner_email=body.owner_email,
    )


@router.get("/me")
def get_me(agent=Depends(get_agent_from_key)):
    """Echo back the agent identity for verification."""
    return agent
