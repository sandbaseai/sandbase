# US Census API: 2 endpoints with pricing and code examples

Call 2 US Census endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`censusdata-xyz/explore-variables`](../models/censusdata-xyz/explore-variables.md) | Discover which US Census variables exist for a topic keyword. | from $0 per run, depending on parameters |
| [`censusdata-xyz/query`](../models/censusdata-xyz/query.md) | Ask any US Census question in plain English for a state, county, city, metro area, or ZIP code. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "censusdata-xyz/explore-variables", "keyword": "income"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
