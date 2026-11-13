# ChatGPT API: 1 endpoints with pricing and code examples

Call 1 ChatGPT endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`chatgpt/search`](../models/chatgpt/search.md) | Ask ChatGPT a web-grounded question and receive an answer with source citations. ChatGPT composes each answer per request, so the same… | about $0.0018 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "chatgpt/search", "prompt": "What are the best practices for home composting?"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
