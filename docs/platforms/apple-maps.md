# Apple Maps API: 2 endpoints with pricing and code examples

Call 2 Apple Maps endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`apple-maps/place`](../models/apple-maps/place.md) | Get an Apple Maps place by MUID with name, category, rating, address, phone, website, hours and coordinates. | $0.01 per call |
| [`apple-maps/search`](../models/apple-maps/search.md) | Search places on Apple Maps by keyword and location, with name, category, rating, address, phone, hours and coordinates. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apple-maps/place", "muid": "<muid>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
