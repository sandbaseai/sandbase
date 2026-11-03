# Douyin General Search (V2) API: pricing, parameters and code examples

`douyin/search/general-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns search results from Douyin's general search tab. Supports filtering by keyword, sort method, post date, video duration, and content type.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/general-search-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/general-search-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/general-search-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/general-search-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/general-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "cat" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier (empty for first request, obtained from previous response for pagination) default `""` |
| `search_id` | string |  | Search ID (empty for first request, obtained from previous response for pagination) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns a page of Douyin general search results for a keyword. Each result is a card that holds either a video or an image post, with its author and card layout info. The only input you need is `keyword`. Filters and pagination tokens are optional.

### Use cases

- Collect the top video and image posts that Douyin shows for a keyword such as `猫咪`.
- Narrow results by sort method, post date, video duration or content type to study a specific slice of content.
- Page through a keyword's results by passing back the cursor, search ID and backtrace from the previous response.
- Find authors who appear for a topic by reading the author data on each result card.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/general-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace identifier (empty for first request, obtained from previous response for pagination) |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "cat" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID (empty for first request, obtained from previous response for pagination) |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": {},
    "backtrace": "MPzqs2LkeAcDN/znby3CZP+OFeA17Pm3NOmSq9pPwVpTEpdyu2wfEi0hq441EeOUv5iYMWtqqyekGmux…",
    "card_count": 19,
    "extra": {
      "comment_config": {
        "disable_comment_bar": true
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
      "hidden_filter": false,
      "hide_guide_search_words": null,
      "impression_server_log": {
        "channel": "aweme_general",
        "from_group_id": "",
        "is_search_after_feed": false,
        "poi": "圣克拉拉县圣克拉拉",
        "query": "猫咪",
        "request_time": 1793691137,
        "session_id": "5742c9a4…",
        "source": "homepage_recom_search"
      },
      "location_info": {
        "server_location_timestamp": "1793691137"
      }
    },
    "extra_fresh_struct": null,
    "feedback": null,
    "filter_bar": null,
    "general_search_config": {
      "activity_tag": null,
      "comment_config": {
        "disable_comment_bar": true
      },
      "display_music_anchor": 2,
      "double_column_button_style": 2,
      "double_column_layout_type": 3,
      "ecom_intent": "intent_not_ecom",
      "extra_server_client_params": "{\"last_strong_style_card_idx\":0}",
      "is_double_column_left": 0,
      "keyword": "猫咪",
      "search_pop_info": [],
      "srp_algo_for_wind_vane": "{\"bp_personal_strategy_level\":0,\"cate_lv1\":[20063,20041],\"ecom_bp_buy_intent\":0,…",
      "user_guide": {
        "inflow_second": 0,
        "inflow_stop": 7,
        "resp_second": 5,
        "show_inflow_guide": true,
        "show_resp_guide": true
      }
    },
    "guide_search_words_extra": {},
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "猫咪"
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_video",
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
            "account_cert_info": "{}",
            "account_region": "",
            "ad_cover_url": null,
            "allow_story_normal_like": false,
            "apple_account": 0,
            "authority_status": 0,
            "avatar_168x168": {
              "height": 720,
              "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_oEKA8FFsbIDrpkAAXWAwfoEqqkQM9fwEeA9hKE",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_oEKA8FFsbIDrpkAAX…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 99421008169
        },
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_video",
        "card_info": {
          "search_autoplay_business": "153_dy"
        },
        "card_protocal_struct": {
          "cachalot_card_id": 1,
          "render_extra": {
            "card_type_name": "general_video_double_col",
            "type": 2534528
          },
          "render_type": 0,
          "schema_id": 2534528,
          "schema_name": "general_video_double_col",
          "schema_url": ""
        },
        "card_style_type": 1,
        "card_type": 1,
        "card_type_id": {
          "card_name": "153|1|double",
          "doc_type": 153,
          "performance_infos": {
            "153": 1,
            "double_column": 1,
            "is_native": 1,
            "search_card_count": 1,
            "video_has_lynx_anchor": 0
          }
        }
      },
      "data_id": "0",
      "log": {
        "dcm": "search.natural.aweme_video.7697482617494657147.2026110315321636213EE99184C24CC1D…",
        "search_id": "2026110315321636213EE99184C24CC1D7",
        "search_result_id": "7697482617494657147"
      },
      "type": 1
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "2026110315321636213EE99184C24CC1D7",
    "now": 1793691138000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "guide_search_words": [
      {
        "attached_text": null,
        "id": "6527573731718468871",
        "query_id": "6537523068217103624",
        "type": "recom",
        "word": "视频"
      }
    ],
    "hidden_filter": false
  },
  "log": {
    "impr_id": "2026110315321636213EE99184C24CC1D7",
    "search_id": "2026110315321636213EE99184C24CC1D7",
    "search_keyword": "猫咪"
  },
  "log_pb": {
    "impr_id": "2026110315321636213EE99184C24CC1D7",
    "search_source": "homepage_recom_search",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "maokai_extra": {},
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card. Cards are a mix of videos and image posts. |
| `business_data[].card_id` | Card type. `douyin.doctype_aweme_video` marks a video and `douyin.doctype_aweme_image` marks an image post. |
| `business_data[].data.aweme_info` | The post inside the card. It holds the post's author and related post details. |
| `business_data[].data.aweme_info.author` | The account that published the post. It includes avatar images such as `avatar_168x168` with `url_list` links. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the post's author. |
| `business_data[].log.search_result_id` | ID of the result post. It matches the ID in the `dcm` value of the same item. |
| `business_config.has_more` | Shows `1` when more results are available for the next page. |
| `business_config.next_page.cursor` | Cursor value for the next page. The sample shows `20` after the first page. |
| `business_config.next_page.search_id` | Search ID to send with the next page request. |
| `business_config.backtrace` | Backtrace token to send with the next page request. |

### Notes

- For the first page, leave `cursor` at `0` and leave `search_id` and `backtrace` empty.
- For the next page, send `business_config.next_page.cursor` as `cursor`, `business_config.next_page.search_id` as `search_id`, and `business_config.backtrace` as `backtrace`. Keep the same `keyword`.
- Result IDs such as `search_result_id` are long numeric strings. Keep them as strings to avoid rounding.
- To search only videos, try [Douyin Video Search](/apis/douyin/search/video-search-v2). To search suggested keywords, try [Douyin Search Suggestions](/apis/douyin/search/search-suggest).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/general-search-v2.json`](../../../../catalog/models/douyin/search/general-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/general-search-v2
