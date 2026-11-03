# Yahoo Finance Historical Data API: pricing, parameters and code examples

`yahoo-finance/historical-data` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Extract historical OHLCV price data for a single ticker over a configurable date range and interval. Returns timestamped records suitable for charting and technical analysis.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/historical-data", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/historical-data', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/historical-data", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/historical-data", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/historical-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `range` | string |  | Date range for historical data.  |
| `symbol` | string | yes | Stock ticker symbol (e.g., AAPL).  |
| `interval` | string |  | Data interval granularity.  |

## Details

Returns historical price records for one stock ticker on Yahoo Finance. Each record has open, high, low, close and volume values with a timestamp. The only required input is `symbol`, and you can set `range` and `interval` to change the window and spacing.

### Use cases

- Plot a candlestick chart for AAPL from the returned `open`, `high`, `low` and `close` values.
- Compute moving averages or other technical indicators over the closing price series.
- Compare trading volume across days to spot unusually active sessions.
- Export daily price history for a ticker into a spreadsheet or backtesting tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/historical-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |
| `interval` | string | No | Data interval granularity. |
| `range` | string | No | Date range for historical data. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "currency": "USD",
    "history": [
      {
        "close": 269.04998779296875,
        "high": 270.8500061035156,
        "low": 266.25,
        "open": 270.4200134277344,
        "timestamp": 1762180200,
        "volume": 50194600
      }
    ],
    "symbol": "AAPL"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.symbol` | The ticker symbol the history belongs to, such as `AAPL`. |
| `data.currency` | The currency code of the price values, such as `USD`. |
| `data.history[]` | One price record per interval, listed in order from oldest to newest. |
| `data.history[].timestamp` | The start time of the record as a Unix timestamp in seconds. |
| `data.history[].open / data.history[].close` | The first and last price of the interval. |
| `data.history[].high / data.history[].low` | The highest and lowest price reached during the interval. |
| `data.history[].volume` | The number of shares traded during the interval. |
| `status` | Shows `success` when the request worked. |

### Notes

- `symbol` is the stock ticker. If you do not know it, use [Yahoo Finance Search Tickers](/apis/yahoo-finance/search-tickers) to find it.
- `timestamp` values are Unix seconds. Convert them to dates before charting.
- Price values are floats with many decimal places. Round them for display.
- For the latest price instead of a series, call [Yahoo Finance Quote](/apis/yahoo-finance/quote).

### Pricing

$0.05 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/historical-data.json`](../../../catalog/models/yahoo-finance/historical-data.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/historical-data
