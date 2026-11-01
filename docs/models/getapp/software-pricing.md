# GetApp Software Pricing

`getapp/software-pricing` · api · GetApp

Retrieve detailed pricing plans for a software product, including plan names, starting prices, and feature lists per plan.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/software-pricing", "slug": "collaboration-software/a/monday-com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/software-pricing', {'slug': 'collaboration-software/a/monday-com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/software-pricing", {
  "slug": "collaboration-software/a/monday-com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/software-pricing", sandbase.Params{
	"slug": "collaboration-software/a/monday-com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/software-pricing` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com').  |

## Details

Retrieve detailed pricing plans for a software product, including plan names, starting prices, and feature lists per plan.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/software-pricing" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "collaboration-software/a/monday-com"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Product URL path segment without leading/trailing slashes (e.g. 'collaboration-software/a/monday-com'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/getapp/software-pricing.json`](../../../catalog/models/getapp/software-pricing.json) · Store page: https://www.sandbase.ai/model/getapp/software-pricing
