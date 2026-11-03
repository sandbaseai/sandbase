# TikTok User Music List API: pricing, parameters and code examples

`tiktok/app-v3/user-music-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of audio tracks associated with a specific TikTok user. Queries require the user's `sec_uid` with optional cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-music-list", "sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-music-list', {'sec_uid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-music-list", {
  "sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-music-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-music-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `10` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `sec_uid` | string | yes | User sec_uid  |

## Details

Returns a list of audio tracks linked to a TikTok user, with title, author, duration, cover images and matched song details. It needs the user's `sec_uid` and accepts `count` and `cursor` for paging.

### Use cases

- List the sounds a creator has posted or is credited on, to review their music catalog.
- Find the album name and credited artists behind a track a creator uses often.
- Check which tracks in a creator's list are commercial music and which are original sounds.
- Collect track IDs for a creator, then look up each sound in detail.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-music-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074400DD567830EC3BCE01CED8",
    "now": 1793691841000
  },
  "groups": null,
  "has_more": 1,
  "honor_label": 3,
  "log_pb": {
    "impr_id": "20261103074400DD567830EC3BCE01CED8"
  },
  "music": [
    {
      "album": "Chữ Vấn Chữ Vương (Huy PT Remix)",
      "allow_offline_music_to_detail_page": false,
      "artists": [
        {
          "avatar": {
            "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
            ],
            "url_prefix": null
          },
          "enter_type": 2,
          "follow_status": 0,
          "follower_status": 0,
          "handle": "tiktok",
          "is_block": false,
          "is_blocked": false,
          "is_private_account": false
        }
      ],
      "audition_duration": 60,
      "author": "Chân CaCa",
      "author_deleted": false,
      "author_position": null,
      "avatar_medium": {
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_thumb": {
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
        "url_list": [
          "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "binded_challenge_id": 0,
      "can_be_stitched": true,
      "can_not_reuse": false
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Value to send as `cursor` to get the next page. |
| `has_more` | Shows whether more tracks are available. The value `1` in this response means another page exists. |
| `music[].id / music[].id_str` | ID of the track. `id_str` holds the same value as a string, which is safer for large numbers. |
| `music[].album` | Album or release name shown for the track. |
| `music[].author` | Display name of the track's author or artists. |
| `music[].artists[].handle` | TikTok handle of each credited artist. |
| `music[].duration / music[].audition_duration` | Length values for the track, in whole numbers. Both are `60` in this response. |
| `music[].create_time` | Unix timestamp of when the sound was created. |
| `music[].is_original_sound / music[].is_commerce_music / music[].is_pgc` | Boolean flags that describe the type of sound. They show whether it is an original sound, commercial music, or marked as PGC. |
| `music[].matched_song.full_duration` | Duration of the full matched song. The first track shows `248861`, which fits milliseconds given the 60 second clip. |
| `music[].matched_song.chorus_info.start_ms / music[].matched_song.chorus_info.duration_ms` | Start time and length of the chorus section of the matched song, in milliseconds. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, send the `cursor` value from the previous response.
- Keep paging while `has_more` is `1`.
- Get a `sec_uid` from a username with [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- Use [TikTok Music Details](/apis/tiktok/app-v3/music-detail) to look up a single track, or [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list) to see videos that use it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-music-list.json`](../../../../catalog/models/tiktok/app-v3/user-music-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-music-list
