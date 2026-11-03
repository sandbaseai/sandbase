# Zillow Zestimate API: pricing, parameters and code examples

`zillow/zestimate` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Get the Zestimate (automated home value estimate) and rent Zestimate for a property by zpid.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/zestimate", "zpid": "2080998636"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/zestimate', {'zpid': '2080998636'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/zestimate", {
  "zpid": "2080998636"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/zestimate", sandbase.Params{
	"zpid": "2080998636",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/zestimate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `zpid` | string | yes | Zillow property ID (numeric string, e.g., '2080998636')  |

## Details

Returns the Zillow Zestimate (automated home value estimate) and rent Zestimate for one property, plus its address and home type. It needs a Zillow property ID (`zpid`) as input.

### Use cases

- Check the current estimated value of a single home by its `zpid`.
- Compare `zestimate` with `rentZestimate` to get a rough view of rent against price for one property.
- Read the low and high percent range around a Zestimate to see how wide the estimate band is.
- Confirm the address and home type that belong to a `zpid` before you run other lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/zestimate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"zpid": "2080998636"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `zpid` | string | Yes | Zillow property ID (numeric string, e.g., '2080998636') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "address": {
      "city": "Prescott Valley",
      "neighborhood": null,
      "state": "AZ",
      "streetAddress": "0 E 2nd St",
      "zipcode": "86314"
    },
    "homeType": "LOT",
    "rentZestimate": null,
    "zestimate": null,
    "zestimateHighPercent": null,
    "zestimateLowPercent": null,
    "zpid": 2080998636
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.zpid` | Zillow property ID of the property, returned as a number. |
| `data.zestimate` | Automated home value estimate. It is `null` when Zillow has no estimate for the property, as in the sample response for a lot. |
| `data.rentZestimate` | Automated monthly rent estimate. It is `null` when none exists for the property. |
| `data.zestimateHighPercent / data.zestimateLowPercent` | High and low percent values for the Zestimate range. Both are `null` when there is no `zestimate`. |
| `data.homeType` | Type of property, for example `LOT`. |
| `data.address.streetAddress` | Street address of the property. |
| `data.address.city / data.address.state / data.address.zipcode` | City, state and ZIP code of the property. |
| `data.address.neighborhood` | Neighborhood name. It can be `null`. |

### Notes

- Valuation fields can be `null`, especially for vacant lots, so check for `null` before you use them.
- `zpid` is a numeric string in the request and a number in `data.zpid`.
- Call [Zillow Property Details](/apis/zillow/property-details) with the same `zpid` for fuller details on the property.

### Pricing

$0.03 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/zestimate.json`](../../../catalog/models/zillow/zestimate.json) · Store page: https://www.sandbase.ai/model/zillow/zestimate
