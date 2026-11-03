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

Returns the daily closing price and related trading data for one stock ticker on one calendar date. It needs a `symbol` and a `date` in `YYYY-MM-DD` form.

### Use cases

- Look up the closing price of a holding on a past date to value a portfolio on that day.
- Check whether a specific date was a trading day for a given ticker with `is_trading_day`.
- Pull the open, high, low and volume for one day to review a price move after an event.
- Compare `close` with `adj_close` to see how the adjusted price differs on a given date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/closing-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-10-01", "symbol": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | Calendar date in ISO form YYYY-MM-DD, interpreted in the exchange's local timezone. Must not be in the future. |
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adj_close": 330.32000732421875,
    "close": 330.32000732421875,
    "currency": "USD",
    "date": "2026-10-01",
    "exchange": "NasdaqGS",
    "exchange_timezone": "America/New_York",
    "high": 332.4800109863281,
    "is_trading_day": true,
    "low": 325.80999755859375,
    "open": 330,
    "symbol": "AAPL",
    "volume": 36306300
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.close` | Closing price for the requested date. |
| `data.adj_close` | Adjusted closing price for the requested date. It matches `close` in this example. |
| `data.open / data.high / data.low` | Opening price, highest price and lowest price for the day. |
| `data.volume` | Number of shares traded that day. |
| `data.currency` | Currency of the price values, such as `USD`. |
| `data.is_trading_day` | `true` when the exchange traded on this date. |
| `data.exchange` | Name of the listing exchange, such as `NasdaqGS`. |
| `data.exchange_timezone` | Timezone used to interpret `date`, such as `America/New_York`. |
| `data.symbol / data.date` | The ticker and the calendar date the result applies to. |

### Notes

- `date` cannot be in the future.
- Each call returns one ticker and one date. To get prices for a range of dates, use [Yahoo Finance Historical Data](/apis/yahoo-finance/historical-data).
- If you do not know the ticker, find it with [Yahoo Finance Search Tickers](/apis/yahoo-finance/search-tickers).
- For the current price instead of a past close, call [Yahoo Finance Quote](/apis/yahoo-finance/quote).

### Pricing

$0.05 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/closing-price.json`](../../../catalog/models/yahoo-finance/closing-price.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/closing-price
