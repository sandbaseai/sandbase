# Tavily API: 3 endpoints with pricing and code examples

Call 3 Tavily endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tavily/extract`](../models/tavily/extract.md) | Extracts clean text content from specified web pages using their URLs. Supports basic or advanced extraction depth and optional image… | $0.012 per call (free daily quota) |
| [`tavily/map`](../models/tavily/map.md) | Discovers the URL structure of a target website without extracting full page content. Accepts a starting URL, maximum traversal depth, and… | $0.012 per call |
| [`tavily/search`](../models/tavily/search.md) | AI-optimized web search for agents and RAG: ranked results with titles, URLs and relevant content, depth control, news and finance topics,… | $0.012 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tavily/extract", "urls": ["https://static.sandbase.ai/examples/de3a14cf-48e2-4dd0-9ef9-4c4c1da485c8/input/2f4290fd-6946-4f6b-8cbe-5b3366e41080.com"]}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
