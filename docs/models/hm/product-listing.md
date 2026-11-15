# H&M Product Listing API: pricing, parameters and code examples

`hm/product-listing` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch paginated product listings for a specific category path. Returns product hits with pricing, images, swatches, sizes, and pagination metadata. Each page returns up to 36 products.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/product-listing", "category": "men/products/view-all"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/product-listing', {'category': 'men/products/view-all'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/product-listing", {
  "category": "men/products/view-all"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/product-listing", sandbase.Params{
	"category": "men/products/view-all",
})
```

Same call via the path form: `POST /v1/api/hm/product-listing` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). default `1` |
| `sort` | string |  | Sort order for results.  |
| `category` | string | yes | Category path (e.g. 'men/products/view-all', 'women/products/view-all', 'kids/girls/products/view-all').  |

## Details

Fetch paginated product listings for a specific category path. Returns product hits with pricing, images, swatches, sizes, and pagination metadata. Each page returns up to 36 products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/product-listing", "page": 1, "sort": "", "category": "men/products/view-all"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Category path (e.g. 'men/products/view-all', 'women/products/view-all', 'kids/girls/products/view-all'). |
| `page` | integer | No | Page number for pagination (1-based). |
| `sort` | string | No | Sort order for results. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/product-listing.json`](../../../catalog/models/hm/product-listing.json) · Store page: https://www.sandbase.ai/model/hm/product-listing
