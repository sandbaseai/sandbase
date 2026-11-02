# CoinGecko Coin OHLC Chart by ID API: pricing, parameters and code examples

`coingecko/coins-ohlc` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-ohlc", "id": "bitcoin", "days": "1", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-ohlc', {'id': 'bitcoin', 'days': '1', 'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-ohlc", {
  "id": "bitcoin",
  "days": "1",
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-ohlc", sandbase.Params{
	"id": "bitcoin",
	"days": "1",
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-ohlc` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). default `"bitcoin"` |
| `days` | string | yes | Data up to number of days ago. one of: `1`, `7`, `14`, `30`, `90`, `180`, `365`, `max`; default `"1"` |
| `interval` | string |  | Data interval, leave empty for auto granularity. one of: `daily`, `hourly` |
| `precision` | string |  | Decimal place for currency price value. one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currency` | string | yes | Target currency of price data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). default `"usd"` |

## Details

Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-ohlc" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "days": "1", "vs_currency": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `days` | string | Yes | Data up to number of days ago. |
| `interval` | string | No | Data interval, leave empty for auto granularity. |
| `precision` | string | No | Decimal place for currency price value. |
| `vs_currency` | string | Yes | Target currency of price data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-ohlc.json`](../../../catalog/models/coingecko/coins-ohlc.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-ohlc
