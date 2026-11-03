# Zillow Open Houses API: pricing, parameters and code examples

`zillow/open-houses` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Retrieve the scheduled open houses for a property listing by its Zillow property ID (zpid), together with the property's address for confirmation. Returns one record per property with an openHouses array (each entry.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/open-houses", "zpid": "29505949"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/open-houses', {'zpid': '29505949'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/open-houses", {
  "zpid": "29505949"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/open-houses", sandbase.Params{
	"zpid": "29505949",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/open-houses` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `zpid` | string | yes | Zillow property ID (numeric string, e.g., '29505949')  |

## Details

Returns the scheduled open houses for one Zillow property listing. It needs the Zillow property ID (`zpid`) and also returns the property address, listing status, and listing agent fields.

### Use cases

- Check whether a listing has any open houses scheduled before planning a visit.
- Confirm the street address and ZIP code behind a `zpid` before using it in other calls.
- Build a weekend open house list by checking open houses across many saved listings.
- Filter out listings that are no longer `FOR_SALE` before showing them to buyers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/open-houses" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"zpid": "29505949"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `zpid` | string | Yes | Zillow property ID (numeric string, e.g., '29505949') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "address": {
      "city": "Austin",
      "state": "TX",
      "streetAddress": "8536 Birmingham Dr",
      "zipcode": "78748"
    },
    "attendanceInstructions": null,
    "homeStatus": "FOR_SALE",
    "listingAgent": {
      "agentName": null,
      "agentPhoneNumber": null,
      "brokerName": null,
      "brokerPhoneNumber": null
    },
    "openHouseCount": 0,
    "openHouses": [],
    "timeZone": "America/Chicago",
    "zpid": 29505949
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.openHouseCount` | Number of open houses scheduled for the property. It is `0` when none are listed. |
| `data.openHouses[]` | List of scheduled open house entries. The list is empty when `openHouseCount` is `0`. |
| `data.address.streetAddress / data.address.city / data.address.state / data.address.zipcode` | Street address, city, state, and ZIP code of the property. Use them to confirm you have the right listing. |
| `data.homeStatus` | Listing status of the property, for example `FOR_SALE`. |
| `data.timeZone` | Time zone name for the property, for example `America/Chicago`. |
| `data.listingAgent.agentName / data.listingAgent.agentPhoneNumber` | Name and phone number of the listing agent. Both can be `null`. |
| `data.listingAgent.brokerName / data.listingAgent.brokerPhoneNumber` | Name and phone number of the listing broker. Both can be `null`. |
| `data.attendanceInstructions` | Instructions for attending an open house. It is `null` when none are given. |
| `data.zpid` | Zillow property ID of the listing, returned as a number. |

### Notes

- Send `zpid` as a numeric string, for example `"29505949"`. The response returns it as a number.
- An empty `openHouses` array with `openHouseCount` of `0` is a valid result for a listing with no scheduled open houses.
- Call [Zillow Property Details](/apis/zillow/property-details) with the same `zpid` for more information about the property.

### Pricing

$0.03 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/open-houses.json`](../../../catalog/models/zillow/open-houses.json) · Store page: https://www.sandbase.ai/model/zillow/open-houses
