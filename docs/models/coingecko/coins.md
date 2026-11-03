# CoinGecko Coin Data by ID API: pricing, parameters and code examples

`coingecko/coins` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on a particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins", "id": "bitcoin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins', {'id': 'bitcoin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins", {
  "id": "bitcoin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins", sandbase.Params{
	"id": "bitcoin",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) default `"bitcoin"` |
| `tickers` | boolean |  | Include tickers data. Default: true  |
| `sparkline` | boolean |  | Include sparkline 7-day data. Default: false  |
| `market_data` | boolean |  | Include market data. Default: true  |
| `localization` | boolean |  | Include all localized languages in the response. Default: true  |
| `community_data` | boolean |  | Include community data. Deprecated: has no effect as of 28 August 2026; the `community_data` object is no longer returned.  |
| `developer_data` | boolean |  | Include developer data. Deprecated: has no effect as of 28 August 2026; the `developer_data` object is no longer returned.  |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |
| `include_categories_details` | boolean |  | Include categories details. Default: false  |

## Details

Returns the CoinGecko page data for one coin: descriptions, links, categories, images, and market data. It needs a CoinGecko coin `id` such as `bitcoin`.

### Use cases

- Show a coin profile page with its logo, description, homepage, and social links.
- Read the all-time high, all-time low, and market rank of a coin for a research dashboard.
- Find a coin's categories, hashing algorithm, and genesis date for research tools.
- Collect official repos, explorers, and whitepaper links for a coin.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) |
| `community_data` | boolean | No | Include community data. Deprecated: has no effect as of 28 August 2026; the `community_data` object is no longer returned. |
| `developer_data` | boolean | No | Include developer data. Deprecated: has no effect as of 28 August 2026; the `developer_data` object is no longer returned. |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |
| `include_categories_details` | boolean | No | Include categories details. Default: false |
| `localization` | boolean | No | Include all localized languages in the response. Default: true |
| `market_data` | boolean | No | Include market data. Default: true |
| `sparkline` | boolean | No | Include sparkline 7-day data. Default: false |
| `tickers` | boolean | No | Include tickers data. Default: true |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "additional_notices": [],
  "asset_platform_id": null,
  "block_time_in_minutes": 10,
  "categories": [
    "Smart Contract Platform"
  ],
  "country_origin": "",
  "description": {
    "ar": "",
    "bg": "",
    "cs": "",
    "da": "",
    "de": "",
    "el": "",
    "en": "Bitcoin is the world's first decentralized cryptocurrency, created in 2009 by th…",
    "es": "¿Qué es Bitcoin (BTC)?\nBitcoin es el primer caso de éxito de dinero de Internet …",
    "fi": "",
    "fr": "",
    "he": "",
    "hi": ""
  },
  "detail_platforms": {
    "": {
      "contract_address": "",
      "decimal_place": null
    }
  },
  "genesis_date": "2009-01-03",
  "has_supply_breakdown": false,
  "hashing_algorithm": "SHA-256",
  "id": "bitcoin",
  "image": {
    "large": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
    "small": "https://coin-images.coingecko.com/coins/images/1/small/bitcoin.png?1696501400",
    "thumb": "https://coin-images.coingecko.com/coins/images/1/thumb/bitcoin.png?1696501400"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The CoinGecko coin ID. Use it in other CoinGecko calls. |
| `categories` | List of category names the coin belongs to, such as `Layer 1 (L1)`. |
| `description.en` | Text description of the coin in English. Other language keys hold translations and may be empty. |
| `image.large / image.small / image.thumb` | URLs of the coin logo in three sizes. |
| `links.homepage / links.blockchain_site / links.whitepaper / links.repos_url.github` | Official website, block explorer links, whitepaper link, and GitHub repository URLs. |
| `genesis_date / hashing_algorithm / block_time_in_minutes` | Launch date, the hashing algorithm name, and block time in minutes. |
| `market_cap_rank` | Rank of the coin by market cap. |
| `market_data.ath / market_data.ath_date / market_data.ath_change_percentage` | All-time high per quote currency, the date it happened, and the percent change from that high to now. |
| `market_data.circulating_supply` | Number of coins in circulation. |
| `market_data.fully_diluted_valuation` | Fully diluted valuation of the coin, with one value per quote currency. |

### Notes

- Get valid `id` values from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- Set `market_data`, `tickers`, or `localization` to `false` to leave those sections out of the response.
- For historical chart data, call [CoinGecko Coin Historical Chart Data by ID](/apis/coingecko/coins-market-chart).
- Timestamps such as `last_updated` and `market_data.ath_date` use ISO 8601 format in UTC.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins.json`](../../../catalog/models/coingecko/coins.json) · Store page: https://www.sandbase.ai/model/coingecko/coins
