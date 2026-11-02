# CoinGecko Coin Price by Token Addresses API: pricing, parameters and code examples

`coingecko/simple-token-price` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get one or more token prices using their token contract addresses

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/simple-token-price", "id": "ethereum", "contract_addresses": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "vs_currencies": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/simple-token-price', {'id': 'ethereum', 'contract_addresses': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'vs_currencies': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/simple-token-price", {
  "id": "ethereum",
  "contract_addresses": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "vs_currencies": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/simple-token-price", sandbase.Params{
	"id": "ethereum",
	"contract_addresses": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
	"vs_currencies": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/simple-token-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Asset platform's ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list) default `"ethereum"` |
| `precision` | string |  | Decimal places for currency price value one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currencies` | string | yes | Target currency of coins, comma-separated if querying more than 1 currency. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) default `"usd"` |
| `include_24hr_vol` | boolean |  | Include 24-hour trading volume. Default: false  |
| `contract_addresses` | string | yes | Token contract addresses, comma-separated if querying more than 1 token default `"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"` |
| `include_market_cap` | boolean |  | Include market capitalization. Default: false  |
| `include_24hr_change` | boolean |  | Include 24-hour change percentage. Default: false  |
| `include_last_updated_at` | boolean |  | Include last updated price time as a UNIX timestamp. Default: false  |

## Details

Get one or more token prices using their token contract addresses

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/simple-token-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "ethereum", "contract_addresses": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "vs_currencies": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Asset platform's ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list) |
| `contract_addresses` | string | Yes | Token contract addresses, comma-separated if querying more than 1 token |
| `include_24hr_change` | boolean | No | Include 24-hour change percentage. Default: false |
| `include_24hr_vol` | boolean | No | Include 24-hour trading volume. Default: false |
| `include_last_updated_at` | boolean | No | Include last updated price time as a UNIX timestamp. Default: false |
| `include_market_cap` | boolean | No | Include market capitalization. Default: false |
| `precision` | string | No | Decimal places for currency price value |
| `vs_currencies` | string | Yes | Target currency of coins, comma-separated if querying more than 1 currency. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencie |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/simple-token-price.json`](../../../catalog/models/coingecko/simple-token-price.json) · Store page: https://www.sandbase.ai/model/coingecko/simple-token-price
