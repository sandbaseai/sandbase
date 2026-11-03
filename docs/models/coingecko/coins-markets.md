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

Returns a list of coins with market data, such as market cap, 24-hour trading volume, supply, and all-time high and low values. It needs `vs_currency`, the currency the values are quoted in, for example `usd`.

### Use cases

- Build a ranked table of the largest coins by market cap in a chosen currency.
- Track how far a coin trades below its all-time high using `ath_change_percentage`.
- Compare `circulating_supply` with `max_supply` across several coins.
- Pull the 24-hour high, low and change for a watchlist of coin IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"vs_currency": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `vs_currency` | string | Yes | Target currency of coins and market data. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) |
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

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "ath": 126080,
    "ath_change_percentage": -39.17528,
    "ath_date": "2025-10-06T10:57:42.000Z",
    "atl": 67.81,
    "atl_change_percentage": 112993.7487,
    "atl_date": "2013-07-05T16:00:00.000Z",
    "circulating_supply": 20105365.0,
    "current_price": 76688,
    "fully_diluted_valuation": 1541835004796,
    "high_24h": 78287,
    "id": "bitcoin",
    "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id / symbol / name` | The coin identifier, its ticker in lowercase and its display name. Use `id` as the key for follow-up calls. |
| `market_cap / market_cap_rank` | Market capitalization in the requested currency and the coin's rank by market cap. |
| `fully_diluted_valuation` | Fully diluted valuation of the coin in the requested currency. |
| `total_volume` | Total trading volume figure for the coin. |
| `high_24h / low_24h` | Highest and lowest value seen in the last 24 hours. |
| `market_cap_change_24h / market_cap_change_percentage_24h` | Absolute and percentage change in market cap over 24 hours. |
| `circulating_supply / total_supply / max_supply` | Coins in circulation, total coins that exist, and the supply cap. `max_supply` can be empty when no cap is set. |
| `ath / ath_date / ath_change_percentage` | All-time high value, the ISO 8601 date it happened, and the current percentage change from that high. |
| `atl / atl_date / atl_change_percentage` | All-time low value, the ISO 8601 date it happened, and the current percentage change from that low. |
| `last_updated` | ISO 8601 timestamp of the last update to this coin's data. |

### Notes

- The response is a JSON array with one object per coin. Use `page` and `per_page` (1 to 250) to step through the list.
- Pass `ids`, `names` or `symbols` as comma-separated values to limit the result to specific coins. Find valid IDs with [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- Find valid `vs_currency` values with [CoinGecko Supported Currencies List](/apis/coingecko/simple-supported-vs-currencies).
- Call [CoinGecko Coin Data by ID](/apis/coingecko/coins) with a coin `id` for full details on one coin.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-markets.json`](../../../catalog/models/coingecko/coins-markets.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-markets
