# Nasdaq Stock Financials

`nasdaq/stock-financials` · api · Nasdaq

Financial statements for a stock: Income Statement, Balance Sheet, Cash Flow, and Financial Ratios. Returns 4 periods of data (annual or quarterly based on frequency parameter).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-financials", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-financials', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-financials", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-financials", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-financials` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |
| `frequency` | integer |  | 1 for annual, 2 for quarterly. range -9007199254740991–9007199254740991 |

## Details

Financial statements for a stock: Income Statement, Balance Sheet, Cash Flow, and Financial Ratios. Returns 4 periods of data (annual or quarterly based on frequency parameter).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-financials" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock symbol (e.g. AAPL). |
| `frequency` | integer | No | 1 for annual, 2 for quarterly. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/stock-financials.json`](../../../catalog/models/nasdaq/stock-financials.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-financials
