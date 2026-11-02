# Brave API: 9 endpoints with pricing and code examples

Call 9 Brave endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`brave/images`](../models/brave/images.md) | Image Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/llm-context`](../models/brave/llm-context.md) | LLM Context from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/local-descriptions`](../models/brave/local-descriptions.md) | POI Descriptions from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/local-place-search`](../models/brave/local-place-search.md) | Place Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/local-pois`](../models/brave/local-pois.md) | Local POIs from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/news`](../models/brave/news.md) | News Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/videos`](../models/brave/videos.md) | Video Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/web`](../models/brave/web.md) | Web Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |
| [`brave/web-rich`](../models/brave/web-rich.md) | Rich Search from Brave. Returns the official Brave API response unchanged. | $0.005 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/images", "q": "golden gate bridge"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
