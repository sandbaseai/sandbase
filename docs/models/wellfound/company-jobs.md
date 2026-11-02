# Wellfound Company Jobs API: pricing, parameters and code examples

`wellfound/company-jobs` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

List all open job positions at a specific company. Returns job listings with title, compensation, location, and job type.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/company-jobs", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/company-jobs', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/company-jobs", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/company-jobs", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/company-jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company_slug` | string | yes | Company slug (e.g., 'mixpanel', 'juniper-square')  |

## Details

List all open job positions at a specific company. Returns job listings with title, compensation, location, and job type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/company-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | Company slug (e.g., 'mixpanel', 'juniper-square') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wellfound/company-jobs.json`](../../../catalog/models/wellfound/company-jobs.json) · Store page: https://www.sandbase.ai/model/wellfound/company-jobs
