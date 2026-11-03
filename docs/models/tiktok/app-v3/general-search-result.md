# TikTok Search API: pricing, parameters and code examples

`tiktok/app-v3/general-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search TikTok by keyword across videos and users (Top tab). Returns videos with descriptions, authors and play, like, comment and share counts, with sort and publish-time filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/general-search-result", "count": 20, "keyword": "faith sweatshirt", "publish_time": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/general-search-result', {'count': 20, 'keyword': 'faith sweatshirt', 'publish_time': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/general-search-result", {
  "count": 20,
  "keyword": "faith sweatshirt",
  "publish_time": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/general-search-result", sandbase.Params{
	"count": 20,
	"keyword": "faith sweatshirt",
	"publish_time": 1,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/general-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |
| `sort_type` | integer |  | 0-Relatedness, 1-Most likes default `0` |
| `publish_time` | integer |  | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year default `0` |

## Details

Searches TikTok's Top tab for a keyword and returns a mixed list of results, including user cards with sample videos and videos with play, like, comment and share counts. It needs one input, `keyword`. You can also sort by relevance or likes and filter by publish time.

### Use cases

- Find the accounts that rank first for a brand or product name such as `openai`.
- Check which videos TikTok shows first for a keyword, sorted by `sort_type` of `1` for most likes.
- Collect recent posts about a topic by setting `publish_time` to `7` or `30`.
- Spot AI-labelled videos in the results for a keyword using the `aigc_info` flags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/general-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai", "count": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |
| `publish_time` | integer | No | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year |
| `sort_type` | integer | No | 0-Relatedness, 1-Most likes |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "backtrace": "ad_cursor%3D16%3Bcurrent_page%3D1",
  "components": null,
  "cursor": 10,
  "data": [
    {
      "card_profile": {
        "category_tag_list": [
          1
        ]
      },
      "card_title": "Users",
      "doc_id": 1,
      "doc_type": 180,
      "feedback_type": "user",
      "has_top_user": 0,
      "preload_img": {
        "urls": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
        ]
      },
      "provider_doc_id_str": "1",
      "type": 4,
      "user_list": [
        {
          "challenges": null,
          "effects": null,
          "horizontal_data": {
            "backtrace": "{\"cache_key\":\"loadmore_v1:202611030743526A582DF2CDFA6E018899|user_video_subcard|…",
            "card_list": null,
            "common_data": {
              "horizontal_has_more": true
            }
          },
          "items": [
            {
              "added_sound_music_info": {
                "album": "",
                "allow_offline_music_to_detail_page": false,
                "artists": [],
                "audition_duration": 64,
                "author": "OpenAI",
                "author_deleted": false,
                "author_position": null,
                "avatar_medium": {
                  "height": 720,
                  "uri": "tos-useast5-avt-0068-tx/d29bf4d0c36077c6aace74b1dd3c8204",
                  "url_list": [
                    "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
                  ],
                  "url_prefix": null,
                  "width": 720
                }
              },
              "ai_remix_info": {
                "has_entrance": false
              },
              "aigc_info": {
                "aigc_label_type": 0,
                "created_by_ai": false
              },
              "anchors": null,
              "anchors_extras": "",
              "animated_image_info": {
                "effect": 0,
                "type": 0
              },
              "author": {
                "accept_private_policy": false,
                "account_labels": null,
                "ad_cover_url": null,
                "advance_feature_item_order": null,
                "advanced_feature_info": null,
                "authority_status": 0,
                "avatar_168x168": {
                  "height": 720,
                  "uri": "tos-useast5-avt-0068-tx/d29bf4d0c36077c6aace74b1dd3c8204",
                  "url_list": [
                    "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
                  ],
                  "url_prefix": null,
                  "width": 720
                },
                "avatar_300x300": {
                  "height": 720,
                  "uri": "tos-useast5-avt-0068-tx/d29bf4d0c36077c6aace74b1dd3c8204",
                  "url_list": [
                    "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
                  ],
                  "url_prefix": null,
                  "width": 720
                }
              },
              "author_user_id": 7256178298626032683
            }
          ],
          "mix_cursor": 3,
          "mix_has_more": 0,
          "mix_list": [
            {
              "create_time": 1733529383,
              "extra": "{}",
              "ids": null,
              "mix_id": "7445448327224724267",
              "mix_name": "12 Days of OpenAI",
              "mix_type": 1,
              "name": "12 Days of OpenAI",
              "status": {
                "status": 1
              }
            }
          ],
          "musics": null
        }
      ],
      "view_more": true
    }
  ],
  "extra": {
    "dc": "useast8",
    "logid": "202611030743526A582DF2CDFA6E018899",
    "now": 1793691833542,
    "search_id": "202611030743526A582DF2CDFA6E018899",
    "search_request_id": "",
    "server_stream_time": 925
  },
  "global_doodle_config": {
    "ab_params": {
      "user_relation_ship": "1"
    },
    "can_pull_refresh": true,
    "disable_reorder": 0,
    "display_filter_bar": 1,
    "ecom_api_version": "",
    "ecom_search_info": {
      "query_addr_intent": {
        "query_addr_intent": false,
        "query_addr_intent_creator": false,
        "query_addr_intent_shop": false
      }
    },
    "enable_multi_search": false,
    "feedback_survey": [
      {
        "feedback_type": "activity_banner",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Unrelated content",
            "value": "Unrelated content"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "has_ecom_intent": false,
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false
  },
  "has_more": true,
  "headers": [],
  "log_pb": {
    "impr_id": "202611030743526A582DF2CDFA6E018899"
  },
  "prefer_layout": "double_column",
  "qc": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Cursor value for the returned page. The request used `count` 5 and the response returned `10`. |
| `data[].card_title / data[].feedback_type` | Label of the result block. A user block has `card_title` set to `Users` and `feedback_type` set to `user`. |
| `data[].user_list[].items[].author` | Profile of the account that posted the video. It includes avatar images in several sizes, such as `avatar_168x168` and `avatar_300x300`, each with a `url_list`. |
| `data[].user_list[].items[].author_user_id` | Numeric ID of the account that posted the video. |
| `data[].user_list[].items[].aigc_info.created_by_ai` | Boolean flag. It is `true` when the video is labelled as AI-generated. `aigc_label_type` holds the label code. |
| `data[].user_list[].items[].added_sound_music_info.author / album` | Name of the sound's author and its album. Either can be an empty string. |
| `data[].user_list[].mix_list[].mix_id / mix_name` | ID and title of a playlist (mix) that belongs to the matched user, such as `12 Days of OpenAI`. |
| `data[].user_list[].mix_list[].create_time` | Unix timestamp in seconds for when the mix was created. |
| `data[].user_list[].horizontal_data.common_data.horizontal_has_more` | Boolean flag. It is `true` when the user card has more horizontal items to load. |
| `data[].preload_img.urls` | Image URLs for previewing the result card. |

### Notes

- Use `count` and `offset` to page through results. `sort_type` takes `0` (relevance) or `1` (most likes). `publish_time` takes `0`, `1`, `7`, `30`, `90` or `180`.
- One response can mix user cards and videos, so check `data[].card_title` or `data[].feedback_type` before you read a result.
- To search only videos, call [TikTok Video Keyword Search](/apis/tiktok/app-v3/video-search-result). To search only accounts, call [TikTok User Search Results](/apis/tiktok/app-v3/user-search-result).
- To get full details for a video from the results, call [TikTok Video Details (V3)](/apis/tiktok/app-v3/one-video-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/apis/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

---
Machine-readable: [`catalog/models/tiktok/app-v3/general-search-result.json`](../../../../catalog/models/tiktok/app-v3/general-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/general-search-result
