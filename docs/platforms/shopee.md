# Shopee API: 1 endpoints with pricing and code examples

Call 1 Shopee endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`shopee/search/facets`](../models/shopee/search/facets.md) | Get the category facets Shopee shows for a search keyword, to see which categories a query maps to on each site. | $0.028571 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopee/search/facets", "site": "TW", "keyword": "iphone case"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
