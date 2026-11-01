# Capterra Product Details

`capterra/product-details` · api · Capterra

Retrieve detailed information about a specific software product, including description, overall rating, review count, and feature list. Requires both product_id and product_name (slug) which are available from.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/product-details", "product_id": "155928", "product_name": "Zoho-CRM"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/product-details', {'product_id': '155928', 'product_name': 'Zoho-CRM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/product-details", {
  "product_id": "155928",
  "product_name": "Zoho-CRM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/product-details", sandbase.Params{
	"product_id": "155928",
	"product_name": "Zoho-CRM",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/capterra/product-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `product_id` | string | yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results.  |
| `product_name` | string | yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results.  |

## Details

Retrieve detailed information about a specific software product, including description, overall rating, review count, and feature list. Requires both product_id and product_name (slug) which are available from.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/product-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "155928", "product_name": "Zoho-CRM"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results. |
| `product_name` | string | Yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/capterra/product-details.json`](../../../catalog/models/capterra/product-details.json) · Store page: https://www.sandbase.ai/model/capterra/product-details
