# Apollo Organization Job Postings API: pricing, parameters and code examples

`apollo/company-job-postings` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Live job postings for one company, by Apollo organization id. Each posting carries its title, location, posted date and source URL. Useful as a hiring signal — which functions a company is expanding, and where.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-job-postings", "organization_id": "5d0a0fbff6512580bf33a120"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-job-postings', {'organization_id': '5d0a0fbff6512580bf33a120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-job-postings", {
  "organization_id": "5d0a0fbff6512580bf33a120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-job-postings", sandbase.Params{
	"organization_id": "5d0a0fbff6512580bf33a120",
})
```

Same call via the path form: `POST /v1/api/apollo/company-job-postings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4  |
| `per_page` | integer |  | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10  |
| `organization_id` | string | yes | The organization ID of the company for which you want to find job postings. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for…  |

## Details

Returns the current job postings for one company on Apollo. Each posting has a title, location, posted time, last seen time and a source URL. You send the Apollo `organization_id` of the company.

### Use cases

- Track which roles a company is hiring for to see which teams are growing.
- Count open postings by `country`, `state` or `city` to see where a company is expanding.
- Alert a sales team when a target account posts jobs in a function you sell to.
- Follow each `url` to read the full posting on the site where it is listed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-job-postings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"organization_id": "5d0a0fbff6512580bf33a120"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `organization_id` | string | Yes | The organization ID of the company for which you want to find job postings. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for orga |
| `page` | integer | No | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 |
| `per_page` | integer | No | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organization_job_postings": [
    {
      "city": "Seattle",
      "country": "United States",
      "id": "6ae6ebcc3aab0600011c9534",
      "last_seen_at": "2026-11-01T07:35:40.880+00:00",
      "posted_at": "2026-10-31T15:35:40.880+00:00",
      "state": "Washington",
      "title": "Backend/API Engineer, Money as a Service",
      "url": "https://www.linkedin.com/jobs/view/backend-api-engineer-money-as-a-service-at-st…"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 10000,
    "total_entries": 513,
    "total_pages": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organization_job_postings[]` | One job posting for the company. The list holds every posting on the current page. |
| `organization_job_postings[].title` | Job title as listed, for example `Backend/API Engineer, Money as a Service`. |
| `organization_job_postings[].city / organization_job_postings[].state / organization_job_postings[].country` | Location of the job. `city` and `state` can be `null` when the posting gives only a country. |
| `organization_job_postings[].posted_at` | Timestamp for when the posting was published, in ISO 8601 format. |
| `organization_job_postings[].last_seen_at` | Timestamp for when the posting was last seen as active, in ISO 8601 format. |
| `organization_job_postings[].url` | Link to the posting. It can point to LinkedIn or to the company's own careers page. |
| `organization_job_postings[].id` | Unique id of the posting. |
| `pagination.total_entries` | Total number of postings found for this company. |
| `pagination.page / pagination.per_page / pagination.total_pages` | Current page number, page size used, and number of pages available. |

### Notes

- Get `organization_id` from [Apollo Organization Search](/apis/apollo/company-search). Use the `organization_id` value of the company you want.
- Use `page` and `per_page` to move through results. Check `pagination.total_pages` to know when to stop.
- Use [Apollo Organization Enrichment](/apis/apollo/company-enrich) to get company details to go with the postings.

### Pricing

$0.01975 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-job-postings.json`](../../../catalog/models/apollo/company-job-postings.json) · Store page: https://www.sandbase.ai/model/apollo/company-job-postings
