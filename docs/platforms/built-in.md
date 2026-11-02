# Built In API: 1 endpoints with pricing and code examples

Call 1 Built In endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`builtin/suggest-job-titles`](../models/builtin/suggest-job-titles.md) | Returns up to 10 autocomplete suggestions for job title searches, matching the query prefix against Built In's job title index. Useful for… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "builtin/suggest-job-titles", "query": "software engineer"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
