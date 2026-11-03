# Douyin User Video Posts API: pricing, parameters and code examples

`douyin/web/user-post-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video data posted on a Douyin user homepage. Query by user identifier with support for pagination and sorting by popularity or default order.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-post-videos", "count": 20, "filter_type": "0", "max_cursor": "0", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-post-videos', {'count': 20, 'filter_type': '0', 'max_cursor': '0', 'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-post-videos", {
  "count": 20,
  "filter_type": "0",
  "max_cursor": "0",
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-post-videos", sandbase.Params{
	"count": 20,
	"filter_type": "0",
	"max_cursor": "0",
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum count number, it is recommended not to exceed 20  |
| `max_cursor` | string |  | Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time.  |
| `filter_type` | string |  | Filter type, optional parameters are as follows: 0: Default sorting; 3: Sort by popularity  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Returns the videos posted on a Douyin user's homepage, one page at a time. It needs the user's `sec_user_id` and returns a list of video objects under `aweme_list`.

### Use cases

- Archive the caption, post time and ID of every video a Douyin creator has published.
- Check a creator's homepage for new uploads by comparing `aweme_id` values between runs.
- Pull a creator's most popular videos with `filter_type` set to `3` to benchmark their best content.
- Collect the hashtags a creator uses by reading each video's `cha_list` entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `count` | integer | No | Maximum count number, it is recommended not to exceed 20 |
| `filter_type` | string | No | Filter type, optional parameters are as follows: 0: Default sorting; 3: Sort by popularity |
| `max_cursor` | string | No | Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time. |

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
        "authority_status": 0,
        "avatar_168x168": {
          "height": 720,
          "uri": "168x168/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
          "url_list": [
            "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7…"
          ],
          "width": 720
        },
        "avatar_300x300": {
          "height": 720,
          "uri": "300x300/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
          "url_list": [
            "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7…"
          ],
          "width": 720
        },
        "avatar_larger": {
          "height": 720,
          "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
          "url_list": [
            "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_d8306450a…"
          ],
          "width": 720
        },
        "avatar_medium": {
          "height": 720,
          "uri": "720x720/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
          "url_list": [
            "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7…"
          ],
          "width": 720
        },
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7468b0b",
          "url_list": [
            "https://p3.douyinpic.com/aweme-avatar/tos-cn-avt-0015_d8306450a4b1f0a9992ce420b7…"
          ],
          "width": 720
        },
        "comment_filter_status": 0,
        "comment_setting": 0
      },
      "author_mask_tag": 0,
      "author_user_id": 92163827336,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7153549929326120227",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"has_listen_cp_new\",\"copyrigh…"
      },
      "aweme_type": 68,
      "aweme_type_tags": ""
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315323555B8D57E31D446120EF6",
    "now": 1793691155000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110315323555B8D57E31D446120EF6"
  },
  "max_cursor": 1767690864000,
  "min_cursor": 1792314963000,
  "not_login_module": {
    "extra": "{\"guide_login_tip_create_time\":1793526612,\"guide_login_tip_desc\":\"\",\"guide_login…",
    "guide_login_tip_cover_url": {
      "height": 720,
      "uri": "tos-cn-i-0813c000-ce/ok7sEnVNTDAxCYAOAwFwE9qADAfw9CI5IgfmnE",
      "url_list": [
        "https://p26-sign.douyinpic.com/tos-cn-i-0813c000-ce/ok7sEnVNTDAxCYAOAwFwE9qADAfw…"
      ],
      "width": 720
    },
    "guide_login_tip_exist": true,
    "guide_login_tip_style": 1
  },
  "post_serial": 2,
  "replace_series_cover": 1,
  "request_item_cursor": 0,
  "sec_uid": "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[].aweme_id` | ID of the video. Use it to look up the single video in other Douyin APIs. |
| `aweme_list[].desc` | Caption text of the video, including hashtags such as `#le`. |
| `aweme_list[].create_time` | Time the video was posted. The value looks like a Unix timestamp in seconds, for example `1665565640`. |
| `aweme_list[].author_user_id` | Numeric ID of the user who posted the video. |
| `aweme_list[].author.avatar_thumb.url_list / aweme_list[].author.avatar_larger.url_list` | Image URLs for the author's avatar in different sizes. Each list holds several URLs for the same image. |
| `aweme_list[].cha_list[].cha_name` | Name of a hashtag (challenge) attached to the video. |
| `aweme_list[].cha_list[].cid` | ID of the hashtag. |
| `aweme_list[].city` | City code attached to the video, for example `440100`. |
| `aweme_list[].aweme_control.can_comment / aweme_list[].aweme_control.can_share` | Flags that show whether comments and sharing are allowed on the video. |
| `aweme_list[].desc_language` | Language code detected for the caption. `un` appears when the language is not identified. |

### Notes

- Get `sec_user_id` from a user homepage link with [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id).
- For the first page, send `max_cursor` as `0`. For the next pages, send the `max_cursor` value returned by the previous response.
- Set `filter_type` to `0` for default order or `3` to sort by popularity. Keep `count` at 20 or below.
- Pass an `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video) to get full details for one video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-post-videos.json`](../../../../catalog/models/douyin/web/user-post-videos.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-post-videos
