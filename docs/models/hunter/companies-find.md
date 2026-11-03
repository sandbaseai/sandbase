# Hunter Companies Find API: pricing, parameters and code examples

`hunter/companies-find` · data API · Hunter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0049 per call (free daily quota) · **Modes:** async

Look up a company's full profile — industry, size, location, tech stack — from its domain.

## Pricing

- **$0.0049 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hunter/companies-find", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hunter/companies-find', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hunter/companies-find", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hunter/companies-find", sandbase.Params{
	"domain": "stripe.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/hunter/companies-find` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Domain name, e.g. 'stripe.com'. Preferred over company — it skips the name-to-domain conversion.  |

## Details

Returns a company profile for a single domain. The profile covers industry codes, headcount, location, funding rounds, social handles, and detected technologies. The only input is `domain`, such as `stripe.com`.

### Use cases

- Enrich a CRM account record with industry, headcount, and address from a company's domain.
- Segment leads by detected technologies in `data.tech`, for example companies that use `adyen`.
- Score accounts by `data.metrics.employeesCount` and `data.metrics.raised` before outreach.
- Collect the LinkedIn, Twitter, and YouTube handles for a company to start social research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hunter/companies-find" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Domain name, e.g. 'stripe.com'. Preferred over company — it skips the name-to-domain conversion. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "category": {
      "gicsCode": "45103010",
      "industry": "Internet Software & Services",
      "industryGroup": "Software & Services",
      "naics6Codes": [
        "519130"
      ],
      "naics6Codes2022": [
        "519290"
      ],
      "naicsCode": "51",
      "sector": "Information Technology",
      "sic4Codes": [
        "73"
      ],
      "sicCode": "36",
      "subIndustry": "Internet Software & Services"
    },
    "companyType": "privately held",
    "crunchbase": {
      "handle": null
    },
    "description": "Stripe is a financial services platform that enables businesses to accept paymen…",
    "domain": "stripe.com",
    "domainAliases": [],
    "emailProvider": "google.com",
    "facebook": {
      "handle": "175383762511776",
      "likes": null
    },
    "foundedYear": 2010,
    "fundingRounds": [
      {
        "amount": "$600000000",
        "date": "2020-04-16",
        "investors": [],
        "type": "Series G"
      }
    ],
    "geo": {
      "city": "South San Francisco",
      "country": "United States",
      "countryCode": "US",
      "lat": 37.65466,
      "lng": -122.40775,
      "postalCode": "94080",
      "state": "California",
      "stateCode": "CA",
      "streetAddress": "Oyster Point Blvd",
      "streetName": "Oyster Point Blvd",
      "streetNumber": null,
      "subPremise": null
    },
    "id": "c60603a0-001c-5ca3-86a2-c571c6d43c25"
  },
  "meta": {
    "domain": "stripe.com"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name / data.legalName` | Display name and legal name of the company. |
| `data.description` | Short text description of what the company does. |
| `data.category.industry / data.category.sector / data.category.subIndustry` | Industry classification of the company. Related code fields such as `gicsCode`, `naicsCode`, and `sicCode` sit in the same object. |
| `data.metrics.employees / data.metrics.employeesCount` | Employee count as a range string and as a single number. |
| `data.metrics.raised` | Total funding raised, as a number. Compare it with the amounts in `data.fundingRounds`. |
| `data.fundingRounds[].type / data.fundingRounds[].amount / data.fundingRounds[].date` | Round name, amount string, and date in `YYYY-MM-DD` format. Some rounds have an incomplete amount such as `$`. |
| `data.geo.city / data.geo.state / data.geo.country / data.geo.lat / data.geo.lng` | Headquarters location with coordinates. |
| `data.tech[] / data.techCategories[]` | Technologies detected for the company and the categories they fall into. |
| `data.linkedin.handle / data.twitter.handle / data.youtube.handle` | Social profile handles. Handles can be `null` when none is known. |
| `data.foundedYear / data.companyType / data.timeZone` | Year founded, ownership type such as `privately held`, and the company's time zone. |

### Notes

- Pass the bare domain, such as `stripe.com`, in `domain`. The response echoes it in `meta.domain`.
- Many fields can be `null`, for example `data.ticker` and `data.metrics.annualRevenue`. Check for `null` before you use them.
- To find more companies that match a profile, try [Hunter Discover Ai](/apis/hunter/discover-ai).

### Pricing

$0.0049 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/hunter/companies-find.json`](../../../catalog/models/hunter/companies-find.json) · Store page: https://www.sandbase.ai/model/hunter/companies-find
