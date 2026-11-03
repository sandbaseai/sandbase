# Douyin Video Details API: pricing, parameters and code examples

`douyin/video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for a Douyin (TikTok China) video by video ID. Use it to look up a known video before content review, archiving, or related analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/video-detail", "videoId": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/video-detail', {'videoId': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/video-detail", {
  "videoId": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/video-detail", sandbase.Params{
	"videoId": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `videoId` | string | yes | The unique video identifier (aweme_id or model_id).  |

## Details

Returns the details of one Douyin (TikTok China) video, including its caption, author, hashtags, and posting time. It needs the video ID in `videoId`.

### Use cases

- Look up a known Douyin video to read its caption, hashtags, and author before a content review.
- Archive the full metadata of a video by saving the response next to its `aweme_id`.
- Check whether comments and sharing are allowed on a video before building a comment or share workflow.
- Collect the author profile data of a video to link it to a creator record.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique video identifier (aweme_id or model_id). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "activity_video_type": 0,
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
      "account_region": "",
      "ad_cover_url": null,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "height": 720,
        "uri": "168x168/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a19…"
        ],
        "width": 720
      },
      "avatar_300x300": {
        "height": 720,
        "uri": "300x300/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a19…"
        ],
        "width": 720
      },
      "avatar_larger": {
        "height": 720,
        "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_f96ccdf24e…"
        ],
        "width": 720
      },
      "avatar_medium": {
        "height": 720,
        "uri": "720x720/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53…"
        ],
        "width": 720
      },
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
        "url_list": [
          "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_f96ccdf24e53…"
        ],
        "width": 720
      },
      "avatar_uri": "aweme-avatar/tos-cn-avt-0015_f96ccdf24e53e435a85a1976f2c7fe0b",
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      }
    },
    "author_mask_tag": 0,
    "author_user_id": 95823111667,
    "aweme_control": {
      "can_comment": true,
      "can_forward": true,
      "can_share": true,
      "can_show_comment": true
    },
    "aweme_id": "7372484719365098803",
    "aweme_listen_struct": {
      "trace_info": "{\"copyright_not_speech\":\"true\",\"copyright_reason\":\"not_intercept\",\"copyright_tag…"
    },
    "aweme_type": 0,
    "aweme_type_tags": ""
  },
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153223EB8397EA020C0C288FFE",
    "now": 1793691143000
  },
  "log_pb": {
    "impr_id": "20261103153223EB8397EA020C0C288FFE"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_detail.aweme_id` | The video ID. It matches the `videoId` you sent. |
| `aweme_detail.desc / aweme_detail.caption` | The video text, including inline hashtags such as `#双子座`. |
| `aweme_detail.desc_language` | Language code of the description. The sample value is `zh`. |
| `aweme_detail.create_time` | Posting time as a Unix timestamp in seconds. |
| `aweme_detail.author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_detail.author.aweme_count` | Number of videos on the author's account. The sample value is `591`. |
| `aweme_detail.author.avatar_larger.url_list[]` | Image URLs for the author's avatar. Other sizes appear in `avatar_168x168`, `avatar_300x300`, `avatar_medium`, and `avatar_thumb`. |
| `aweme_detail.cha_list[].cha_name` | Name of each hashtag attached to the video. `cid` holds the hashtag ID. |
| `aweme_detail.aweme_control.can_comment / can_forward / can_share` | Flags that show whether commenting, forwarding, and sharing are allowed on the video. |
| `aweme_detail.danmaku_control.danmaku_cnt` | Number of on-screen comments (danmaku) on the video. `enable_danmaku` shows whether they are turned on. |

### Notes

- Take the video ID from the number at the end of a Douyin video link, or from `aweme_id` in other Douyin API responses. The parameter accepts an `aweme_id` or `model_id`.
- A `status_code` of `0` means the request succeeded. `extra.logid` holds a request log ID.
- To get a video from a share link, use [Douyin Single Video by Share URL](/apis/douyin/app-v3/one-video-by-share-url).
- For view and like counts, call [Douyin Video Statistics](/apis/douyin/app-v3/video-statistics). For comments, call [Douyin Video Comments](/apis/douyin/app-v3/video-comments).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/video-detail.json`](../../../catalog/models/douyin/video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/video-detail
