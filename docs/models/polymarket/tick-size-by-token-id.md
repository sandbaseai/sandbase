# Polymarket Get tick size by path parameter API: pricing, parameters and code examples

`polymarket/tick-size-by-token-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the minimum tick size (price increment) for a specific token ID using the token ID as a path parameter.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tick-size-by-token-id", "token_id": "0xabc123def456..."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tick-size-by-token-id', {'token_id': '0xabc123def456...'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tick-size-by-token-id", {
  "token_id": "0xabc123def456..."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tick-size-by-token-id", sandbase.Params{
	"token_id": "0xabc123def456...",
})
```

Same call via the path form: `POST /v1/api/polymarket/tick-size-by-token-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | Token ID (asset ID)  |

## Details

Returns the minimum tick size, which is the smallest allowed price step, for one Polymarket outcome token. It needs the token ID (asset ID) of that outcome.

### Use cases

- Round limit order prices to a valid increment before you place or simulate an order on a Polymarket outcome.
- Validate a price grid in a trading bot before it submits quotes for a token.
- Check the price step of a token before you draw an order book or a price ladder in a UI.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tick-size-by-token-id" \
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
  "minimum_tick_size": 0.001
}
```

### Response fields

| Field | Meaning |
|---|---|
| `minimum_tick_size` | The smallest price increment allowed for the token. The response contains only this one field. |
| `minimum_tick_size` | In the example response the value is `0.001`. Prices for this token then move in steps of `0.001`, such as `0.123` but not `0.1234`. |
| `minimum_tick_size` | The value is a JSON number, not a string. You can compare it or divide by it without parsing text. |

### Notes

- Pass the token ID as `token_id`. It is a long decimal string, so send it as a string and keep every digit.
- Use [Polymarket Get market by token](/apis/polymarket/markets-by-token) to find the market that a token ID belongs to.
- Call [Polymarket Get order book](/apis/polymarket/book) next to see the live bids and asks for the same token.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tick-size-by-token-id.json`](../../../catalog/models/polymarket/tick-size-by-token-id.json) · Store page: https://www.sandbase.ai/model/polymarket/tick-size-by-token-id
