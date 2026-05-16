"""Example: research assistant agent finds a knowledge API."""
import os
from agentstorefront import Agent

BASE = os.getenv("AGENTSTOREFRONT_BASE", "http://localhost:8000")


def main():
    agent = Agent(api_key=os.environ["AGENT_KEY"], base_url=BASE)
    # Find any service tagged "research" under $5
    services = agent.discover(
        "academic paper search arxiv research",
        max_price_cents=500,
        pricing_model="per_call",
    )
    for s in services[:5]:
        print(f"- {s.name} (${s.price_usd}) — {s.description[:80]}")


if __name__ == "__main__":
    main()
