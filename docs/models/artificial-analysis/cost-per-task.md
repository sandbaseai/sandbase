# Artificial Analysis Cost Per Task API: pricing, parameters and code examples

`artificial-analysis/cost-per-task` · data API · Artificial Analysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Get per-model cost-per-task data from the Artificial Analysis homepage. Returns Intelligence Index score, cost per task (USD) with granular cost breakdown, time per task, end-to-end response time, TTFT, token counts.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/cost-per-task"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('artificial-analysis/cost-per-task', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("artificial-analysis/cost-per-task", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "artificial-analysis/cost-per-task", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/artificial-analysis/cost-per-task` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `models` | string |  | Comma-separated list of model slugs to filter results (e.g. 'claude-sonnet-5,gpt-5-6-sol,gemini-3-5-flash-lite'). When omitted, returns the default set of models shown on the homepage.  |

## Details

Get per-model cost-per-task data from the Artificial Analysis homepage. Returns Intelligence Index score, cost per task (USD) with granular cost breakdown, time per task, end-to-end response time, TTFT, token counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/artificial-analysis/cost-per-task" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `models` | string | No | Comma-separated list of model slugs to filter results (e.g. 'claude-sonnet-5,gpt-5-6-sol,gemini-3-5-flash-lite'). When omitted, returns the default set of models shown on the homepage. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/artificial-analysis/cost-per-task.json`](../../../catalog/models/artificial-analysis/cost-per-task.json) · Store page: https://www.sandbase.ai/model/artificial-analysis/cost-per-task
