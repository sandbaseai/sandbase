# Douyin Image-Text Search API: pricing, parameters and code examples

`douyin/search/image-search-v3` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns image-text content search results from Douyin based on a target query keyword. Supports pagination using cursor and search session identifiers.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/image-search-v3", "cursor": 0, "keyword": "猫咪", "search_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/image-search-v3', {'cursor': 0, 'keyword': '猫咪', 'search_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/image-search-v3", {
  "cursor": 0,
  "keyword": "猫咪",
  "search_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/image-search-v3", sandbase.Params{
	"cursor": 0,
	"keyword": "猫咪",
	"search_id": "",
})
```

Same call via the path form: `POST /v1/api/douyin/search/image-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string | yes | Search keyword, e.g., "food"  |
| `search_id` | string |  | Search ID for pagination (use value from previous response) default `""` |

## Details

Returns Douyin image-text post search results for a keyword. Each result is a card with the post data, the author, and a rank. The only required input is `keyword`.

### Use cases

- Collect image-text posts that match a topic such as `猫咪` to study what content ranks for it.
- Build a list of author IDs and avatar images for accounts that post about a keyword.
- Page through all results for a keyword with `cursor` and `search_id` to build a larger sample.
- Store the `data_id` values to track which posts appear for a keyword over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/image-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, e.g., "food" |
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `search_id` | string | No | Search ID for pagination (use value from previous response) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 7,
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
      "search_id": "202611031532178EA25612545EC9B86A9F",
      "search_request_id": "202611031532178EA25612545EC9B86A9F"
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
            "account_region": "",
            "ad_cover_url": null,
            "allow_story_normal_like": false,
            "apple_account": 0,
            "authority_status": 0,
            "avatar_168x168": {
              "height": 720,
              "uri": "168x168/aweme-avatar/tos-cn-avt-0015_db24175ed4fad5b8c3189ec252d41369",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_db24175ed4fad5b8c3189e…"
              ],
              "width": 720
            },
            "avatar_300x300": {
              "height": 720,
              "uri": "300x300/aweme-avatar/tos-cn-avt-0015_db24175ed4fad5b8c3189ec252d41369",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_db24175ed4fad5b8c3189e…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 4338007174810816
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
      "data_id": "0_7693825739632053071",
      "log": {
        "dcm": "search.natural.aweme_image.7693825739632053071.202611031532178EA25612545EC9B86A9…",
        "rank": "1",
        "search_id": "202611031532178EA25612545EC9B86A9F"
      },
      "type": 12
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532178EA25612545EC9B86A9F",
    "now": 1793691138000,
    "scenes": null,
    "search_request_id": "202611026F72F7399D796ABC"
  },
  "global_config": {},
  "log": {
    "impr_id": "202611031532178EA25612545EC9B86A9F",
    "search_id": "202611031532178EA25612545EC9B86A9F",
    "search_keyword": "猫咪"
  },
  "log_pb": {
    "impr_id": "202611031532178EA25612545EC9B86A9F"
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 1094
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card. The list holds the image-text posts returned for this page. |
| `business_data[].data_id` | Result identifier. It starts with the zero-based position in the list, then an underscore, then a long numeric post ID. |
| `business_data[].log.rank` | Position of the result in the search, as a string. The first result is `"1"`. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the account that posted the content. |
| `business_data[].data.aweme_info.author.avatar_168x168.url_list / business_data[].data.aweme_info.author.avatar_300x300.url_list` | Avatar image URLs for the author at 168x168 and 300x300. Each list has a `webp` and a `jpeg` link. |
| `business_data[].data.aweme_info.authentication_token` | Long token string attached to the post. The response gives no description of what it is used for. |
| `business_config.has_more` | Shows whether more results exist. `1` means you can request another page. |
| `business_config.next_page.cursor / business_config.next_page.search_id` | Values to send in the next request to get the following page. |
| `business_config.card_count` | Number of cards the response reports for this page. |

### Notes

- Set `cursor` to `0` and leave `search_id` empty on the first request.
- For the next page, send `business_config.next_page.cursor` as `cursor` and `business_config.next_page.search_id` as `search_id`. Keep the same `keyword`.
- Stop paging when `business_config.has_more` is not `1`.
- For a different result mix, try [Douyin Image Search](/apis/douyin/search/image-search) or [Douyin General Search](/apis/douyin/search/general-search-v1).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/image-search-v3.json`](../../../../catalog/models/douyin/search/image-search-v3.json) · Store page: https://www.sandbase.ai/model/douyin/search/image-search-v3
