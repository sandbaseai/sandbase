# Unsplash API: 1 endpoints with pricing and code examples

Call 1 Unsplash endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`unsplash/search-photos`](../models/unsplash/search-photos.md) | Search Unsplash for free stock photos by keyword. Returns image URLs in several sizes, dimensions, alt text, the photographer's name and… | about $0.0033 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "unsplash/search-photos", "query": "coffee"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
