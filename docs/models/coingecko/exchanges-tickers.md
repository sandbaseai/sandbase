# CoinGecko Exchange Tickers by ID API: pricing, parameters and code examples

`coingecko/exchanges-tickers` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Exchange Tickers by ID from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges-tickers", "id": "binance"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges-tickers', {'id': 'binance'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges-tickers", {
  "id": "binance"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges-tickers", sandbase.Params{
	"id": "binance",
})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges-tickers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). default `"binance"` |
| `page` | number |  | Page through results.  |
| `depth` | boolean |  | Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false  |
| `order` | string |  | Sort the order of responses. Default: `trust_score_desc` one of: `market_cap_asc`, `market_cap_desc`, `trust_score_desc`, `trust_score_asc`, `volume_desc`, `volume_asc`, `base_target` |
| `coin_ids` | string |  | Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list).  |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |
| `include_exchange_logo` | boolean |  | Include exchange logo. Default: false  |

## Details

Returns the trading pairs (tickers) listed on one CoinGecko exchange, with last traded value, volume, spread, and converted values in BTC, ETH, and USD. It needs an exchange `id` such as `binance`.

### Use cases

- Compare the `BTC/USDT` quote on one exchange against the same pair on another exchange.
- Rank an exchange's pairs by `converted_volume.usd` to find its most traded markets.
- Filter an exchange to a few coins with `coin_ids` and track their spread and last trade time.
- Build trade links to open a pair directly on the exchange.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-tickers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). |
| `coin_ids` | string | No | Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list). |
| `depth` | boolean | No | Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |
| `include_exchange_logo` | boolean | No | Include exchange logo. Default: false |
| `order` | string | No | Sort the order of responses. Default: `trust_score_desc` |
| `page` | number | No | Page through results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "name": "Binance",
  "tickers": [
    {
      "base": "USDC",
      "bid_ask_spread_percentage": 0.010999,
      "coin_id": "usd-coin",
      "coin_mcap_usd": 71013530626.33456,
      "converted_last": {
        "btc": 1.303e-05,
        "eth": 0.00044409,
        "usd": 0.99989
      },
      "converted_volume": {
        "btc": 21722,
        "eth": 740303,
        "usd": 1666830578
      },
      "is_anomaly": false,
      "is_stale": false,
      "last": 1.00131,
      "last_fetch_at": "2026-11-03T07:27:50+00:00",
      "last_traded_at": "2026-11-03T07:27:53+00:00",
      "market": {
        "has_trading_incentive": false,
        "identifier": "binance",
        "name": "Binance"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name` | Name of the exchange. |
| `tickers[].base / tickers[].target` | Symbols of the base and quote assets in the pair. For example `BTC` and `USDT`. |
| `tickers[].coin_id / tickers[].target_coin_id` | CoinGecko IDs of the base coin and the target coin. Use them with other coin APIs. |
| `tickers[].last` | Last traded value of the pair, in units of the target asset. |
| `tickers[].volume` | Trading volume of the pair, in units of the base asset. |
| `tickers[].converted_last.usd / tickers[].converted_last.btc / tickers[].converted_last.eth` | Last traded value converted to USD, BTC, and ETH. |
| `tickers[].converted_volume.usd / tickers[].converted_volume.btc / tickers[].converted_volume.eth` | Trading volume converted to USD, BTC, and ETH. |
| `tickers[].bid_ask_spread_percentage` | Bid-ask spread of the pair, given as a percentage value. |
| `tickers[].coin_mcap_usd` | Market cap of the base coin in USD. |
| `tickers[].last_traded_at / tickers[].last_fetch_at / tickers[].timestamp` | ISO 8601 timestamps for the last trade, the last data fetch, and the ticker record. |
| `tickers[].is_anomaly / tickers[].is_stale` | Boolean flags that mark a ticker as anomalous or stale. |
| `tickers[].trade_url` | Link to the pair's trading page on the exchange. |

### Notes

- Get valid `id` values from [CoinGecko Exchanges List (ID Map)](/apis/coingecko/exchanges-list).
- Get valid `coin_ids` values from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- Use `page` to step through results, and `order` to sort them. For example, use `volume_desc` to put the highest volume first.
- Set `depth` to `true` to add 2% orderbook depth (`cost_to_move_up_usd` and `cost_to_move_down_usd`). Call [CoinGecko Exchange Data by ID](/apis/coingecko/exchanges-by-id) for exchange-level details.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/exchanges-tickers.json`](../../../catalog/models/coingecko/exchanges-tickers.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-tickers
