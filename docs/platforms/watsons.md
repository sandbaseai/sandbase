# Watsons API: 1 endpoints with pricing and code examples

Call 1 Watsons endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`watsons/scrape/category`](../models/watsons/scrape/category.md) | Extract product listings from a Watsons category page URL, including names, prices and promotions. | $0.021 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "watsons/scrape/category", "url": "https://www.watsons.com.my/health-care/vitamins-minerals/c/110100"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
