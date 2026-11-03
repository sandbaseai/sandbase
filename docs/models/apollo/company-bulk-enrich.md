# Apollo Bulk Organization Enrichment API: pricing, parameters and code examples

`apollo/company-bulk-enrich` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.01975 per run, depending on parameters · **Modes:** sync

Enrich up to 10 companies in one call. Body takes `domains`, an array of bare domains.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.01975 |

Formula: `0.01975 * Math.max(1.0, Math.min(10.0, len(params["domains[]"] ?? []) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-bulk-enrich", "domains[]": ["stripe.com", "notion.so"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-bulk-enrich', {'domains[]': ['stripe.com', 'notion.so']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-bulk-enrich", {
  "domains[]": [
    "stripe.com",
    "notion.so"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-bulk-enrich", sandbase.Params{
	"domains[]": []any{"stripe.com", "notion.so"},
})
```

Same call via the path form: `POST /v1/api/apollo/company-bulk-enrich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domains[]` | array | yes | The domain of each company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io and microsoft.com  |

## Details

Returns firmographic data for up to 10 companies in one call. Each company comes back as an object in `organizations`, with headcount, revenue, industry, location, funding events and social links. The input is `domains[]`, an array of bare domains such as `stripe.com`.

### Use cases

- Fill in missing company size, industry and location for a list of CRM accounts from their domains.
- Score and rank target accounts by `estimated_num_employees`, `organization_revenue` and headcount growth.
- Find recently funded companies by reading `latest_funding_round_date` and `funding_events[]`.
- Group accounts by department size to see which have large engineering or data science teams.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-bulk-enrich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domains[]": ["stripe.com", "notion.so"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domains[]` | array | Yes | The domain of each company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io and microsoft.com |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "error_code": null,
  "error_message": null,
  "missing_records": 0,
  "organizations": [
    {
      "alexa_ranking": 200,
      "angellist_url": "http://angel.co/stripe",
      "city": "South San Francisco",
      "country": "United States",
      "crunchbase_url": null,
      "departmental_head_count": {
        "accounting": 85,
        "administrative": 61,
        "arts_and_design": 248,
        "business_development": 262,
        "consulting": 117,
        "data_science": 402,
        "education": 12,
        "engineering": 4380
      },
      "estimated_num_employees": 9400,
      "facebook_url": "https://www.facebook.com/StripeHQ",
      "founded_year": 2010,
      "funding_events": [
        {
          "amount": "14.6M",
          "currency": "$",
          "date": "2026-03-01T00:00:00.000+00:00",
          "detected_at": "2026-05-15T18:09:42.121Z",
          "id": "6a076166792a21000119ce70",
          "investors": "",
          "news_url": null,
          "type": "Venture (Round not Specified)"
        }
      ],
      "has_intent_signal_account": false,
      "id": "5d0a0fbff6512580bf33a120"
    }
  ],
  "status": "success",
  "total_requested_domains": 2,
  "total_requested_records": null,
  "unique_domains": 2,
  "unique_enriched_records": 2,
  "unique_records": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organizations[].name / organizations[].primary_domain` | Company name and its main domain. |
| `organizations[].id` | Apollo ID of the organization. Use it to look up the same company in other Apollo APIs. |
| `organizations[].estimated_num_employees` | Estimated number of employees. |
| `organizations[].organization_revenue / organizations[].organization_revenue_printed` | Revenue as a full number and as a short printed string such as `6.9B`. |
| `organizations[].organization_headcount_six_month_growth / organizations[].organization_headcount_twelve_month_growth / organizations[].organization_headcount_twenty_four_month_growth` | Headcount growth over the last 6, 12 and 24 months, given as a decimal fraction. A value of `0.2` reads as 20 percent. |
| `organizations[].departmental_head_count` | Object of head counts per department, such as `engineering` and `accounting`. |
| `organizations[].industry / organizations[].industries[] / organizations[].keywords[]` | Main industry, all listed industries and descriptive keywords for the company. |
| `organizations[].funding_events[]` | List of funding events. Each has `amount`, `currency`, `date`, `type`, `investors` and `news_url`. Some events lack an `amount`. |
| `organizations[].latest_funding_stage / organizations[].latest_funding_round_date` | Stage and date of the most recent funding round. |
| `organizations[].linkedin_url / organizations[].facebook_url / organizations[].angellist_url` | Links to the company profiles on LinkedIn, Facebook and AngelList. Any of them can be `null`. |
| `organizations[].city / organizations[].country / organizations[].postal_code / organizations[].phone` | Headquarters location and phone number. |

### Notes

- Pass bare domains in `domains[]`, without `www.` or the `@` symbol.
- Check `total_requested_domains`, `unique_enriched_records` and `missing_records` to see how many domains were matched.
- Match each result to your input by `primary_domain`. The returned `name` may differ from what you expect for a domain, so verify the pair.
- For a single company, use [Apollo Organization Enrichment](/apis/apollo/company-enrich). For full details on one company by ID, use [Apollo Get Complete Organization Info](/apis/apollo/company-record).

### Pricing

Billed at the actual cost of each call, about $0.01975 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-bulk-enrich.json`](../../../catalog/models/apollo/company-bulk-enrich.json) · Store page: https://www.sandbase.ai/model/apollo/company-bulk-enrich
