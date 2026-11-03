# Financial Datasets Get Stock Price Snapshot API: pricing, parameters and code examples

`financial-datasets/prices-snapshot` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the real-time price snapshot for a stock, including the current price, day change, and day change percent.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/prices-snapshot"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/prices-snapshot', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/prices-snapshot", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/prices-snapshot", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/prices-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string |  | The stock ticker symbol (e.g. AAPL, MSFT).  |

## Details

Returns the latest price snapshot for one stock: the current price, the change since the previous close, and the time of the quote. It needs a stock ticker symbol such as `AAPL`.

### Use cases

- Show a live quote for a ticker on a dashboard or watchlist.
- Check how far a stock has moved today before running a trade alert.
- Add the current price to a portfolio value calculation.
- Compare today's percent move across several tickers by calling the API once per ticker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/prices-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | No | The stock ticker symbol (e.g. AAPL, MSFT). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "snapshot": {
    "day_change": -13.93,
    "day_change_percent": -4.04,
    "price": 330.7,
    "ticker": "AAPL",
    "time": "2026-11-03T00:37:12Z",
    "time_milliseconds": 1793666232299
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `snapshot.ticker` | The stock ticker symbol the snapshot is for. |
| `snapshot.price` | The current stock price in the response, for example `330.7`. |
| `snapshot.day_change` | The price change for the day. A negative value means the stock is down. |
| `snapshot.day_change_percent` | The day change as a percent. The example value `-4.04` matches a drop of about 4 percent. |
| `snapshot.time` | The quote time as an ISO 8601 timestamp in UTC, for example `2026-11-03T00:37:12Z`. |
| `snapshot.time_milliseconds` | The same quote time as a Unix timestamp in milliseconds. |

### Notes

- Pass the ticker in the `ticker` parameter. Use the exchange symbol, such as `AAPL` or `MSFT`.
- The `ticker` parameter is marked optional in the schema, but the request needs it to return a snapshot for a stock.
- For past prices over a date range, use [Financial Datasets Get Historical Stock Prices](/apis/financial-datasets/prices).
- For valuation and ratio data on the same ticker, use [Financial Datasets Get Financial Metrics Snapshot](/apis/financial-datasets/financial-metrics-snapshot).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/prices-snapshot.json`](../../../catalog/models/financial-datasets/prices-snapshot.json) · Store page: https://www.sandbase.ai/model/financial-datasets/prices-snapshot
