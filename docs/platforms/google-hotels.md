# Google Hotels API: 2 endpoints with pricing and code examples

Call 2 Google Hotels endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-hotels/reviews`](../models/google-hotels/reviews.md) | Get guest reviews for a hotel on Google Hotels by property token, with rating, text, date, source and category filters. | $0.01 per call |
| [`google-hotels/search`](../models/google-hotels/search.md) | Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/reviews", "property_token": "CgsIlOPW65yHnZPwARAB"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
