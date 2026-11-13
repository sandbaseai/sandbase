# EDINET API: 1 endpoints with pricing and code examples

Call 1 EDINET endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`edinet/documents`](../models/edinet/documents.md) | List the corporate disclosure documents filed with Japan's EDINET on a given date, with document ID, filer, document type, period and… | about $1e-05 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "edinet/documents", "date": "2026-11-10"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
