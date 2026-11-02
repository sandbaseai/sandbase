# Nasdaq Stock Institutional Holdings API: pricing, parameters and code examples

`nasdaq/stock-institutional-holdings` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Institutional holdings data for a stock: ownership summary, active/new/sold-out position counts, and individual holder transactions sorted by market value.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-institutional-holdings", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-institutional-holdings', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-institutional-holdings", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-institutional-holdings", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-institutional-holdings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Holdings type filter: TOTAL, INCREASED, DECREASED, NEW, SOLD_OUT.  |
| `limit` | integer |  | Max records to return in holdingsTransactions. range -9007199254740991–9007199254740991 |
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |

## Details

Institutional holdings data for a stock: ownership summary, active/new/sold-out position counts, and individual holder transactions sorted by market value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-institutional-holdings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock symbol (e.g. AAPL). |
| `limit` | integer | No | Max records to return in holdingsTransactions. |
| `type` | string | No | Holdings type filter: TOTAL, INCREASED, DECREASED, NEW, SOLD_OUT. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/stock-institutional-holdings.json`](../../../catalog/models/nasdaq/stock-institutional-holdings.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-institutional-holdings
