# Web3.career API: 9 endpoints with pricing and code examples

Call 9 Web3.career endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`web3-career/company-jobs`](../models/web3-career/company-jobs.md) | Fetch all job listings for a specific company by its URL slug. Returns paginated job listings posted by the company. | $0.01 per call (free daily quota) |
| [`web3-career/intelligence-report`](../models/web3-career/intelligence-report.md) | Fetch the Web3 Career Intelligence Report content and statistics. Returns the report title, full text content, key statistical findings,… | $0.01 per call (free daily quota) |
| [`web3-career/job-detail`](../models/web3-career/job-detail.md) | Fetch full details for a single job listing by URL. Returns the job title, company name, full description text, salary range, and… | $0.01 per call (free daily quota) |
| [`web3-career/job-listings`](../models/web3-career/job-listings.md) | Fetch general job listings from the homepage with pagination. Returns Web3 job postings including title, company, location, salary, tags,… | $0.01 per call (free daily quota) |
| [`web3-career/jobs-by-tag`](../models/web3-career/jobs-by-tag.md) | Fetch job listings filtered by a skill or category tag. Returns paginated results for the given tag. | $0.01 per call (free daily quota) |
| [`web3-career/remote-jobs`](../models/web3-career/remote-jobs.md) | Fetch remote-only job listings with pagination. Filters to positions explicitly tagged as remote work opportunities. | $0.01 per call (free daily quota) |
| [`web3-career/search-jobs`](../models/web3-career/search-jobs.md) | Search for jobs using a keyword query. Returns paginated job listings matching the search term. | $0.01 per call (free daily quota) |
| [`web3-career/web3-companies`](../models/web3-career/web3-companies.md) | Fetch a paginated list of Web3 companies hiring on the platform. Each company includes its name and profile page URL. | $0.01 per call (free daily quota) |
| [`web3-career/web3-salaries`](../models/web3-career/web3-salaries.md) | Fetch average salaries for various Web3 roles. Returns a list of roles with their average salary and a link to the role's detail page. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/company-jobs", "company_slug": "stripe"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
