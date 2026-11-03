# Apollo Get Complete Organization Info API: pricing, parameters and code examples

`apollo/company-record` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

The complete Apollo record for one company, by Apollo organization id (not by domain).

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-record", "id": "5d0a0fbff6512580bf33a120"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-record', {'id': '5d0a0fbff6512580bf33a120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-record", {
  "id": "5d0a0fbff6512580bf33a120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-record", sandbase.Params{
	"id": "5d0a0fbff6512580bf33a120",
})
```

Same call via the path form: `POST /v1/api/apollo/company-record` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The Apollo ID for the organization that you want to research. To find organization IDs, call the Organization Search endpoint and identify the organizaton_id value for the organization. Example: 5e66b6381e05b4008c8331b8  |

## Details

Returns the full Apollo record for one company, looked up by its Apollo organization `id`. The response includes firmographics, industry codes, technologies, funding events, headcount changes and social links.

### Use cases

- Build a company profile page with revenue, headcount, location and industry for a known Apollo organization.
- Track a company's funding history and latest round to spot recent investment activity.
- Check which technologies a company uses to qualify leads for a developer tool or security product.
- Watch monthly hiring and churn by department to see where a company is growing or shrinking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-record" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5d0a0fbff6512580bf33a120"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The Apollo ID for the organization that you want to research. To find organization IDs, call the Organization Search endpoint and identify the organizaton_id value for the organization. Example: 5e66b6381e05b4008c8331b8 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organization": {
    "alexa_ranking": 200,
    "angellist_url": "http://angel.co/stripe",
    "annual_revenue": 6935000000.0,
    "annual_revenue_printed": "6.9B",
    "city": "South San Francisco",
    "country": "United States",
    "crunchbase_url": null,
    "current_technologies": [
      {
        "category": "Frameworks and Programming Languages",
        "name": ".NET",
        "uid": "net"
      }
    ],
    "detail_view_loaded": true,
    "employee_metrics": [
      {
        "departments": [
          {
            "churned": 13,
            "functions": null,
            "new": 0,
            "retained": 1389
          }
        ],
        "start_date": "2024-10-01"
      }
    ],
    "estimated_num_employees": 9400,
    "facebook_url": "https://www.facebook.com/StripeHQ"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organization.id / organization.name` | The Apollo organization id and the company name. |
| `organization.estimated_num_employees` | Estimated number of employees at the company. |
| `organization.annual_revenue / organization.annual_revenue_printed` | Annual revenue as a number and as a short printed string such as `6.9B`. |
| `organization.industry / organization.industries / organization.keywords` | The main industry, the full list of industries, and descriptive keywords for the company. |
| `organization.naics_codes` | NAICS industry codes assigned to the company. |
| `organization.current_technologies[]` | Technologies the company uses. Each item has a `name`, a `category` and a `uid`. |
| `organization.funding_events[]` | Funding events with `type`, `amount`, `currency`, `date`, `investors` and `news_url`. Some events have no `amount`. |
| `organization.latest_funding_stage / organization.latest_funding_round_date` | The stage and date of the most recent funding round. |
| `organization.employee_metrics[].departments[]` | Monthly headcount counts per department, starting at `start_date`. Each row has `new`, `retained` and `churned` counts and a `functions` name. A `functions` value of `null` is the row without a department name. |
| `organization.linkedin_url / organization.facebook_url / organization.angellist_url` | Links to the company's social profiles. |

### Notes

- Get the `id` from [Apollo Organization Search](/apis/apollo/company-search). The search results carry the organization id.
- This API takes an Apollo organization `id`, not a domain. To look up a company by domain, use [Apollo Organization Enrichment](/apis/apollo/company-enrich).
- `date` values in `funding_events` are ISO 8601 timestamps. `start_date` in `employee_metrics` is a `YYYY-MM-DD` date.
- For several companies at once, call [Apollo Bulk Organization Enrichment](/apis/apollo/company-bulk-enrich).

### Pricing

$0.01975 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-record.json`](../../../catalog/models/apollo/company-record.json) · Store page: https://www.sandbase.ai/model/apollo/company-record
