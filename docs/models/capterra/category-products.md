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

Retrieve products listed within a specific software category. Returns product names, numeric IDs, URL slugs, and full URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/capterra/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "accounting"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | The slug of the category from get_software_categories (e.g. 'accounting', 'project-management', 'human-resource'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/capterra/category-products.json`](../../../catalog/models/capterra/category-products.json) · Store page: https://www.sandbase.ai/model/capterra/category-products
