# Clutch API: 6 endpoints with pricing and code examples

Call 6 Clutch endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`clutch/company-locations`](../models/clutch/company-locations.md) | Get office locations for a company including addresses, phone numbers, and employee counts per location. | $0.01 per call (free daily quota) |
| [`clutch/company-portfolio`](../models/clutch/company-portfolio.md) | Get portfolio items (case studies/projects) for a company. Returns project titles and associated service lines. | $0.01 per call (free daily quota) |
| [`clutch/company-profile`](../models/clutch/company-profile.md) | Get detailed profile of a company by its slug. Returns company name, rating, tagline, key details (project size, hourly rate, employees,… | $0.02 per call |
| [`clutch/company-reviews`](../models/clutch/company-reviews.md) | Get paginated reviews for a company. Returns review titles, ratings, dates, and project information (services, project size, project… | $0.01 per call (free daily quota) |
| [`clutch/list-categories`](../models/clutch/list-categories.md) | List top service categories available on Clutch.co. Returns a curated set of popular category slugs that can be used with search_companies… | $0.01 per call (free daily quota) |
| [`clutch/search-companies`](../models/clutch/search-companies.md) | Search for companies in a specific service category on Clutch.co. Returns a paginated list of company summaries. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-locations", "slug": "simform"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
