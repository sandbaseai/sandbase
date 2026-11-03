# Polymarket Get spread API: pricing, parameters and code examples

`polymarket/spread` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the spread for a specific token ID. The spread is the difference between the best ask and best bid prices.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/spread", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/spread', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/spread", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/spread", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/spread` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Returns the current spread for one Polymarket outcome token. The spread is the gap between the best ask price and the best bid price. You send one `token_id`.

### Use cases

- Check how tight the market is for an outcome token before placing an order.
- Flag thin markets by filtering out tokens with a wide spread.
- Track the spread of a token over time to see how the gap between bid and ask changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/spread" \
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
  "spread": "0.001"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `spread` | The difference between the best ask price and the best bid price for the token. |
| `spread` | Returned as a decimal string. In the sample, `0.001` means the best ask and best bid are 0.001 apart. |
| `spread` | A smaller value means the best bid and best ask sit closer together. A larger value means they sit further apart. |

### Notes

- The `token_id` is the long numeric asset ID of one outcome. Get it from [Polymarket Get market by slug](/apis/polymarket/markets-slug) or [Polymarket List markets](/apis/polymarket/markets).
- The `spread` value is a string. Convert it to a number before you compare or calculate with it.
- For the full list of bids and asks behind the spread, call [Polymarket Get order book](/apis/polymarket/book).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/spread.json`](../../../catalog/models/polymarket/spread.json) · Store page: https://www.sandbase.ai/model/polymarket/spread
