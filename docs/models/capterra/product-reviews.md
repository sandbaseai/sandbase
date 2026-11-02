# Capterra Product Reviews API: pricing, parameters and code examples

`capterra/product-reviews` · data API · Capterra · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve user reviews for a software product. Returns paginated reviews with title, date, overall rating, pros, and cons text (up to 25 reviews per page).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/product-reviews", "product_id": "155928", "product_name": "Zoho-CRM"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/product-reviews', {'product_id': '155928', 'product_name': 'Zoho-CRM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/product-reviews", {
  "product_id": "155928",
  "product_name": "Zoho-CRM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/product-reviews", sandbase.Params{
	"product_id": "155928",
	"product_name": "Zoho-CRM",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/capterra/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number of reviews to retrieve. range -9007199254740991–9007199254740991 |
| `product_id` | string | yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results.  |
| `product_name` | string | yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results.  |

## Details

Retrieve user reviews for a software product. Returns paginated reviews with title, date, overall rating, pros, and cons text (up to 25 reviews per page).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "155928", "product_name": "Zoho-CRM", "page": 1}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results. |
| `product_name` | string | Yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results. |
| `page` | integer | No | Page number of reviews to retrieve. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/capterra/product-reviews.json`](../../../catalog/models/capterra/product-reviews.json) · Store page: https://www.sandbase.ai/model/capterra/product-reviews
