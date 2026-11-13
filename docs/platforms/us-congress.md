# US Congress API: 1 endpoints with pricing and code examples

Call 1 US Congress endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`congress/trades`](../models/congress/trades.md) | Get US Congress members' financial disclosures and stock trades (member, ticker, transaction type, amount range, and dates), filterable by… | about $0.00905 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "congress/trades"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
