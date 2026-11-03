# CoinGecko Trending Search List API: pricing, parameters and code examples

`coingecko/search-trending` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

This endpoint allows you query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/search-trending"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/search-trending', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/search-trending", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/search-trending", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/search-trending` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `show_max` | string |  | Show max number of results available for the given type. Available values: `coins`, `nfts`, `categories` e.g. `coins` or `coins,nfts,categories`  |

## Details

This API returns the coins, NFTs and categories that are trending in CoinGecko search over the last 24 hours. It also returns a list of trending real-world assets (`rwas`). The only input is the optional `show_max` parameter, so you can call it with an empty body.

### Use cases

- Show a "trending now" widget for coins in a crypto portfolio app.
- Track which NFT collections gain search interest and compare their floor price changes.
- Spot trending categories such as privacy coins to find themes that attract attention.
- Feed trending coin IDs into a price or market data lookup to build a daily watchlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/search-trending" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `show_max` | string | No | Show max number of results available for the given type. Available values: `coins`, `nfts`, `categories` e.g. `coins` or `coins,nfts,categories` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "coins_count": "52",
      "data": {
        "market_cap": 31439103134.825195,
        "market_cap_btc": 410229.2784844282,
        "market_cap_change_percentage_24h": {
          "aed": -5.929889987889743,
          "afn": -5.283929290050673,
          "all": -6.298361504127248,
          "amd": -6.190641475939194,
          "ang": -5.929889987889749,
          "aoa": -5.929889987889743,
          "ars": -5.332151587377018,
          "aud": -5.464280715064876
        },
        "sparkline": "https://data.coingecko.com/categories/37/sparkline.svg",
        "total_volume": 1020611831.2371521,
        "total_volume_btc": 13317.01257624726
      },
      "id": 37,
      "market_cap_1h_change": 0.9715813048497784,
      "name": "Privacy Coins",
      "slug": "privacy-coins",
      "top_3_coins_images": [
        "https://assets.coingecko.com/coins/images/14151/small/prcy.png?1696513870"
      ]
    }
  ],
  "coins": [
    {
      "item": {
        "coin_id": 10365,
        "data": {
          "content": {
            "title": "What is NEAR Protocol?"
          },
          "market_cap": "$4,957,211,429",
          "market_cap_btc": "64740.13632566405",
          "price": 3.7821721815763367,
          "price_btc": "0.00004939437144377415",
          "price_change_percentage_24h": {
            "aed": -7.371348189118371,
            "ars": -6.782769073308284,
            "aud": -6.912873555604516,
            "bch": -5.37667014078531,
            "bdt": -7.4892009099759,
            "bhd": -7.6920682540991505,
            "bits": -5.591082641095886,
            "bmd": -7.371348189118382
          },
          "sparkline": "https://data.coingecko.com/coins/10365/sparkline.svg",
          "total_volume": "$582,084,067"
        },
        "id": "near",
        "large": "https://coin-images.coingecko.com/coins/images/10365/large/near.jpg?1696510367",
        "market_cap_rank": 21,
        "name": "NEAR Protocol",
        "price_btc": 4.939437144377415e-05,
        "score": 0
      }
    }
  ],
  "nfts": [
    {
      "data": {
        "content": null,
        "floor_price": "0.018 BTC",
        "floor_price_in_usd_24h_percentage_change": "3.11180681057578",
        "h24_average_sale_price": "0.11 BTC",
        "h24_volume": "0.34 BTC",
        "sparkline": "https://data.coingecko.com/nft/3256/sparkline.svg"
      },
      "floor_price_24h_percentage_change": 3.11180681057578,
      "floor_price_in_native_currency": 0.0175,
      "id": "ordinal-maxi-biz-omb",
      "name": "Ordinal Maxi Biz (OMB)",
      "native_currency_symbol": "btc",
      "nft_contract_id": 3256,
      "symbol": "OMB",
      "thumb": "https://coin-images.coingecko.com/nft_contracts/images/3256/standard/ordinal-max…"
    }
  ],
  "rwas": [
    {
      "data": {
        "benchmark_price": 3910.833007430583,
        "price_change_percentage_24h": 0.2,
        "spot_price": 3902.543741701648
      },
      "id": "gold",
      "market_cap_rank": 1,
      "name": "Gold",
      "symbol": "XAU",
      "thumb": "https://coin-images.coingecko.com/rwas/images/1/standard/8d1b974a084d4810d68ef70…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `coins[].item.id / coins[].item.name` | The CoinGecko coin ID (for example `near`) and the display name of the trending coin. |
| `coins[].item.score` | Position in the trending list for the coin. `0` is the first coin. |
| `coins[].item.market_cap_rank` | Market cap rank of the coin on CoinGecko. |
| `coins[].item.data.price / coins[].item.data.market_cap / coins[].item.data.total_volume` | Current price as a number, plus market cap and trading volume as formatted dollar strings. |
| `coins[].item.data.price_change_percentage_24h` | 24 hour price change percentage, keyed by currency code such as `aed`, `aud` or `bmd`. |
| `nfts[].id / nfts[].name / nfts[].symbol` | The CoinGecko ID, name and symbol of the trending NFT collection. |
| `nfts[].floor_price_in_native_currency / nfts[].native_currency_symbol` | Floor price of the collection as a number, and the symbol of the currency it is priced in, such as `btc` or `sol`. |
| `nfts[].floor_price_24h_percentage_change` | Percentage change in the floor price over 24 hours. |
| `categories[].name / categories[].coins_count` | Name of the trending category and the number of coins in it. |
| `categories[].data.market_cap / categories[].data.total_volume / categories[].market_cap_1h_change` | Market cap and trading volume of the category, and its market cap change over the last hour. |
| `rwas[].name / rwas[].symbol / rwas[].data.spot_price / rwas[].data.price_change_percentage_24h` | Name and symbol of a trending real-world asset, its spot price, and its 24 hour price change percentage. |

### Notes

- Pass `show_max` as `coins`, `nfts`, `categories` or a comma separated mix such as `coins,nfts,categories` to get the maximum number of results for those types.
- Use the `coins[].item.id` value (for example `solana`) as the coin ID in [CoinGecko Coin Data by ID](/apis/coingecko/coins) or [CoinGecko Coin Price by IDs, Symbols, or Names](/apis/coingecko/simple-price).
- Use `categories[].id` and `categories[].slug` to match a trending category with [CoinGecko Coins Categories List with Market Data](/apis/coingecko/coins-categories).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/search-trending.json`](../../../catalog/models/coingecko/search-trending.json) · Store page: https://www.sandbase.ai/model/coingecko/search-trending
