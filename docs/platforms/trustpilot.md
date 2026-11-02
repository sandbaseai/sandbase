# Trustpilot API: 6 endpoints with pricing and code examples

Call 6 Trustpilot endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`trustpilot/categories`](../models/trustpilot/categories.md) | Retrieve all top-level categories and their sub-categories available on Trustpilot. | $0.01 per call (free daily quota) |
| [`trustpilot/companies-by-category`](../models/trustpilot/companies-by-category.md) | List companies within a specific category with pagination. Returns companies sorted by trust score. | $0.01 per call (free daily quota) |
| [`trustpilot/company-overview`](../models/trustpilot/company-overview.md) | Get full company profile overview including TrustScore, rating distribution, AI summary, and initial reviews. | $0.03 per call |
| [`trustpilot/company-review-summary`](../models/trustpilot/company-review-summary.md) | Get AI summary, review topics, rating breakdown, and recent review texts for a company. Accepts either a direct company domain or a search… | $0.05 per call |
| [`trustpilot/company-reviews`](../models/trustpilot/company-reviews.md) | Fetch paginated reviews for a company with optional star filtering, sort order, and keyword search. | $0.03 per call |
| [`trustpilot/search-companies`](../models/trustpilot/search-companies.md) | Search for companies by name or keyword. Returns basic company info including domain, trust score, star rating, and review count. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/categories"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
