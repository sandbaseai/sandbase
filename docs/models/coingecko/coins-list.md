# CoinGecko Coins List (ID Map) API: pricing, parameters and code examples

`coingecko/coins-list` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the supported coins on CoinGecko with coins ID, name and symbol

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/coins-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status` | string |  | Filter by status of coins. Default: active one of: `active`, `inactive` |
| `include_platform` | boolean |  | Include platform and token's contract addresses. Default: false  |

## Details

Returns the list of coins that CoinGecko supports, as a flat array. Each entry has the coin `id`, `name` and `symbol`. No input is required. Optional parameters add contract addresses or switch to inactive coins.

### Use cases

- Build a lookup table that maps CoinGecko coin IDs to symbols and names.
- Resolve a ticker symbol to a coin `id` before you call a coin data or market data API.
- Check whether a coin is listed on CoinGecko by searching the list for its `id` or `symbol`.
- Set `status` to `inactive` to find coins that are not active.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `include_platform` | boolean | No | Include platform and token's contract addresses. Default: false |
| `status` | string | No | Filter by status of coins. Default: active |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "id": "_",
    "name": "༼ つ ◕_◕ ༽つ",
    "symbol": "gib"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].id` | CoinGecko coin ID, such as `000-capital`. Pass this value to other CoinGecko APIs that ask for a coin ID. |
| `[].name` | Display name of the coin. It can contain digits or unusual characters. |
| `[].symbol` | Ticker symbol of the coin. It appears in lowercase in the response. Use `id` as the identifier when you call other APIs. |

### Notes

- The request body can be empty (`{}`). By default the call returns coins with `status` set to `active`.
- Set `include_platform` to `true` to add platform and token contract address data to each coin. The sample response was requested without it and shows only `id`, `name` and `symbol`.
- Use the `id` value as the coin ID in [CoinGecko Coin Data by ID](/apis/coingecko/coins).
- To get market data for many coins in one call, use [CoinGecko Coins List with Market Data](/apis/coingecko/coins-markets).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-list.json`](../../../catalog/models/coingecko/coins-list.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-list
