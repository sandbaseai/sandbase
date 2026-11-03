# CoinGecko Coin Price by IDs, Symbols, or Names API: pricing, parameters and code examples

`coingecko/simple-price` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

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

Returns the market value of one or more coins on CoinGecko, quoted in the currencies you choose. You pass `vs_currencies` plus a coin identifier as `ids`, `symbols`, or `names`. The response is an object keyed by coin ID, with one number per target currency.

### Use cases

- Show the Bitcoin rate in USD on a dashboard or in a chat bot.
- Convert a portfolio of coins into several fiat currencies with one call by listing multiple `ids` and `vs_currencies`.
- Add 24-hour change, volume, or market cap to a ticker with the `include_*` flags.
- Look up a coin by ticker with `symbols` when you do not know the CoinGecko coin ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/simple-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": "bitcoin", "vs_currencies": "usd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `vs_currencies` | string | Yes | Target currency of coins, comma-separated if querying more than 1 currency. *refers to [`/simple/supported_vs_currencies`](/reference/simple-supported-currencies) |
| `ids` | string | No | Coins' IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list) |
| `include_24hr_change` | boolean | No | Include 24-hour change percentage. Default: false |
| `include_24hr_vol` | boolean | No | Include 24-hour trading volume. Default: false |
| `include_last_updated_at` | boolean | No | Include last updated price time as a UNIX timestamp. Default: false |
| `include_market_cap` | boolean | No | Include market capitalization. Default: false |
| `include_tokens` | string | No | For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens by market cap or volume. |
| `names` | string | No | Coins' names, comma-separated if querying more than 1 coin. |
| `precision` | string | No | Decimal places for currency price value |
| `symbols` | string | No | Coins' symbols, comma-separated if querying more than 1 coin. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "bitcoin": {
    "usd": 76688
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `bitcoin` | Top-level key. It is the coin ID that was requested. Each requested coin gets its own key. |
| `bitcoin.usd` | Value of one coin in the target currency. The key name is the currency code from `vs_currencies`, so other currencies appear as sibling keys. |

### Notes

- Get valid coin IDs from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- Get valid `vs_currencies` values from [CoinGecko Supported Currencies List](/apis/coingecko/simple-supported-vs-currencies).
- Set `include_24hr_change`, `include_24hr_vol`, `include_market_cap`, or `include_last_updated_at` to `true` to add extra keys next to each currency value. The sample request did not use them, so the sample response has only the currency value.
- For contract addresses instead of coin IDs, use [CoinGecko Coin Data by Token Address](/apis/coingecko/coins-contract).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/simple-price.json`](../../../catalog/models/coingecko/simple-price.json) · Store page: https://www.sandbase.ai/model/coingecko/simple-price
