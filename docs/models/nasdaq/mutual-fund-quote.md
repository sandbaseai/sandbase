# Nasdaq Mutual Fund Quote

`nasdaq/mutual-fund-quote` · api · Nasdaq

Quote and details for a mutual fund including NAV and daily change. Mutual funds show isRealTime=false and have no bid/ask/volume data.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/mutual-fund-quote", "symbol": "VFIAX"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/mutual-fund-quote', {'symbol': 'VFIAX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/mutual-fund-quote", {
  "symbol": "VFIAX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/mutual-fund-quote", sandbase.Params{
	"symbol": "VFIAX",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/mutual-fund-quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Mutual fund symbol (e.g. VFIAX).  |

## Details

Quote and details for a mutual fund including NAV and daily change. Mutual funds show isRealTime=false and have no bid/ask/volume data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/mutual-fund-quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "VFIAX"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Mutual fund symbol (e.g. VFIAX). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/mutual-fund-quote.json`](../../../catalog/models/nasdaq/mutual-fund-quote.json) · Store page: https://www.sandbase.ai/model/nasdaq/mutual-fund-quote
