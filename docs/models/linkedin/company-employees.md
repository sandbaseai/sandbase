# LinkedIn Company Employees API: pricing, parameters and code examples

`linkedin/company-employees` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.006 per call · **Modes:** sync

List the employees of a LinkedIn company by name or company URL, with optional job-title filtering.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-employees", "company": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-employees', {'company': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-employees", {
  "company": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-employees", sandbase.Params{
	"company": "stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-employees` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-10, default 10). range 1–10 |
| `company` | string | yes | Company name or LinkedIn company URL (e.g. google or https://www.linkedin.com/company/google/).  |
| `jobTitle` | string |  | Optional job-title filter supporting boolean operators (e.g. CEO OR CTO).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `openToWork` or `premium`, and it is served only by a source that…  |

## Details

This API returns a list of people who work at a LinkedIn company. It needs a company name or a LinkedIn company URL, and it can filter the people by job title.

### Use cases

- Build a list of product or sales contacts at a target company.
- Find the CEO or CTO of a company with a `jobTitle` filter such as `CEO OR CTO`.
- Map where a company's staff are based by reading the country and city fields.
- Collect profile URLs to pass to a profile lookup for deeper details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-employees" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "company": "stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company` | string | Yes | Company name or LinkedIn company URL (e.g. google or https://www.linkedin.com/company/google/). |
| `jobTitle` | string | No | Optional job-title filter supporting boolean operators (e.g. CEO OR CTO). |
| `limit` | integer | No | Maximum number of results to return (1-10, default 10). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `openToWork` or `premium`, and it is served only by a source that retu |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "city": "San Francisco, California",
        "companyUrl": "https://www.linkedin.com/company/stripe",
        "country": "United States",
        "countryCode": "US",
        "handle": "jeffwweinstein",
        "influencer": false,
        "jobTitle": "Product at Stripe",
        "location": "San Francisco, California, United States",
        "name": "Jeff Weinstein",
        "openToWork": false,
        "premium": true,
        "url": "https://www.linkedin.com/in/jeffwweinstein"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].name` | Full name of the employee as shown on the profile. |
| `data.items[].jobTitle` | Headline text with the role and company, for example `Product at Stripe`. |
| `data.items[].url / data.items[].handle` | Link to the LinkedIn profile and the handle at the end of that link. |
| `data.items[].location` | Location text shown on the profile, such as city, region and country. |
| `data.items[].city` | City or metro area of the employee. Some items leave it out. |
| `data.items[].country / data.items[].countryCode` | Country name and its two-letter code, for example `United States` and `US`. |
| `data.items[].companyUrl` | LinkedIn URL of the company the employee was listed under. |
| `data.items[].openToWork / data.items[].premium / data.items[].influencer` | Boolean flags for the open-to-work status, a premium account, and an influencer label. |
| `data.items[].image` | Profile photo URL. Some items leave it out. |
| `found` | `true` when the lookup returned results. |

### Notes

- Use `limit` to set the number of results, from 1 to 10. The default is 10.
- Pass a company name such as `stripe` or a full company URL in `company`.
- Use `requireFields` only when you need a field such as `openToWork` or `premium` guaranteed. It can change the price of the call.
- To read details about one person, take the `url` value and call [LinkedIn User Profile](/apis/linkedin/user-detail). For company details, use [LinkedIn Company](/apis/linkedin/company).

### Pricing

Billed at the actual cost of each call, about $0.006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/company-employees.json`](../../../catalog/models/linkedin/company-employees.json) · Store page: https://www.sandbase.ai/model/linkedin/company-employees
