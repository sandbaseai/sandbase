# Nasdaq Stock Historical Quotes API: pricing, parameters and code examples

`nasdaq/stock-historical-quotes` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Historical OHLCV price data for a symbol. Without explicit date range, defaults to one year ending today.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/stock-historical-quotes", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/stock-historical-quotes', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/stock-historical-quotes", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/stock-historical-quotes", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/stock-historical-quotes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of records to return. range -9007199254740991–9007199254740991 |
| `symbol` | string | yes | Stock symbol (e.g. AAPL).  |
| `to_date` | string |  | End date in YYYY-MM-DD format. Omitting defaults to today.  |
| `from_date` | string |  | Start date in YYYY-MM-DD format. Omitting defaults to one year ago.  |
| `asset_class` | string |  | Asset class: stocks, etf, mutualfunds, crypto.  |

## Details

Historical OHLCV price data for a symbol. Without explicit date range, defaults to one year ending today.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/stock-historical-quotes" \
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
| `from_date` | string | No | Start date in YYYY-MM-DD format. Omitting defaults to one year ago. |
| `limit` | integer | No | Number of records to return. |
| `to_date` | string | No | End date in YYYY-MM-DD format. Omitting defaults to today. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/nasdaq/stock-historical-quotes.json`](../../../catalog/models/nasdaq/stock-historical-quotes.json) · Store page: https://www.sandbase.ai/model/nasdaq/stock-historical-quotes
