# agentstorefront — Python SDK

Drop-in client for AI agents to discover, subscribe to, and call services on AgentStorefront — the App Store for AI agents.

## Install

```bash
pip install agentstorefront
```

(MVP install local: `pip install -e .` from this directory.)

## 60-second quickstart

```python
from agentstorefront import Agent

# First time: register
agent = Agent.register(name="MyTradingBot", owner_email="you@example.com")
print("SAVE THIS:", agent.api_key)  # only shown once

# Later sessions: reuse key
agent = Agent(api_key="as_xxxxxxxx")

# Find a service
results = agent.discover("crypto trading signals", max_price_cents=5000)
for s in results:
    print(s.name, s.price_usd, s.endpoint_url)

# Subscribe + pay (12% platform fee handled server-side via Stripe Connect)
sub = agent.subscribe(service_id=results[0].id)

# Call the service
data = agent.call(service_id=results[0].id, payload={"symbol": "BTC"})
print(data)
```

## Examples

See `examples/` directory for:
- `crypto_bot.py` — trading bot discovers a signal feed and acts on it
- `research_assistant.py` — agent finds and uses a knowledge API
- `personal_assistant.py` — agent extends itself with new tools at runtime

## Why this exists

The agentic economy is here. Visa, Mastercard, OpenAI, and Google all shipped agent payment rails in Q1 2026. McKinsey projects $3–5T in agentic commerce by 2030.

But until now there was no marketplace where AI agents could *find* services to buy. AgentStorefront is that marketplace, and this SDK is how your agent shops there.

## License

MIT.
