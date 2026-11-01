# Home Depot Product

`home-depot/product` · api · Home Depot

Get a Home Depot product by product ID: title, brand, model number, UPC, price, specifications, images, fulfillment and ratings, localized by store or ZIP.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "home-depot/product", "product_id": "310009453"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('home-depot/product', {'product_id': '310009453'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("home-depot/product", {
  "product_id": "310009453"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "home-depot/product", sandbase.Params{
	"product_id": "310009453",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/home-depot/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `store_id` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only.  |
| `product_id` | string \\| number \\| boolean | yes | The Home Depot identifier of a product. Only Product IDs gathered from the Home Depot US are supported.  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Home Depot product by product ID: title, brand, model number, UPC, price, specifications, images, fulfillment and ratings, localized by store or ZIP.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/home-depot/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "310009453"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string/number/boolean | Yes | The Home Depot identifier of a product. Only Product IDs gathered from the Home Depot US are supported. |
| `delivery_zip` | string/number/boolean | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `json_restrictor` | string/number/boolean | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `store_id` | string/number/boolean | No | Store ID to filter the products by the specific store only. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/home-depot/product.json`](../../../catalog/models/home-depot/product.json) · Store page: https://www.sandbase.ai/model/home-depot/product
