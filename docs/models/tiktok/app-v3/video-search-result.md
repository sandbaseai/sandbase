# TikTok Video Keyword Search API: pricing, parameters and code examples

`tiktok/app-v3/video-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of TikTok videos matching a search query. Supports filtering by target region, time range, and relevance or like count sorting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-search-result", "count": 3, "keyword": "AI", "publish_time": 7, "region": "US", "sort_type": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-search-result', {'count': 3, 'keyword': 'AI', 'publish_time': 7, 'region': 'US', 'sort_type': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-search-result", {
  "count": 3,
  "keyword": "AI",
  "publish_time": 7,
  "region": "US",
  "sort_type": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-search-result", sandbase.Params{
	"count": 3,
	"keyword": "AI",
	"publish_time": 7,
	"region": "US",
	"sort_type": 0,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |
| `sort_type` | integer |  | 0-Relatedness, 1-Most likes default `0` |
| `publish_time` | integer |  | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year default `0` |

## Details

Returns a page of TikTok videos that match a search `keyword`. You can narrow results by `region`, `publish_time`, and `sort_type`. Each result sits in `search_item_list` with its video data under `aweme_info`.

### Use cases

- Collect videos that mention a brand or product name, such as `openai`, for a content review.
- Rank videos for a keyword by most likes to find the top performing posts.
- Pull videos from the last day or last week to follow a topic as it develops.
- Compare what videos show up for the same keyword in different regions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |
| `publish_time` | integer | No | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |
| `sort_type` | integer | No | 0-Relatedness, 1-Most likes |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [],
  "backtrace": "",
  "components": null,
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "202611030744034DEA7E6E04FD450291DD",
    "now": 1793691843000,
    "search_request_id": "",
    "server_stream_time": 368
  },
  "feedback_type": "video",
  "global_doodle_config": {
    "disable_inner_flow": false,
    "display_filter_bar": 1,
    "enable_image_record": true,
    "feedback_survey": [
      {
        "feedback_type": "video",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Dislike",
            "value": "Dislike"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": true,
    "keyword": "openai",
    "new_source": "switch_tab",
    "search_channel": "musically_video",
    "search_intent": {},
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611030744034DEA7E6E04FD450291DD"
  },
  "search_item_list": [
    {
      "aweme_info": {
        "added_sound_music_info": {
          "album": "",
          "allow_offline_music_to_detail_page": false,
          "artists": [],
          "audition_duration": 96,
          "author": ".politicallyspeaking",
          "author_deleted": false,
          "author_position": null,
          "avatar_medium": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-maliva-avt-0068/696d0a17460329ef81f8ff8f524b9b37",
            "url_list": [
              "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/696d0a17460329ef81f…"
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
            "data_size": 0,
            "height": 720,
            "uri": "tos-maliva-avt-0068/696d0a17460329ef81f8ff8f524b9b37",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/696d0a17460329ef81f…"
            ],
            "url_prefix": null,
            "width": 720
          },
          "avatar_300x300": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-maliva-avt-0068/696d0a17460329ef81f8ff8f524b9b37",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/696d0a17460329ef81f…"
            ],
            "url_prefix": null,
            "width": 720
          }
        },
        "author_user_id": 6702871155316147205
      },
      "search_aweme_info": {
        "has_creation_intention": false
      }
    }
  ],
  "status_code": 0,
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search_item_list[]` | One search result per item. The video data is inside `aweme_info`. |
| `search_item_list[].aweme_info.author_user_id` | Numeric ID of the account that posted the video. |
| `search_item_list[].aweme_info.author` | Profile data for the posting account, including avatar images in `avatar_168x168` and `avatar_300x300`. |
| `search_item_list[].aweme_info.added_sound_music_info.author` | Name of the author of the sound attached to the video. |
| `search_item_list[].aweme_info.added_sound_music_info.audition_duration` | Preview length of the sound, as given in the response. |
| `search_item_list[].aweme_info.aigc_info.created_by_ai` | Shows whether the video is flagged as made with AI. `aigc_label_type` holds the label type. |
| `has_more` | Shows `1` when more results are available for the same query. |
| `cursor` | Position value returned with the page. In the sample it is `20`. |
| `status_code` | `0` means the request succeeded. |
| `extra.logid / log_pb.impr_id` | Request identifiers for the call. They are useful when you trace a specific response. |

### Notes

- Page through results with `offset` and `count`. Use the returned `cursor` as the next `offset` while `has_more` is `1`.
- Set `sort_type` to `0` for relevance or `1` for most likes. Set `publish_time` to `0`, `1`, `7`, `30`, `90`, or `180` days.
- `region` takes an ISO 3166-1 alpha-2 code and defaults to `US`.
- To get full details for one video, call [TikTok Video Details](/apis/tiktok/app-v3/one-video) or [TikTok Batch Video Info (App V3)](/apis/tiktok/app-v3/multi-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-search-result.json`](../../../../catalog/models/tiktok/app-v3/video-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-search-result
