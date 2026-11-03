# CoinGecko Exchanges List with Data API: pricing, parameters and code examples

`coingecko/exchanges` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the supported exchanges with exchanges' data (ID, name, country, ...) that have active trading volumes on CoinGecko

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | number |  | Page through results. Default: 1  |
| `per_page` | number |  | Total results per page. Default: 100. Valid values: 1...250  |

## Details

Returns a list of crypto exchanges tracked on CoinGecko, with each exchange's ID, name, country, trust score and 24-hour trading volume in BTC. It needs no input. You can set `page` and `per_page` to step through the list.

### Use cases

- Build a ranking table of exchanges sorted by `trust_score_rank` or `trade_volume_24h_btc`.
- Collect exchange `id` values to feed into per-exchange lookups.
- Group exchanges by `country` or `year_established` to study how the market is spread out.
- Show exchange names, logos and links in a crypto app's exchange directory.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | number | No | Page through results. Default: 1 |
| `per_page` | number | No | Total results per page. Default: 100. Valid values: 1...250 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "country": "United States",
    "has_trading_incentive": false,
    "id": "kraken",
    "image": "https://coin-images.coingecko.com/markets/images/29/small/kraken.jpg?1706864265",
    "name": "Kraken",
    "trade_volume_24h_btc": 21814.843227406407,
    "trust_score": 10,
    "trust_score_rank": 1,
    "url": "https://www.kraken.com/",
    "year_established": 2011
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Exchange ID on CoinGecko, such as `kraken` or `gdax`. Use it to identify the exchange in other CoinGecko calls. |
| `name` | Display name of the exchange. |
| `country` | Country listed for the exchange. It can be missing or empty for some entries. |
| `year_established` | Year the exchange was founded. |
| `trust_score / trust_score_rank` | `trust_score` is a numeric score for the exchange, and `trust_score_rank` is its position in the ranking. Rank 1 is the top entry. |
| `trade_volume_24h_btc` | Trading volume of the exchange over 24 hours, expressed in BTC. |
| `has_trading_incentive` | Boolean flag that shows whether the exchange has a trading incentive. |
| `description` | Short text about the exchange. It appears only on some entries. |
| `url / image` | `url` is the exchange's website. `image` is the link to its logo. |

### Notes

- Each response is a JSON array of exchange objects, not an object with a wrapper key.
- Use `page` (default 1) and `per_page` (default 100, valid values 1 to 250) to move through the list.
- The `id` value works as the exchange ID input for [CoinGecko Exchange Data by ID](/apis/coingecko/exchanges-by-id) and [CoinGecko Exchange Tickers by ID](/apis/coingecko/exchanges-tickers).
- For a lighter list that holds only IDs and names, use [CoinGecko Exchanges List (ID Map)](/apis/coingecko/exchanges-list).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/exchanges.json`](../../../catalog/models/coingecko/exchanges.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges
