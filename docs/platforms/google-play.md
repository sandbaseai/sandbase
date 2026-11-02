# Google Play API: 2 endpoints with pricing and code examples

Call 2 Google Play endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-play/movies`](../models/google-play/movies.md) | Search or browse movies, TV shows, episodes, categories, and charts on Google Play. | $0.00015 per call (free daily quota) |
| [`google-play/reviews`](../models/google-play/reviews.md) | Get Google Play reviews for a product with rating, sort, platform, and paging. | $0.00015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/movies"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
