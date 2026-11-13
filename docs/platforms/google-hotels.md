# Google Hotels API: 5 endpoints with pricing and code examples

Call 5 Google Hotels endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-hotels/autocomplete`](../models/google-hotels/autocomplete.md) | Get Google Hotels destination and property suggestions for a partial name, with property tokens for hotel lookups. | $0.01 per call |
| [`google-hotels/photos`](../models/google-hotels/photos.md) | Get photos of a hotel on Google Hotels by property token, with image URLs, categories and paging. | $0.01 per call |
| [`google-hotels/price-calendar`](../models/google-hotels/price-calendar.md) | Get the nightly price of a hotel on Google Hotels for each date in a range, by property token and guest count. | $0.01 per call |
| [`google-hotels/reviews`](../models/google-hotels/reviews.md) | Get guest reviews for a hotel on Google Hotels by property token, with rating, text, date, source and category filters. | $0.01 per call |
| [`google-hotels/search`](../models/google-hotels/search.md) | Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers. | $0.015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/autocomplete", "q": "austin"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
