# Naver API: 5 endpoints with pricing and code examples

Call 5 Naver endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`naver/ai-mode`](../models/naver/ai-mode.md) | Get Naver's AI-generated answer for a query with the answer text, cited sources and follow-up token for continuing the conversation. | $0.01 per call |
| [`naver/ai-overview`](../models/naver/ai-overview.md) | Naver's AI-generated overview answer for a search query, with the cited sources. | $0.015 per call |
| [`naver/blog-search`](../models/naver/blog-search.md) | Search up to five enriched Naver blog results by keyword with stable cursor pagination: result rank, title, excerpt, post and blogger… | about $0.032 per call |
| [`naver/maps`](../models/naver/maps.md) | Search places on Naver Maps by keyword around a location, with name, category, rating, reviews, address, phone and booking options. | $0.01 per call |
| [`naver/search`](../models/naver/search.md) | Get Naver web results for a query with organic results, news, blogs, knowledge panels and other Naver sections. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/ai-mode", "query": "서울 맛집 추천"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
