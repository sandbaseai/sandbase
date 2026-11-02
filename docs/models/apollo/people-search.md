# Apollo People API Search API: pricing, parameters and code examples

`apollo/people-search` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Use the People API Search endpoint to find net new people in the Apollo database. Several filters are available to help narrow your search. This endpoint is optimized for API usage and does not consume credits.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/people-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/people-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/people-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/people-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/apollo/people-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4  |
| `per_page` | integer |  | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10  |
| `q_keywords` | string |  | A string of words over which we want to filter the results.  |
| `person_titles[]` | array |  | Job titles held by the people you want to find. For a person to be included in search results, they only need to match 1 of the job titles you add. Adding more job titles expands your search results. Results also…  |
| `organization_ids[]` | array |  | The Apollo IDs for the companies (employers) you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the…  |
| `person_locations[]` | array |  | The location where people live. You can search across cities, US states, and countries. To find people based on the headquarters locations of their current employer, use the organization_locations parameter. Examples:…  |
| `revenue_range[max]` | integer |  | The maximum revenue the person's current employer generates. Use this parameter in combination with revenue_range[min] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure.…  |
| `revenue_range[min]` | integer |  | The minimum revenue the person's current employer generates. Use this parameter in combination with revenue_range[max] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure.…  |
| `person_seniorities[]` | array |  | The job seniority that people hold within their current employer. This enables you to find people that currently hold positions at certain reporting levels, such as Director level or senior IC level. For a person to be…  |
| `contact_email_status[]` | array |  | The email statuses for the people you want to find. You can add multiple statuses to expand your search. The statuses you can search include: verified unverified likely to engage unavailable  |
| `include_similar_titles` | boolean |  | This parameter determines whether people with job titles similar to the titles you define in the person_titles[] parameter are returned in the response. Set this parameter to false when using person_titles[] to return…  |
| `organization_locations[]` | array |  | The location of the company headquarters for a person's current employer. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters…  |
| `q_organization_job_titles[]` | array |  | The job titles that are listed in active job postings at the person's current employer. Examples: sales manager; research analyst  |
| `organization_job_locations[]` | array |  | The locations of the jobs being actively recruited by the person's employer. Examples: atlanta; japan  |
| `q_organization_domains_list[]` | array |  | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This parameter accepts up to 1,000 domains in a single request.…  |
| `organization_num_jobs_range[max]` | integer |  | The maximum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. Examples: 50; 500  |
| `organization_num_jobs_range[min]` | integer |  | The minimum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. Examples: 50; 500  |
| `organization_num_employees_ranges[]` | array |  | The number range of employees working for the person's current company. This enables you to find people based on the headcount of their employer. You can add multiple ranges to expand your search results. Each range…  |
| `organization_job_posted_at_range[max]` | string |  | The latest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when jobs posted. Example: 2025-09-25  |
| `organization_job_posted_at_range[min]` | string |  | The earliest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for when jobs posted. Example: 2025-07-25  |
| `currently_using_all_of_technology_uids[]` | array |  | Find people based on all of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly.…  |
| `currently_using_any_of_technology_uids[]` | array |  | Find people based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly.…  |
| `currently_not_using_any_of_technology_uids[]` | array |  | Exclude people from your search based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is…  |

## Details

Use the People API Search endpoint to find net new people in the Apollo database. Several filters are available to help narrow your search. This endpoint is optimized for API usage and does not consume credits.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/people-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"person_titles[]": ["ceo"], "organization_locations[]": ["United States"], "per_page": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contact_email_status[]` | array | No | The email statuses for the people you want to find. You can add multiple statuses to expand your search. The statuses you can search include: verified unverifie |
| `currently_not_using_any_of_technology_uids[]` | array | No | Exclude people from your search based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculate |
| `currently_using_all_of_technology_uids[]` | array | No | Find people based on all of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data  |
| `currently_using_any_of_technology_uids[]` | array | No | Find people based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data  |
| `include_similar_titles` | boolean | No | This parameter determines whether people with job titles similar to the titles you define in the person_titles[] parameter are returned in the response. Set thi |
| `organization_ids[]` | array | No | The Apollo IDs for the companies (employers) you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find ID |
| `organization_job_locations[]` | array | No | The locations of the jobs being actively recruited by the person's employer. Examples: atlanta; japan |
| `organization_job_posted_at_range[max]` | string | No | The latest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[min] to set a da |
| `organization_job_posted_at_range[min]` | string | No | The earliest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[max] to set a  |
| `organization_locations[]` | array | No | The location of the company headquarters for a person's current employer. You can search across cities, US states, and countries. If a company has several offic |
| `organization_num_employees_ranges[]` | array | No | The number range of employees working for the person's current company. This enables you to find people based on the headcount of their employer. You can add mu |
| `organization_num_jobs_range[max]` | integer | No | The maximum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[min] to set a job |
| `organization_num_jobs_range[min]` | integer | No | The minimum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[max] to set a job |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page pa |
| `person_locations[]` | array | No | The location where people live. You can search across cities, US states, and countries. To find people based on the headquarters locations of their current empl |
| `person_seniorities[]` | array | No | The job seniority that people hold within their current employer. This enables you to find people that currently hold positions at certain reporting levels, suc |
| `person_titles[]` | array | No | Job titles held by the people you want to find. For a person to be included in search results, they only need to match 1 of the job titles you add. Adding more  |
| `q_keywords` | string | No | A string of words over which we want to filter the results. |
| `q_organization_domains_list[]` | array | No | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This paramete |
| `q_organization_job_titles[]` | array | No | The job titles that are listed in active job postings at the person's current employer. Examples: sales manager; research analyst |
| `revenue_range[max]` | integer | No | The maximum revenue the person's current employer generates. Use this parameter in combination with revenue_range[min] to set a revenue range. Do not enter curr |
| `revenue_range[min]` | integer | No | The minimum revenue the person's current employer generates. Use this parameter in combination with revenue_range[max] to set a revenue range. Do not enter curr |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/people-search.json`](../../../catalog/models/apollo/people-search.json) · Store page: https://www.sandbase.ai/model/apollo/people-search
