# TikTok User Videos (App V3) API: pricing, parameters and code examples

`tiktok/app-v3/user-post-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos posted on a TikTok user profile. Filter by account identifier, specify sorting order by latest or popular items, and paginate through results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-post-videos"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-post-videos', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-post-videos", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-post-videos", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number default `20` |
| `region` | string |  | Region, optional parameter, if not passed, the US region data will be used by default. After passing, the data of the corresponding country and region will be preferred, for example: US, GB, FR, JP, SG, VN, etc. default `""` |
| `sort_type` | integer |  | Sort type, 0-Latest, 1-Hot default `0` |
| `unique_id` | string |  | User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. default `""` |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. default `0` |
| `sec_user_id` | string |  | User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. default `""` |

## Details

Returns a list of videos posted on a TikTok user profile. You pass the account's `sec_user_id`, or its `unique_id` (the username), and the API returns each video under `aweme_list`.

### Use cases

- Build a catalog of a creator's recent posts with their video IDs and post times.
- Find which collaborators appear on a creator's videos through `collab_info`.
- Check which videos carry an AI-generated label with `aigc_info`.
- Pull a creator's most popular videos by setting `sort_type` to `1`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM", "region": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Maximum count number |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |
| `region` | string | No | Region, optional parameter, if not passed, the US region data will be used by default. After passing, the data of the corresponding country and region will be preferred, for example: US, GB, FR, JP, SG, VN, etc. |
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
          "data_size": 0,
          "height": 720,
          "uri": "tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…"
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
      "banners": [
        {
          "key": {
            "component_key": "bottom_banner_search_rs"
          }
        }
      ]
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110307440751E2AC0A7755494ACB67",
    "now": 1793691847000
  },
  "has_locate_item": false,
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110307440751E2AC0A7755494ACB67"
  },
  "max_cursor": 1790367198527,
  "min_cursor": 1793482136132,
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | One video per item. The list holds the videos on the requested page. |
| `aweme_list[].aweme_id` | ID of the video, as a string. |
| `aweme_list[].create_time` | Time the video was posted. The value is a Unix timestamp in seconds. |
| `aweme_list[].content_type` | Kind of post. The sample value is `video`. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].added_sound_music_info.author` | Name of the author of the sound added to the video. |
| `aweme_list[].collab_info.collaborators[].user_info` | Profile data for each collaborator on the video, such as the avatar in `avatar_thumb`. |
| `aweme_list[].collab_info.collaborators[].collab_status` | Status code of the collaboration. The response does not say what each code means. |
| `aweme_list[].aigc_info.created_by_ai` | Whether the video is flagged as created by AI. `aigc_label_type` holds the label type. |
| `aweme_list[].comment_config.emoji_recommend_list[].emoji` | Emoji suggested for comments on this video, with a `score` for each. |

### Notes

- Send either `sec_user_id` or `unique_id`. If both are given, `sec_user_id` is used first.
- For the next page, pass the `max_cursor` value from the previous response. The first page uses `0`.
- Use `sort_type` `0` for latest videos and `1` for hot videos.
- To get a `sec_user_id` from a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-post-videos.json`](../../../../catalog/models/tiktok/app-v3/user-post-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-post-videos
