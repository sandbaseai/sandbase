# Google Flights API: 1 endpoints with pricing and code examples

Call 1 Google Flights endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-flights/search`](../models/google-flights/search.md) | Google Flights itineraries for a route and date: airlines, times, stops, durations, prices and price insights. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/search", "departure_id": "CDG", "arrival_id": "AUS", "outbound_date": "2026-12-15"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
