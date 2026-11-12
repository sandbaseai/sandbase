# Slickdeals API: 2 endpoints with pricing and code examples

Call 2 Slickdeals endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`slickdeals/deal`](../models/slickdeals/deal.md) | Fetch one Slickdeals deal by URL and get title, price, list price, store, coupon code, score, views, comments, and description in one… | about $0.00213 per call |
| [`slickdeals/search`](../models/slickdeals/search.md) | Search Slickdeals deals by keyword with optional sort, price, discount, and page filters and get title, price, list price, store, score,… | about $0.00213 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "slickdeals/deal", "url": "https://slickdeals.net/f/20177112-lg-55-c6-series-oled-evo-ai-4k-smart-webos-tv-2026-best-buy-amazon-999-99"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
