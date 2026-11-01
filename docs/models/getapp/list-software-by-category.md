# GetApp List Software By Category

`getapp/list-software-by-category` · api · GetApp

List software products in a specific category with pagination. Returns listings with ratings, reviews, pricing info, and facets for filtering.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/list-software-by-category", "category_slug": "customer-management-software/crm"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/list-software-by-category', {'category_slug': 'customer-management-software/crm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/list-software-by-category", {
  "category_slug": "customer-management-software/crm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/list-software-by-category", sandbase.Params{
	"category_slug": "customer-management-software/crm",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/list-software-by-category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). range -9007199254740991–9007199254740991 |
| `category_slug` | string | yes | Category URL path segment from list_categories cta_urls.detail, without leading/trailing slashes (e.g. 'customer-management-software/crm', 'collaboration-software/project-management').  |

## Details

List software products in a specific category with pagination. Returns listings with ratings, reviews, pricing info, and facets for filtering.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/list-software-by-category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "customer-management-software/crm", "page": 1}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | Category URL path segment from list_categories cta_urls.detail, without leading/trailing slashes (e.g. 'customer-management-software/crm', 'collaboration-software/project-management'). |
| `page` | integer | No | Page number for pagination (1-based). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/getapp/list-software-by-category.json`](../../../catalog/models/getapp/list-software-by-category.json) · Store page: https://www.sandbase.ai/model/getapp/list-software-by-category
