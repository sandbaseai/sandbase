# Apollo Organization Enrichment API: pricing, parameters and code examples

`apollo/company-enrich` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Enrich one company by domain. `domain` is the only parameter and it must be the bare domain (apple.com), not a full URL.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-enrich", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-enrich', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-enrich", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-enrich", sandbase.Params{
	"domain": "stripe.com",
})
```

Same call via the path form: `POST /v1/api/apollo/company-enrich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | The domain of the company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com  |

## Details

Returns a company profile for one domain, such as `stripe.com`. The profile includes headcount, revenue, industry, funding events, technologies in use, and social links. The only input is `domain`, written as a bare domain.

### Use cases

- Fill in missing company details in a CRM from a list of customer domains.
- Score sales leads by employee count, annual revenue, and latest funding stage.
- Find companies that use a given tool by reading the technology list.
- Track hiring focus by comparing department head counts and headcount growth.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-enrich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | The domain of the company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com |

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
    "departmental_head_count": {
      "accounting": 85,
      "administrative": 61,
      "arts_and_design": 248,
      "business_development": 262,
      "consulting": 117,
      "data_science": 402,
      "education": 12,
      "engineering": 4380,
      "entrepreneurship": 11,
      "finance": 924,
      "human_resources": 669,
      "information_technology": 76
    },
    "estimated_num_employees": 9400,
    "facebook_url": "https://www.facebook.com/StripeHQ",
    "founded_year": 2010
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organization.name / organization.id` | Company name and its record ID. Use the `id` with other Apollo company APIs. |
| `organization.estimated_num_employees` | Estimated number of employees at the company. |
| `organization.annual_revenue / organization.annual_revenue_printed` | Annual revenue as a number and as a short printed string such as `6.9B`. |
| `organization.industry / organization.industries / organization.keywords` | Main industry, the full list of industries, and keywords that describe what the company does. |
| `organization.departmental_head_count` | Head count per department, such as `engineering`, `sales`, and `finance`. |
| `organization.organization_headcount_six_month_growth / organization.organization_headcount_twelve_month_growth / organization.organization_headcount_twenty_four_month_growth` | Headcount growth over 6, 12, and 24 months, given as decimal fractions. For example, `0.1995` is about 20 percent. |
| `organization.funding_events[]` | List of funding events. Each has `type`, `date`, `amount`, `currency`, `investors`, and `news_url`. Some events have no `amount`. |
| `organization.latest_funding_stage / organization.latest_funding_round_date` | Stage and date of the most recent funding round. |
| `organization.current_technologies[].name / organization.current_technologies[].category` | Name and category of each technology the company uses. |
| `organization.linkedin_url / organization.facebook_url / organization.angellist_url` | Links to the company's social and profile pages. Some links can be `null`. |

### Notes

- Pass `domain` as a bare domain such as `stripe.com`. Leave out `www.`, `@`, and the URL scheme.
- `organization.id` is a 24-character hex string. Use it with [Apollo Get Complete Organization Info](/apis/apollo/company-record).
- To enrich many domains in one call, use [Apollo Bulk Organization Enrichment](/apis/apollo/company-bulk-enrich).
- Dates in `funding_events[]` are ISO 8601 strings in UTC.

### Pricing

$0.01975 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-enrich.json`](../../../catalog/models/apollo/company-enrich.json) · Store page: https://www.sandbase.ai/model/apollo/company-enrich
