# Nasdaq Retail Trading Activity

`nasdaq/retail-trading-activity` · api · Nasdaq

Retail Trading Activity Tracker (RTAT) showing the top 5 stocks by percent of retail equity flow, with activity percentage change and buy/sell sentiment.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/retail-trading-activity"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/retail-trading-activity', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/retail-trading-activity", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/retail-trading-activity", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/retail-trading-activity` with the body above minus `model`.

## Details

Retail Trading Activity Tracker (RTAT) showing the top 5 stocks by percent of retail equity flow, with activity percentage change and buy/sell sentiment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/retail-trading-activity" \
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
Machine-readable: [`catalog/models/nasdaq/retail-trading-activity.json`](../../../catalog/models/nasdaq/retail-trading-activity.json) · Store page: https://www.sandbase.ai/model/nasdaq/retail-trading-activity
