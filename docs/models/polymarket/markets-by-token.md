# Polymarket Get market by token API: pricing, parameters and code examples

`polymarket/markets-by-token` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get market by token from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-by-token", "token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-by-token', {'token_id': '32338220190071351435772801779725302244575775216413325951443816017994629993401'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-by-token", {
  "token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-by-token", sandbase.Params{
	"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401",
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-by-token` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string | yes | The token ID to look up the parent market for  |

## Details

Returns the parent market identifiers for a Polymarket outcome token. You send one `token_id` and get back the market's `condition_id` and the token IDs of both outcomes.

### Use cases

- Map a token ID seen in a trade or order book to its market `condition_id`.
- Find the opposite outcome token for a token you already hold.
- Collect the `condition_id` needed to call market-level APIs from a list of token IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-by-token" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | Yes | The token ID to look up the parent market for |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
  "primary_token_id": "25659310…",
  "secondary_token_id": "32338220…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `condition_id` | Identifier of the parent market. It is a hex string starting with `0x`. |
| `primary_token_id` | Token ID of the market's first outcome token. |
| `secondary_token_id` | Token ID of the market's second outcome token. In the example it matches the requested `token_id`. |

### Notes

- The request needs only `token_id`. Token IDs are long numeric strings, so send them as strings.
- The response gives the two token IDs for the market. Whichever one you send, the other is also returned.
- Use the `condition_id` with [Polymarket Get CLOB market info](/apis/polymarket/clob-markets) to get more detail on the market.
- Pass a token ID to [Polymarket Get order book](/apis/polymarket/book) to see current bids and asks for that outcome.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/markets-by-token.json`](../../../catalog/models/polymarket/markets-by-token.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-by-token
