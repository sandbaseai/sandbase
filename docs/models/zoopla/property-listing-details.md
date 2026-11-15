# Zoopla Property Listing Details API: pricing, parameters and code examples

`zoopla/property-listing-details` · data API · Zoopla · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Get full details of a specific property listing by its Zoopla listing ID. Tries for-sale first, then to-rent if not found. Returns property metadata including address, type, room counts, agent details, location coordinates, and utility information.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zoopla/property-listing-details", "listing_id": "67501148"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zoopla/property-listing-details', {'listing_id': '67501148'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zoopla/property-listing-details", {
  "listing_id": "67501148"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zoopla/property-listing-details", sandbase.Params{
	"listing_id": "67501148",
})
```

Same call via the path form: `POST /v1/api/zoopla/property-listing-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `listing_id` | string | yes | Zoopla listing ID (numeric string, e.g., '73036018'). Obtainable from search_properties_for_sale or search_properties_to_rent results.  |

## Details

Get full details of a specific property listing by its Zoopla listing ID. Tries for-sale first, then to-rent if not found. Returns property metadata including address, type, room counts, agent details, location coordinates, and utility information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zoopla/property-listing-details", "listing_id": "67501148"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `listing_id` | string | Yes | Zoopla listing ID (numeric string, e.g., '73036018'). Obtainable from search_properties_for_sale or search_properties_to_rent results. |

### Pricing

Flat $0.09 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zoopla/property-listing-details.json`](../../../catalog/models/zoopla/property-listing-details.json) · Store page: https://www.sandbase.ai/model/zoopla/property-listing-details
