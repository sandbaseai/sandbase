# Douyin Video Search (V1) API: pricing, parameters and code examples

`douyin/search/video-search-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync, async

Search Douyin videos by keyword: descriptions, authors and play, like, comment and share counts, with sort, publish-time, duration and content-type filters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync, async (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v1", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v1', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v1", {
  "backtrace": "",
  "content_type": "0",
  "cursor": 0,
  "filter_duration": "0",
  "keyword": "猫咪",
  "publish_time": "0",
  "search_id": "",
  "sort_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/video-search-v1", sandbase.Params{
	"backtrace": "",
	"content_type": "0",
	"cursor": 0,
	"filter_duration": "0",
	"keyword": "猫咪",
	"publish_time": "0",
	"search_id": "",
	"sort_type": "0",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "Artificial Intelligence" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier used for pagination(obtained from the last response) default `""` |
| `search_id` | string |  | Search ID used for pagination(obtained from the last response) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns a page of Douyin video search results for a keyword. Each result holds the video record with its author, plus search tracking values for the next page. The only input you need is `keyword`.

### Use cases

- Collect videos that match a product name or topic on Douyin.
- Find creators who post about a keyword and read their author IDs and avatars.
- Page through all results for a keyword to count how many videos appear for it.
- Use the related search words to expand a keyword list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace identifier used for pagination(obtained from the last response) |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "Artificial Intelligence" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID used for pagination(obtained from the last response) |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "aweme_list": null,
  "backtrace": "w8KOvPTzjA32DWEYf/cuFW45DQGXnMhbmtMMdOJA8MfKx+wJO5eOs3pIHfwYBckrqCwIlbiGsquRCyjR…",
  "cursor": 8,
  "data": [
    {
      "aweme_info": {
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
        "ai_search_struct": {
          "show_ai_entrance": true
        },
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
        "author_mask_tag": 0
      },
      "aweme_list": null,
      "card_id": "douyin.doctype_aweme_video.video_search_video_new_double",
      "card_info": {
        "search_autoplay_business": "153_dy"
      },
      "card_style_type": 1,
      "card_type": 1,
      "card_type_name": "video_search_video_new_double",
      "debug_data": {
        "filter_debug_info_list": null
      },
      "debug_diff_info": {},
      "doc_type": 153,
      "ecom_goods_list": null,
      "feedback": {
        "url": "aweme://lynxview_popup/?channel=morphling_normal&bundle=douyin_questionnaire%2Fi…"
      }
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153222807FBF14578AD2BCB393",
    "now": 1793691143000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_doodle_config": {
    "keyword": "猫咪"
  },
  "guide_search_words": [
    {
      "attached_text": null,
      "id": "6527573731718468871",
      "query_id": "6537523068217103624",
      "type": "recom",
      "word": "视频"
    }
  ],
  "has_more": 1,
  "log_pb": {
    "impr_id": "20261103153222807FBF14578AD2BCB393",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].aweme_info` | The video record for one search result. It holds the video details and the `author` object. |
| `data[].aweme_info.author_user_id` | Numeric ID of the account that posted the video. |
| `data[].aweme_info.author.avatar_168x168.url_list / data[].aweme_info.author.avatar_300x300.url_list` | Avatar image URLs for the author at 168x168 and 300x300 sizes. Each list has a `.webp` and a `.jpeg` link. |
| `data[].log_data.search_id` | ID of this search. It is the same for every item on the page. |
| `data[].card_type_name` | Name of the result card type. Video results show `video_search_video_new_double`. |
| `cursor / backtrace` | Pagination values to send back in the next request. |
| `has_more` | Shows `1` when more results are available. |
| `guide_search_words[].word` | Related search words suggested for the keyword. Each entry also has an `id` and a `type`. |
| `status_code` | `0` when the request succeeded. |

### Notes

- The videos are in `data`. The top-level `aweme_list` is `null`.
- For the first page, leave `cursor` at `0`. For the next page, send the response `cursor` and `backtrace`, and send `data[].log_data.search_id` as `search_id`.
- `sort_type`, `content_type`, `publish_time` and `filter_duration` are strings and default to `"0"`.
- To search other Douyin result types or compare video results, try [Douyin Video Search](/apis/douyin/search/video-search-v2) or [Douyin General Search](/apis/douyin/search/general-search-v1). To get keyword ideas first, call [Douyin Search Suggestions](/apis/douyin/search/search-suggest).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin General Search](/apis/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Douyin Search Suggestions](/apis/douyin/search/search-suggest): Get Douyin search autocomplete suggestions for a keyword: the related queries users see while typing in the Douyin app.
- [Douyin Video Search](/apis/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v1.json`](../../../../catalog/models/douyin/search/video-search-v1.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v1
