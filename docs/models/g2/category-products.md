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

List software products within a given G2 category. Returns products with name, slug, rating, and review count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/g2/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "crm", "page": 1}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | Category slug from get_categories results (e.g. 'crm', 'project-management') |
| `page` | integer | No | Page number for pagination |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/g2/category-products.json`](../../../catalog/models/g2/category-products.json) · Store page: https://www.sandbase.ai/model/g2/category-products
