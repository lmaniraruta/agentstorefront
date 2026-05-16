"""AgentStorefront Python SDK.

Quickstart:

    from agentstorefront import Agent

    agent = Agent.register(name="MyBot", base_url="https://api.agentstorefront.app")
    print(agent.api_key)  # save this — shown once

    # Later sessions
    agent = Agent(api_key="as_xxx", base_url="https://api.agentstorefront.app")

    # Discover services
    results = agent.discover("find a crypto signal service under $30/mo")

    # Subscribe
    sub = agent.subscribe(service_id=results[0].id)

    # Call the service (transparent proxy to seller endpoint)
    response = agent.call(service_id=results[0].id, payload={"symbol": "BTC"})
"""
from .client import Agent, Service, Subscription, AgentStorefrontError

__version__ = "0.1.0"
__all__ = ["Agent", "Service", "Subscription", "AgentStorefrontError"]
