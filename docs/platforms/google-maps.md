# Google Maps API: 4 endpoints with pricing and code examples

Call 4 Google Maps endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-maps/directions`](../models/google-maps/directions.md) | Get Google Maps directions between two places by car, transit, walking, cycling or flight, with routes, distance, duration and… | $0.01 per call |
| [`google-maps/photo-metadata`](../models/google-maps/photo-metadata.md) | Contributor, place, coordinates, type and date of one Google Maps photo by its data ID. | $0.00015 per call (free daily quota) |
| [`google-maps/reviews`](../models/google-maps/reviews.md) | Get Google Maps reviews for one place with sorting, filtering, and paging. | $0.00015 per call |
| [`google-maps/search`](../models/google-maps/search.md) | Search places on Google Maps by keyword around a location, with name, rating, reviews, address, hours, phone, website, GPS coordinates and… | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/directions"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
