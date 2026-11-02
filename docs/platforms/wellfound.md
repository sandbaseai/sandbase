# Wellfound API: 5 endpoints with pricing and code examples

Call 5 Wellfound endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`wellfound/company-jobs`](../models/wellfound/company-jobs.md) | List all open job positions at a specific company. Returns job listings with title, compensation, location, and job type. | $0.02 per call |
| [`wellfound/company-profile`](../models/wellfound/company-profile.md) | Retrieve a company profile by slug, including description, size, badges, and basic info. Returns stale_input if the company is not found. | $0.02 per call |
| [`wellfound/job-autocomplete-roles`](../models/wellfound/job-autocomplete-roles.md) | Get a list of common job role slugs available on Wellfound. These slugs can be used to construct Wellfound role search URLs. | $0.01 per call (free daily quota) |
| [`wellfound/trending-jobs`](../models/wellfound/trending-jobs.md) | Fetch featured/trending jobs from the Wellfound homepage, organized by category (trending, engineering, product, design, data, sales,… | $0.01 per call (free daily quota) |
| [`wellfound/trending-startups`](../models/wellfound/trending-startups.md) | Fetch trending startups currently hiring from the Wellfound homepage. Returns a curated list of startups that Wellfound is currently… | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/company-jobs", "company_slug": "stripe"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
