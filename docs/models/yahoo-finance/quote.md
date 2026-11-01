# Yahoo Finance Quote

`yahoo-finance/quote` · api · Yahoo Finance

Retrieve real-time stock quotes including current price, bid/ask, volume, market cap, and market status for one or more tickers. Supports batch lookups via comma-separated symbols.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/quote", "symbols": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/quote', {'symbols': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/quote", {
  "symbols": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/quote", sandbase.Params{
	"symbols": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbols` | string | yes | Comma-separated list of stock ticker symbols (e.g., AAPL,MSFT,TSLA).  |

## Details

Retrieve real-time stock quotes including current price, bid/ask, volume, market cap, and market status for one or more tickers. Supports batch lookups via comma-separated symbols.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbols": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbols` | string | Yes | Comma-separated list of stock ticker symbols (e.g., AAPL,MSFT,TSLA). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/quote.json`](../../../catalog/models/yahoo-finance/quote.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/quote
