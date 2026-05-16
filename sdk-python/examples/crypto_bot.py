"""Example: trading bot discovers a crypto signal feed at runtime."""
import os
from agentstorefront import Agent

BASE = os.getenv("AGENTSTOREFRONT_BASE", "http://localhost:8000")


def main():
    api_key = os.getenv("AGENT_KEY")
    if not api_key:
        agent = Agent.register(name="DemoTradingBot", base_url=BASE)
        print(f"NEW KEY (save it): {agent.api_key}")
    else:
        agent = Agent(api_key=api_key, base_url=BASE)

    # Find a crypto signal service under $30/mo
    services = agent.discover(
        "crypto trading signals BTC ETH",
        max_price_cents=3000,
        category="signals",
    )
    if not services:
        print("No services found.")
        return

    pick = services[0]
    print(f"Picked: {pick.name} @ ${pick.price_usd}/mo")
    print(f"  → {pick.description}")

    # Subscribe
    sub = agent.subscribe(service_id=pick.id)
    print(f"Subscribed: {sub.status}")

    # Call the service
    response = agent.call(service_id=pick.id, payload={"symbol": "BTC"})
    print(f"Service response: {response}")


if __name__ == "__main__":
    main()
