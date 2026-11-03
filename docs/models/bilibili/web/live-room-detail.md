# Bilibili Live Room Details API: pricing, parameters and code examples

`bilibili/web/live-room-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata and status information for a specified Bilibili live broadcast room based on the provided room identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/live-room-detail", "room_id": "22816111"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/live-room-detail', {'room_id': '22816111'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/live-room-detail", {
  "room_id": "22816111"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/live-room-detail", sandbase.Params{
	"room_id": "22816111",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/live-room-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room ID  |

## Details

Returns metadata and status for one Bilibili live room, including its title, streamer ID, area, cover image and live status. It needs a single input, the `room_id` of the live room.

### Use cases

- Check whether a Bilibili live room is currently broadcasting by reading `data.live_status`.
- Show a room's title, cover image and category in an external dashboard.
- Find the streamer's `uid` for a room, then look up that user's profile.
- Group tracked rooms by `data.parent_area_name` and `data.area_name`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/live-room-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "22816111"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "allow_change_area_time": 0,
    "allow_upload_cover_time": 0,
    "area_id": 745,
    "area_name": "虚拟Gamer",
    "area_pendants": "",
    "attention": 892815,
    "background": "https://i0.hdslb.com/bfs/live/room_bg/c4eed3ef37ef4cd30bbcac7491a7ed9ac78e1459.j…",
    "battle_id": 0,
    "description": "",
    "hot_words": [
      "2333333"
    ],
    "hot_words_status": 0,
    "is_anchor": 0
  },
  "message": "ok",
  "msg": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.room_id / data.short_id` | The numeric room ID. `short_id` is the short room ID, and `0` means no short ID is set for this room. |
| `data.uid` | The user ID of the room owner. |
| `data.title` | The current title of the live room. |
| `data.live_status` | The broadcast state code of the room. This sample returns `2`, with `online` at `0` and `live_time` at `0000-00-00 00:00:00`. |
| `data.live_time` | The start time of the current broadcast as a `YYYY-MM-DD HH:MM:SS` string. The value `0000-00-00 00:00:00` appears when no start time is set. |
| `data.parent_area_id / data.parent_area_name` | The ID and name of the top-level category the room belongs to. |
| `data.area_id / data.area_name` | The ID and name of the sub-category the room belongs to. |
| `data.attention` | The follower count for the room, as shown in this response (`892815`). |
| `data.user_cover / data.background / data.keyframe` | Image URLs for the room cover and the room background. `keyframe` is an empty string in this sample. |
| `data.hot_words[]` | A list of preset hot words (quick chat phrases) for the room. |

### Notes

- `room_id` is passed as a string, for example `"22816111"`. The response returns `data.room_id` as a number.
- Use `data.uid` from this response as the input to a user API such as [Bilibili User Profile](/apis/bilibili/web/user-profile).
- Use `data.area_id` and `data.parent_area_id` with [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas) to match the IDs to the full list of categories.
- For stream data of a room, call [Bilibili Room Stream Data](/apis/bilibili/web/live-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/live-room-detail.json`](../../../../catalog/models/bilibili/web/live-room-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/live-room-detail
