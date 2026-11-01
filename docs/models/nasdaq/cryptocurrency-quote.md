# Nasdaq Cryptocurrency Quote

`nasdaq/cryptocurrency-quote` · api · Nasdaq

Real-time cryptocurrency price and daily change. Coverage limited to major coins supported by Nasdaq (confirmed: BTC, ETH).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/cryptocurrency-quote", "symbol": "BTC"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/cryptocurrency-quote', {'symbol': 'BTC'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/cryptocurrency-quote", {
  "symbol": "BTC"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/cryptocurrency-quote", sandbase.Params{
	"symbol": "BTC",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/cryptocurrency-quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Crypto symbol (e.g. BTC, ETH).  |

## Details

Real-time cryptocurrency price and daily change. Coverage limited to major coins supported by Nasdaq (confirmed: BTC, ETH).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/cryptocurrency-quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "BTC"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Crypto symbol (e.g. BTC, ETH). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/cryptocurrency-quote.json`](../../../catalog/models/nasdaq/cryptocurrency-quote.json) · Store page: https://www.sandbase.ai/model/nasdaq/cryptocurrency-quote
