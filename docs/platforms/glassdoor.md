# Glassdoor API: 3 endpoints with pricing and code examples

Call 3 Glassdoor endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`glassdoor/companies`](../models/glassdoor/companies.md) | Search companies on Glassdoor by name and get company ID, rating, review and salary counts, size, industry and headquarters. | $0.01 per call |
| [`glassdoor/jobs`](../models/glassdoor/jobs.md) | Search Glassdoor job listings by keyword and location, with title, company, rating, salary estimate, location and posting age. | $0.01 per call |
| [`glassdoor/reviews`](../models/glassdoor/reviews.md) | Get employee reviews for a company on Glassdoor by company ID, with rating, pros, cons, job title, date and sub-ratings. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "glassdoor/companies"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
