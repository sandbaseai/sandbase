# Zoopla Search Sold House Prices API: pricing, parameters and code examples

`zoopla/search-sold-house-prices` · data API · Zoopla · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Search sold house prices in a specific area. Returns paginated results with property sale history including last sale price and date, full address, and property attributes (bedrooms, bathrooms, floor area, tenure). Uses cursor-based pagination internally but exposes page numbers.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zoopla/search-sold-house-prices", "location": "london"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zoopla/search-sold-house-prices', {'location': 'london'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zoopla/search-sold-house-prices", {
  "location": "london"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zoopla/search-sold-house-prices", sandbase.Params{
	"location": "london",
})
```

Same call via the path form: `POST /v1/api/zoopla/search-sold-house-prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `location` | string | yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester', 'se1').  |
| `max_beds` | integer |  | Maximum number of bedrooms.  |
| `min_beds` | integer |  | Minimum number of bedrooms.  |
| `max_baths` | integer |  | Maximum number of bathrooms.  |
| `min_baths` | integer |  | Minimum number of bathrooms.  |
| `property_type` | string |  | Property type code for sold prices.  |

## Details

Search sold house prices in a specific area. Returns paginated results with property sale history including last sale price and date, full address, and property attributes (bedrooms, bathrooms, floor area, tenure). Uses cursor-based pagination internally but exposes page numbers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zoopla/search-sold-house-prices", "page": 1, "location": "london", "max_beds": 4, "min_beds": 1, "max_baths": 3, "min_baths": 1, "property_type": "detached"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location` | string | Yes | Location slug matching Zoopla URL structure (e.g., 'london', 'manchester', 'se1'). |
| `max_baths` | integer | No | Maximum number of bathrooms. |
| `max_beds` | integer | No | Maximum number of bedrooms. |
| `min_baths` | integer | No | Minimum number of bathrooms. |
| `min_beds` | integer | No | Minimum number of bedrooms. |
| `page` | integer | No | Page number for pagination. |
| `property_type` | string | No | Property type code for sold prices. |

### Pricing

Flat $0.06 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zoopla/search-sold-house-prices.json`](../../../catalog/models/zoopla/search-sold-house-prices.json) · Store page: https://www.sandbase.ai/model/zoopla/search-sold-house-prices
