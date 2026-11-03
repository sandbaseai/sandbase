# Douyin Discussion Search API: pricing, parameters and code examples

`douyin/search/discuss-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns discussion and question-and-answer search results from Douyin. Supports filtering by keyword, sort order, content type, post time, and video duration.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/discuss-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/discuss-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/discuss-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/discuss-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/discuss-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page, use the last response cursor for subsequent pages)  |
| `keyword` | string |  | Search keyword, e.g., "study abroad"  |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response  |
| `search_id` | string |  | Search ID used for pagination  |
| `sort_type` | string |  | Sorting method  |
| `content_type` | string |  | Content type filter  |
| `publish_time` | string |  | Publish time filter  |
| `filter_duration` | string |  | Video duration filter  |

## Details

Returns Douyin discussion and Q&A search results for a keyword. Each result is a card that holds a video (`aweme_list`) with its author. Send `keyword`, and add filters such as `sort_type`, `content_type`, `publish_time` or `filter_duration` to narrow the results.

### Use cases

- Collect the videos and questions people post about a topic such as a pet breed or a study abroad destination.
- Find creators who often appear in discussion results for a keyword.
- Page through discussion results for a keyword to build a dataset of community posts.
- Match each result to its search session with `log.search_id` when you store results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/discuss-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for first page, use the last response cursor for subsequent pages) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "study abroad" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID used for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "backtrace": "QljQY1wnumX0q3TKVwL5sA==",
    "card_count": 13,
    "extra": {
      "comment_config": {
        "card_template": {
          "data_template": "{\"data_id\":\"1\",\"type\":999,\"data\":{\"card_type_name\":\"douyin_topic_comment_card\",\"…",
          "raw_data_template": "{\"type\":350,\"is_newly_published\":1,\"doc_type\":345,\"sub_card_list\":null,\"tab\":nul…",
          "render_info_template": "{\"render_id\":\"1\",\"render_type\":1,\"render_extra\":{\"card_type_name\":\"douyin_topic_…"
        },
        "comment_group_id": 6537523068217103624,
        "comment_service_id": 148,
        "disable_comment_bar": true,
        "enable_insert_newest_comment": false
      },
      "is_filter_search": 0,
      "req_start_ts": 1793691135460
    },
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": null,
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "猫咪",
    "next_page": {
      "cursor": 15,
      "keyword": "猫咪",
      "poi_search_info": "",
      "search_id": "202611031532158D0D959FB7060254C42E",
      "search_request_id": "202611031532158D0D959FB7060254C42E"
    }
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_comment",
      "data": {
        "aweme_list": [
          {
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
                "uri": "168x168/aweme-avatar/tos-cn-avt-0015_e134e286acc2426f94df8f4e29e607d3",
                "url_list": [
                  "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_e134e286acc2426f94df8f…"
                ],
                "width": 720
              }
            },
            "author_mask_tag": 0,
            "author_user_id": 65584265695534
          }
        ],
        "card_id": "douyin.doctype_aweme_comment",
        "card_type_name": "doctype_aweme_comment",
        "filtered_in_video_detail": 0,
        "height": 0,
        "not_inject_aweme_list": false,
        "origin_type": 0,
        "prefetch_resource": {
          "dynamic_component": null,
          "prefetch_image": null
        }
      },
      "data_id": "0",
      "log": {
        "dcm": "search.natural.aweme_comment.7631160052896334641.202611031532158D0D959FB7060254C…",
        "entity_paths": "{\"entity_id\":\"7631160052896334641\",\"entity_name\":\"aweme_comment\",\"dcm_info\":{\"dc…"
      },
      "type": 999
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "202611031532158D0D959FB7060254C42E",
    "now": 1793691135000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "hidden_filter": false
  },
  "log": {
    "impr_id": "202611031532158D0D959FB7060254C42E",
    "pass_through": {
      "hotspot_params": {
        "gid": "",
        "new_source": "discuss_tab"
      }
    },
    "search_id": "202611031532158D0D959FB7060254C42E",
    "search_keyword": "猫咪",
    "topic": "猫咪"
  },
  "log_pb": {
    "impr_id": "202611031532158D0D959FB7060254C42E",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 520
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One result card per item. Each card holds a list of videos in `data.aweme_list`. |
| `business_data[].data.aweme_list[]` | The videos in the card. Each item has video details and an `author` object. |
| `business_data[].data.aweme_list[].author` | The creator of the video. It includes avatar images such as `avatar_168x168` and `avatar_300x300`, each with a `url_list`. |
| `business_data[].data.aweme_list[].author_user_id` | Numeric ID of the creator who posted the video. |
| `business_data[].data.aweme_list[].authentication_token` | Token string attached to the video item. |
| `business_data[].log.entity_paths` | JSON string with the `entity_id` of the result, which matches the ID at the end of `log.dcm`. |
| `business_config.has_more` | Shows `1` when more results are available. |
| `business_config.next_page.cursor` | Cursor value to send as `cursor` for the next page. |
| `business_config.backtrace / business_config.next_page.search_id` | Values to send as `backtrace` and `search_id` for the next page. |
| `log.search_keyword` | The keyword that the search used. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, send `business_config.next_page.cursor`, `business_config.backtrace` and `business_config.next_page.search_id`.
- Check `business_config.has_more` before you request another page.
- The `data` of each card in `business_data` has `card_type_name` set to `doctype_aweme_comment`.
- For regular video search, see [Douyin Video Search](/apis/douyin/search/video-search-v2) or [Douyin General Search](/apis/douyin/search/general-search-v1).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/discuss-search.json`](../../../../catalog/models/douyin/search/discuss-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/discuss-search
