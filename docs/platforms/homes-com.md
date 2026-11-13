# Homes.com API: 1 endpoints with pricing and code examples

Call 1 Homes.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`homes-com/search`](../models/homes-com/search.md) | Get Homes.com listings from a search results URL with address, price, beds, baths, size and listing link. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "homes-com/search", "url": "https://www.homes.com/austin-tx/"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
