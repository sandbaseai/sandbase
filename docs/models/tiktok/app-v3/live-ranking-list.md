# TikTok Stream Audience Ranking List API: pricing, parameters and code examples

`tiktok/app-v3/live-ranking-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the audience ranking list for a stream room based on the specified room identifier and anchor identifier. Helps inspect top viewer participation.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-ranking-list", "anchor_id": "7222941468722758702", "room_id": "7358603858249009962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-ranking-list', {'anchor_id': '7222941468722758702', 'room_id': '7358603858249009962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-ranking-list", {
  "anchor_id": "7222941468722758702",
  "room_id": "7358603858249009962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-ranking-list", sandbase.Params{
	"anchor_id": "7222941468722758702",
	"room_id": "7358603858249009962",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-ranking-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |
| `anchor_id` | string | yes | Anchor id  |

## Details

Look up audience rankings for a broadcast by supplying the target `room_id` and `anchor_id`.

### Use cases

- Analyze audience leaderboard rankings during a stream.
- Identify top contributing viewers for a specific anchor.
- Track audience engagement patterns across stream sessions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-ranking-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"anchor_id": "7222941468722758702", "room_id": "7358603858249009962"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |
| `anchor_id` | string | Yes | Anchor id |

### Notes

- Requires both `room_id` and `anchor_id` to look up room rankings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-ranking-list.json`](../../../../catalog/models/tiktok/app-v3/live-ranking-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-ranking-list
