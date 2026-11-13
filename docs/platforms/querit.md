# Querit API: 1 endpoints with pricing and code examples

Call 1 Querit endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`querit/search`](../models/querit/search.md) | Search the web with Querit and get ranked results with title, URL, snippet and optional page content chunks for AI grounding. | about $0.0048 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "querit/search", "query": "electric vehicle market share 2026"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
