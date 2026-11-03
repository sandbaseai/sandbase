# Douyin Series Video List API: pricing, parameters and code examples

`douyin/app-v3/series-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of videos included in a specific Douyin series or playlet using a series identifier and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/series-video-list", "cursor": 0, "series_id": "7592054624643713067"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/series-video-list', {'cursor': 0, 'series_id': '7592054624643713067'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/series-video-list", {
  "cursor": 0,
  "series_id": "7592054624643713067"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/series-video-list", sandbase.Params{
	"cursor": 0,
	"series_id": "7592054624643713067",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/series-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15).  |
| `series_id` | string | yes | Series id  |

## Details

Returns the list of videos in a Douyin series or playlet. Each item is a full video object with author, caption, hashtags and playlet settings. The only required input is `series_id`.

### Use cases

- Collect every video ID in a Douyin collection so you can fetch details or statistics for each one.
- Archive the captions and hashtags of a science or explainer series.
- Check which creator account publishes a given series.
- Map the episodes of a playlet to build a catalog or tracking sheet.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/series-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "7585746250092251178"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | Series id |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "activity_video_type": -1,
      "ad_charge_passive_unlock_config": {
        "broadcast_btn_config": {
          "btn_show_frequency": 1,
          "btn_show_second": 5,
          "btn_text": "秒后解锁下一集",
          "show_second_type": 2
        },
        "trial_btn_config": {
          "btn_show_frequency": 1,
          "btn_show_second": 3,
          "btn_text": "秒后解锁本集",
          "show_second_type": 2
        }
      },
      "ai_follow_images": null,
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "accept_private_policy": false,
        "account_region": "",
        "ad_cover_url": null,
        "allow_story_normal_like": false,
        "apple_account": 0,
        "authority_status": 0,
        "avatar_168x168": {
          "height": 720,
          "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2…"
          ],
          "width": 720
        },
        "avatar_300x300": {
          "height": 720,
          "uri": "300x300/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2SF8fyDjgbmvgBAJDE07A1",
          "url_list": [
            "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_o8AAjKEQIJgQyYff2…"
          ],
          "width": 720
        }
      },
      "author_mask_tag": 0,
      "author_user_id": 2740414975578590,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7529494667390586171",
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
    "logid": "20261103153140A0874E16F54F254A392D",
    "now": 1793691101000
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153140A0874E16F54F254A392D"
  },
  "max_cursor": 15,
  "min_cursor": 0,
  "related_item_tag": -1,
  "selection_panel_conf": {
    "has_segment": true,
    "segment_num": 20
  },
  "status_code": 0,
  "status_msg": "",
  "watch_histories": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | The videos in the series for this page. Each entry is one video object. |
| `aweme_list[].aweme_id` | ID of the video, as a string. Use it to call other video APIs. |
| `aweme_list[].caption` | Text of the video caption, including hashtags. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_168x168.url_list[] / aweme_list[].author.avatar_300x300.url_list[]` | Avatar image URLs of the author at two sizes. |
| `aweme_list[].cha_list[].cha_name` | Name of a hashtag (challenge) attached to the video. |
| `aweme_list[].cha_list[].cid` | ID of the hashtag, as a string. |
| `aweme_list[].comment_permission_info.can_comment` | Whether comments are allowed on the video. |
| `aweme_list[].commerce_info.is_ad` | Whether the video is marked as an ad. |
| `aweme_list[].brief_aweme` | JSON string with a short summary of the video. It includes `series_info_series_id` and the series name. |

### Notes

- Pass `cursor` as `0` for the first page. For later pages, the parameter description says to use the page size (for example `15`) as the next value.
- `aweme_id` values are long numeric strings. Send them to [Douyin Single Video Details](/apis/douyin/app-v3/one-video) for full data on one video.
- To read the series title and summary, call [Douyin Series Detail](/apis/douyin/app-v3/series-detail) with the same `series_id`.
- Use [Douyin User Series List](/apis/douyin/app-v3/user-series-list) to find series IDs for a given creator.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/series-video-list.json`](../../../../catalog/models/douyin/app-v3/series-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/series-video-list
