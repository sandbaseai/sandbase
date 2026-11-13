# Bing API: 6 endpoints with pricing and code examples

Call 6 Bing endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`bing/copilot`](../models/bing/copilot.md) | Bing Copilot's conversational answer to a prompt, with the text blocks and cited references. | $0.015 per call |
| [`bing/images`](../models/bing/images.md) | Bing Images results for a keyword: image URLs, thumbnails, titles, sizes and source pages. | $0.015 per call |
| [`bing/news`](../models/bing/news.md) | Search Bing News by keyword and get headlines with source, date, snippet and thumbnail, filtered by freshness and market. | $0.01 per call |
| [`bing/reverse-image`](../models/bing/reverse-image.md) | Search Bing Visual Search with an image URL and get visually similar images, pages that contain the image and related searches. | $0.01 per call |
| [`bing/search`](../models/bing/search.md) | Get Bing web results for a query with organic results, answer boxes, related searches and pagination, localized by market and country. | $0.01 per call |
| [`bing/videos`](../models/bing/videos.md) | Bing Videos results for a keyword: titles, thumbnails, durations, views and source sites. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/copilot", "q": "what is the capital of france"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
