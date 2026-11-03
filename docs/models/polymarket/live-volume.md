# Polymarket Live Event Volume API: pricing, parameters and code examples

`polymarket/live-volume` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Live taker volume for an event by event ID, in total and per market.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/live-volume", "event_id": "1262243"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/live-volume', {'event_id': '1262243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/live-volume", {
  "event_id": "1262243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/live-volume", sandbase.Params{
	"event_id": "1262243",
})
```

Same call via the path form: `POST /v1/api/polymarket/live-volume` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `event_id` | string | yes | Event id(s), comma-separated (at most 20 distinct values). Required. `event_id` is the unified key across v2 (same as the feeds); `id` and `eventId` are accepted aliases.  |

## Details

Returns the live taker volume for one or more Polymarket events. The response gives a total for the event and a volume figure for each market (condition) inside it. The only input is `event_id`.

### Use cases

- Track how much trading activity an event has attracted in total.
- Rank the markets inside an event by `taker_volume` to find where trading is concentrated.
- Compare several events side by side by sending up to 20 event IDs in one call.
- Add a volume figure to a dashboard that already lists Polymarket events.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/live-volume" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"event_id": "1262243"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `event_id` | string | Yes | Event id(s), comma-separated (at most 20 distinct values). Required. `event_id` is the unified key across v2 (same as the feeds); `id` and `eventId` are accepted aliases. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "conditions": [
      {
        "condition_id": "0xa32317ba83c3c83dc43ef260c3744c22ed8000db53d30bc09372c45cff5fb07a",
        "taker_volume": 5836737.706408
      }
    ],
    "taker_volume_total": 61577729.177805
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.taker_volume_total` | Total taker volume for the event, summed across its markets. |
| `data.conditions[]` | One entry per market (condition) in the event. |
| `data.conditions[].condition_id` | Identifier of the market condition. It is a hex string that starts with `0x`. |
| `data.conditions[].taker_volume` | Taker volume for that single market. |

### Notes

- `event_id` accepts several IDs separated by commas, with at most 20 distinct values. `id` and `eventId` work as aliases.
- To find an event ID, call [Polymarket List events](/apis/polymarket/events) or [Polymarket Get event by slug](/apis/polymarket/events-slug).
- To see details for an event, such as its markets and titles, call [Polymarket Get event by id](/apis/polymarket/events-by-id).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/live-volume.json`](../../../catalog/models/polymarket/live-volume.json) · Store page: https://www.sandbase.ai/model/polymarket/live-volume
