# TikTok User Stream Detail API: pricing, parameters and code examples

`tiktok/web/user-live-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current broadcast information for a TikTok user based on their unique handle. Provides stream quality options and room playback data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-live-detail", "uniqueId": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-live-detail', {'uniqueId': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-live-detail", {
  "uniqueId": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-live-detail", sandbase.Params{
	"uniqueId": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-live-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uniqueId` | string | yes | User uniqueId  |

## Details

Returns the current live room details for a TikTok user, including the stream title, viewer counts, available playback qualities and basic profile data. It needs one input: the user's `uniqueId` handle, such as `tiktok`.

### Use cases

- Read the title, cover image and start time of a creator's current live room.
- List the playback quality options (`Original`, `1080p`, `720p`) offered for a live stream.
- Get the `roomId` of a user so you can pass it to other live room APIs.
- Pair a creator's follower count with their live viewer stats.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-live-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uniqueId": "tiktok"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uniqueId` | string | Yes | User uniqueId |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "liveRoom": {
      "coverUrl": "https://p16-webcast.tiktokcdn.com/webcast-va/2d40841fa55af281b3c825908f04ebc1.jp…",
      "gameTagId": 0,
      "hevcStreamData": {
        "pull_data": {
          "options": {
            "default_preview_quality": {
              "icon_type": 0,
              "level": 0,
              "name": "",
              "resolution": "",
              "sdk_key": "",
              "v_codec": ""
            },
            "default_quality": {
              "icon_type": 0,
              "level": 0,
              "name": "720p",
              "resolution": "",
              "sdk_key": "hd",
              "v_codec": ""
            },
            "forced_low_latency": false,
            "max_drm_lenient_size": "",
            "max_drm_lenient_size_backup": "",
            "qualities": [
              {
                "icon_type": 6,
                "level": 10,
                "name": "Original",
                "resolution": "",
                "sdk_key": "origin",
                "v_codec": ""
              }
            ],
            "show_quality_button": false,
            "support_low_latency": false
          },
          "stream_data": "{\"common\":{\"session_id\":\"173-202611031544314D3AD99C28275204E5E8\",\"room_id\":76936…"
        },
        "push_data": {
          "push_stream_level": 0,
          "resolution_params": {},
          "stream_data": ""
        }
      },
      "liveRoomMode": 1,
      "liveRoomStats": {
        "enterCount": 382959,
        "userCount": 1
      },
      "liveSubOnly": 0,
      "multiStreamScene": 0,
      "multiStreamSource": 0,
      "paidEvent": {
        "event_id": 0,
        "paid_type": 0
      },
      "squareCoverImg": "",
      "startTime": 1791323812,
      "status": 4
    },
    "stats": {
      "followerCount": 96545668,
      "followingCount": 1
    },
    "user": {
      "avatarLarger": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
      "avatarMedium": "https://p19-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
      "avatarThumb": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
      "followStatus": 0,
      "id": "107955",
      "nickname": "TikTok",
      "roomId": "7693676830666705678",
      "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
      "secret": false,
      "signature": "Your nex…",
      "status": 4,
      "uniqueId": "tiktok"
    }
  },
  "extra": {
    "id": "202611031544314D3AD99C28275204E5E8"
  },
  "message": "",
  "statusCode": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.liveRoom.title` | Title of the live room. |
| `data.liveRoom.coverUrl` | URL of the cover image for the live room. |
| `data.liveRoom.startTime` | Start time of the broadcast. The value looks like a Unix timestamp in seconds. |
| `data.liveRoom.status` | Numeric status code of the live room. The response does not explain what each value means. |
| `data.liveRoom.liveRoomStats.enterCount / data.liveRoom.liveRoomStats.userCount` | Viewer counts for the room. `enterCount` is the number of entries and `userCount` is the user count reported for the room. |
| `data.liveRoom.streamData.pull_data.options.qualities[].name / data.liveRoom.streamData.pull_data.options.qualities[].sdk_key` | Display name and key of each available quality level, such as `Original` with `origin`, or `720p` with `hd`. |
| `data.liveRoom.streamData.pull_data.options.default_quality.name` | Name of the default playback quality. |
| `data.liveRoom.streamData.pull_data.stream_data` | String that holds the stream session data. It starts with a `common` object that contains `session_id` and `room_id`. |
| `data.user.roomId` | ID of the user's live room, as a string. |
| `data.user.nickname / data.user.signature / data.user.verified` | Display name, bio text and verified flag of the account. |
| `data.stats.followerCount / data.stats.followingCount` | Number of followers and number of accounts the user follows. |

### Notes

- Pass the handle in `uniqueId` without the `@` sign. The example uses `tiktok`.
- `data.liveRoom.hevcStreamData` has the same structure as `data.liveRoom.streamData`.
- To check whether a room is active, call [TikTok Stream Status Check](/apis/tiktok/web/check-live-alive).
- For more details about a room, call [TikTok Stream Room Information](/apis/tiktok/web/live-data) with the room ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-live-detail.json`](../../../../catalog/models/tiktok/web/user-live-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-live-detail
