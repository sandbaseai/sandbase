# Clutch Company Locations API: pricing, parameters and code examples

`clutch/company-locations` · data API · Clutch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get office locations for a company including addresses, phone numbers, and employee counts per location.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-locations", "slug": "simform"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/company-locations', {'slug': 'simform'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/company-locations", {
  "slug": "simform"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/company-locations", sandbase.Params{
	"slug": "simform",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/company-locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Company profile slug from search_companies results.  |

## Details

Returns the office locations for a company listed on Clutch. Each location includes a name, street address, postal code, phone number, and an employee count range. The only input is the company `slug`.

### Use cases

- List every office a vendor runs to check if it has a presence in a target city or country.
- Build a lead list with office addresses and phone numbers for outreach to agencies.
- Compare how a company spreads its staff across headquarters and branch offices.
- Enrich a company record in a CRM with its office postal addresses.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/company-locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "simform"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company profile slug from search_companies results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "locations": [
      {
        "city": "Orlando",
        "country": "United States",
        "employees": "10 - 15",
        "name": "Headquarters",
        "phone": "3212372727",
        "postal_code": "32801",
        "state": "FL",
        "street": "111 North Orange Avenue Suite 800"
      }
    ],
    "slug": "simform"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.slug` | The company profile slug that was requested. |
| `data.locations[].name` | Label for the office, such as `Headquarters` or a city and state like `Los Angeles, CA`. |
| `data.locations[].street` | Street address of the office, including suite number when present. |
| `data.locations[].city / data.locations[].state` | City and state of the office. Both can be `null`, so fall back to `name` for the place. |
| `data.locations[].postal_code` | Postal code of the office. |
| `data.locations[].country` | Country of the office. |
| `data.locations[].phone` | Phone number as digits only. It can be an empty string when the office has no listed phone. |
| `data.locations[].employees` | Employee count for the office, given as a range string such as `10 - 15`. |

### Notes

- Get the `slug` from the results of [Clutch Search Companies](/apis/clutch/search-companies).
- The `employees` value is a text range, not a number, so parse it before you do math.
- For company details beyond offices, call [Clutch Company Profile](/apis/clutch/company-profile).
- The call runs asynchronously: read the result from `outputs[0].data` after the task completes.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/clutch/company-locations.json`](../../../catalog/models/clutch/company-locations.json) · Store page: https://www.sandbase.ai/model/clutch/company-locations
