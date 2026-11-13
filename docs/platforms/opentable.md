# OpenTable API: 1 endpoints with pricing and code examples

Call 1 OpenTable endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`opentable/reviews`](../models/opentable/reviews.md) | Get diner reviews for a restaurant on OpenTable by restaurant ID, with overall and sub-ratings, text, date and diner info. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opentable/reviews", "rid": "r/central-park-boathouse-new-york-2"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
