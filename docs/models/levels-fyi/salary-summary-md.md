# Levels.fyi Salary Summary Md

`levels-fyi/salary-summary-md` · api · Levels.fyi

Retrieve an aggregate salary summary in Markdown format for a given company and optional job family. Includes median compensation, level breakdowns by job family, and attribution information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/salary-summary-md", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('levels-fyi/salary-summary-md', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("levels-fyi/salary-summary-md", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "levels-fyi/salary-summary-md", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/levels-fyi/salary-summary-md` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company_slug` | string | yes | Company slug identifier (e.g. 'google', 'meta', 'amazon'). Obtain from get_popular_companies.  |
| `job_family_slug` | string |  | Job family slug (e.g. 'software-engineer', 'product-manager', 'data-scientist'). Omitting returns an overall company salary summary across all roles.  |

## Details

Retrieve an aggregate salary summary in Markdown format for a given company and optional job family. Includes median compensation, level breakdowns by job family, and attribution information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/levels-fyi/salary-summary-md" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | Company slug identifier (e.g. 'google', 'meta', 'amazon'). Obtain from get_popular_companies. |
| `job_family_slug` | string | No | Job family slug (e.g. 'software-engineer', 'product-manager', 'data-scientist'). Omitting returns an overall company salary summary across all roles. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/levels-fyi/salary-summary-md.json`](../../../catalog/models/levels-fyi/salary-summary-md.json) · Store page: https://www.sandbase.ai/model/levels-fyi/salary-summary-md
