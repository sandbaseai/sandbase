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

Get the historical chart data of a coin including time in UNIX, price, market cap and 24hr volume based on particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-market-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "days": "1", "vs_currency": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `days` | string | Yes | Data up to number of days ago. You may use any integer or `max` for number of days. |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |
| `vs_currency` | string | Yes | Target currency of market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-market-chart.json`](../../../catalog/models/coingecko/coins-market-chart.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-market-chart
