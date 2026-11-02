# Yahoo Finance Closing Price API: pricing, parameters and code examples

`yahoo-finance/closing-price` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Return the official daily closing price for a single ticker on one specific calendar date, interpreted in the listing exchange's local timezone (returned as exchange_timezone). One request per call.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/closing-price", "date": "2026-10-01", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/closing-price', {'date': '2026-10-01', 'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/closing-price", {
  "date": "2026-10-01",
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/closing-price", sandbase.Params{
	"date": "2026-10-01",
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/closing-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Calendar date in ISO form YYYY-MM-DD, interpreted in the exchange's local timezone. Must not be in the future.  |
| `symbol` | string | yes | Stock ticker symbol (e.g., AAPL).  |

## Details

Return the official daily closing price for a single ticker on one specific calendar date, interpreted in the listing exchange's local timezone (returned as exchange_timezone). One request per call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/closing-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-10-01", "symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | Calendar date in ISO form YYYY-MM-DD, interpreted in the exchange's local timezone. Must not be in the future. |
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/closing-price.json`](../../../catalog/models/yahoo-finance/closing-price.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/closing-price
