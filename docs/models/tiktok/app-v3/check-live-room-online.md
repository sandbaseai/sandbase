# TikTok LIVE Status API: pricing, parameters and code examples

`tiktok/app-v3/check-live-room-online` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Check whether a TikTok LIVE room is currently live by room ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/check-live-room-online", "room_id": "7358603858249009962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/check-live-room-online', {'room_id': '7358603858249009962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/check-live-room-online", {
  "room_id": "7358603858249009962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/check-live-room-online", sandbase.Params{
	"room_id": "7358603858249009962",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/check-live-room-online` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |

## Details

Check whether a TikTok LIVE room is broadcasting right now. Pass the `room_id`; the answer says `alive: true` while the creator is live.

### Use cases

- Alert when a tracked creator goes live.
- Skip live-comment or gift collection for rooms that are offline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/check-live-room-online" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7358603858249009962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "alive": false,
      "room_id": 7358603858249009962,
      "room_id_str": "7358603858249009962"
    }
  ],
  "extra": {
    "now": 1793676899476
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].alive` | `true` if the room is live now. |
| `data[].room_id_str` | The room ID as a string. |

### Notes

- A creator gets a new `room_id` for each broadcast. Get the current one from a live link with [TikTok Live Room ID](/apis/tiktok/web/live-room-id).

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/apis/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.
- [TikTok Search](/apis/tiktok/app-v3/general-search-result): Search TikTok by keyword across videos and users (Top tab).

---
Machine-readable: [`catalog/models/tiktok/app-v3/check-live-room-online.json`](../../../../catalog/models/tiktok/app-v3/check-live-room-online.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/check-live-room-online
