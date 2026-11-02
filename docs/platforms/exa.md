# Exa API: 3 endpoints with pricing and code examples

Call 3 Exa endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`exa/answer`](../models/exa/answer.md) | Returns direct answers and cited web sources for a given query. Supports custom retrieval modes, optional full page text, and structured… | $0.0075 per call (free daily quota) |
| [`exa/contents`](../models/exa/contents.md) | Extract clean page contents for a list of URLs: full text, highlights, AI summaries and metadata, from cache or with a live crawl. | $0.0045 per call |
| [`exa/search`](../models/exa/search.md) | Neural web search for AI apps and agents. Ask in natural language and get the most relevant pages, with optional highlights, summaries or… | $0.0105 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "exa/answer", "query": "Which manufacturers had the top three global EV sales in 2025?"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
