# CoinGecko Coin Price by IDs, Symbols, or Names

`coingecko/simple-price` · api · CoinGecko

Get the prices of one or more coins by using their unique Coin API IDs, symbols, or names

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/simple-price", "vs_currencies": "usd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/simple-price', {'vs_currencies': 'usd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/simple-price", {
  "vs_currencies": "usd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/simple-price", sandbase.Params{
	"vs_currencies": "usd",
})
```

Same call via the path form: `POST /v1/api/coingecko/simple-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | string |  | Coins' IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list) default `"bitcoin"` |
| `names` | string |  | Coins' names, comma-separated if querying more than 1 coin. default `"Bitcoin"` |
| `symbols` | string |  | Coins' symbols, comma-separated if querying more than 1 coin. default `"btc"` |
| `precision` | string |  | Decimal places for currency price value one of: `full`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` … |
| `vs_currencies` | string | yes | Target currency of coins, comma-separated if querying more than 1 currency. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) default `"usd"` |
| `include_tokens` | string |  | For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens by market cap or volume. one of: `top`, `all` |
| `include_24hr_vol` | boolean |  | Include 24-hour trading volume. Default: false  |
| `include_market_cap` | boolean |  | Include market capitalization. Default: false  |
| `include_24hr_change` | boolean |  | Include 24-hour change percentage. Default: false  |
| `include_last_updated_at` | boolean |  | Include last updated price time as a UNIX timestamp. Default: false  |

## Details

Get the prices of one or more coins by using their unique Coin API IDs, symbols, or names

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/simple-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": "bitcoin", "vs_currencies": "usd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | string | No | Coins' IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list) |
| `include_24hr_change` | boolean | No | Include 24-hour change percentage. Default: false |
| `include_24hr_vol` | boolean | No | Include 24-hour trading volume. Default: false |
| `include_last_updated_at` | boolean | No | Include last updated price time as a UNIX timestamp. Default: false |
| `include_market_cap` | boolean | No | Include market capitalization. Default: false |
| `include_tokens` | string | No | For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens by market cap or volume. |
| `names` | string | No | Coins' names, comma-separated if querying more than 1 coin. |
| `precision` | string | No | Decimal places for currency price value |
| `symbols` | string | No | Coins' symbols, comma-separated if querying more than 1 coin. |
| `vs_currencies` | string | Yes | Target currency of coins, comma-separated if querying more than 1 currency. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencie |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/simple-price.json`](../../../catalog/models/coingecko/simple-price.json) · Store page: https://www.sandbase.ai/model/coingecko/simple-price
