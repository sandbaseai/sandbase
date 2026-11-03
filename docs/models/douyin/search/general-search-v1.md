# Douyin General Search API: pricing, parameters and code examples

`douyin/search/general-search-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts. Filter by sort, publish time, duration and content type.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/general-search-v1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/general-search-v1', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/general-search-v1", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/general-search-v1", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/general-search-v1` with the body above minus `model`.

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

Returns Douyin search results for a keyword from the app's general search tab. Each result is a video or image post with its caption, author and an ID. The only input needed is `keyword`.

### Use cases

- Collect the top Douyin posts for a keyword such as a pet breed or product name.
- Find creators who post about a topic by reading `publish_username` and `author_user_id`.
- Track new posts that mention a brand by filtering on publish time and reading the caption text.
- Build a list of post IDs for a topic and fetch each one in full with another API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/general-search-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
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
  "ad_info": {},
  "backtrace": "QcYdxJw7yf6duzkWgjcv9m6lNSZ4EWGHlekiwBFcWNm/eLx9nrk3/Ud/xt7uVeZWofx64xqtZ7DyvuOe…",
  "cursor": 20,
  "data": [
    {
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
      },
      "card_type_name": "",
      "comment_list": [
        {
          "aweme_id": "7697482617494657147",
          "cid": "7697483159202726665",
          "create_time": 1792209959,
          "decorated_emoji_info": null,
          "digg_count": 6,
          "enter_from": "others_homepage",
          "group_id": 7697482617494657147,
          "image_list": null
        }
      ],
      "data": {
        "card_tags": null,
        "common_tab_config": null,
        "hotspot_tab_config": null,
        "recom_extra_info": {
          "suggest_words_config": 3,
          "suggest_words_params": {
            "doc_type": "153",
            "item_id": "7697482617494657147",
            "product_id": ""
          }
        }
      },
      "debug_data": {
        "filter_debug_info_list": null
      },
      "debug_diff_info": {}
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532171EB06BE851C10A585E5E",
    "now": 1793691138684,
    "scenes": null,
    "search_request_id": "",
    "start_ms": 1793691137274
  },
  "global_doodle_config": {
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
  "guide_search_words": [
    {
      "attached_text": null,
      "id": "6594507188880807176",
      "query_id": "6537523068217103624",
      "type": "recom",
      "word": "图片"
    }
  ],
  "guide_search_words_extra": {},
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611031532171EB06BE851C10A585E5E",
    "search_source": "homepage_recom_search",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "maokai_extra": {},
  "new_framework_single_column_card_count": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].impression_server_log.doc_title` | Caption text of the result. Long captions can include line breaks and hashtags. |
| `data[].impression_server_log.gid / data[].provider_doc_id_str / data[].log_data.search_result_id` | ID of the result as a string. All three hold the same value for a given item. |
| `data[].impression_server_log.publish_username` | Display name of the author who posted the result. |
| `data[].impression_server_log.publish_time` | Publish time of the result as a Unix timestamp in seconds. |
| `data[].aweme_info.author_user_id` | Numeric ID of the author. |
| `data[].aweme_info.author.avatar_168x168.url_list[]` | Image URLs for the author's 168x168 avatar, in WebP and JPEG formats. |
| `data[].card_id / data[].doc_type` | Type of the result. `douyin.doctype_aweme_video` with `doc_type` 153 is a video, and `douyin.doctype_aweme_image` with `doc_type` 303 is an image post. |
| `data[].comment_list[].digg_count` | Like count of a comment shown with the result. The `comment_list` can be missing on some items. |
| `data[].comment_list[].cid / data[].comment_list[].create_time` | ID of that comment and its creation time as a Unix timestamp in seconds. |
| `data[].log_data.search_id` | ID of this search. Send it back as `search_id` to get the next page. |

### Notes

- For the first page, send only `keyword`. For the next page, send the top-level `cursor` and `backtrace` from the previous response, plus `search_id`.
- `sort_type`, `content_type`, `publish_time` and `filter_duration` are strings. The default `"0"` applies no filter.
- Results mix videos and image posts. Check `card_id` or `doc_type` to tell them apart.
- Pass a result ID to [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3) to load one item. For another search layout, try [Douyin General Search (V2)](/apis/douyin/search/general-search-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Video Search](/apis/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.
- [Fetch hashtag search V1](/apis/douyin/search/challenge-search-v1): Fetch hashtag/challenge search results from Douyin App.
- [Fetch hashtag search V2](/apis/douyin/search/challenge-search-v2): Fetch hashtag/challenge search results from Douyin App using V2 API.

---
Machine-readable: [`catalog/models/douyin/search/general-search-v1.json`](../../../../catalog/models/douyin/search/general-search-v1.json) · Store page: https://www.sandbase.ai/model/douyin/search/general-search-v1
