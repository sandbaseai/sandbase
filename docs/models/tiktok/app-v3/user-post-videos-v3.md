# TikTok User Homepage Videos (V3) API: pricing, parameters and code examples

`tiktok/app-v3/user-post-videos-v3` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns simplified video data from a TikTok user homepage feed. Supports sorting by latest or hot posts and filtering by username or user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-post-videos-v3"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-post-videos-v3', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-post-videos-v3", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-post-videos-v3", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-post-videos-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number default `20` |
| `sort_type` | integer |  | Sort type, 0-Latest, 1-Hot default `0` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. default `""` |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. default `0` |
| `sec_user_id` | string |  | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. default `""` |

## Details

Returns a list of videos from a TikTok user's profile feed. The input is either a `sec_user_id` or a `unique_id` (the username). You can sort by latest or hot posts.

### Use cases

- Pull the newest posts from a brand account to track what it publishes.
- Sort a creator's feed by hot posts to find their best-performing videos.
- Read video captions and tagged accounts from a profile to audit its content.
- Page through a full profile feed to build a video archive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-post-videos-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Maximum count number |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |
| `sec_user_id` | string | No | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. |
| `sort_type` | integer | No | Sort type, 0-Latest, 1-Hot |
| `unique_id` | string | No | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "added_sound_music_info": {
        "album": "",
        "allow_offline_music_to_detail_page": false,
        "artists": [],
        "audition_duration": 43,
        "author": "TikTok",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "height": 720,
          "uri": "tos-maliva-avt-0068/ba67b11de451691939223e9d978e613a",
          "url_list": [
            "https://p19-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…"
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
        "accept_private_policy": false,
        "account_labels": null,
        "account_region": "",
        "ad_cover_url": null,
        "advance_feature_item_order": null,
        "advanced_feature_info": null,
        "apple_account": 0,
        "authority_status": 0
      },
      "author_user_id": 107955,
      "aweme_acl": {
        "download_general": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "download_mask_panel": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "platform_list": null,
        "press_action_list": null,
        "share_action_list": null,
        "share_general": {
          "code": 0,
          "mute": false,
          "show_type": 2,
          "transcode": 3
        },
        "share_list_status": 0
      },
      "aweme_id": "7702947070604332319",
      "aweme_type": 0,
      "banners": null
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103154401564FA481B424FA041A11",
    "now": 1793691841000
  },
  "has_locate_item": false,
  "has_more": 1,
  "lite_filter_reasons": "{}",
  "log_pb": {
    "impr_id": "20261103154401564FA481B424FA041A11"
  },
  "max_cursor": 1787847286366,
  "min_cursor": 1793482137319,
  "status_code": 0,
  "status_msg": "",
  "version": "v3"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | The list of videos on the user's feed. Each item is one video. |
| `aweme_list[].aweme_id` | The ID of the video, as a string. |
| `aweme_list[].desc` | The caption text of the video. |
| `aweme_list[].create_time` | The time the video was posted. The value is a Unix timestamp in seconds. |
| `aweme_list[].desc_language` | The language code of the caption, for example `en`. |
| `aweme_list[].content_type` | The type of content, for example `video`. |
| `aweme_list[].author_user_id` | The numeric ID of the account that posted the video. |
| `aweme_list[].content_desc_extra[].sec_uid / aweme_list[].content_desc_extra[].user_id` | The `sec_uid` and `user_id` of an account tagged in the caption. |
| `aweme_list[].content_desc_extra[].start / aweme_list[].content_desc_extra[].end` | The start and end position of the tag in the caption text. |
| `aweme_list[].aigc_info.created_by_ai` | Shows whether the video is marked as created by AI. |

### Notes

- Pass `sec_user_id` when you have it. If it is empty, the API uses `unique_id` instead.
- Set `sort_type` to `0` for latest posts or `1` for hot posts. Use `count` to set the maximum number of videos.
- For the next page, send the `max_cursor` value from the previous response. The first page uses `0`.
- To find a `sec_user_id` from a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-post-videos-v3.json`](../../../../catalog/models/tiktok/app-v3/user-post-videos-v3.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-post-videos-v3
