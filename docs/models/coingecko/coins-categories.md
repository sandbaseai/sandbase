# CoinGecko Coins Categories List with Market Data API: pricing, parameters and code examples

`coingecko/coins-categories` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the coins categories with market data (market cap, volume, ...) on CoinGecko

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/coins-categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | string |  | Sort results by field. Default: `market_cap_desc` one of: `market_cap_desc`, `market_cap_asc`, `name_desc`, `name_asc`, `market_cap_change_24h_desc`, `market_cap_change_24h_asc` |

## Details

Returns a list of CoinGecko coin categories with market data for each one. The list includes market cap, 24 hour volume, and the top 3 coins in the category. The only input is the optional `order` parameter, so you can call it with an empty body.

### Use cases

- Rank crypto sectors such as Layer 1 or Proof of Work by total `market_cap`.
- Find categories with the biggest 24 hour market cap move by sorting with `market_cap_change_24h_desc` or `market_cap_change_24h_asc`.
- Build a sector dashboard that shows volume and the leading coins for each category.
- Collect category `id` values to use in other CoinGecko category filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `order` | string | No | Sort results by field. Default: `market_cap_desc` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "content": "Smart contract platforms are usually blockchains that host smart contracts or de…",
    "id": "smart-contract-platform",
    "market_cap": 2222866902946.95,
    "market_cap_change_24h": -1.807761056228854,
    "name": "Smart Contract Platform",
    "top_3_coins": [
      "https://coin-images.coingecko.com/coins/images/1/small/bitcoin.png"
    ],
    "top_3_coins_id": [
      "bitcoin"
    ],
    "updated_at": "2026-11-03T07:25:48.000Z",
    "volume_24h": 48445845979.916245
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Category ID in slug form, for example `layer-1`. Use it to identify the category in other calls. |
| `name` | Display name of the category, for example `Layer 1 (L1)`. |
| `content` | Short text that describes the category. Long text is cut in the sample, so the full value may be longer. |
| `market_cap` | Total market cap of all coins in the category. |
| `market_cap_change_24h` | Change in the category market cap over the last 24 hours. The values in the sample are small signed numbers such as `-1.81`. |
| `volume_24h` | Trading volume of the category over the last 24 hours. |
| `top_3_coins_id` | List of CoinGecko coin IDs for the three leading coins in the category, for example `bitcoin`. |
| `top_3_coins` | List of image URLs for the same three coins, in the same order as `top_3_coins_id`. |
| `updated_at` | ISO 8601 UTC timestamp of the last update of the category row. |

### Notes

- `order` accepts `market_cap_desc` (default), `market_cap_asc`, `name_desc`, `name_asc`, `market_cap_change_24h_desc` and `market_cap_change_24h_asc`.
- The response is a plain JSON array. The request has no pagination parameters.
- Pass values from `top_3_coins_id` to [CoinGecko Coin Data by ID](/apis/coingecko/coins) to get full data for a coin.
- Call [CoinGecko Coins Categories List (ID Map)](/apis/coingecko/coins-categories-list) if you only need category IDs and names without market data.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-categories.json`](../../../catalog/models/coingecko/coins-categories.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-categories
