# DuckDuckGo API: 6 endpoints with pricing and code examples

Call 6 DuckDuckGo endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`duckduckgo/ai-chat`](../models/duckduckgo/ai-chat.md) | Get the answer DuckDuckGo's Duck.ai chat gives for a question with a chosen chat model, with answer text and a token for follow-up… | $0.01 per call |
| [`duckduckgo/images`](../models/duckduckgo/images.md) | Search DuckDuckGo Images by keyword with size, color, type and layout filters, returning image URLs, thumbnails, titles and sources. | $0.01 per call |
| [`duckduckgo/maps`](../models/duckduckgo/maps.md) | Search DuckDuckGo Maps for places inside a viewport rectangle or around a center. | $0.00015 per call (free daily quota) |
| [`duckduckgo/news`](../models/duckduckgo/news.md) | DuckDuckGo News results for a keyword: headline, source, date, snippet and link. | $0.015 per call |
| [`duckduckgo/search`](../models/duckduckgo/search.md) | DuckDuckGo organic search results for a keyword, with region and safe-search options. | $0.015 per call |
| [`duckduckgo/shopping`](../models/duckduckgo/shopping.md) | Search DuckDuckGo Shopping by keyword and get product listings with title, price, merchant, rating and link, by region. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/ai-chat", "q": "How does a heat pump work?"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
