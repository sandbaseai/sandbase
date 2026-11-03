# Financial Datasets Get Historical Stock Prices API: pricing, parameters and code examples

`financial-datasets/prices` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Historical Stock Prices from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/prices", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The stock ticker symbol (e.g. AAPL, MSFT).  |
| `end_date` | string |  | The end date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `interval` | string |  | The time interval for the price data. Provider reference (supplier schema): `{"enum":["day","week","month","year"],"type":"string"}`.  |
| `start_date` | string |  | The start date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `interval_multiplier` | string |  | interval_multiplier  |

## Details

Returns historical price bars for one stock ticker as a list of open, high, low, close and volume values. It needs a `ticker`, and you can set `interval`, `interval_multiplier`, `start_date` and `end_date` to choose the range and bar size.

### Use cases

- Plot a daily candlestick chart for `AAPL` over a chosen date range.
- Compute daily returns or moving averages from the `close` values.
- Backtest a trading rule against historical open, high, low and close data.
- Check trading volume on specific days to spot unusual activity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/prices" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "interval": "day", "interval_multiplier": "1", "start_date": "2026-10-01", "end_date": "2026-10-10"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `end_date` | string | No | The end date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `interval` | string | No | The time interval for the price data. Provider reference (supplier schema): `{"enum":["day","week","month","year"],"type":"string"}`. |
| `interval_multiplier` | string | No | interval_multiplier |
| `start_date` | string | No | The start date for the price data (format: YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `ticker` | string | No | The stock ticker symbol (e.g. AAPL, MSFT). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "prices": [
    {
      "close": 330.32,
      "high": 332.48,
      "low": 325.81,
      "open": 330.0,
      "ticker": "AAPL",
      "time": "2026-10-01",
      "volume": 36306346
    }
  ],
  "ticker": "AAPL"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `prices` | List of price bars, one per interval in the requested date range. |
| `prices[].time` | Date of the bar in `YYYY-MM-DD` format. |
| `prices[].open / prices[].close` | Price at the start and at the end of the bar. |
| `prices[].high / prices[].low` | Highest and lowest price reached during the bar. |
| `prices[].volume` | Number of shares traded during the bar. |
| `prices[].ticker / ticker` | Ticker symbol the prices belong to. |

### Notes

- Use `YYYY-MM-DD` for `start_date` and `end_date`. The `interval` parameter accepts `day`, `week`, `month` or `year`.
- Weekend dates are absent from the daily response. The sample jumps from `2026-10-02` to `2026-10-05`.
- To page through a long result, pass the cursor from `next_page_url` as `cursor`. When you send `cursor`, all other parameters are ignored.
- For the latest price only, call [Financial Datasets Get Stock Price Snapshot](/apis/financial-datasets/prices-snapshot).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/prices.json`](../../../catalog/models/financial-datasets/prices.json) · Store page: https://www.sandbase.ai/model/financial-datasets/prices
