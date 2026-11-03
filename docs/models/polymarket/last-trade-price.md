# Polymarket Get last trade price API: pricing, parameters and code examples

`polymarket/last-trade-price` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the last trade price and side for a specific token ID. Returns default values of 0.5 for price and empty string for side if no trades found.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/last-trade-price", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/last-trade-price', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/last-trade-price", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/last-trade-price", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/last-trade-price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Returns the most recent trade price and trade side for one Polymarket outcome token. It needs a `token_id` (the asset ID of the outcome token). If the token has no trades, the description says the API returns `0.5` for `price` and an empty string for `side`.

### Use cases

- Show the latest traded price for a Yes or No outcome on a dashboard.
- Check whether the last trade on a token was a buy or a sell.
- Compare the last trade price with the current midpoint or spread to spot stale quotes.
- Poll a list of token IDs to track price moves on markets you follow.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/last-trade-price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | Yes | Token ID (asset ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "price": "0.02",
  "side": "SELL"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `price` | Price of the last trade for the token, returned as a string. In the sample it is `0.02`. The description says it is `0.5` when no trades exist. |
| `side` | Side of the last trade, such as `SELL`. The description says it is an empty string when no trades exist. |

### Notes

- `token_id` is a long numeric string in the sample request. Send it as a string, not a number.
- A `price` of `0.5` with an empty `side` is the default for a token with no trades. It is not a real trade.
- To find a token ID from a market, call [Polymarket Get market by slug](/apis/polymarket/markets-slug) or [Polymarket Get market by id](/apis/polymarket/markets-by-id).
- For current quotes instead of the last trade, call [Polymarket Get midpoint price](/apis/polymarket/midpoint).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/last-trade-price.json`](../../../catalog/models/polymarket/last-trade-price.json) · Store page: https://www.sandbase.ai/model/polymarket/last-trade-price
