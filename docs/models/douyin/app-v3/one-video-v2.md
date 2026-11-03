# Douyin Single Video Data (App V3) API: pricing, parameters and code examples

`douyin/app-v3/one-video-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin item, including video and photo posts, using the specific video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/one-video-v2", "aweme_id": "7675551740036612985"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/one-video-v2', {'aweme_id': '7675551740036612985'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/one-video-v2", {
  "aweme_id": "7675551740036612985"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/one-video-v2", sandbase.Params{
	"aweme_id": "7675551740036612985",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Returns metadata for one Douyin post, either a video or a photo post, under the `aweme_detail` object. It needs one input: the post's `aweme_id`.

### Use cases

- Pull the caption, hashtags, and author details for a known Douyin post.
- Check the publish time and comment settings of a post before you archive it.
- Collect hashtag names and IDs from a post to find related topic content.
- Read the author profile block to map a post back to its creator account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7448118827402972455"}'
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
    "activity_video_type": -1,
    "admire_auth": {
      "admire_button": 1,
      "author_can_admire": 0,
      "exit_admire_in_aweme_post": 0,
      "is_admire": 0,
      "is_click_admire_icon_recently": 0,
      "is_fifty_admire_author_stable_fans": 0,
      "is_iron_fans_in_aweme_post": 0,
      "is_show_admire_button": 0,
      "is_show_admire_tab": 0
    },
    "anchors": null,
    "authentication_token": "MS4wLjAA…",
    "author": {
      "accept_private_policy": false,
      "account_cert_info": "{}",
      "account_region": "",
      "ad_cover_url": null,
      "allow_story_normal_like": false,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "height": 720,
        "uri": "168x168/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0…"
        ],
        "width": 720
      },
      "avatar_300x300": {
        "height": 720,
        "uri": "300x300/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0…"
        ],
        "width": 720
      },
      "avatar_larger": {
        "height": 720,
        "uri": "1080x1080/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVF…"
        ],
        "width": 720
      },
      "avatar_medium": {
        "height": 720,
        "uri": "720x720/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFAp…"
        ],
        "width": 720
      },
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFAp…"
        ],
        "width": 720
      }
    },
    "author_mask_tag": 0,
    "author_user_id": 2557909361237356,
    "aweme_acl": {
      "download_mask_panel": {
        "code": 1,
        "show_type": 0
      }
    },
    "aweme_control": {
      "can_comment": true,
      "can_forward": true,
      "can_share": true,
      "can_show_comment": true
    },
    "aweme_id": "7448118827402972455",
    "aweme_listen_struct": {
      "listen_diversion": {
        "extra": [
          {
            "key": "new_guide_prefix",
            "val": "下载汽水"
          }
        ],
        "popup_scene": 4,
        "side_desc": "听更多精彩内容",
        "sub_title_type": "relation"
      },
      "music_cover_listen": 1,
      "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"has_listen_cp_new\",\"copyrigh…"
    },
    "aweme_type": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_detail.aweme_id` | The ID of the post. It matches the `aweme_id` you sent. |
| `aweme_detail.caption` | The post text, including hashtags written as `#tag`. |
| `aweme_detail.create_time` | Publish time of the post. The value `1734150565` looks like a Unix timestamp in seconds. |
| `aweme_detail.author_user_id` | Numeric ID of the account that posted the item. |
| `aweme_detail.author.aweme_count` | Number of posts shown on the author's account. |
| `aweme_detail.author.avatar_168x168 / avatar_300x300 / avatar_larger / avatar_medium / avatar_thumb` | Author avatar images in different sizes. Each has `url_list`, `uri`, `width`, and `height`. |
| `aweme_detail.cha_list[].cha_name` | Name of a hashtag attached to the post. |
| `aweme_detail.cha_list[].cid` | ID of the hashtag. It also appears in the hashtag `schema` link. |
| `aweme_detail.aweme_control.can_comment / can_forward / can_share` | Flags that show whether comments, forwarding, and sharing are allowed on the post. |
| `aweme_detail.danmaku_control.danmaku_cnt` | Count of danmaku (on-screen comments) on the post. `enable_danmaku` shows whether they are turned on. |

### Notes

- Send `aweme_id` as a string. It is the long numeric ID of the post, for example `7448118827402972455`.
- Many fields are `null`, empty strings, or `0` for this post. Check for these values before you use a field.
- Image links in the response, such as avatar `url_list` entries, are full URLs. Some of the cover links carry `x-expires` and `x-signature` query parameters.
- To fetch several posts in one call, use [Douyin Batch Video Information (App V3)](/apis/douyin/app-v3/multi-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-v2.json`](../../../../catalog/models/douyin/app-v3/one-video-v2.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-v2
