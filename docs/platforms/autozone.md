# AutoZone API: 1 endpoints with pricing and code examples

Call 1 AutoZone endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`autozone/scrape/category`](../models/autozone/scrape/category.md) | Extract product listings from an AutoZone category page URL with pagination and preferred-store pricing. | $0.012 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "autozone/scrape/category", "url": "https://www.autozone.com/batteries-starting-and-charging/battery"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
