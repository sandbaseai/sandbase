# Artificial Analysis Llm Providers Leaderboard

`artificial-analysis/llm-providers-leaderboard` · api · Artificial Analysis

Get the main LLM API Providers Leaderboard data, including all model endpoints and their performance metrics (speed, latency, price, etc.). Returns a large dataset of provider-model combinations with pricing,.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/llm-providers-leaderboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('artificial-analysis/llm-providers-leaderboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("artificial-analysis/llm-providers-leaderboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "artificial-analysis/llm-providers-leaderboard", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/artificial-analysis/llm-providers-leaderboard` with the body above minus `model`.

## Details

Get the main LLM API Providers Leaderboard data, including all model endpoints and their performance metrics (speed, latency, price, etc.). Returns a large dataset of provider-model combinations with pricing,.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/artificial-analysis/llm-providers-leaderboard" \
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
Machine-readable: [`catalog/models/artificial-analysis/llm-providers-leaderboard.json`](../../../catalog/models/artificial-analysis/llm-providers-leaderboard.json) · Store page: https://www.sandbase.ai/model/artificial-analysis/llm-providers-leaderboard
