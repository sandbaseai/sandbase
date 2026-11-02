# GetApp Category Leaders API: pricing, parameters and code examples

`getapp/category-leaders` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve the category page data including top-ranked software products, buyers guide content, facets, and pagination for a given category.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/category-leaders", "category_slug": "customer-management-software/crm"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/category-leaders', {'category_slug': 'customer-management-software/crm'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/category-leaders", {
  "category_slug": "customer-management-software/crm"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/category-leaders", sandbase.Params{
	"category_slug": "customer-management-software/crm",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/category-leaders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category_slug` | string | yes | Category URL path segment without leading/trailing slashes (e.g. 'customer-management-software/crm'). Same format as list_software_by_category.  |

## Details

Retrieve the category page data including top-ranked software products, buyers guide content, facets, and pagination for a given category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/category-leaders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_slug": "customer-management-software/crm"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_slug` | string | Yes | Category URL path segment without leading/trailing slashes (e.g. 'customer-management-software/crm'). Same format as list_software_by_category. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/getapp/category-leaders.json`](../../../catalog/models/getapp/category-leaders.json) · Store page: https://www.sandbase.ai/model/getapp/category-leaders
