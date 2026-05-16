"""Example: personal AI assistant extends its capabilities at runtime."""
import os
from agentstorefront import Agent

BASE = os.getenv("AGENTSTOREFRONT_BASE", "http://localhost:8000")


def main():
    agent = Agent(api_key=os.environ["AGENT_KEY"], base_url=BASE)

    needs = [
        "send transactional email",
        "weather forecast api",
        "calendar scheduling",
    ]
    portfolio = []
    for need in needs:
        results = agent.discover(need, limit=3)
        if results:
            print(f"For '{need}': picked {results[0].name}")
            portfolio.append(results[0])

    print(f"\nExtended capabilities: {len(portfolio)} new services discovered.")
    for s in portfolio:
        print(f"  · {s.name} → {s.endpoint_url}")


if __name__ == "__main__":
    main()
