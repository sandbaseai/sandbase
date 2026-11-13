# Flightradar24 API: 1 endpoints with pricing and code examples

Call 1 Flightradar24 endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`flightradar24/flights`](../models/flightradar24/flights.md) | Get live flights from Flightradar24 by airport, flight number, airline, aircraft type or map bounds, with position, altitude, speed, route… | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "flightradar24/flights"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
