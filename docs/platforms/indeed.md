# Indeed API: 2 endpoints with pricing and code examples

Call 2 Indeed endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`indeed/company-profile`](../models/indeed/company-profile.md) | Get a comprehensive company profile including overview, employee reviews, ratings by category, salary data by role, interview information,… | $0.01 per call (free daily quota) |
| [`indeed/jobs`](../models/indeed/jobs.md) | Search Indeed job listings by keyword and location, with title, company, location, salary, job type and posting date. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "indeed/company-profile", "company": "stripe"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
