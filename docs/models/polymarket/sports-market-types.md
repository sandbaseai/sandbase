# Polymarket Get valid sports market types API: pricing, parameters and code examples

`polymarket/sports-market-types` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get valid sports market types from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/sports-market-types"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/sports-market-types', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/sports-market-types", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/sports-market-types", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/sports-market-types` with the body above minus `model`.

## Details

Returns the list of valid sports market type strings on Polymarket. The call needs no input.

### Use cases

- Build a filter menu of sports market types for a Polymarket sports dashboard.
- Check that a market type string is valid before you use it in another query.
- Track which sports market types Polymarket adds or removes by saving the list on a schedule.
- Keep a reference table of market type names for a sports analytics pipeline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/sports-market-types" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/SportsMarketTypesResponse.json",
  "marketTypes": [
    "any_player_rampage"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `marketTypes` | List of valid sports market type names. Each item is a snake_case string such as `any_player_rampage`, `any_player_ultra_kill` or `anytime_touchdowns`. |
| `marketTypes[]` | One sports market type identifier. Use the exact string when you match or compare types. |

### Notes

- The request body is an empty JSON object `{}`. There are no parameters and no pagination.
- Call [Polymarket Get sports metadata information](/apis/polymarket/sports) for metadata about the sports themselves.
- Call [Polymarket List markets](/apis/polymarket/markets) to list markets on Polymarket.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/sports-market-types.json`](../../../catalog/models/polymarket/sports-market-types.json) · Store page: https://www.sandbase.ai/model/polymarket/sports-market-types
