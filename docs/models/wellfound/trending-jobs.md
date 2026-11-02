# Wellfound Trending Jobs API: pricing, parameters and code examples

`wellfound/trending-jobs` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch featured/trending jobs from the Wellfound homepage, organized by category (trending, engineering, product, design, data, sales, marketing, operations, recruiting, finance). Each category contains 3 recently.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/trending-jobs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/trending-jobs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/trending-jobs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/trending-jobs", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/trending-jobs` with the body above minus `model`.

## Details

Fetch featured/trending jobs from the Wellfound homepage, organized by category (trending, engineering, product, design, data, sales, marketing, operations, recruiting, finance). Each category contains 3 recently.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/trending-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wellfound/trending-jobs.json`](../../../catalog/models/wellfound/trending-jobs.json) · Store page: https://www.sandbase.ai/model/wellfound/trending-jobs
