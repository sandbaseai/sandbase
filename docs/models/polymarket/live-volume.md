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

Live taker volume for an event by event ID, in total and per market.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/live-volume" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"event_id": "1262243"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `event_id` | string | Yes | Event id(s), comma-separated (at most 20 distinct values). Required. `event_id` is the unified key across v2 (same as the feeds); `id` and `eventId` are accepted aliases. |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/live-volume.json`](../../../catalog/models/polymarket/live-volume.json) · Store page: https://www.sandbase.ai/model/polymarket/live-volume
