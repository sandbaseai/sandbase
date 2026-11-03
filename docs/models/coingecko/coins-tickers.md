# CoinGecko Coin Tickers by ID API: pricing, parameters and code examples

`coingecko/coins-tickers` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-tickers", "id": "bitcoin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-tickers', {'id': 'bitcoin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-tickers", {
  "id": "bitcoin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-tickers", sandbase.Params{
	"id": "bitcoin",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-tickers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) default `"bitcoin"` |
| `page` | integer |  | Page through results  |
| `depth` | boolean |  | Include 2% orderbook depth, i.e. `cost_to_move_up_usd` and `cost_to_move_down_usd`. Default: false  |
| `order` | string |  | Sort the order of responses. Default: trust_score_desc one of: `trust_score_desc`, `trust_score_asc`, `volume_desc`, `volume_asc` |
| `exchange_ids` | string |  | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list)  |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |
| `include_exchange_logo` | boolean |  | Include exchange logo. Default: false  |

## Details

Returns the list of trading pairs (tickers) for one coin across centralized and decentralized exchanges. Each ticker has the last traded value, volume, bid-ask spread, and the exchange it trades on. You pass a CoinGecko coin `id` such as `bitcoin`.

### Use cases

- Compare the value of one coin on different exchanges to spot gaps between markets.
- Rank exchanges by converted trading volume for a coin to find where it trades most.
- Filter out stale or anomalous tickers before you compute an average across exchanges.
- Build a list of trade page links for a coin, one per exchange.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-tickers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) |
| `depth` | boolean | No | Include 2% orderbook depth, i.e. `cost_to_move_up_usd` and `cost_to_move_down_usd`. Default: false |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |
| `exchange_ids` | string | No | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list) |
| `include_exchange_logo` | boolean | No | Include exchange logo. Default: false |
| `order` | string | No | Sort the order of responses. Default: trust_score_desc |
| `page` | integer | No | Page through results |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "name": "Bitcoin",
  "tickers": [
    {
      "base": "BTC",
      "bid_ask_spread_percentage": 0.010039,
      "coin_id": "bitcoin",
      "coin_mcap_usd": 1541835004795.5227,
      "converted_last": {
        "btc": 0.99969503,
        "eth": 34.125454,
        "usd": 76711
      },
      "converted_volume": {
        "btc": 30669,
        "eth": 1046928,
        "usd": 2353403725
      },
      "is_anomaly": false,
      "is_stale": false,
      "last": 76819.99,
      "last_fetch_at": "2026-11-03T07:27:50+00:00",
      "last_traded_at": "2026-11-03T07:27:49+00:00",
      "market": {
        "has_trading_incentive": false,
        "identifier": "coinup",
        "name": "CoinUp.io"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name` | Name of the coin the tickers belong to, for example `Bitcoin`. |
| `tickers[].base / tickers[].target` | The two sides of the trading pair. `base` is the coin you asked for and `target` is the quote asset, such as `USDT`. |
| `tickers[].market.name / tickers[].market.identifier` | Display name and ID of the exchange that lists the pair. For example, `identifier` is `btcc` for BTCC. |
| `tickers[].last / tickers[].volume` | Last traded value of the pair, quoted in the `target` asset, and the trading volume reported for the pair on that exchange. |
| `tickers[].converted_last.usd / tickers[].converted_last.btc / tickers[].converted_last.eth` | The last traded value converted to USD, BTC and ETH. Use these to compare tickers that quote in different assets. |
| `tickers[].converted_volume.usd / tickers[].converted_volume.btc / tickers[].converted_volume.eth` | The trading volume converted to USD, BTC and ETH. |
| `tickers[].bid_ask_spread_percentage` | Gap between the best bid and best ask for the pair, given as a percentage. |
| `tickers[].is_anomaly / tickers[].is_stale` | Boolean flags that mark a ticker as an anomaly or as stale. Filter on these when you need clean data. |
| `tickers[].last_traded_at / tickers[].last_fetch_at / tickers[].timestamp` | ISO 8601 timestamps with a UTC offset. They show when the last trade happened, when the ticker was last fetched, and the ticker timestamp. |
| `tickers[].trade_url` | Link to the trading page for the pair on the exchange. |

### Notes

- Get the coin `id` from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list). Get `exchange_ids` values from [CoinGecko Exchanges List (ID Map)](/apis/coingecko/exchanges-list).
- Use `page` to get more tickers. Use `order` with `trust_score_desc`, `trust_score_asc`, `volume_desc` or `volume_asc` to change the sort.
- Set `depth` to `true` to add `cost_to_move_up_usd` and `cost_to_move_down_usd`. Set `include_exchange_logo` to `true` to add exchange logos.
- To list all tickers on one exchange instead, call [CoinGecko Exchange Tickers by ID](/apis/coingecko/exchanges-tickers).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-tickers.json`](../../../catalog/models/coingecko/coins-tickers.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-tickers
