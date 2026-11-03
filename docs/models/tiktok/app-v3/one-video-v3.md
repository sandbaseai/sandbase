# TikTok Video Details (V3) API: pricing, parameters and code examples

`tiktok/app-v3/one-video-v3` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive details for a single TikTok video based on its video ID and optional country code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/one-video-v3", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/one-video-v3', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/one-video-v3", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/one-video-v3", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/one-video-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Country code, default is US, supports ISO 3166-1 alpha-2 country codes, such as: US, GB, FR, DE, IN, JP, etc. default `"US"` |
| `aweme_id` | string | yes | Video id  |

## Details

Returns the details of one TikTok video, including its author, sound, AI labels and comment settings. It needs the video ID in `aweme_id` and takes an optional `region` country code.

### Use cases

- Read the author and sound attached to a single TikTok post.
- Check whether a video carries an AI-generated label with `aigc_info`.
- Look up the comment panel settings and suggested emojis for one video.
- Pull the sound used in a video and see if it is cleared for commercial use.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/one-video-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `region` | string | No | Country code, default is US, supports ISO 3166-1 alpha-2 country codes, such as: US, GB, FR, DE, IN, JP, etc. |

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
    "logid": "2026110307435791E97A580FD56B02BC26",
    "now": 1793691837000
  },
  "log_pb": {
    "impr_id": "2026110307435791E97A580FD56B02BC26"
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
| `aweme_detail.author_user_id` | The numeric ID of the account that posted the video. |
| `aweme_detail.author.avatar_larger / avatar_medium / avatar_thumb` | Author profile picture in several sizes. Each has `url_list` with image links, plus `width` and `height`. |
| `aweme_detail.author.follower_count / aweme_count / favoriting_count` | Counters on the author object. They return `0` in this response, so check them before relying on them. |
| `aweme_detail.aigc_info.created_by_ai / aigc_label_type` | Shows whether the video is marked as made with AI. `created_by_ai` is a boolean. |
| `aweme_detail.added_sound_music_info.author` | Name of the creator of the sound used in the video. |
| `aweme_detail.added_sound_music_info.id_str` | The ID of the sound as a string. |
| `aweme_detail.added_sound_music_info.is_original_sound / is_commerce_music / has_commerce_right` | Flags that show whether the sound is an original sound and whether it has commercial rights. |
| `aweme_detail.added_sound_music_info.duration_high_precision.duration_precision` | Sound length with decimals, for example `5.904`. |
| `aweme_detail.comment_config.emoji_recommend_list[].emoji / score` | Emojis suggested for comments on this video, each with a `score`. Higher scores rank first. |

### Notes

- `aweme_id` is the numeric ID of the video, for example `7350810998023949599`. It is the long number at the end of a TikTok video link.
- The response is large and holds many display and configuration fields. Read the fields you need under `aweme_detail`.
- To read the comments on the video, call [TikTok Video Comments (App V3)](/apis/tiktok/app-v3/video-comments).
- To fetch several videos in one call, use [TikTok Batch Video Info (App V3)](/apis/tiktok/app-v3/multi-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/one-video-v3.json`](../../../../catalog/models/tiktok/app-v3/one-video-v3.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/one-video-v3
