# Channel3 API: 8 endpoints with pricing and code examples

Call 8 Channel3 endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`channel3/brands`](../models/channel3/brands.md) | List top brands, optionally only those selling given categories, with cursor paging. | from $0 per run, depending on parameters |
| [`channel3/brands-search`](../models/channel3/brands-search.md) | Find brands by name or keyword, optionally within categories, to filter product searches. | from $0 per run, depending on parameters |
| [`channel3/categories`](../models/channel3/categories.md) | List product categories page by page, optionally only the top-level ones. | from $0 per run, depending on parameters |
| [`channel3/categories-search`](../models/channel3/categories-search.md) | Find product categories by keyword or meaning, to filter product searches by slug. | from $0 per run, depending on parameters |
| [`channel3/lookup`](../models/channel3/lookup.md) | Resolve a retailer product-page URL to a canonical product with offers and variants. | $0.007 per call |
| [`channel3/search`](../models/channel3/search.md) | Search products across retailers by text or image URL, with offers and pagination. | $0.007 per call |
| [`channel3/websites`](../models/channel3/websites.md) | List top retailers, optionally only those selling given categories, with cursor paging. | from $0 per run, depending on parameters |
| [`channel3/websites-search`](../models/channel3/websites-search.md) | Find retailers by name or domain, optionally within categories, to filter product search. | from $0 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "channel3/brands"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
