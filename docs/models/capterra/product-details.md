# Capterra Product Details API: pricing, parameters and code examples

`capterra/product-details` · data API · Capterra · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

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

This API returns details for one software product listed on Capterra: its name, description, overall rating, review count, and page URL. It needs the numeric `product_id` and the URL slug `product_name`.

### Use cases

- Show the current Capterra rating and review count for a CRM product on a comparison page.
- Track how the `rating` and `review_count` of a product change between your own checks.
- Pull the description and Capterra URL of a product to enrich a company or vendor record.
- Compare several products from one category by calling this API once for each product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/product-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "155928", "product_name": "Zoho-CRM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | The numeric product ID (e.g. '155928'). Available from get_category_products or search_software results. |
| `product_name` | string | Yes | The URL slug of the product (e.g. 'Zoho-CRM', 'HubSpot-CRM'). Available from get_category_products or search_software results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "description": "Zoho CRM empowers businesses of all sizes with a 360º customer relationship life…",
    "features": [],
    "id": "155928",
    "name": "Zoho CRM",
    "rating": "4.3",
    "review_count": "6983",
    "url": "https://www.capterra.com/p/155928/Zoho-CRM/"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Display name of the product, for example `Zoho CRM`. |
| `data.id` | Numeric Capterra product ID, returned as a string. It matches the `product_id` you sent. |
| `data.description` | Text description of the product from its Capterra listing. Long descriptions may be cut off. |
| `data.rating` | Overall rating of the product, returned as a string such as `4.3`. |
| `data.review_count` | Number of reviews for the product, returned as a string. |
| `data.url` | Link to the product page on Capterra. It contains the ID and the slug. |
| `data.features` | List of product features. It can be an empty list, as in this example. |
| `status` | Shows `success` when the request worked. |

### Notes

- Get `product_id` and `product_name` from [Capterra Search Software](/apis/capterra/search-software) or [Capterra Category Products](/apis/capterra/category-products).
- The slug in `product_name` is the last part of the product URL, for example `Zoho-CRM` in `https://www.capterra.com/p/155928/Zoho-CRM/`.
- `rating` and `review_count` are strings, so convert them to numbers before you sort or calculate.
- To read individual reviews, call [Capterra Product Reviews](/apis/capterra/product-reviews).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/capterra/product-details.json`](../../../catalog/models/capterra/product-details.json) · Store page: https://www.sandbase.ai/model/capterra/product-details
