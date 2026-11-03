# TikTok Creator Search Insights API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category and language.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights", "language_filters": "en", "limit": 10, "offset": 0, "tab": "all"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights', {'language_filters': 'en', 'limit': 10, 'offset': 0, 'tab': 'all'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights", {
  "language_filters": "en",
  "limit": 10,
  "offset": 0,
  "tab": "all"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights", sandbase.Params{
	"language_filters": "en",
	"limit": 10,
	"offset": 0,
	"tab": "all",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) default `"all"` |
| `limit` | integer |  | Number per page, default 20 default `20` |
| `offset` | integer |  | Pagination offset, default 0 default `0` |
| `force_refresh` | boolean |  | Force refresh, default False default `false` |
| `creator_source` | string |  | Creator source, default "general_search" default `"general_search"` |
| `category_filters` | string |  | Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports default `""` |
| `language_filters` | string |  | Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko default `"en"` |

## Details

Returns the search topics TikTok shows creators in Creator Search Insights. Each topic has a popularity score, a short trend series and a video count. All inputs are optional, so an empty request returns the first page of English topics.

### Use cases

- Find trending search topics to build new videos around.
- Filter with `tab=content_gap` to find topics that carry the `content_gap` label.
- Compare topics by their `textnet` category layers to see which subject areas are rising.
- Track a topic's `trending_seq` values across repeated calls to see if interest rises or falls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_filters` | string | No | Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports |
| `creator_source` | string | No | Creator source, default "general_search" |
| `force_refresh` | boolean | No | Force refresh, default False |
| `language_filters` | string | No | Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko |
| `limit` | integer | No | Number per page, default 20 |
| `offset` | integer | No | Pagination offset, default 0 |
| `tab` | string | No | Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "banners": {
    "conversion_bar_list": [
      {
        "item_link": "https://activity.tiktokw.us/magic/eco/runtime/release/66581e19df4daf02866b5cc9?a…",
        "item_text": "Learn more"
      }
    ],
    "event_banners": {
      "ecommerce_education": {
        "eligible": {
          "image_url": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/6cjd5rh917161…",
          "link": "https://activity.tiktokw.us/magic/eco/runtime/release/664c4298f65e08d77319049b?a…",
          "text": "Promote products people want to buy. Start earning now!"
        },
        "enrolled": {
          "image_url": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/b0fmjabl17161…",
          "link": "https://activity.tiktokw.us/magic/eco/runtime/release/6645db2e6f3a610291d0b0ac?a…",
          "text": "Create shoppable videos with products people want to buy!"
        },
        "non_eligible": {
          "image_url": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/hdskk6yq17161…",
          "link": "https://activity.tiktokw.us/magic/eco/runtime/release/664c4c03f33586028244e7fb?a…",
          "text": "Explore opportunities to earn with shopping insights"
        }
      }
    },
    "home_page_banner": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/q8hl7ump17134…",
    "image_url": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/r8z2ni6s17084…",
    "image_url_dark": "https://sf16-muse-va.ibytedtos.com/obj/search-static-maliva/maliva/a1av245117084…",
    "loading_page_banner": "https://p16-search-fe-static.tiktokcdn-us.com/tos-alisg-i-baf7wf9fmw-sg/e06d4221…"
  },
  "cost_tracker": {
    "es_cost": 23,
    "model_cost": 124,
    "post_process_cost": 36,
    "recall_cost": 83,
    "recommend_reason_cost": 4,
    "rough_sort_cost": 2,
    "total_cost": 272
  },
  "cursor": 20,
  "extra": {
    "cold_start": true,
    "latency": 273,
    "logid": "20261103074352704495AFB5FFFB018670",
    "now": 1793691832985,
    "vgeo": "VGeo-US"
  },
  "has_follower_searched": false,
  "has_more": true,
  "inspiration_list": [
    {
      "business_types": [
        "basic"
      ],
      "cover_image": "",
      "debug_info": {
        "creator_category": [
          {
            "reason": "byFollowerCnt",
            "type": "new_creator"
          }
        ],
        "creator_lang": {
          "infer_languages": [
            "en"
          ],
          "use_mul_lang": false
        },
        "experiment": {
          "csi_csi_entertainment_ip": "v1",
          "csi_csi_exp_group_name_3": "involve_photomode_topic",
          "csi_csi_rec_workflow_si_related": "v2_l1_i2i_and_generic_filter",
          "csi_csi_useful_exp_gen_1026": "csi_useful_eu_ttp_exp_gen_v0"
        },
        "language": "en",
        "recall_scores": [
          0.033678531646728516
        ],
        "recall_source": [
          "FromDssmViking"
        ],
        "recall_source_position": {
          "FromDssmViking": 46,
          "FromMidLongTailDssmViking": 46
        },
        "rough_score": 0
      },
      "dislike_option_enabled": true,
      "entity_id": 0,
      "favorited_updated_at": 0,
      "inspiration_types": [
        "search"
      ],
      "is_favorited": false,
      "order_popularity_seq": [],
      "popularity": 71,
      "popularity_updated_at": 1793686119,
      "popularity_v2": 174152
    }
  ],
  "session_refresh_index": 6,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `inspiration_list[].query_text` | The search phrase shown to creators. The text is raw and can contain typos or stray quote marks. |
| `inspiration_list[].query_id_str` | The topic ID as a string. Use this string instead of `query_id`, which is a large number. |
| `inspiration_list[].popularity / inspiration_list[].popularity_v2` | Two popularity scores for the topic. `popularity` is a small number such as 71 or 93. `popularity_v2` is a much larger count. |
| `inspiration_list[].trending_seq / inspiration_list[].trending_seq_v2` | Recent trend history for the topic. Each list holds one value per time step, in the same scale as `popularity` and `popularity_v2`. |
| `inspiration_list[].video_num` | The number of videos linked to the topic. |
| `inspiration_list[].query_labels` | Labels on the topic. The value `content_gap` marks a content-gap topic. |
| `inspiration_list[].rec_reason.rec_reason_short_show_text` | A short reason why TikTok recommends the topic, such as `Easy to create`. The `rec_reason_detail_show_text` field gives the longer text. |
| `inspiration_list[].textnet.layer1 / inspiration_list[].textnet.layer2 / inspiration_list[].textnet.layer3` | Category path for the topic, from broad to specific. Deeper layers can be empty strings. |
| `inspiration_list[].popularity_updated_at` | Unix timestamp in seconds for the last popularity update. |
| `has_more / cursor` | `has_more` shows whether more topics exist. `cursor` is the next offset, which was 20 in this response. |

### Notes

- Page through results with `limit` and `offset`. Use the returned `cursor` as the next `offset` while `has_more` is `true`.
- Set `tab` to one of `all`, `content_gap`, `follower_searched`, `life_style`, `topics`, `challenges`, `sounds` or `hashtags`.
- Narrow results with `category_filters` (for example `Gaming` or `Food`) and `language_filters` (for example `en` or `es`).
- For one topic's history or related videos, call [TikTok Creator Search Insights Trend](/apis/tiktok/app-v3/creator-search-insights-trend), [TikTok Creator Search Insights Detail](/apis/tiktok/app-v3/creator-search-insights-detail) or [TikTok Creator Search Insights Videos](/apis/tiktok/app-v3/creator-search-insights-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check if live room is online The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id` interface through the live room link.
- [Batch check if live rooms are online](/apis/tiktok/app-v3/check-live-room-online-batch): Batch check TikTok live rooms' online status, supports up to 50 room IDs Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`.
- [Get content translation data](/apis/tiktok/app-v3/content-translate): Get content translation data.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights
