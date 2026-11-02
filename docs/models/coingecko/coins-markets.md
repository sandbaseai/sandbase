# CoinGecko Coins List with Market Data API: pricing, parameters and code examples

`coingecko/coins-markets` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the supported coins with price, market cap, volume and market related data

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-markets", "vs_currency": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-markets', {'vs_currency': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-markets", {
  "vs_currency": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-markets", sandbase.Params{
	"vs_currency": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | string |  | Coins' IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list) default `"bitcoin"` |
| `page` | integer |  | Page through results. Default: 1  |
| `names` | string |  | Coins' names, comma-separated if querying more than 1 coin. default `"Bitcoin"` |
| `order` | string |  | Sort result by field. Default: market_cap_desc one of: `market_cap_asc`, `market_cap_desc`, `volume_asc`, `volume_desc`, `id_asc`, `id_desc` |
| `locale` | string |  | Language background. Default: en one of: `ar`, `bg`, `cs`, `da`, `de`, `el`, `en`, `es`, `fi`, `fr`, `he`, `hi` … |
| `symbols` | string |  | Coins' symbols, comma-separated if querying more than 1 coin. default `"btc"` |
| `category` | string |  | Filter based on coins' category. *refers to [`/coins/categories/list`](/reference/coins-categories-list)  |
| `per_page` | integer |  | Total results per page. Default: 100 Valid values: 1...250  |
| `precision` | string |  | Decimal places for currency price value one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `sparkline` | boolean |  | Include sparkline 7-day data. Default: false  |
| `vs_currency` | string | yes | Target currency of coins and market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) default `"usd"` |
| `include_tokens` | string |  | For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens by market cap or volume. one of: `top`, `all` |
| `include_rehypothecated` | boolean |  | Include rehypothecated tokens in results. When true, returns `market_cap_rank_with_rehypothecated` field. Default: false  |
| `price_change_percentage` | string |  | Include price change percentage timeframe, comma-separated if querying more than 1 timeframe. Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y`  |

## Details

Get all the supported coins with price, market cap, volume and market related data

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"vs_currency": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Filter based on coins' category. *refers to [`/coins/categories/list`](/reference/coins-categories-list) |
| `ids` | string | No | Coins' IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list) |
| `include_rehypothecated` | boolean | No | Include rehypothecated tokens in results. When true, returns `market_cap_rank_with_rehypothecated` field. Default: false |
| `include_tokens` | string | No | For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens by market cap or volume. |
| `locale` | string | No | Language background. Default: en |
| `names` | string | No | Coins' names, comma-separated if querying more than 1 coin. |
| `order` | string | No | Sort result by field. Default: market_cap_desc |
| `page` | integer | No | Page through results. Default: 1 |
| `per_page` | integer | No | Total results per page. Default: 100 Valid values: 1...250 |
| `precision` | string | No | Decimal places for currency price value |
| `price_change_percentage` | string | No | Include price change percentage timeframe, comma-separated if querying more than 1 timeframe. Valid values: `1h`, `24h`, `7d`, `14d`, `30d`, `200d`, `1y` |
| `sparkline` | boolean | No | Include sparkline 7-day data. Default: false |
| `symbols` | string | No | Coins' symbols, comma-separated if querying more than 1 coin. |
| `vs_currency` | string | Yes | Target currency of coins and market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-markets.json`](../../../catalog/models/coingecko/coins-markets.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-markets
