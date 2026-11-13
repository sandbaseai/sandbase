# Yandex API: 3 endpoints with pricing and code examples

Call 3 Yandex endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yandex/images`](../models/yandex/images.md) | Yandex Images results for a keyword: image URLs, thumbnails, sizes and source pages. | $0.015 per call |
| [`yandex/search`](../models/yandex/search.md) | Get Yandex web results for a query with organic results and pagination, localized by Yandex domain, region and language. | $0.01 per call |
| [`yandex/videos`](../models/yandex/videos.md) | Yandex Videos results for a keyword: titles, thumbnails, durations and source sites. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yandex/images", "text": "coffee"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
