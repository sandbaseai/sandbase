# Substack API: 1 endpoints with pricing and code examples

Call 1 Substack endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`substack/posts`](../models/substack/posts.md) | Pull posts from any Substack publication by its URL, or pass a single post URL (…/p/slug) to fetch just that one article. Returns title,… | about $0.0444 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "substack/posts", "url": "https://www.astralcodexten.com"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
