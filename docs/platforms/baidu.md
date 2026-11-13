# Baidu API: 3 endpoints with pricing and code examples

Call 3 Baidu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`baidu/maps`](../models/baidu/maps.md) | Search places on Baidu Maps by keyword in a city or around coordinates, with name, address, category, rating, phone and coordinates. | $0.01 per call |
| [`baidu/news`](../models/baidu/news.md) | Baidu News results for a keyword: headline, source, date, snippet and link. | $0.015 per call |
| [`baidu/search`](../models/baidu/search.md) | Get Baidu web results for a query with organic results, answer boxes, related searches and pagination. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/maps", "q": "咖啡"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
