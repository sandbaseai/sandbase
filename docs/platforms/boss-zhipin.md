# BOSS Zhipin API: 1 endpoints with pricing and code examples

Call 1 BOSS Zhipin endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`boss-zhipin/recommend-jobs`](../models/boss-zhipin/recommend-jobs.md) | Retrieve recommended and trending job listings from the BOSS直聘 homepage. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "boss-zhipin/recommend-jobs"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
