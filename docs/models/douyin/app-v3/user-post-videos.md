# Douyin User Videos API: pricing, parameters and code examples

`douyin/app-v3/user-post-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts. Sort by latest or most popular, with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-post-videos", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-post-videos', {'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-post-videos", {
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-post-videos", sandbase.Params{
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number, do not exceed 20, it is recommended to keep it unchanged.  |
| `sort_type` | integer |  | Sort type, optional values are as follows: `0`: Latest sorting - default; `1`: Hottest sorting  |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Returns the videos on a Douyin user's profile, with descriptions, publish time and play, like, comment and share counts. You pass the user's `sec_user_id`. You can sort by latest or most popular and page through the list with a cursor.

### Use cases

- Track how often a Douyin creator posts by reading the `create_time` of each video.
- Review an influencer's recent videos before a campaign.
- Collect a brand account's videos and descriptions for content analysis.
- Pull the most popular videos of an account with `sort_type` set to `1`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAKzTVRAaDq7fTxkJteVYjRsyVPxxofLDAyViyWT43BNRdTjgmqCcolsU_UqRgbzBU", "count": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `count` | integer | No | Maximum count number, do not exceed 20, it is recommended to keep it unchanged. |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |
| `sort_type` | integer | No | Sort type, optional values are as follows: `0`: Latest sorting - default; `1`: Hottest sorting |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "activity_video_type": -1,
      "admire_auth": {
        "admire_button": 1,
        "author_can_admire": 0,
        "exit_admire_in_aweme_post": 0,
        "is_admire": 0,
        "is_click_admire_icon_recently": 0,
        "is_fifty_admire_author_stable_fans": 0,
        "is_iron_fans_in_aweme_post": 0,
        "is_show_admire_button": 0
      },
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "account_cert_info": "{}",
        "allow_story_normal_like": false,
        "authority_status": 0,
        "avatar_168x168": {
          "height": 720,
          "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fnHIATQDRAl2FEJtuEglF4f",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fn…"
          ],
          "width": 720
        },
        "avatar_300x300": {
          "height": 720,
          "uri": "300x300/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fnHIATQDRAl2FEJtuEglF4f",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fn…"
          ],
          "width": 720
        },
        "avatar_larger": {
          "height": 720,
          "uri": "1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fnHIATQDRAl2FEJtuEglF…",
          "url_list": [
            "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_oQeCK…"
          ],
          "width": 720
        },
        "avatar_medium": {
          "height": 720,
          "uri": "720x720/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fnHIATQDRAl2FEJtuEglF4f",
          "url_list": [
            "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAi…"
          ],
          "width": 720
        },
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAiB7QKAW81fnHIATQDRAl2FEJtuEglF4f",
          "url_list": [
            "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_oQeCKAi…"
          ],
          "width": 720
        }
      },
      "author_mask_tag": 0,
      "author_user_id": 7565728661744845873,
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
      "aweme_id": "7701251112510949029",
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
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"has_listen_cp_new\",\"copyrigh…"
      },
      "aweme_type": 0
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315314151CAD125368591AA2FC7",
    "now": 1793691101000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110315314151CAD125368591AA2FC7"
  },
  "max_cursor": 1793087105000,
  "min_cursor": 1793087254000,
  "post_serial": 3,
  "replace_series_cover": 1,
  "request_item_cursor": 0,
  "sec_uid": "MS4wLjABAAAAKzTVRAaDq7fTxkJteVYjRsyVPxxofLDAyViyWT43BNRdTjgmqCcolsU_UqRgbzBU",
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | One entry per video on the user's profile. |
| `aweme_list[].aweme_id` | The video ID, returned as a string of digits. |
| `aweme_list[].create_time` | Publish time of the video, as a 10-digit number such as `1793087254`. |
| `aweme_list[].desc` | The video description text. It is an empty string when the creator wrote none. |
| `aweme_list[].author_user_id` | Numeric ID of the user who posted the video. |
| `aweme_list[].author.avatar_168x168.url_list / author.avatar_300x300.url_list / author.avatar_thumb.url_list` | Avatar image URLs of the author at different sizes. Each list holds a `.heic` and a `.jpeg` link. |
| `aweme_list[].aweme_control.can_comment / can_forward / can_share` | Booleans that show whether commenting, forwarding and sharing are allowed on the video. |
| `aweme_list[].commerce_info.is_ad` | Boolean that shows whether the video is marked as an ad. |
| `aweme_list[].city` | A city code attached to the video, such as `410100`. |

### Notes

- `count` should not exceed 20. The default is recommended.
- `sort_type` is `0` for latest first (default) and `1` for hottest first.
- For the first page, send `max_cursor` as `0`. For the next page, send the `max_cursor` value from the previous response.
- Pass `aweme_id` values to [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics), which takes comma-separated video IDs.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Get Douyin brand hot search list data](/apis/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-post-videos.json`](../../../../catalog/models/douyin/app-v3/user-post-videos.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-post-videos
