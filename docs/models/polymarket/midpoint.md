# Polymarket Get midpoint price API: pricing, parameters and code examples

`polymarket/midpoint` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the midpoint price for a specific token ID. The midpoint is calculated as the average of the best bid and best ask prices.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/midpoint", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/midpoint', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/midpoint", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/midpoint", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/midpoint` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Returns the midpoint price for one Polymarket outcome token. The midpoint is the average of the best bid and best ask. You send a `token_id`.

### Use cases

- Show the midpoint price of a Polymarket outcome token on a dashboard.
- Store `mid` on a schedule to build a price series for one token.
- Value an open position in an outcome token without reading the full order book.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/midpoint" \
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
  "mid": "0.0205"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mid` | Midpoint price of the token, calculated as the average of the best bid and best ask. |
| `mid` | Comes back as a string, for example `"0.0205"`. Parse it to a number before you do math. |
| `mid` | The only key in the response. It has no timestamp, so record your own request time when you store values. |

### Notes

- `token_id` is the long numeric asset ID of one outcome token.
- Call [Polymarket Get order book](/apis/polymarket/book) to see the best bid and best ask that the midpoint is based on.
- Call [Polymarket Get spread](/apis/polymarket/spread) or [Polymarket Get last trade price](/apis/polymarket/last-trade-price) for the same token to compare against `mid`.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/midpoint.json`](../../../catalog/models/polymarket/midpoint.json) · Store page: https://www.sandbase.ai/model/polymarket/midpoint
