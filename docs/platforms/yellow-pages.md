# Yellow Pages API: 7 endpoints with pricing and code examples

Call 7 Yellow Pages endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yellowpages/business-details`](../models/yellowpages/business-details.md) | Fetch comprehensive details for a specific business by its YellowPages URL path. Returns name, contact info, hours of operation,… | $0.03 per call |
| [`yellowpages/business-reviews`](../models/yellowpages/business-reviews.md) | Retrieve customer reviews for a business from its YellowPages detail page. Returns review author, date, star rating, optional title, and… | $0.03 per call |
| [`yellowpages/category-list`](../models/yellowpages/category-list.md) | List business categories from the YellowPages categories page, organized by service group (e.g., Home Services, Medical Services, Auto… | $0.03 per call |
| [`yellowpages/check-pos-technology`](../models/yellowpages/check-pos-technology.md) | Check a business website for POS (Point of Sale) technology signals by scanning the page HTML for mentions of specific software platforms… | $0.03 per call |
| [`yellowpages/explore-cities`](../models/yellowpages/explore-cities.md) | Return a list of all US states from the YellowPages sitemap for browsing businesses by location. Each state entry includes the state name… | $0.03 per call |
| [`yellowpages/search-businesses`](../models/yellowpages/search-businesses.md) | Full-text search for businesses by keyword and location on YellowPages.com. | $0.03 per call |
| [`yellowpages/search-filters`](../models/yellowpages/search-filters.md) | Get available search filters for a query and location. Returns quick filter options (e.g., 'OPEN 24 Hours') and nearby location… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/business-details", "url": "https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
