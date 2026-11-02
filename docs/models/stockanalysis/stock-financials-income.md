# StockAnalysis Stock Financials Income API: pricing, parameters and code examples

`stockanalysis/stock-financials-income` · data API · StockAnalysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Detailed income statement for a stock. Returns annual financial data including revenue, gross profit, operating income, net income, EPS, margins, and growth rates organized in a financialData object with arrays per.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/stock-financials-income", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stockanalysis/stock-financials-income', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stockanalysis/stock-financials-income", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stockanalysis/stock-financials-income", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/stockanalysis/stock-financials-income` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock ticker symbol (e.g. 'AAPL', 'MSFT', 'NVDA').  |

## Details

Detailed income statement for a stock. Returns annual financial data including revenue, gross profit, operating income, net income, EPS, margins, and growth rates organized in a financialData object with arrays per.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/stockanalysis/stock-financials-income" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g. 'AAPL', 'MSFT', 'NVDA'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/stockanalysis/stock-financials-income.json`](../../../catalog/models/stockanalysis/stock-financials-income.json) · Store page: https://www.sandbase.ai/model/stockanalysis/stock-financials-income
