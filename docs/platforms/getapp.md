# GetApp API: 10 endpoints with pricing and code examples

Call 10 GetApp endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`getapp/blog-research`](../models/getapp/blog-research.md) | Retrieve blog posts and software research guides from GetApp's resources section. Returns all published posts with metadata, topics, and… | $0.01 per call (free daily quota) |
| [`getapp/category-leaders`](../models/getapp/category-leaders.md) | Retrieve the category page data including top-ranked software products, buyers guide content, facets, and pagination for a given category. | $0.01 per call (free daily quota) |
| [`getapp/compare-software`](../models/getapp/compare-software.md) | Compare two software products side-by-side, including features, pricing, reviews, pros/cons, and support options. slug1 is the full… | $0.01 per call (free daily quota) |
| [`getapp/list-categories`](../models/getapp/list-categories.md) | List all software categories available on GetApp, organized by group header. Returns category names, slugs, header groups, and listing… | $0.01 per call (free daily quota) |
| [`getapp/list-software-by-category`](../models/getapp/list-software-by-category.md) | List software products in a specific category with pagination. Returns listings with ratings, reviews, pricing info, and facets for… | $0.01 per call (free daily quota) |
| [`getapp/software-alternatives`](../models/getapp/software-alternatives.md) | Retrieve alternative software products for a given product, with detailed comparisons including ratings, pricing, and feature overlap. | $0.01 per call (free daily quota) |
| [`getapp/software-details`](../models/getapp/software-details.md) | Retrieve full details for a software product including description, ratings, reviews, features, integrations, pricing, screenshots, and… | $0.01 per call (free daily quota) |
| [`getapp/software-integrations`](../models/getapp/software-integrations.md) | Retrieve integrations for a software product, including integration names, ratings, and review summaries. | $0.01 per call (free daily quota) |
| [`getapp/software-pricing`](../models/getapp/software-pricing.md) | Retrieve detailed pricing plans for a software product, including plan names, starting prices, and feature lists per plan. | $0.01 per call (free daily quota) |
| [`getapp/software-reviews`](../models/getapp/software-reviews.md) | Retrieve user reviews and rating breakdowns for a software product, including review snippets, individual reviews, and field-level ratings. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/blog-research"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
