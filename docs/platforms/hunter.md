# Hunter API: 2 endpoints with pricing and code examples

Call 2 Hunter endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`hunter/companies-find`](../models/hunter/companies-find.md) | Look up a company's full profile — industry, size, location, tech stack — from its domain. | $0.0049 per call (free daily quota) |
| [`hunter/discover-ai`](../models/hunter/discover-ai.md) | Describe target companies in plain language; an AI picks the filters and runs the search. | $0.1 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hunter/companies-find", "domain": "stripe.com"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
