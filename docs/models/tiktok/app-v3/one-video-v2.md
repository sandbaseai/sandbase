# TikTok Single Video Details (V2) API: pricing, parameters and code examples

`tiktok/app-v3/one-video-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed post information and comment configuration for a specific TikTok video using its unique post identifier. Provide the video ID to retrieve item metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/one-video-v2", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/one-video-v2', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/one-video-v2", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/one-video-v2", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Returns the details of one TikTok video, including its author, attached sound and comment panel settings. It needs one input: the video ID in `aweme_id`.

### Use cases

- Read the comment panel settings of a video, such as the quick comment flag and the recommended emojis.
- Identify the author of a video from `aweme_detail.author_user_id` and the `author` object.
- Check whether a video is marked as AI generated with `aweme_detail.aigc_info`.
- Read the sound attached to a video, including its duration, original sound flag and commerce rights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "added_sound_music_info": {
      "album": "",
      "allow_offline_music_to_detail_page": false,
      "artists": [],
      "audition_duration": 5,
      "author": "Jenn Melon",
      "author_deleted": false,
      "author_position": null,
      "avatar_medium": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_thumb": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "binded_challenge_id": 0,
      "can_be_stitched": true,
      "can_not_reuse": false
    },
    "ai_remix_info": {
      "has_entrance": false
    },
    "aigc_info": {
      "aigc_label_type": 0,
      "created_by_ai": false
    },
    "allow_gift": true,
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
      "authority_status": 0,
      "avatar_168x168": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_300x300": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_larger": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_medium": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/d988982c34fc5be0875f117fa25fd40c",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d988982c34fc5be…"
        ],
        "url_prefix": null,
        "width": 720
      }
    },
    "author_user_id": 6617578271134646277,
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
    "aweme_id": "7350810998023949599",
    "aweme_type": 0
  },
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074357AFA25E9E91A736029A7E",
    "now": 1793691837000
  },
  "log_pb": {
    "impr_id": "20261103074357AFA25E9E91A736029A7E"
  },
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_detail.aweme_id` | The ID of the video, returned as a string. It matches the `aweme_id` you sent. |
| `aweme_detail.aweme_type` | A numeric type code for the post. This example returns `0`. |
| `aweme_detail.author_user_id` | The numeric ID of the user who posted the video. |
| `aweme_detail.author` | The profile object of the video author. It holds avatar images in several sizes, `follower_count` and comment and duet settings. |
| `aweme_detail.aigc_info.created_by_ai / aweme_detail.aigc_info.aigc_label_type` | Show whether the video is flagged as created by AI and which AI label type it carries. |
| `aweme_detail.added_sound_music_info.author / aweme_detail.added_sound_music_info.id_str` | The name of the sound's author and the string ID of the sound attached to the video. |
| `aweme_detail.added_sound_music_info.duration / aweme_detail.added_sound_music_info.create_time` | The sound length in seconds, and the sound creation time as a Unix timestamp in seconds. |
| `aweme_detail.added_sound_music_info.is_original_sound / aweme_detail.added_sound_music_info.is_commerce_music` | Flags that show if the sound is an original sound and if it is marked as commercial music. |
| `aweme_detail.comment_config.emoji_recommend_list[]` | Emojis suggested for comments on this video. Each row has `emoji`, `emoji_id` and a `score`. |
| `aweme_detail.comment_config.zero_comment_button_config.zero_comment_button_main_text` | The prompt text shown on the comment panel when the video has no comments. |

### Notes

- Take the video ID from the end of a TikTok video URL, or from `aweme_id` in other TikTok video list APIs.
- Several fields hold image objects with a `url_list`. Each list has more than one URL for the same image.
- To read the comments themselves, call [TikTok Video Comments (App V3)](/apis/tiktok/app-v3/video-comments).
- For other versions of this lookup, see [TikTok Video Details (V3)](/apis/tiktok/app-v3/one-video-v3) or [TikTok Video Details](/apis/tiktok/app-v3/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/one-video-v2.json`](../../../../catalog/models/tiktok/app-v3/one-video-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/one-video-v2
