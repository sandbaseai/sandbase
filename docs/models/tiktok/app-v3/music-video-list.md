# TikTok Music Video List API: pricing, parameters and code examples

`tiktok/app-v3/music-video-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a paginated list of videos associated with a specific TikTok audio track. Filter results by music ID and control pagination using cursor values.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of TikTok videos that use a given audio track. Each item in `aweme_list` holds the video ID, caption, creation time, content type, author, and details about the sound. The only required input is `music_id`.

### Use cases

- List the videos posted with a specific sound to see how creators use it.
- Collect video IDs for a sound and pass them to a video details API to read full stats.
- Check which hashtags appear most often in captions of videos that use a track.
- Find the accounts that post with a given song and review their profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "6943027371519772674"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "added_sound_music_info": {
        "album": "Minecraft - Volume Alpha",
        "allow_offline_music_to_detail_page": false,
        "artists": [
          {
            "avatar": {
              "uri": "tos-maliva-avt-0068/e9a5867e4f1c3c626f99bfe5ddecf9b9",
              "url_list": [
                "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/e9a5867e4f1c3c626f9…"
              ],
              "url_prefix": null
            },
            "enter_type": 2,
            "follow_status": 0,
            "follower_status": 0,
            "handle": "c418",
            "is_block": false,
            "is_blocked": false,
            "is_private_account": false
          }
        ],
        "audition_duration": 60,
        "author": "C418",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-maliva-avt-0068/e9a5867e4f1c3c626f99bfe5ddecf9b9",
          "url_list": [
            "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/e9a5867e4f1c3c626f9…"
          ],
          "url_prefix": null,
          "width": 720
        }
      },
      "ai_remix_info": {
        "has_entrance": false
      },
      "aigc_info": {
        "aigc_label_type": 0,
        "created_by_ai": false
      },
      "anchors": null,
      "anchors_extras": "",
      "animated_image_info": {
        "effect": 0,
        "type": 0
      },
      "author": {
        "ad_cover_url": null,
        "authority_status": 0,
        "avatar_168x168": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast8-avt-0068-tx2/d940dd5caf8453dceba50b7ed24de018",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/d940dd5caf8453…"
          ],
          "url_prefix": null,
          "width": 720
        },
        "avatar_300x300": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast8-avt-0068-tx2/d940dd5caf8453dceba50b7ed24de018",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/d940dd5caf8453…"
          ],
          "url_prefix": null,
          "width": 720
        },
        "avatar_larger": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast8-avt-0068-tx2/d940dd5caf8453dceba50b7ed24de018",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/d940dd5caf8453…"
          ],
          "url_prefix": null,
          "width": 720
        },
        "avatar_medium": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast8-avt-0068-tx2/d940dd5caf8453dceba50b7ed24de018",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/d940dd5caf8453…"
          ],
          "url_prefix": null,
          "width": 720
        },
        "avatar_thumb": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast8-avt-0068-tx2/d940dd5caf8453dceba50b7ed24de018",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/d940dd5caf8453…"
          ],
          "url_prefix": null,
          "width": 720
        },
        "cha_list": null
      },
      "author_user_id": 7491661076202816558,
      "aweme_acl": {
        "download_general": {
          "code": 0,
          "extra": "#",
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "download_mask_panel": {
          "code": 0,
          "extra": "#",
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "platform_list": null,
        "press_action_list": null,
        "share_action_list": [
          {
            "action_id": "create_sticker",
            "code": 1,
            "extra": "216",
            "show_type": 1,
            "toast_msg": "Create sticker isn’t available for this video"
          }
        ],
        "share_general": {
          "code": 0,
          "extra": "#",
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "share_list_status": 0
      },
      "aweme_id": "7582341697078562079",
      "aweme_type": 150,
      "banners": [
        {
          "key": {
            "component_key": "bottom_banner_search_rs"
          }
        }
      ]
    }
  ],
  "can_pin_video": false,
  "cursor": 12,
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030743571E3E334FDA8FA102C913",
    "now": 1793691837000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611030743571E3E334FDA8FA102C913"
  },
  "need_lazy_loading": false,
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[].aweme_id` | ID of the video, as a string. Use it to look up the video in other video APIs. |
| `aweme_list[].desc` | Caption of the video, including its hashtags. |
| `aweme_list[].create_time` | Time the video was posted. The value looks like a Unix timestamp in seconds. |
| `aweme_list[].content_type` | Kind of post, for example `multi_photo` for a photo post or `video` for a regular video. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_thumb.url_list` | Image links for the poster's avatar. The `avatar_168x168`, `avatar_300x300`, `avatar_medium` and `avatar_larger` fields hold other sizes of the same image. |
| `aweme_list[].added_sound_music_info.author` | Name of the artist credited for the sound, for example `C418`. |
| `aweme_list[].added_sound_music_info.album` | Album name of the sound, when TikTok has one. |
| `aweme_list[].cha_list[].cha_name / aweme_list[].cha_list[].cid` | Name and ID of each hashtag attached to the video. |

### Notes

- Get `music_id` from a music search or music detail call, for example [TikTok Music Search](/apis/tiktok/app-v3/music-search-result) or [TikTok Music Details](/apis/tiktok/app-v3/music-detail).
- Send `cursor` as `0` for the first page. For the next page, send the cursor value from the previous response. Use `count` to set how many videos come back per page.
- Pass an `aweme_id` to [TikTok Video Details](/apis/tiktok/app-v3/one-video) to get the full record for one video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-video-list.json`](../../../../catalog/models/tiktok/app-v3/music-video-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-video-list
