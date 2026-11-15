# Zoopla Search Properties For Sale API: pricing, parameters and code examples

`zoopla/search-properties-for-sale` · data API · Zoopla · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Search properties for sale in a specific UK location.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zoopla/search-properties-for-sale", "location": "london"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zoopla/search-properties-for-sale', {'location': 'london'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zoopla/search-properties-for-sale", {
  "location": "london"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zoopla/search-properties-for-sale", sandbase.Params{
	"location": "london",
})
```

Same call via the path form: `POST /v1/api/zoopla/search-properties-for-sale` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `radius` | integer |  | Search radius in miles.  |
| `location` | string | yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester', 'se1', 'oxford').  |
| `max_beds` | integer |  | Maximum number of bedrooms.  |
| `min_beds` | integer |  | Minimum number of bedrooms.  |
| `max_price` | integer |  | Maximum price in GBP.  |
| `min_price` | integer |  | Minimum price in GBP.  |
| `property_type` | string |  | Property type slug.  |

## Details

Search properties for sale in a specific UK location.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zoopla/search-properties-for-sale", "page": 1, "radius": 5, "location": "london", "max_beds": 4, "min_beds": 1, "max_price": 500000, "min_price": 100000, "property_type": "detached"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location` | string | Yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester', 'se1', 'oxford'). |
| `max_beds` | integer | No | Maximum number of bedrooms. |
| `max_price` | integer | No | Maximum price in GBP. |
| `min_beds` | integer | No | Minimum number of bedrooms. |
| `min_price` | integer | No | Minimum price in GBP. |
| `page` | integer | No | Page number for pagination. |
| `property_type` | string | No | Property type slug. |
| `radius` | integer | No | Search radius in miles. |

### Pricing

Flat $0.09 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zoopla/search-properties-for-sale.json`](../../../catalog/models/zoopla/search-properties-for-sale.json) · Store page: https://www.sandbase.ai/model/zoopla/search-properties-for-sale
