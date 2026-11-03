# CoinGecko Exchange Data by ID API: pricing, parameters and code examples

`coingecko/exchanges-by-id` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get exchange's data (name, year established, country, ...), exchange volume in BTC and top 100 tickers based on exchange's ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges-by-id", "id": "binance"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges-by-id', {'id': 'binance'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges-by-id", {
  "id": "binance"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges-by-id", sandbase.Params{
	"id": "binance",
})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). default `"binance"` |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |

## Details

Returns profile data for one crypto exchange on CoinGecko, including its country, year established, 24-hour BTC trading volume and trust score. It also returns a list of the exchange's tickers with last traded values and volumes. The input is an exchange `id`, such as `binance`.

### Use cases

- Show an exchange profile page with its name, logo, country, description and social links.
- Compare exchanges by `trust_score`, `trust_score_rank` and `trade_volume_24h_btc`.
- List the trading pairs on an exchange with last traded values converted to BTC, ETH and USD.
- Show an exchange's public notice and past status updates in a monitoring dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "alert_notice": "",
  "centralized": true,
  "coins": 521,
  "country": "Cayman Islands",
  "description": "One of the world’s largest cryptocurrency exchanges by trading volume, offering …",
  "facebook_url": "https://www.facebook.com/binanceexchange",
  "has_trading_incentive": false,
  "image": "https://coin-images.coingecko.com/markets/images/52/small/binance.jpg?1706864274",
  "name": "Binance",
  "other_url_1": "https://medium.com/binanceexchange",
  "other_url_2": "https://steemit.com/@binanceexchange",
  "pairs": 1377
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name / country / year_established / centralized` | Exchange name, country, the year it was established, and whether it is a centralized exchange (`true`) or not. |
| `trade_volume_24h_btc` | Trading volume of the exchange over 24 hours, shown in BTC. |
| `trust_score / trust_score_rank` | The exchange's trust score and its rank by that score. |
| `coins / pairs` | Number of coins and number of trading pairs listed on the exchange. |
| `public_notice / alert_notice` | Notices about the exchange. They can be empty strings, and long text may be cut. |
| `tickers[].base / tickers[].target` | The base and target of each trading pair, for example `BTC` and `USDT`. |
| `tickers[].last / tickers[].volume` | Last traded value of the pair and its trading volume. |
| `tickers[].converted_last / tickers[].converted_volume` | Last traded value and volume converted to `btc`, `eth` and `usd`. |
| `tickers[].coin_id / tickers[].target_coin_id` | CoinGecko coin IDs for the base and target coins. |
| `status_updates[].created_at / status_updates[].description` | Time and text of a past status update posted for the exchange. |

### Notes

- Get valid `id` values from [CoinGecko Exchanges List (ID Map)](/apis/coingecko/exchanges-list).
- Set `dex_pair_format` to `symbol` to show DEX pair base and target as symbols instead of contract addresses.
- Timestamps such as `last_traded_at` and `status_updates[].created_at` use ISO 8601 format.
- Use the `coin_id` values from tickers with [CoinGecko Coin Data by ID](/apis/coingecko/coins) to look up each coin. For a longer ticker list, call [CoinGecko Exchange Tickers by ID](/apis/coingecko/exchanges-tickers).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/exchanges-by-id.json`](../../../catalog/models/coingecko/exchanges-by-id.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-by-id
