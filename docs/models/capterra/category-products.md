# Capterra Category Products API: pricing, parameters and code examples

`capterra/category-products` · data API · Capterra · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve products listed within a specific software category. Returns product names, numeric IDs, URL slugs, and full URLs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/category-products", "category_slug": "accounting"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/category-products', {'category_slug': 'accounting'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/category-products", {
  "category_slug": "accounting"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/category-products", sandbase.Params{
	"category_slug": "accounting",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/capterra/category-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category_slug` | string | yes | The slug of the category from get_software_categories (e.g. 'accounting', 'project-management', 'human-resource').  |

## Details

Returns the list of software products that Capterra lists under one software category. You send a `category_slug` such as `accounting`, and each product comes back with its ID, name, slug, and Capterra URL.

### Use cases

- Build a list of every accounting or project management tool that Capterra lists in a category.
- Collect product IDs for a category to look up details or reviews for each product.
- Track which vendors appear in a category by comparing product names across categories.
- Feed Capterra product URLs into a research sheet or CRM list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "accounting"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | The slug of the category from get_software_categories (e.g. 'accounting', 'project-management', 'human-resource'). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "products": [
      {
        "id": "76",
        "name": "Sage Intacct",
        "slug": "Intacct",
        "url": "https://www.capterra.com/p/76/Intacct/"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.products[]` | List of products in the category. |
| `data.products[].id` | Numeric product ID on Capterra, returned as a string (for example `76`). It also appears in the product URL. |
| `data.products[].name` | Display name of the product, for example `Xero`. |
| `data.products[].slug` | URL slug of the product, for example `Intacct`. It is the last part of the product URL. |
| `data.products[].url` | Full Capterra page URL for the product. It has the form `https://www.capterra.com/p/{id}/{slug}/`. |
| `status` | Shows `success` when the call worked. |

### Notes

- Get valid `category_slug` values from the software categories API on SandBase. Examples are `accounting`, `project-management` and `human-resource`.
- The response shows no pagination parameters. The request takes only `category_slug`.
- Use the `id` and `slug` values with [Capterra Product Details](/apis/capterra/product-details) or [Capterra Product Reviews](/apis/capterra/product-reviews) to get more about a product.
- This API runs asynchronously. Poll the run endpoint and read the result from `outputs[0].data`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/capterra/category-products.json`](../../../catalog/models/capterra/category-products.json) · Store page: https://www.sandbase.ai/model/capterra/category-products
