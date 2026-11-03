# Douyin Image Search API: pricing, parameters and code examples

`douyin/search/image-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns image-based search results from Douyin matching a search keyword. Supports sorting, content filtering, post date filters, and pagination parameters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/image-search", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/image-search', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/image-search", {
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
run, err := c.Run(ctx, "douyin/search/image-search", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/image-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "cat" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type (Fixed to 2 for images) default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns Douyin image post search results for a keyword. The main input is `keyword`. You can also pass sort, publish time, and pagination values.

### Use cases

- Collect image posts that match a topic keyword, such as `猫咪`, for content research.
- Find the accounts that post image content for a keyword through the author details on each result.
- Page through a keyword's image results with the `search_id` and `cursor` values from the previous response.
- Narrow results to recent posts with the `publish_time` filter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/image-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type (Fixed to 2 for images) |
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "cat" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 18,
    "extra": {
      "is_filter_search": 0,
      "req_start_ts": 1793691138079
    },
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": null,
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "猫咪",
    "next_page": {
      "cursor": 20,
      "keyword": "猫咪",
      "poi_search_info": "",
      "search_id": "20261103153218ED49D03DEF6B274EE5BA",
      "search_request_id": "20261103153218ED49D03DEF6B274EE5BA"
    },
    "poi_search_info": ""
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_image",
      "data": {
        "aweme_info": {
          "activity_video_type": 0,
          "ai_follow_images": null,
          "ai_search_struct": {
            "show_ai_entrance": true
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
              "uri": "168x168/aweme-avatar/tos-cn-avt-0015_242e4f83969897e3a72d5f07692df051",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_242e4f83969897e3a72d5f…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 99642755744
        },
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_image",
        "card_info": {
          "search_autoplay_business": "303_dy"
        },
        "card_style_type": 1,
        "card_type": 1,
        "debug_data": {
          "filter_debug_info_list": null
        },
        "debug_diff_info": {}
      },
      "data_id": "0",
      "log": {
        "search_id": "20261103153218ED49D03DEF6B274EE5BA"
      },
      "type": 11
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "20261103153218ED49D03DEF6B274EE5BA",
    "now": 1793691139000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "hidden_filter": false
  },
  "log": {
    "impr_id": "20261103153218ED49D03DEF6B274EE5BA",
    "search_id": "20261103153218ED49D03DEF6B274EE5BA",
    "search_keyword": "猫咪"
  },
  "log_pb": {
    "impr_id": "20261103153218ED49D03DEF6B274EE5BA",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 932
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card. Each card holds one image post. |
| `business_data[].data.aweme_info` | Details of the image post, including its author and a token string. |
| `business_data[].data.aweme_info.author.avatar_168x168.url_list[]` | Image URLs for the author's 168x168 avatar. The list holds the same picture in `webp` and `jpeg` formats. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the account that posted the image. |
| `business_data[].data_id` | Position of the card in this page of results, as a string starting at `0`. |
| `business_config.has_more` | Shows whether more results exist. `1` in this response. |
| `business_config.next_page.cursor` | Cursor value to send as `cursor` to get the next page. |
| `business_config.next_page.search_id` | Search ID to send as `search_id` with the next page request. |
| `business_config.card_count` | Number of cards in this response. |
| `log.search_keyword` | The keyword that the search used. |

### Notes

- For the first page, leave `cursor` at `0` and leave `search_id` and `backtrace` empty.
- For the next page, copy `business_config.next_page.cursor` into `cursor` and `business_config.next_page.search_id` into `search_id`.
- The `content_type` description says to fix it to `2` for images.
- For image-text results from a different endpoint, try [Douyin Image-Text Search](/apis/douyin/search/image-search-v3).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/image-search.json`](../../../../catalog/models/douyin/search/image-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/image-search
