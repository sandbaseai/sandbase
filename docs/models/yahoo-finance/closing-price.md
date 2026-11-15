# Yahoo Finance Closing Price API: pricing, parameters and code examples

`yahoo-finance/closing-price` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00099 per call · **Modes:** sync

Get a stock or ETF's latest price and previous closing price from Yahoo Finance by ticker symbol, with day high/low, change, volume, and market cap. Returns the most recent session only; historical dates are not supported.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00099**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/closing-price", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/closing-price', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/closing-price", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/closing-price", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/yahoo-finance/closing-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | The ticker symbol to look up.  |

## Details

Get a stock or ETF's latest price and previous closing price from Yahoo Finance by ticker symbol, with day high/low, change, volume, and market cap. Returns the most recent session only; historical dates are not supported.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yahoo-finance/closing-price", "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | The ticker symbol to look up. |

### Pricing

Billed at the actual cost of each call: about $0.00099 per result returned (about $0.00099 for 1 results). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/closing-price.json`](../../../catalog/models/yahoo-finance/closing-price.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/closing-price
