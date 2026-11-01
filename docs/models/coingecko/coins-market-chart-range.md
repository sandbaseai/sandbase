# CoinGecko Coin Historical Chart Data within Time Range by ID

`coingecko/coins-market-chart-range` · api · CoinGecko

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

Get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hr volume based on particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-market-chart-range" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "from": "1735516800", "to": "1735603200", "vs_currency": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `from` | string | Yes | Starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |
| `to` | string | Yes | Ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. Use ISO date string for best compatibility. |
| `vs_currency` | string | Yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-market-chart-range.json`](../../../catalog/models/coingecko/coins-market-chart-range.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-market-chart-range
