# Airbnb API: 1 endpoints with pricing and code examples

Call 1 Airbnb endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`airbnb/search`](../models/airbnb/search.md) | Search Airbnb stays by location and dates, with listing name, price, rating, reviews, room type, photos and coordinates. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "airbnb/search"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
