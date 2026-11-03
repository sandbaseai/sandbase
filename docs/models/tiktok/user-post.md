# TikTok User Published Posts API: pricing, parameters and code examples

`tiktok/user-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get posts published by a TikTok user identified by secUid, with cursor pagination and latest or popular sorting. Use it to browse a creator's posting history or continue through their public post feed.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/user-post", "secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/user-post', {'secUid': 'MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/user-post", {
  "secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/user-post", sandbase.Params{
	"secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk",
})
```

Same call via the path form: `POST /v1/api/tiktok/user-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sorting criteria for the user's posts. one of: `LATEST`, `MOST_POPULAR`; default `"LATEST"` |
| `cursor` | string |  | Pagination cursor. Use '0' for the first page, then use the max_cursor value returned in the previous response. default `"0"` |
| `secUid` | string | yes | The opaque security ID returned for the TikTok user.  |

## Details

Returns a page of posts published by a TikTok user. The input is the user's `secUid`, with optional `cursor` and `sort` (`LATEST` or `MOST_POPULAR`) parameters.

### Use cases

- Pull a creator's recent posts to track what they publish and when.
- Sort by `MOST_POPULAR` to find a creator's top-performing videos.
- Collect hashtags and sounds a creator uses across their posts.
- Page through a full public post history to build an archive of a creator's content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The opaque security ID returned for the TikTok user. |
| `cursor` | string | No | Pagination cursor. Use '0' for the first page, then use the max_cursor value returned in the previous response. |
| `sort` | string | No | Sorting criteria for the user's posts. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "added_sound_music_info": {
        "album": "Arrival",
        "allow_offline_music_to_detail_page": false,
        "artists": [
          {
            "avatar": {
              "uri": "tos-maliva-avt-0068/aafa706a21e5b32e79d08684f17ba2b5",
              "url_list": [
                "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/aafa706a21e5b32e79d…"
              ],
              "url_prefix": null
            },
            "enter_type": 2,
            "follow_status": 0,
            "follower_status": 0,
            "handle": "abba",
            "is_block": false,
            "is_blocked": false,
            "is_private_account": false
          }
        ],
        "audition_duration": 60,
        "author": "ABBA",
        "author_deleted": false,
        "author_position": null,
        "avatar_medium": {
          "data_size": 0,
          "height": 720,
          "uri": "tos-maliva-avt-0068/aafa706a21e5b32e79d08684f17ba2b5",
          "url_list": [
            "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/aafa706a21e5b32e79d…"
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
      "author_user_id": 52018348334530560,
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
      "aweme_id": "7703087341845384479",
      "aweme_type": 0,
      "banners": null
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074418A9DE0C887E3F124A2041",
    "now": 1793691858000
  },
  "has_locate_item": false,
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103074418A9DE0C887E3F124A2041"
  },
  "max_cursor": 1791845975050,
  "min_cursor": 1793514806165,
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | List of posts on this page. Each item is one post. |
| `aweme_list[].aweme_id` | ID of the post, as a string. Use it to look up the single post. |
| `aweme_list[].desc` | Caption text of the post, including hashtags. |
| `aweme_list[].create_time` | Time the post was created. The value is a 10-digit number, which looks like a Unix timestamp in seconds. |
| `aweme_list[].content_type` | Type of content, for example `video`. |
| `aweme_list[].cha_list[].cha_name / aweme_list[].cha_list[].cid` | Name and ID of each hashtag (challenge) attached to the post. |
| `aweme_list[].content_desc_extra[].hashtag_name` | Hashtag names found in the caption. `start` and `end` give the position of each tag in its caption line. |
| `aweme_list[].added_sound_music_info.author` | Name of the author of the sound used in the post. |
| `aweme_list[].added_sound_music_info.album` | Album name of the sound, which may be empty. |
| `aweme_list[].author_user_id` | Numeric ID of the user who published the post. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, pass the `max_cursor` value from the previous response.
- The `secUid` is the opaque ID returned for a TikTok user, for example by a user profile API.
- Post IDs in `aweme_id` are long numeric strings. Keep them as strings to avoid rounding.
- To get full details for a single post, call [TikTok Video Details](/apis/tiktok/app-v3/one-video).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/user-post.json`](../../../catalog/models/tiktok/user-post.json) · Store page: https://www.sandbase.ai/model/tiktok/user-post
