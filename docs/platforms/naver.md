# Naver API: 2 endpoints with pricing and code examples

Call 2 Naver endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`naver/ai-overview`](../models/naver/ai-overview.md) | Naver's AI-generated overview answer for a search query, with the cited sources. | $0.015 per call |
| [`naver/search`](../models/naver/search.md) | Get Naver web results for a query with organic results, news, blogs, knowledge panels and other Naver sections. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/ai-overview", "query": "coffee"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
