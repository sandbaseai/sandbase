# Upwork API: 1 endpoints with pricing and code examples

Call 1 Upwork endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`upwork/jobs`](../models/upwork/jobs.md) | Search Upwork job postings by keyword, with up to 25 fresh listings per request. | about $0.007 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "upwork/jobs", "query": "web developer"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
