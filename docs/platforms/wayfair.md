# Wayfair API: 1 endpoints with pricing and code examples

Call 1 Wayfair endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`wayfair/search`](../models/wayfair/search.md) | Search Wayfair products by keyword and get listings with price, rating, review count and product URL, page by page. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wayfair/search", "query": "sofa"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
