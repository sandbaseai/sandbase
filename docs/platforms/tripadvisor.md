# Tripadvisor API: 2 endpoints with pricing and code examples

Call 2 Tripadvisor endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tripadvisor/reviews`](../models/tripadvisor/reviews.md) | Public reviews of a Tripadvisor hotel, restaurant or attraction by place ID: rating, title, text, date and reviewer. | $0.00015 per call (free daily quota) |
| [`tripadvisor/search`](../models/tripadvisor/search.md) | Search Tripadvisor hotels, restaurants, attractions and places by keyword. | $0.00015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripadvisor/reviews", "place_id": 18941405}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
