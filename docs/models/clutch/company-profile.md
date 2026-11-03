# Clutch Company Profile API: pricing, parameters and code examples

`clutch/company-profile` · data API · Clutch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Get detailed profile of a company by its slug. Returns company name, rating, tagline, key details (project size, hourly rate, employees, year founded), website URL, and service line breakdown with percentages.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-profile", "slug": "simform"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/company-profile', {'slug': 'simform'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/company-profile", {
  "slug": "simform"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/company-profile", sandbase.Params{
	"slug": "simform",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Company profile slug from search_companies results (e.g. 'simform').  |

## Details

Returns the Clutch profile of one company: name, rating, review count, website URL, key business details, and a breakdown of its service lines. It needs one input, the company `slug`.

### Use cases

- Compare team size and minimum project size of several agencies before sending a request for proposal.
- Build a lead list of agencies with their size, founding year, and website URL.
- Check which services an agency focuses on by reading its service line percentages.
- Enrich a CRM record with a company's Clutch rating and review count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "simform"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company profile slug from search_companies results (e.g. 'simform'). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "details": {
      "employees": "1,000 - 9,999",
      "hourly_rate": "$25 - $49 / hr",
      "languages": "1 Language",
      "locations": "Orlando, FL\n\t\t\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\n\n\t\t\t\t\t\n\t\t\t\t\t+8",
      "min_project_size": "$25,000+",
      "timezones": "4 Timezones",
      "year_founded": "Founded 2010"
    },
    "name": "Simform",
    "rating": "4.8",
    "review_count": "89 reviews",
    "service_lines": [
      {
        "percentage": "20%",
        "service": "AI Development"
      }
    ],
    "slug": "simform",
    "tagline": null,
    "website_url": "https://www.simform.com/?utm_source=clutch.co&utm_medium=referral&utm_campaign=d…"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Company name as shown on its Clutch profile. |
| `data.rating / data.review_count` | Average rating as a string (for example `4.8`) and the number of reviews as text (for example `89 reviews`). |
| `data.tagline` | Short company tagline. It is `null` when the profile has none. |
| `data.website_url` | Company website link. The value can include tracking query parameters. |
| `data.details.min_project_size` | Minimum project size the company lists, as display text. |
| `data.details.hourly_rate` | Hourly rate range the company lists, as display text. |
| `data.details.employees` | Employee count range, as text (for example `1,000 - 9,999`). |
| `data.details.year_founded` | Founding year as text, such as `Founded 2010`. |
| `data.details.locations` | Main office location plus a count of more locations (for example `+8`). The string contains extra whitespace that you should trim. |
| `data.service_lines[].service / data.service_lines[].percentage` | Name of a service line and the share of the company's work it covers, as a percent string. |

### Notes

- Get the `slug` from the results of [Clutch Search Companies](/apis/clutch/search-companies).
- All values in `data.details` are display text, not numbers. Parse them yourself if you need numeric values.
- Call [Clutch Company Reviews](/apis/clutch/company-reviews) for client reviews, or [Clutch Company Portfolio](/apis/clutch/company-portfolio) for past work, using the same company.
- Call [Clutch Company Locations](/apis/clutch/company-locations) to see the full list of offices instead of the shortened `data.details.locations` value.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/clutch/company-profile.json`](../../../catalog/models/clutch/company-profile.json) · Store page: https://www.sandbase.ai/model/clutch/company-profile
