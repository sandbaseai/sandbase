# CoinGecko Coin Historical Chart Data by ID API: pricing, parameters and code examples

`coingecko/coins-market-chart` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the historical chart data of a coin including time in UNIX, price, market cap and 24hr volume based on particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-market-chart", "id": "bitcoin", "days": "1", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-market-chart', {'id': 'bitcoin', 'days': '1', 'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-market-chart", {
  "id": "bitcoin",
  "days": "1",
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-market-chart", sandbase.Params{
	"id": "bitcoin",
	"days": "1",
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-market-chart` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). default `"bitcoin"` |
| `days` | string | yes | Data up to number of days ago. You may use any integer or `max` for number of days. default `"1"` |
| `interval` | string |  | Data interval, leave empty for auto granularity. one of: `1m`, `5m`, `hourly`, `daily` |
| `precision` | string |  | Decimal place for currency price value. one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currency` | string | yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). default `"usd"` |

## Details

Returns historical price, market cap and total volume series for one coin on CoinGecko. You pass a coin `id` such as `bitcoin`, a number of `days` and a `vs_currency` such as `usd`.

### Use cases

- Draw a price chart for a coin over the last day, week or full history.
- Compare market cap and trading volume trends for one coin over time.
- Export time series data for backtesting or analysis in a spreadsheet or notebook.
- Show price in a local currency by changing `vs_currency`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-market-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "days": "1", "vs_currency": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `days` | string | Yes | Data up to number of days ago. You may use any integer or `max` for number of days. |
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `vs_currency` | string | Yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "market_caps": [
    [
      1793604600000
    ]
  ],
  "prices": [
    [
      1793604600000
    ]
  ],
  "total_volumes": [
    [
      1793604600000
    ]
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `prices` | List of `[timestamp, price]` pairs. The price is in the currency set by `vs_currency`. |
| `prices[][0] / market_caps[][0] / total_volumes[][0]` | Timestamp of the data point, as a UNIX time value in milliseconds (for example `1793604600000`). |
| `prices[][1]` | Coin price at that timestamp. |
| `market_caps` | List of `[timestamp, market cap]` pairs for the coin. |
| `market_caps[][1]` | Market cap value at that timestamp. |
| `total_volumes` | List of `[timestamp, volume]` pairs for the coin's trading volume. |
| `total_volumes[][1]` | Trading volume value at that timestamp. |

### Notes

- Get the coin `id` from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- Get valid `vs_currency` values from [CoinGecko Supported Currencies List](/apis/coingecko/simple-supported-vs-currencies).
- Each entry in the three lists is a two-item array, and the lists share the same timestamps. In the sample with `days` set to `1`, points are 5 minutes apart.
- For a fixed start and end time, use [CoinGecko Coin Historical Chart Data within Time Range by ID](/apis/coingecko/coins-market-chart-range).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-market-chart.json`](../../../catalog/models/coingecko/coins-market-chart.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-market-chart
