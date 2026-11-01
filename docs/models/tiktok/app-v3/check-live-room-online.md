# TikTok LIVE Status

`tiktok/app-v3/check-live-room-online` · api · TikTok

Check whether a TikTok LIVE room is currently live by room ID.

## Pricing

- **$0.0015 per call** (USD)
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

Pass a TikTok LIVE `room_id` and find out whether the stream is live right now.

### Use cases

- Trigger alerts when a creator goes live.
- Schedule live-stream data collection.
- Monitor competitors' live activity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/check-live-room-online" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7358603858249009962"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "alive": false,
      "room_id": 7358603858249009962,
      "room_id_str": "7358603858249009962"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/model/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.
- [TikTok Search](/model/tiktok/app-v3/general-search-result): Search TikTok by keyword across videos and users (Top tab).

---
Machine-readable: [`catalog/models/tiktok/app-v3/check-live-room-online.json`](../../../../catalog/models/tiktok/app-v3/check-live-room-online.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/check-live-room-online
