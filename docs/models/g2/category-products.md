# G2 Category Products API: pricing, parameters and code examples

`g2/category-products` · data API · G2 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

List software products within a given G2 category. Returns products with name, slug, rating, and review count.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "g2/category-products", "category_slug": "crm"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('g2/category-products', {'category_slug': 'crm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("g2/category-products", {
  "category_slug": "crm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "g2/category-products", sandbase.Params{
	"category_slug": "crm",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/g2/category-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination range -9007199254740991–9007199254740991 |
| `category_slug` | string | yes | Category slug from get_categories results (e.g. 'crm', 'project-management')  |

## Details

Returns a list of software products in one G2 category, with each product's name, slug, rating, and review count. It needs a `category_slug` such as `crm`, and an optional `page` number.

### Use cases

- Build a ranked list of the main CRM tools with their ratings and review volumes.
- Compare how many reviews competing products have in one software category.
- Collect product slugs for a category so you can pull details or reviews for each one.
- Track which products appear on each page of a category over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/g2/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "crm", "page": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | Category slug from get_categories results (e.g. 'crm', 'project-management') |
| `page` | integer | No | Page number for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "category": "crm",
    "page": 1,
    "products": [
      {
        "name": "Salesforce Sales Cloud",
        "rating": 4.4,
        "review_count": 27587,
        "slug": "agentforce-sales-formerly-salesforce-sales-cloud"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.category` | The category slug that the request used, for example `crm`. |
| `data.page` | The page number of this result set. |
| `data.products[].name` | Display name of the software product. |
| `data.products[].slug` | G2 slug for the product. Use it as the product input in other G2 APIs. |
| `data.products[].rating` | Average rating of the product on G2, shown as a decimal such as `4.4`. |
| `data.products[].review_count` | Number of reviews the product has on G2. |
| `status` | Shows `success` when the call worked. |

### Notes

- Get valid `category_slug` values from [G2 Categories](/apis/g2/categories).
- Increase `page` to read more products in the same category. The response echoes the current page in `data.page`.
- Pass a product `slug` to [G2 Product Overview](/apis/g2/product-overview) for details or to [G2 Product Reviews](/apis/g2/product-reviews) for individual reviews.

### Pricing

$0.05 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/g2/category-products.json`](../../../catalog/models/g2/category-products.json) · Store page: https://www.sandbase.ai/model/g2/category-products
