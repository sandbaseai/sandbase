# Cloudsway API: 1 endpoints with pricing and code examples

Call 1 Cloudsway endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`cloudsway/search`](../models/cloudsway/search.md) | Web search API for AI agents with topic focus (news, academic, company, finance and more), country, date range and domain filters, plus… | $0.005 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "cloudsway/search", "end_date": "2026-08-06", "include_highlights": true, "max_results": 5, "query": "Groq LPU inference funding valuation revenue 2025 2026", "search_depth": "basic", "start_date": "2024-01-01", "topic": "company"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
