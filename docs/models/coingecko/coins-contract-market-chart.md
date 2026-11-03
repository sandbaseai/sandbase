# CoinGecko Coin Historical Chart Data by Token Address API: pricing, parameters and code examples

`coingecko/coins-contract-market-chart` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the historical chart data including time in UNIX, price, market cap and 24hr volume based on asset platform and particular token contract address

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-contract-market-chart", "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum", "days": "1", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-contract-market-chart', {'contract_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'id': 'ethereum', 'days': '1', 'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-contract-market-chart", {
  "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "id": "ethereum",
  "days": "1",
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-contract-market-chart", sandbase.Params{
	"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
	"id": "ethereum",
	"days": "1",
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-contract-market-chart` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). default `"ethereum"` |
| `days` | string | yes | Data up to number of days ago. You may use any integer or `max` for number of days. default `"1"` |
| `interval` | string |  | Data interval, leave empty for auto granularity. one of: `1m`, `5m`, `hourly`, `daily` |
| `precision` | string |  | Decimal place for currency price value. one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currency` | string | yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). default `"usd"` |
| `contract_address` | string | yes | The contract address of token. default `"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"` |

## Details

Returns time series of price, market cap and total volume for a token, looked up by its contract address on an asset platform. It needs `contract_address`, the platform `id`, `days` and `vs_currency`.

### Use cases

- Plot a price chart for an ERC-20 token when you only know its contract address.
- Track how a token's market cap changes over the last day or over its full history with `days` set to `max`.
- Compare traded volume against price moves for a stablecoin or other token.
- Export price points to a spreadsheet or database for backtesting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-contract-market-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum", "days": "1", "vs_currency": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contract_address` | string | Yes | The contract address of token. |
| `days` | string | Yes | Data up to number of days ago. You may use any integer or `max` for number of days. |
| `id` | string | Yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). |
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
| `prices[][0] / market_caps[][0] / total_volumes[][0]` | Timestamp of the data point. It is a number such as `1793604600000`, which looks like UNIX time in milliseconds. |
| `prices[][1]` | Token price at that timestamp in the target currency. |
| `market_caps` | List of `[timestamp, market cap]` pairs for the token. |
| `market_caps[][1]` | Market cap value at that timestamp in the target currency. |
| `total_volumes` | List of `[timestamp, volume]` pairs for the token. |
| `total_volumes[][1]` | Trading volume value at that timestamp in the target currency. |

### Notes

- Set `id` to an asset platform ID such as `ethereum`. The `contract_address` must be a token on that platform.
- Set `interval` to `1m`, `5m`, `hourly` or `daily`, or leave it empty for automatic granularity. In the sample call, points are 5 minutes apart.
- Use `precision` to set the decimal places of the price values.
- To chart a custom start and end date, call [CoinGecko Coin Historical Chart Data within Time Range by Token Address](/apis/coingecko/coins-contract-market-chart-range). For coins by CoinGecko ID, use [CoinGecko Coin Historical Chart Data by ID](/apis/coingecko/coins-market-chart).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-contract-market-chart.json`](../../../catalog/models/coingecko/coins-contract-market-chart.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-contract-market-chart
