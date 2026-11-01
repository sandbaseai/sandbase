# TikTok Broadcast Danmaku

`tiktok/web/live-room` · api · TikTok

Returns danmaku and chat messages from a TikTok livestream room based on the provided room URL and message type.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-room", "danmaku_type": "<danmaku_type>", "live_room_url": "<live_room_url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-room', {'danmaku_type': '<danmaku_type>', 'live_room_url': '<live_room_url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-room", {
  "danmaku_type": "<danmaku_type>",
  "live_room_url": "<live_room_url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-room", sandbase.Params{
	"danmaku_type": "<danmaku_type>",
	"live_room_url": "<live_room_url>",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-room` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `danmaku_type` | string | yes | Message type  |
| `live_room_url` | string | yes | Live room link  |

## Details

Retrieve real-time stream messages by providing the broadcast link via `live_room_url` along with the desired `danmaku_type`.

### Use cases

- Monitor audience chat messages during a TikTok stream.
- Extract broadcast interaction data for engagement analysis.
- Collect stream danmaku logs filtered by message type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-room" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"danmaku_type": "<danmaku_type>", "live_room_url": "<live_room_url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `danmaku_type` | string | Yes | Message type |
| `live_room_url` | string | Yes | Live room link |

### Notes

- Requires `live_room_url` to identify the target TikTok stream.
- Filter the category of returned stream messages with `danmaku_type`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-room.json`](../../../../catalog/models/tiktok/web/live-room.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-room
