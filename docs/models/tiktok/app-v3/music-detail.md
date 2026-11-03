# TikTok Music Details API: pricing, parameters and code examples

`tiktok/app-v3/music-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed track information for a specific audio track on TikTok using its identifier, including connected DSP song mappings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-detail", "music_id": "6943027371519772674"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-detail', {'music_id': '6943027371519772674'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-detail", {
  "music_id": "6943027371519772674"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-detail", sandbase.Params{
	"music_id": "6943027371519772674",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `music_id` | string | yes | Music id  |

## Details

Returns details for one TikTok audio track, including title, artist, album, duration, cover images and the matched full-length song. It needs one input, `music_id`, the TikTok identifier of the track.

### Use cases

- Read the title, artist and album of a sound that appears in a TikTok video.
- Check whether a track is a licensed catalog song (`is_pgc`) or an original sound (`is_original_sound`).
- Get the chorus start time and full song length of the matched song to pick a clip segment.
- Download artist avatar and cover image URLs to show a track card in your own app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "6943027371519772674"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ai_recommend_music": null,
  "ai_recommend_video": null,
  "behind_the_song_exist": false,
  "cost_time_info": {
    "music_server_cost_time": 243
  },
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074355EBF9DC594D9008405170",
    "now": 1793691836000
  },
  "log_pb": {
    "impr_id": "20261103074355EBF9DC594D9008405170"
  },
  "msg": "success",
  "music_chart_rank": {
    "chart_music_info": "{\"currentTabId\":0,\"tabList\":[{\"tabId\":0,\"tabNameKey\":\"music_chart_top_50_title\",…",
    "desc": "Music Charts",
    "link_style": {
      "bg_end_color": 12881901,
      "bg_start_color": 9405693
    }
  },
  "music_info": {
    "album": "Minecraft - Volume Alpha",
    "allow_offline_music_to_detail_page": false,
    "artists": [
      {
        "avatar": {
          "uri": "tos-maliva-avt-0068/e9a5867e4f1c3c626f99bfe5ddecf9b9",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/e9a5867e4f1c3c626f9…"
          ],
          "url_prefix": null
        },
        "enter_type": 2,
        "follow_status": 0,
        "follower_status": 0,
        "handle": "c418",
        "is_block": false,
        "is_blocked": false,
        "is_private_account": false,
        "is_verified": true,
        "is_visible": false,
        "nick_name": "C418",
        "sec_uid": "MS4wLjABAAAAxrKNI-I7Qvhqi72NG5QIP9o3LUpcy5rW4JqvEcb_Ajd68cn89E_XMABNYa2mrdUf"
      }
    ],
    "audition_duration": 60,
    "author": "C418",
    "author_deleted": false,
    "author_position": null,
    "avatar_medium": {
      "height": 720,
      "uri": "tos-maliva-avt-0068/e9a5867e4f1c3c626f99bfe5ddecf9b9",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/e9a5867e4f1c3c626f9…"
      ],
      "url_prefix": null,
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "tos-maliva-avt-0068/e9a5867e4f1c3c626f99bfe5ddecf9b9",
      "url_list": [
        "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/e9a5867e4f1c3c626f9…"
      ],
      "url_prefix": null,
      "width": 720
    },
    "binded_challenge_id": 0,
    "can_be_stitched": true,
    "can_not_reuse": false
  },
  "rec_list": [],
  "similar_music": [],
  "similar_music_ids": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music_info.id_str` | The track ID as a string. Use this form to avoid number rounding in some JSON parsers. |
| `music_info.author / music_info.album` | The artist name and album name shown for the track. |
| `music_info.duration / music_info.audition_duration` | Length of the track and of its preview, as whole numbers. Both are 60 in this response. |
| `music_info.create_time` | Unix timestamp in seconds for when the track was created on TikTok. |
| `music_info.artists[].nick_name / music_info.artists[].handle` | Display name and handle of each artist account linked to the track. |
| `music_info.artists[].is_verified` | Whether the artist account is verified. |
| `music_info.is_pgc / music_info.is_original_sound / music_info.is_commerce_music` | Flags for how the track is classified: catalog track, user-made original sound, or commercial music. |
| `music_info.matched_song.title` | Title of the full song that TikTok matched to this audio track. |
| `music_info.matched_song.full_duration` | Length of the full matched song. The value 186250 matches the millisecond fields beside it. |
| `music_info.matched_song.chorus_info.start_ms / music_info.matched_song.chorus_info.duration_ms` | Where the chorus starts and how long it lasts, in milliseconds. |
| `music_info.cover_large.url_list[]` | Cover image URLs for the track at 720x720. |

### Notes

- Take `music_id` from a video's music data, or from [TikTok Music Search](/apis/tiktok/app-v3/music-search-result).
- Call [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list) next to see videos that use the track.
- `music_info.extra` and `music_chart_rank.chart_music_info` are JSON strings. Parse them again to read their contents.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-detail.json`](../../../../catalog/models/tiktok/app-v3/music-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-detail
