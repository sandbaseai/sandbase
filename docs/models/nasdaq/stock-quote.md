# Nasdaq Stock Quote API: pricing, parameters and code examples

`nasdaq/stock-quote` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Real-time quote for a single equity including last sale price, net change, percentage change, bid/ask, volume, 52-week range, and market status. Response shape varies by asset class (stocks show keyStats; ETFs and.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-quote", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-quote', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-quote", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-quote", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |
| `asset_class` | string |  | Asset class: stocks, etf, mutualfunds, crypto.  |

## Details

Real-time quote for a single equity including last sale price, net change, percentage change, bid/ask, volume, 52-week range, and market status. Response shape varies by asset class (stocks show keyStats; ETFs and.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock symbol (e.g. AAPL). |
| `asset_class` | string | No | Asset class: stocks, etf, mutualfunds, crypto. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/stock-quote.json`](../../../catalog/models/nasdaq/stock-quote.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-quote
