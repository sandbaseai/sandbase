# Vaquill API: 4 endpoints with pricing and code examples

Call 4 Vaquill endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`vaquill/count`](../models/vaquill/count.md) | Count the law sections in a jurisdiction, corpus, code, title, chapter, or part. | $0.01 per call |
| [`vaquill/coverage`](../models/vaquill/coverage.md) | List which US law corpora are queryable in each jurisdiction, with live section counts. | from $0 per run, depending on parameters |
| [`vaquill/divisions`](../models/vaquill/divisions.md) | Walk a US legal code level by level: titles, chapters, parts, then sections. | $0.01 per call |
| [`vaquill/resolve`](../models/vaquill/resolve.md) | Resolve up to 50 Bluebook citation strings to the exact US law sections they name. | about $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vaquill/count"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
