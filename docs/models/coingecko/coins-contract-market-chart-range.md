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

Get the historical chart data within certain time range in UNIX along with price, market cap and 24hr volume based on asset platform and particular token contract address

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-contract-market-chart-range" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum", "from": "1735516800", "to": "1735603200", "vs_currency": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contract_address` | string | Yes | The contract address of token. |
| `id` | string | Yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). |
| `from` | string | Yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |
| `to` | string | Yes | Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `vs_currency` | string | Yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-contract-market-chart-range.json`](../../../catalog/models/coingecko/coins-contract-market-chart-range.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-contract-market-chart-range
