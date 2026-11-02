# GetApp Software Details API: pricing, parameters and code examples

`getapp/software-details` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve full details for a software product including description, ratings, reviews, features, integrations, pricing, screenshots, and alternatives. The slug is the product URL path (e.g.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/software-details", "slug": "collaboration-software/a/monday-com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/software-details', {'slug': 'collaboration-software/a/monday-com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/software-details", {
  "slug": "collaboration-software/a/monday-com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/software-details", sandbase.Params{
	"slug": "collaboration-software/a/monday-com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/software-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com', 'customer-management-software/a/salesforce'). Obtainable from list_software_by_category listings or cta_urls.detail…  |

## Details

Retrieve full details for a software product including description, ratings, reviews, features, integrations, pricing, screenshots, and alternatives. The slug is the product URL path (e.g.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/software-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "collaboration-software/a/monday-com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com', 'customer-management-software/a/salesforce'). Obtainable from list_software_by_category listings … |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/getapp/software-details.json`](../../../catalog/models/getapp/software-details.json) · Store page: https://www.sandbase.ai/model/getapp/software-details
