# TikTok Broadcast Danmaku API: pricing, parameters and code examples

`tiktok/web/live-room` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

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
  -d '{"model": "tiktok/web/live-room", "danmaku_type": "WebcastChatMessage", "live_room_url": "https://www.tiktok.com/@mpl.id.official/live"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-room', {'danmaku_type': 'WebcastChatMessage', 'live_room_url': 'https://www.tiktok.com/@mpl.id.official/live'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-room", {
  "danmaku_type": "WebcastChatMessage",
  "live_room_url": "https://www.tiktok.com/@mpl.id.official/live"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-room", sandbase.Params{
	"danmaku_type": "WebcastChatMessage",
	"live_room_url": "https://www.tiktok.com/@mpl.id.official/live",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-room` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `danmaku_type` | string | yes | Message type  |
| `live_room_url` | string | yes | Live room link  |

## Details

This endpoint is meant to return danmaku and chat messages from a TikTok livestream room. It takes a room URL in `live_room_url` and a message type in `danmaku_type`. The real response currently returns only a notice that the online service is no longer available.

### Use cases

- Check the current availability of this endpoint before you build a live chat pipeline on it.
- Read the `message_EN` text to see how to get the source code for local deployment.
- Switch to a related SandBase live room API when you need room messages or room status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-room" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"danmaku_type": "WebcastChatMessage", "live_room_url": "https://www.tiktok.com/@mpl.id.official/live"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `danmaku_type` | string | Yes | Message type |
| `live_room_url` | string | Yes | Live room link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "message_EN": "This interface is no longer available online, you need to purchase the source co…",
  "message_ZH": "该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discor…",
  "ws_url": "No longer available"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `message_EN` | English notice that the interface is no longer available online. It says you must buy the source code and deploy it locally. |
| `message_ZH` | Chinese version of the same notice. It also points to a Discord server where you can contact the administrator to buy the source code. |
| `ws_url` | Holds the text `No longer available` instead of a WebSocket address. |

### Notes

- The request needs `danmaku_type` (for example `WebcastChatMessage`) and `live_room_url` (for example `https://www.tiktok.com/@mpl.id.official/live`).
- The sample call returned no chat messages, only the notice fields shown above.
- To read room messages through SandBase, try [TikTok Room Danmaku Messages](/apis/tiktok/web/live-im-fetch).
- To check whether a room is live first, call [TikTok Stream Status Check](/apis/tiktok/web/check-live-alive).

### Pricing

$0.0015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-room.json`](../../../../catalog/models/tiktok/web/live-room.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-room
