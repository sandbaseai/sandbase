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

Returns a list of people from the Apollo database that match your filters, plus a total match count. Each person comes back with a title, a partly hidden last name, and flags that show which contact and location details exist. You filter by job title, location, company size, technology, and more.

### Use cases

- Build a list of CEOs at companies headquartered in a given country.
- Count how many people with a given title match a filter set before you plan outreach.
- Find people at specific companies by passing Apollo company IDs in `organization_ids[]`.
- Narrow a lead list to people whose employer uses certain technologies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/people-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"person_titles[]": ["ceo"], "organization_locations[]": ["United States"], "per_page": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contact_email_status[]` | array | No | The email statuses for the people you want to find. You can add multiple statuses to expand your search. The statuses you can search include: verified unverified likely to engage unavailable |
| `currently_not_using_any_of_technology_uids[]` | array | No | Exclude people from your search based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is upda |
| `currently_using_all_of_technology_uids[]` | array | No | Find people based on all of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check |
| `currently_using_any_of_technology_uids[]` | array | No | Find people based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check |
| `include_similar_titles` | boolean | No | This parameter determines whether people with job titles similar to the titles you define in the person_titles[] parameter are returned in the response. Set this parameter to false when using person_titles[] to return on |
| `organization_ids[]` | array | No | The Apollo IDs for the companies (employers) you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the va |
| `organization_job_locations[]` | array | No | The locations of the jobs being actively recruited by the person's employer. Examples: atlanta; japan |
| `organization_job_posted_at_range[max]` | string | No | The latest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when jobs posted. Example: 2025-09-25 |
| `organization_job_posted_at_range[min]` | string | No | The earliest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for when jobs posted. Example: 2025-07-25 |
| `organization_locations[]` | array | No | The location of the company headquarters for a person's current employer. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters loc |
| `organization_num_employees_ranges[]` | array | No | The number range of employees working for the person's current company. This enables you to find people based on the headcount of their employer. You can add multiple ranges to expand your search results. Each range you  |
| `organization_num_jobs_range[max]` | integer | No | The maximum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. Examples: 50; 500 |
| `organization_num_jobs_range[min]` | integer | No | The minimum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. Examples: 50; 500 |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 |
| `person_locations[]` | array | No | The location where people live. You can search across cities, US states, and countries. To find people based on the headquarters locations of their current employer, use the organization_locations parameter. Examples: ca |
| `person_seniorities[]` | array | No | The job seniority that people hold within their current employer. This enables you to find people that currently hold positions at certain reporting levels, such as Director level or senior IC level. For a person to be i |
| `person_titles[]` | array | No | Job titles held by the people you want to find. For a person to be included in search results, they only need to match 1 of the job titles you add. Adding more job titles expands your search results. Results also include |
| `q_keywords` | string | No | A string of words over which we want to filter the results. |
| `q_organization_domains_list[]` | array | No | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This parameter accepts up to 1,000 domains in a single request. Examples: |
| `q_organization_job_titles[]` | array | No | The job titles that are listed in active job postings at the person's current employer. Examples: sales manager; research analyst |
| `revenue_range[max]` | integer | No | The maximum revenue the person's current employer generates. Use this parameter in combination with revenue_range[min] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure. Examp |
| `revenue_range[min]` | integer | No | The minimum revenue the person's current employer generates. Use this parameter in combination with revenue_range[max] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure. Examp |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "people": [
    {
      "first_name": "Ely",
      "has_city": true,
      "has_country": true,
      "has_direct_phone": "Yes",
      "has_email": true,
      "has_state": true,
      "id": "61fff8b2a417810001a8f4fd",
      "last_name_obfuscated": "Ap***c",
      "last_refreshed_at": "2026-11-01T06:11:22.252+00:00",
      "organization": {
        "has_city": true,
        "has_country": true,
        "has_employee_count": true,
        "has_industry": true,
        "has_phone": true,
        "has_revenue": false,
        "has_state": true,
        "has_zip_code": true
      },
      "title": "CEO Chief Executive Officer"
    }
  ],
  "total_entries": 557824
}
```

### Response fields

| Field | Meaning |
|---|---|
| `people[]` | The list of people that match the search. Its length follows `per_page`. |
| `people[].id` | The Apollo ID of the person. |
| `people[].first_name` | The person's first name. |
| `people[].last_name_obfuscated` | The last name with some letters masked, such as `Ap***c`. |
| `people[].title` | The person's current job title. |
| `people[].has_email / people[].has_direct_phone` | Show whether Apollo holds an email or a direct phone number for the person. `has_email` is a boolean. `has_direct_phone` is a string such as `Yes`. |
| `people[].has_city / people[].has_state / people[].has_country` | Show whether Apollo holds the person's city, state, or country. The values themselves are not in this response. |
| `people[].last_refreshed_at` | ISO 8601 timestamp of when Apollo last refreshed this person's record. |
| `people[].organization.has_employee_count / people[].organization.has_industry / people[].organization.has_revenue` | Show whether Apollo holds the employer's headcount, industry, or revenue. Other `has_` flags on `organization` cover city, state, country, zip code, and phone. |
| `total_entries` | The total number of people that match the filters across all pages. |

### Notes

- Set `page` and `per_page` to move through the results. Use `total_entries` to see how many people match.
- The response gives `has_` flags instead of the actual contact details. Use `id` with [Apollo People Enrichment](/apis/apollo/people-match) to look up a specific person.
- To get values for `organization_ids[]`, call [Apollo Organization Search](/apis/apollo/company-search) and use the `organization_id` values.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/apollo/people-search.json`](../../../catalog/models/apollo/people-search.json) · Store page: https://www.sandbase.ai/model/apollo/people-search
