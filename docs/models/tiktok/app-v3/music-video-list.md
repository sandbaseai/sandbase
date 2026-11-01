# TikTok Music Video List

`tiktok/app-v3/music-video-list` · api · TikTok

Retrieves a paginated list of videos associated with a specific TikTok audio track. Filter results by music ID and control pagination using cursor values.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-video-list", "music_id": "6943027371519772674"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-video-list', {'music_id': '6943027371519772674'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-video-list", {
  "music_id": "6943027371519772674"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-video-list", sandbase.Params{
	"music_id": "6943027371519772674",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `10` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `music_id` | string | yes | Music id  |

## Details

Access TikTok videos that use a designated sound track by providing `music_id`. Supports pagination via `cursor` and custom result limits via `count`.

### Use cases

- Discover popular videos utilizing a specific trending sound track.
- Track the reach and viral adoption of an original audio track on TikTok.
- Analyze community engagement and video styles linked to a designated sound.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "6943027371519772674"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "author_user_id": 7423628028584756270,
      "aweme_id": "7578277641086651678",
      "aweme_type": 0,
      "bodydance_score": 0,
      "content_desc": "[\"cat\",\"#fyp #catsoftiktok #catcontent #rigbycat #rigbycat \"]",
      "content_original_type": 1,
      "content_size_type": 1,
      "content_type": "video",
      "create_time": 1764455286,
      "desc": "cat #fyp #catsoftiktok #catcontent #rigbycat #rigbycat",
      "added_sound_music_info": {
        "audition_duration": 60,
        "author": "C418",
        "author_deleted": false,
        "binded_challenge_id": 0,
        "commercial_right_type": 3,
        "create_time": 1616549537
      },
      "aigc_info": {
        "aigc_label_type": 0
      },
      "animated_image_info": {
        "type": 0
      },
      "author": {
        "authority_status": 0,
        "comment_filter_status": 0,
        "follow_status": 0,
        "follower_status": 0,
        "friends_status": 0,
        "nickname": "<user>"
      }
    }
  ]
}
```

### Notes

- `music_id` is required to specify the audio track.
- Use `cursor` for pagination, passing 0 for the first page and the returned cursor value for subsequent pages.
- `count` sets the number of videos returned per request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-video-list.json`](../../../../catalog/models/tiktok/app-v3/music-video-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-video-list
