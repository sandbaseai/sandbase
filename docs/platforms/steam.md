# Steam API: 4 endpoints with pricing and code examples

Call 4 Steam endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`steam/app`](../models/steam/app.md) | Get a Steam game or app by app ID with title, price, discount, release date, developer, publisher, genres, review summary and platform… | $0.00015 per call |
| [`steam/app-reviews`](../models/steam/app-reviews.md) | Get user reviews for a Steam product with filtering and cursor-based pagination. Returns reviews with author info (playtime, games owned),… | $0.03 per call |
| [`steam/featured`](../models/steam/featured.md) | Get featured, special, trending, and top-selling products from the Steam store. Returns products grouped by category (specials,… | $0.03 per call |
| [`steam/search`](../models/steam/search.md) | Search the Steam store by keyword and get games and apps with app ID, title, price, discount, release date and review summary. | $0.00015 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "steam/app", "app_id": 730}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
