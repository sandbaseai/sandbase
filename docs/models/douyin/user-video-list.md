# Douyin User Published Videos API: pricing, parameters and code examples

`douyin/user-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get videos published by a Douyin (TikTok China) user, with cursor pagination and newest or most-popular sorting. Use it to browse or monitor a creator's public video output.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/user-video-list", "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/user-video-list', {'secUid': 'MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/user-video-list", {
  "secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/user-video-list", sandbase.Params{
	"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24",
})
```

Same call via the path form: `POST /v1/api/douyin/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string | yes | The unique user ID (sec_user_id) on Douyin.  |
| `sortType` | string |  | Sort order: `LATEST` for newest first (default), or `MOST_POPULAR` for most popular first. one of: `LATEST`, `MOST_POPULAR`; default `"LATEST"` |
| `maxCursor` | string |  | Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages. default `"0"` |

## Details

Returns a page of videos published by one Douyin user, including the caption, hashtags, author info and creation time of each video. It needs the user's `secUid` and can sort by newest or most popular.

### Use cases

- Monitor a creator's account and detect new posts by polling the `LATEST` sort.
- Pull a creator's top videos with `MOST_POPULAR` to see which content worked best.
- Collect the hashtags a creator uses across their posts to study their topics.
- Build a list of `aweme_id` values to pass to a video detail or statistics API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The unique user ID (sec_user_id) on Douyin. |
| `maxCursor` | string | No | Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages. |
| `sortType` | string | No | Sort order: `LATEST` for newest first (default), or `MOST_POPULAR` for most popular first. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "activity_video_type": 0,
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
        "allow_story_normal_like": true,
        "authority_status": 0,
        "avatar_168x168": {
          "height": 720,
          "uri": "168x168/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16…"
          ],
          "width": 720
        },
        "avatar_300x300": {
          "height": 720,
          "uri": "300x300/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16…"
          ],
          "width": 720
        },
        "avatar_larger": {
          "height": 720,
          "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
          "url_list": [
            "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_1fcfb510bb…"
          ],
          "width": 720
        },
        "avatar_medium": {
          "height": 720,
          "uri": "720x720/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
          "url_list": [
            "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde…"
          ],
          "width": 720
        },
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde4beed96d16e8aca2a0bd",
          "url_list": [
            "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_1fcfb510bbde…"
          ],
          "width": 720
        }
      },
      "author_mask_tag": 0,
      "author_user_id": 60065294161,
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
      "aweme_id": "6993909291686104350",
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
        "trace_info": "{\"copyright_not_speech\":\"true\",\"copyright_reason\":\"label_risk_music_or_speech\",\"…"
      },
      "aweme_type": 68
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153222349B77C71B05BAD0534C",
    "now": 1793691143000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153222349B77C71B05BAD0534C"
  },
  "max_cursor": 1792554922000,
  "min_cursor": 1793600601000,
  "post_serial": 2,
  "replace_series_cover": 1,
  "request_item_cursor": 0,
  "sec_uid": "MS4wLjABAAAAanuWoPEMHem_eaWR8RQFyLQ8_QiouZlPlb7KAe9GS24",
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | One published video per item. Each item is the full video record. |
| `aweme_list[].aweme_id` | ID of the video, as a string. Use it to look up the same video in other APIs. |
| `aweme_list[].desc` | Caption text of the video, including inline hashtags such as `#家常菜`. |
| `aweme_list[].create_time` | Publish time of the video as a Unix timestamp in seconds. |
| `aweme_list[].cha_list[].cha_name / aweme_list[].cha_list[].cid` | Name and ID of each hashtag (challenge) attached to the video. |
| `aweme_list[].author_user_id` | Numeric ID of the account that published the video. |
| `aweme_list[].author.avatar_larger.url_list` | Image URLs for the author's avatar, offered in several sizes and formats such as `.heic` and `.jpeg`. |
| `aweme_list[].city` | City code of the video, for example `371300`. |
| `aweme_list[].aweme_control.can_comment / aweme_list[].aweme_control.can_share` | Flags that show whether comments and sharing are allowed on the video. |
| `aweme_list[].commerce_info.is_ad` | `true` if the video is marked as an ad. |

### Notes

- Get `secUid` (the `sec_user_id`) from a Douyin user profile. The [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile) API is a place to look it up.
- Send `maxCursor` as `0` for the first page. For later pages, pass the `max_cursor` value from the previous response.
- `sortType` accepts `LATEST` (default) or `MOST_POPULAR`.
- For play counts and other stats on the returned videos, pass the `aweme_id` values to [Douyin Video Statistics](/apis/douyin/app-v3/video-statistics).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/user-video-list.json`](../../../catalog/models/douyin/user-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/user-video-list
