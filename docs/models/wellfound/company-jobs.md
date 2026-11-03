# Wellfound Company Jobs API: pricing, parameters and code examples

`wellfound/company-jobs` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

List all open job positions at a specific company. Returns job listings with title, compensation, location, and job type.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/company-jobs", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/company-jobs', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/company-jobs", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/company-jobs", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/company-jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company_slug` | string | yes | Company slug (e.g., 'mixpanel', 'juniper-square')  |

## Details

Returns the open job listings for one company on Wellfound. You pass the company's Wellfound slug, such as `stripe`, and get back each job's title, job type, locations, remote flag, and compensation text.

### Use cases

- Track the open roles at a target employer and spot new postings over time.
- Build a list of engineering or product openings at a company you want to apply to.
- Compare hiring locations across a company's open positions.
- Feed a recruiting dashboard with the current job slugs and IDs for a set of startups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/company-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | Company slug (e.g., 'mixpanel', 'juniper-square') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "company": "Stripe",
    "jobs": [
      {
        "compensation": "",
        "id": "4956127",
        "jobType": "full_time",
        "locationNames": [
          "Toronto"
        ],
        "remote": false,
        "slug": "product-manager-terminal-payments",
        "title": "Product Manager, Terminal Payments"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.company` | Name of the company the jobs belong to. |
| `data.jobs[].id` | Identifier of the job listing, returned as a string. |
| `data.jobs[].title` | Job title as listed, for example `Product Manager, Terminal Payments`. |
| `data.jobs[].slug` | URL-style name of the job listing. |
| `data.jobs[].jobType` | Type of employment, for example `full_time`. |
| `data.jobs[].locationNames[]` | List of city names where the job is based. |
| `data.jobs[].remote` | Boolean that shows whether the job is marked as remote. |
| `data.jobs[].compensation` | Compensation text for the job. It can be an empty string when the listing shows no pay. |
| `status` | Result status of the call, `success` when it worked. |

### Notes

- Use the company's Wellfound slug for `company_slug`. It is the company name part of its Wellfound URL, in lowercase with hyphens, such as `juniper-square`.
- The `compensation` value is often empty, so do not rely on it being filled.
- To get details about the company itself, call [Wellfound Company Profile](/apis/wellfound/company-profile).
- To see which roles and startups are popular right now, try [Wellfound Trending Jobs](/apis/wellfound/trending-jobs) or [Wellfound Trending Startups](/apis/wellfound/trending-startups).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wellfound/company-jobs.json`](../../../catalog/models/wellfound/company-jobs.json) · Store page: https://www.sandbase.ai/model/wellfound/company-jobs
