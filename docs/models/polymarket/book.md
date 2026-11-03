# Polymarket Get order book API: pricing, parameters and code examples

`polymarket/book` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the order book summary for a specific token ID. Includes bids, asks, market details, and last trade price.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/book", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/book', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/book", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/book", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/book` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Returns the current order book for one Polymarket outcome token. The response lists bids and asks with price and size, plus the market ID, last trade price, tick size and minimum order size. The only input is `token_id`.

### Use cases

- Check how much size sits at each price level before placing a large order on an outcome.
- Measure the gap between the best bid and best ask to judge how liquid a market is.
- Compare `last_trade_price` with the current book to see if the last trade is near the current quotes.
- Round order prices to the market's `tick_size` and check them against `min_order_size` before submitting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/book" \
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
  "asks": [
    {
      "price": "0.999",
      "size": "2181808.98"
    }
  ],
  "asset_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401",
  "bids": [
    {
      "price": "0.001",
      "size": "10292518.46"
    }
  ],
  "hash": "285c09d5641a442182342bba3d67e237031ff918",
  "last_trade_price": "0.979",
  "market": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
  "min_order_size": "5",
  "neg_risk": false,
  "tick_size": "0.001",
  "timestamp": "1793691713417"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `bids[].price / asks[].price` | Price level of a resting order, given as a string. Prices in this response run from `0.001` to `0.999`. |
| `bids[].size / asks[].size` | Total size resting at that price level, given as a string. |
| `asset_id` | The token ID this order book belongs to. It matches the `token_id` in the request. |
| `market` | Identifier of the market the token belongs to. It starts with `0x`. |
| `last_trade_price` | Price of the most recent trade for this token, given as a string. |
| `tick_size` | Smallest price step for this market. In this response it is `0.001`. |
| `min_order_size` | Minimum order size allowed for this market. |
| `neg_risk` | Boolean flag from the market details. It is `false` for this token. |
| `hash` | Hash string for the order book snapshot. |
| `timestamp` | Time of the snapshot as a string of digits. The value looks like a Unix time in milliseconds. |

### Notes

- Get `token_id` from [Polymarket Get market by slug](/apis/polymarket/markets-slug) or [Polymarket List markets](/apis/polymarket/markets). Each outcome of a market has its own token ID.
- The book is sorted from the outermost price inward in this response. Bids start at `0.001` and asks start at `0.999`, so the best bid and best ask are at the end of each list.
- For a single quote instead of the full book, call [Polymarket Get midpoint price](/apis/polymarket/midpoint).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/book.json`](../../../catalog/models/polymarket/book.json) · Store page: https://www.sandbase.ai/model/polymarket/book
