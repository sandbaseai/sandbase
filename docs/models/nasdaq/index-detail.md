# Nasdaq Index Detail

`nasdaq/index-detail` · api · Nasdaq

Detailed quote data for a specific market index including price, net change, percentage change, volume, and daily high/low.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/index-detail"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/index-detail', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/index-detail", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/index-detail", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/index-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string |  | Index symbol (e.g. COMP, NDX, NBI).  |

## Details

Detailed quote data for a specific market index including price, net change, percentage change, volume, and daily high/low.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/index-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | No | Index symbol (e.g. COMP, NDX, NBI). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/index-detail.json`](../../../catalog/models/nasdaq/index-detail.json) · Store page: https://www.sandbase.ai/model/nasdaq/index-detail
