# Shop Product Details API: pricing, parameters and code examples

`shop-app/product-details` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves full details for a single product including current price, original price (if discounted), images, rating, review count, and merchant info. Requires both product_id and product_slug which are available from get_homepage_featured_products or get_merchant_products results.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/product-details", "product_id": "9144684642526", "product_slug": "sospiro-vibrato-edp"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/product-details', {'product_id': '9144684642526', 'product_slug': 'sospiro-vibrato-edp'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/product-details", {
  "product_id": "9144684642526",
  "product_slug": "sospiro-vibrato-edp"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/product-details", sandbase.Params{
	"product_id": "9144684642526",
	"product_slug": "sospiro-vibrato-edp",
})
```

Same call via the path form: `POST /v1/api/shop-app/product-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `product_id` | string | yes | Numeric product ID from get_homepage_featured_products or get_merchant_products results.  |
| `product_slug` | string | yes | Product URL slug from get_homepage_featured_products or get_merchant_products results.  |

## Details

Retrieves full details for a single product including current price, original price (if discounted), images, rating, review count, and merchant info. Requires both product_id and product_slug which are available from get_homepage_featured_products or get_merchant_products results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/product-details", "product_id": "9144684642526", "product_slug": "sospiro-vibrato-edp"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Numeric product ID from get_homepage_featured_products or get_merchant_products results. |
| `product_slug` | string | Yes | Product URL slug from get_homepage_featured_products or get_merchant_products results. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/product-details.json`](../../../catalog/models/shop-app/product-details.json) · Store page: https://www.sandbase.ai/model/shop-app/product-details
