# Perplexity API: 1 endpoints with pricing and code examples

Call 1 Perplexity endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`perplexity/search`](../models/perplexity/search.md) | Ask Perplexity a web-grounded question and receive an answer with source citations. | about $0.002 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "perplexity/search", "prompt": "What are the best practices for home composting?"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
