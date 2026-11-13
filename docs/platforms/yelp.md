# Yelp API: 3 endpoints with pricing and code examples

Call 3 Yelp endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yelp/place`](../models/yelp/place.md) | Get a Yelp business by place ID or alias with rating, review count, categories, hours, address, phone, website, amenities and menu. | $0.01 per call |
| [`yelp/reviews`](../models/yelp/reviews.md) | Public reviews of a Yelp business by place ID: rating, text, date and reviewer, with paging and sorting. | $0.00015 per call (free daily quota) |
| [`yelp/search`](../models/yelp/search.md) | Search Yelp businesses by keyword and location: name, rating, review count, price level, categories and address. | $0.00015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yelp/place", "place_id": "arabica-brooklyn"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
