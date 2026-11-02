# Levels.fyi API: 7 endpoints with pricing and code examples

Call 7 Levels.fyi endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`levels-fyi/company-benefits`](../models/levels-fyi/company-benefits.md) | Retrieve benefits and perks data for a specific company including benefit categories, descriptions, field values, and computed monetary… | $0.01 per call (free daily quota) |
| [`levels-fyi/company-overview`](../models/levels-fyi/company-overview.md) | Retrieve a company profile overview including full company details (name, description, industry, ticker, HQ location, vesting info), a… | $0.01 per call (free daily quota) |
| [`levels-fyi/h1b-salaries`](../models/levels-fyi/h1b-salaries.md) | Retrieve paginated H-1B visa salary records for a given year, sorted by date descending. Each record includes company, job title, wage,… | $0.01 per call (free daily quota) |
| [`levels-fyi/internship-salaries`](../models/levels-fyi/internship-salaries.md) | Retrieve internship salary data across all companies. Returns the full dataset including monthly and hourly pay, location, season, year,… | $0.01 per call (free daily quota) |
| [`levels-fyi/job-families`](../models/levels-fyi/job-families.md) | Retrieve the full directory of job titles and families organized as a flat list. Each job family includes slug, name, category, focus… | $0.01 per call (free daily quota) |
| [`levels-fyi/popular-companies`](../models/levels-fyi/popular-companies.md) | Retrieve a list of popular companies from the Levels.fyi directory with their slugs and salary page URLs. Returns approximately 24 top… | $0.01 per call (free daily quota) |
| [`levels-fyi/salary-summary-md`](../models/levels-fyi/salary-summary-md.md) | Retrieve an aggregate salary summary in Markdown format for a given company and optional job family. Includes median compensation, level… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/company-benefits", "company_slug": "stripe"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
