# DoorDash API: 1 endpoints with pricing and code examples

Call 1 DoorDash endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`doordash/search`](../models/doordash/search.md) | Search DoorDash stores and dishes by keyword and delivery address, with store name, rating, delivery fee, ETA and menu items. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "doordash/search", "q": "pizza", "address": "Austin, TX"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
