# Polymarket Open Interest API: pricing, parameters and code examples

`polymarket/oi` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Open interest in USDC for one or more markets by condition ID.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/oi", "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/oi', {'condition': '0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/oi", {
  "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/oi", sandbase.Params{
	"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
})
```

Same call via the path form: `POST /v1/api/polymarket/oi` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `condition` | string | yes | Condition id(s), comma-separated (at most 20 distinct values). `condition` is the unified key across v2 (same as the feeds); `condition_id` / `conditionId` are accepted aliases. Omit for global open interest.  |

## Details

Returns the open interest in USDC for one or more Polymarket markets. You pass one or more condition IDs in `condition`, separated by commas.

### Use cases

- Track how much money is still committed to a market before deciding whether it is liquid enough to trade.
- Rank a set of markets by open interest to find the most active ones.
- Chart open interest for a market over time by calling the API on a schedule and storing the `value`.
- Compare open interest across up to 20 related markets in a single call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/oi" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition` | string | Yes | Condition id(s), comma-separated (at most 20 distinct values). `condition` is the unified key across v2 (same as the feeds); `condition_id` / `conditionId` are accepted aliases. Omit for global open interest. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "condition_id": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
      "value": 7708257.285468
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | List of results. Each row covers one condition ID. |
| `data[].condition_id` | The condition ID of the market. It matches the value you sent in `condition`. |
| `data[].value` | Open interest for that market in USDC, as a decimal number. |

### Notes

- Condition IDs are 0x-prefixed hex strings. Pass at most 20 distinct values, separated by commas.
- `condition_id` and `conditionId` work as aliases for `condition`.
- Get condition IDs from [Polymarket List markets](/apis/polymarket/markets) or [Polymarket Get market by slug](/apis/polymarket/markets-slug).
- Use [Polymarket Market Holders](/apis/polymarket/holders) to see who holds positions in the same market.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/oi.json`](../../../catalog/models/polymarket/oi.json) · Store page: https://www.sandbase.ai/model/polymarket/oi
