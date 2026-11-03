# CoinGecko Coin Historical Chart Data within Time Range by Token Address API: pricing, parameters and code examples

`coingecko/coins-contract-market-chart-range` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the historical chart data within certain time range in UNIX along with price, market cap and 24hr volume based on asset platform and particular token contract address

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-contract-market-chart-range", "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum", "from": "2025-12-22", "to": "2025-12-31", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-contract-market-chart-range', {'contract_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'id': 'ethereum', 'from': '2025-12-22', 'to': '2025-12-31', 'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-contract-market-chart-range", {
  "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "id": "ethereum",
  "from": "2025-12-22",
  "to": "2025-12-31",
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-contract-market-chart-range", sandbase.Params{
	"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
	"id": "ethereum",
	"from": "2025-12-22",
	"to": "2025-12-31",
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-contract-market-chart-range` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). default `"ethereum"` |
| `to` | string | yes | Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. default `"2025-12-31"` |
| `from` | string | yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. default `"2025-12-22"` |
| `interval` | string |  | Data interval, leave empty for auto granularity. one of: `1m`, `5m`, `hourly`, `daily` |
| `precision` | string |  | Decimal place for currency price value. one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currency` | string | yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). default `"usd"` |
| `contract_address` | string | yes | The contract address of token. default `"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"` |

## Details

Returns time series of price, market cap and total volume for a token between two dates. You pass the token `contract_address`, the asset platform `id`, a `from` and `to` range, and a `vs_currency`.

### Use cases

- Chart the USD price of a stablecoin such as USDC over a chosen week to check how closely it holds its peg.
- Compare market cap and trading volume of a token across two date ranges.
- Export hourly price points for a token contract into a spreadsheet or database for backtesting.
- Add a historical price chart for a token address to a wallet or portfolio app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-contract-market-chart-range" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum", "from": "1735516800", "to": "1735603200", "vs_currency": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contract_address` | string | Yes | The contract address of token. |
| `from` | string | Yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `id` | string | Yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). |
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
| `prices` | List of `[timestamp, price]` pairs. The price is in the currency you set in `vs_currency`. |
| `prices[][0] / market_caps[][0] / total_volumes[][0]` | Timestamp of the data point as a UNIX time in milliseconds, for example `1735516800000`. |
| `prices[][1]` | Token price at that timestamp, in the `vs_currency` you requested. |
| `market_caps` | List of `[timestamp, market cap]` pairs for the token. |
| `market_caps[][1]` | Market cap value at that timestamp. |
| `total_volumes` | List of `[timestamp, volume]` pairs for the token. |
| `total_volumes[][1]` | Trading volume value at that timestamp. |

### Notes

- Set `id` to an asset platform ID such as `ethereum`, and set `contract_address` to the token contract on that platform.
- `from` and `to` accept `YYYY-MM-DD`, `YYYY-MM-DDTHH:MM` or a UNIX timestamp in seconds. The returned timestamps are in milliseconds.
- Leave `interval` empty for automatic granularity, or set it to `1m`, `5m`, `hourly` or `daily`. Use `precision` to set the decimal places of the price.
- To chart by coin ID instead of contract address, use [CoinGecko Coin Historical Chart Data within Time Range by ID](/apis/coingecko/coins-market-chart-range).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-contract-market-chart-range.json`](../../../catalog/models/coingecko/coins-contract-market-chart-range.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-contract-market-chart-range
