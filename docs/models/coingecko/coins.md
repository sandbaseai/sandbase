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

Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on a particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin"}'
```

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

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins.json`](../../../catalog/models/coingecko/coins.json) · Store page: https://www.sandbase.ai/model/coingecko/coins
