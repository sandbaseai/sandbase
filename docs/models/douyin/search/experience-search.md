# Douyin Experience Content Search API: pricing, parameters and code examples

`douyin/search/experience-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Douyin search results for tutorial, knowledge, and experience videos based on keyword queries. Supports filtering by release timing, sorting method, and video duration.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/experience-search", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/experience-search', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/experience-search", {
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
run, err := c.Run(ctx, "douyin/search/experience-search", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/experience-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page) default `0` |
| `keyword` | string |  | Search keyword, e.g., "gaming guide" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter (usually fixed to video) default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns Douyin search results for tutorial, knowledge and experience content that match a `keyword`. Each result is a card with the post details and the author profile. You can filter by publish time, sort order and video duration.

### Use cases

- Collect top-ranked tutorial posts for a topic such as a pet care keyword.
- Track which authors appear in knowledge and how-to results for a keyword.
- Page through ranked results to build a list of post IDs for later lookup.
- Compare result sets for the same `keyword` under different `sort_type` or `publish_time` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/experience-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type filter (usually fixed to video) |
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "gaming guide" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 4,
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": null,
    "general_search_config": {
      "double_column_layout_type": 3
    },
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "猫咪",
    "next_page": {
      "cursor": 8,
      "keyword": "猫咪",
      "origin_query": "猫咪",
      "poi_search_info": "",
      "search_id": "2026110315321619DAF5FEC318CF7C2E49",
      "search_request_id": "2026110315321619DAF5FEC318CF7C2E49"
    },
    "poi_search_info": ""
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_image",
      "data": {
        "aweme_info": {
          "activity_video_type": -1,
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
              "uri": "168x168/aweme-avatar/tos-cn-i-0813_ocAIC3AyU6p4YE6gAjIPaWiABZAOqQpgiqPwI",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ocAIC3AyU6p4YE6gAjIPaWiA…"
              ],
              "width": 720
            },
            "avatar_300x300": {
              "height": 720,
              "uri": "300x300/aweme-avatar/tos-cn-i-0813_ocAIC3AyU6p4YE6gAjIPaWiABZAOqQpgiqPwI",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ocAIC3AyU6p4YE6gAjIPaWiA…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 103867977610
        },
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_image",
        "card_style_type": 1,
        "card_type": 1,
        "debug_data": {
          "filter_debug_info_list": null
        },
        "debug_diff_info": {},
        "doc_type": 303
      },
      "data_id": "0_7703817726737656164",
      "log": {
        "dcm": "search.natural.aweme_image.7703817726737656164.2026110315321619DAF5FEC318CF7C2E4…",
        "rank": "1",
        "search_id": "2026110315321619DAF5FEC318CF7C2E49"
      },
      "type": 12
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315321619DAF5FEC318CF7C2E49",
    "now": 1793691137000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {},
  "log": {
    "impr_id": "2026110315321619DAF5FEC318CF7C2E49",
    "search_id": "2026110315321619DAF5FEC318CF7C2E49",
    "search_keyword": "猫咪"
  },
  "log_pb": {
    "impr_id": "2026110315321619DAF5FEC318CF7C2E49"
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 769
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card. Results are listed in rank order. |
| `business_data[].data_id` | Result ID. It starts with the zero-based position, then an underscore, then the post ID, for example `0_7703817726737656164`. |
| `business_data[].log.rank` | Rank of the result in the list, given as a string. |
| `business_data[].data.aweme_info.author` | Profile of the post author, including avatar images in several sizes. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the author. |
| `business_data[].data.aweme_info.author.avatar_168x168.url_list[] / business_data[].data.aweme_info.author.avatar_300x300.url_list[]` | Avatar image URLs at 168x168 and 300x300 sizes. Each list gives the same image in more than one format. |
| `business_data[].data.card_id / business_data[].data.doc_type` | Card type of the result. The sample cards use `douyin.doctype_aweme_image` with `doc_type` `303`. |
| `business_config.has_more` | Shows whether more results exist. `1` means another page is available. |
| `business_config.next_page.cursor / business_config.next_page.search_id` | Values to send as `cursor` and `search_id` to fetch the next page. |
| `business_config.keyword` | The keyword the search ran on. |

### Notes

- Set `cursor` to `0` for the first page. For the next page, send `business_config.next_page.cursor` as `cursor` and `business_config.next_page.search_id` as `search_id`.
- Pass `backtrace` from the previous response when the request schema asks for it. The sample response has no `backtrace` field.
- The sample response returned image-post cards, not only videos, so check `card_id` for each result.
- To search general Douyin content, try [Douyin General Search](/apis/douyin/search/general-search-v1) or [Douyin Video Search](/apis/douyin/search/video-search-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/experience-search.json`](../../../../catalog/models/douyin/search/experience-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/experience-search
