# Apollo Organization Search API: pricing, parameters and code examples

`apollo/company-search` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Find companies matching criteria: name, domain, headcount, industry, location, funding stage and technologies in use.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/apollo/company-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4  |
| `per_page` | integer |  | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10  |
| `organization_ids[]` | array |  | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, identify the values for organization_id when you call this…  |
| `revenue_range[max]` | integer |  | Search for organizations based on their revenue. Use this parameter to set the upper range of organization revenue. Use the revenue_range[min] parameter to set the lower range of revenue. Do not enter currency symbols,…  |
| `revenue_range[min]` | integer |  | Search for organizations based on their revenue. Use this parameter to set the lower range of organization revenue. Use the revenue_range[max] parameter to set the upper range of revenue. Do not enter currency symbols,…  |
| `q_organization_name` | string |  | Filter search results to include a specific company name. If the value you enter for this parameter does not match with a company's name, the company will not appear in search results, even if it matches other…  |
| `organization_locations[]` | array |  | The location of the company headquarters. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters location. For example, if you…  |
| `total_funding_range[max]` | integer |  | The maximum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[min] to set a monetary range for all of the company's funding rounds. Do not…  |
| `total_funding_range[min]` | integer |  | The minimum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[max] to set a monetary range for all of the company's funding rounds. Do not…  |
| `q_organization_job_titles[]` | array |  | The job titles that are listed in active job postings at the company. Examples: sales manager; research analyst  |
| `organization_job_locations[]` | array |  | The locations of the jobs being actively recruited by the company. Examples: atlanta; japan  |
| `organization_not_locations[]` | array |  | Exclude companies from search results based on the location of the company headquarters. You can use cities, US states, and countries as locations to exclude. This parameter is useful for ensuring you do not prospect…  |
| `q_organization_domains_list[]` | array |  | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This parameter accepts up to 1,000 domains in a single request.…  |
| `q_organization_keyword_tags[]` | array |  | Filter search results based on keywords associated with companies. For example, you can enter mining as a value to return only companies that have an association with the mining industry. Examples: mining; sales…  |
| `latest_funding_date_range[max]` | string |  | The latest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[min] to set a date range for when the company received its most recent funding…  |
| `latest_funding_date_range[min]` | string |  | The earliest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[max] to set a date range for when the company received its most recent funding…  |
| `latest_funding_amount_range[max]` | integer |  | The maximium amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[min] to set a monetary range for the company's most recent funding round.…  |
| `latest_funding_amount_range[min]` | integer |  | The minimum amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[max] to set a monetary range for the company's most recent funding round.…  |
| `organization_num_jobs_range[max]` | integer |  | The maximum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. Examples: 50; 500  |
| `organization_num_jobs_range[min]` | integer |  | The minimum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. Examples: 50; 500  |
| `organization_num_employees_ranges[]` | array |  | The number range of employees working for the company. This enables you to find companies based on headcount. You can add multiple ranges to expand your search results. Each range you add needs to be a string, with the…  |
| `organization_job_posted_at_range[max]` | string |  | The latest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when jobs posted. Example: 2025-09-25  |
| `organization_job_posted_at_range[min]` | string |  | The earliest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for when jobs posted. Example: 2025-07-25  |
| `currently_using_any_of_technology_uids[]` | array |  | Find organizations based on the technologies they currently use. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check out…  |

## Details

Find companies matching criteria: name, domain, headcount, industry, location, funding stage and technologies in use.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"organization_locations[]": ["United States"], "per_page": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `currently_using_any_of_technology_uids[]` | array | No | Find organizations based on the technologies they currently use. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from mult |
| `latest_funding_amount_range[max]` | integer | No | The maximium amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[min] to set a mo |
| `latest_funding_amount_range[min]` | integer | No | The minimum amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[max] to set a mon |
| `latest_funding_date_range[max]` | string | No | The latest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[min] to set a date ran |
| `latest_funding_date_range[min]` | string | No | The earliest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[max] to set a date r |
| `organization_ids[]` | array | No | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, identify  |
| `organization_job_locations[]` | array | No | The locations of the jobs being actively recruited by the company. Examples: atlanta; japan |
| `organization_job_posted_at_range[max]` | string | No | The latest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when  |
| `organization_job_posted_at_range[min]` | string | No | The earliest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for whe |
| `organization_locations[]` | array | No | The location of the company headquarters. You can search across cities, US states, and countries. If a company has several office locations, results are still b |
| `organization_not_locations[]` | array | No | Exclude companies from search results based on the location of the company headquarters. You can use cities, US states, and countries as locations to exclude. T |
| `organization_num_employees_ranges[]` | array | No | The number range of employees working for the company. This enables you to find companies based on headcount. You can add multiple ranges to expand your search  |
| `organization_num_jobs_range[max]` | integer | No | The maximum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. E |
| `organization_num_jobs_range[min]` | integer | No | The minimum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. E |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page pa |
| `q_organization_domains_list[]` | array | No | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This paramete |
| `q_organization_job_titles[]` | array | No | The job titles that are listed in active job postings at the company. Examples: sales manager; research analyst |
| `q_organization_keyword_tags[]` | array | No | Filter search results based on keywords associated with companies. For example, you can enter mining as a value to return only companies that have an associatio |
| `q_organization_name` | string | No | Filter search results to include a specific company name. If the value you enter for this parameter does not match with a company's name, the company will not a |
| `revenue_range[max]` | integer | No | Search for organizations based on their revenue. Use this parameter to set the upper range of organization revenue. Use the revenue_range[min] parameter to set  |
| `revenue_range[min]` | integer | No | Search for organizations based on their revenue. Use this parameter to set the lower range of organization revenue. Use the revenue_range[max] parameter to set  |
| `total_funding_range[max]` | integer | No | The maximum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[min] to set a mone |
| `total_funding_range[min]` | integer | No | The minimum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[max] to set a mone |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-search.json`](../../../catalog/models/apollo/company-search.json) · Store page: https://www.sandbase.ai/model/apollo/company-search
