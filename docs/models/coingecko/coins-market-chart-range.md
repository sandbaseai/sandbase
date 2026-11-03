# CoinGecko Coin Historical Chart Data within Time Range by ID API: pricing, parameters and code examples

`coingecko/coins-market-chart-range` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hr volume based on particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-market-chart-range", "id": "bitcoin", "from": "2025-12-22", "to": "2025-12-31", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-market-chart-range', {'id': 'bitcoin', 'from': '2025-12-22', 'to': '2025-12-31', 'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-market-chart-range", {
  "id": "bitcoin",
  "from": "2025-12-22",
  "to": "2025-12-31",
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-market-chart-range", sandbase.Params{
	"id": "bitcoin",
	"from": "2025-12-22",
	"to": "2025-12-31",
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-market-chart-range` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). default `"bitcoin"` |
| `to` | string | yes | Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. default `"2025-12-31"` |
| `from` | string | yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. default `"2025-12-22"` |
| `interval` | string |  | Data interval, leave empty for auto granularity. one of: `1m`, `5m`, `hourly`, `daily` |
| `precision` | string |  | Decimal place for currency price value. one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currency` | string | yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). default `"usd"` |

## Details

Returns historical price, market cap and total volume time series for one coin between a start and end time. Pass the coin `id` (for example `bitcoin`), `from`, `to` and `vs_currency`.

### Use cases

- Plot a price chart for a coin over a custom date window.
- Compare market cap and trading volume of a coin across two periods.
- Backtest a trading rule against hourly or daily price points.
- Export price history in a chosen quote currency into a spreadsheet or database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-market-chart-range" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "from": "1735516800", "to": "1735603200", "vs_currency": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | Yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `to` | string | Yes | Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `vs_currency` | string | Yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "market_caps": [
    [
      1735516800000
    ]
  ],
  "prices": [
    [
      1735516800000
    ]
  ],
  "total_volumes": [
    [
      1735516800000
    ]
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `prices` | List of `[timestamp, price]` pairs. Each price is in the currency set by `vs_currency`. |
| `prices[][0] / market_caps[][0] / total_volumes[][0]` | Timestamp of the data point as a number, for example `1735516800000`. It has 13 digits, so it is in milliseconds. |
| `prices[][1]` | Coin price at that timestamp, in the `vs_currency` currency. |
| `market_caps` | List of `[timestamp, market cap]` pairs for the same time points. |
| `market_caps[][1]` | Market cap of the coin at that timestamp, in the `vs_currency` currency. |
| `total_volumes` | List of `[timestamp, volume]` pairs for the same time points. |
| `total_volumes[][1]` | Trading volume of the coin at that timestamp, in the `vs_currency` currency. |

### Notes

- Get valid values for `id` from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list). Get valid `vs_currency` values from [CoinGecko Supported Currencies List](/apis/coingecko/simple-supported-vs-currencies).
- `from` and `to` accept `YYYY-MM-DD`, `YYYY-MM-DDTHH:MM` or a UNIX timestamp in seconds. The sample request used `1735516800` and `1735603200`.
- Set `interval` to `1m`, `5m`, `hourly` or `daily`, or leave it empty for automatic granularity. Use `precision` to set the decimal places of price values.
- For OHLC candles instead of line points, call [CoinGecko Coin OHLC Chart by ID](/apis/coingecko/coins-ohlc).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-market-chart-range.json`](../../../catalog/models/coingecko/coins-market-chart-range.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-market-chart-range
