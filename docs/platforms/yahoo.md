# Yahoo API: 4 endpoints with pricing and code examples

Call 4 Yahoo endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yahoo/images`](../models/yahoo/images.md) | Yahoo Images results for a keyword: image URLs, thumbnails, sizes and source pages. | $0.015 per call |
| [`yahoo/search`](../models/yahoo/search.md) | Get Yahoo web results for a query with organic results, related searches and pagination, localized by domain and language. | $0.01 per call |
| [`yahoo/trends`](../models/yahoo/trends.md) | List trending searches on Yahoo right now, with topic, related links and videos. | $0.01 per call |
| [`yahoo/videos`](../models/yahoo/videos.md) | Yahoo Videos results for a keyword: titles, thumbnails, durations and source sites. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/images", "p": "coffee"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
