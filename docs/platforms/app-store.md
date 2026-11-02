# App Store API: 3 endpoints with pricing and code examples

Call 3 App Store endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`app-store/product`](../models/app-store/product.md) | Read an iOS or Mac app's details, version history, ratings, privacy, and related apps. | $0.00015 per call (free daily quota) |
| [`app-store/reviews`](../models/app-store/reviews.md) | Read Apple App Store reviews for an app in one storefront country, page by page. | $0.00015 per call (free daily quota) |
| [`app-store/search`](../models/app-store/search.md) | Search iPhone, iPad, and Mac apps or developers on the Apple App Store by storefront. | $0.00015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/product", "product_id": "570060128"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
