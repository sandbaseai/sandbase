# TikTok Creator Search Insights Videos API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns popular videos related to a specific search term from creator search insights. Results support pagination using offset and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights-videos", "count": 1, "keyword": "app that", "offset": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights-videos', {'count': 1, 'keyword': 'app that', 'offset': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights-videos", {
  "count": 1,
  "keyword": "app that",
  "offset": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights-videos", sandbase.Params{
	"count": 1,
	"keyword": "app that",
	"offset": 0,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default 20 default `20` |
| `offset` | integer |  | Pagination offset, default 0 default `0` |
| `keyword` | string | yes | Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend  |

## Details

Returns a list of popular TikTok videos related to a search term from creator search insights. It needs a `keyword` and supports paging with `offset` and `count`.

### Use cases

- Find which videos currently perform well for a topic such as `openai` before planning a TikTok post.
- Collect the authors behind popular videos on a keyword to build a list of creators in that niche.
- Page through the full result list for a keyword to study the content around a trending topic.
- Check whether a keyword returns videos at all before running a deeper analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend |
| `count` | integer | No | Number per page, default 20 |
| `offset` | integer | No | Pagination offset, default 0 |

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
    "logid": "202611030743528181513E8C144D01C1FB",
    "now": 1793691833000,
    "search_request_id": "",
    "server_stream_time": 830
  },
  "feedback_type": "video",
  "global_doodle_config": {
    "display_filter_bar": 1,
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
    "hit_shark": false,
    "keyword": "openai",
    "new_source": "",
    "search_channel": "musically_video",
    "search_intent": {},
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611030743528181513E8C144D01C1FB"
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
            "height": 720,
            "uri": "tos-maliva-avt-0068/696d0a17460329ef81f8ff8f524b9b37",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/696d0a17460329ef81f…"
            ],
            "url_prefix": null,
            "width": 720
          },
          "avatar_300x300": {
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
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `search_item_list[]` | One result per popular video for the keyword. Each item holds the video data under `aweme_info`. |
| `search_item_list[].aweme_info.author_user_id` | Numeric ID of the account that posted the video. |
| `search_item_list[].aweme_info.author` | Object with the video author's profile data, including avatar images in several sizes such as `avatar_168x168` and `avatar_300x300`. |
| `search_item_list[].aweme_info.added_sound_music_info.author` | Name shown as the author of the sound used in the video. |
| `search_item_list[].aweme_info.added_sound_music_info.audition_duration` | Length value for the sound preview. The response does not state the unit. |
| `search_item_list[].aweme_info.aigc_info.created_by_ai` | Boolean flag that shows whether the video is marked as AI-generated. `aigc_label_type` holds the label type. |
| `has_more` | Shows whether more results exist. `1` means more pages are available. |
| `cursor` | Position marker for the next page. It was `20` in the sample request. |
| `global_doodle_config.keyword` | The keyword the search ran for. |
| `status_code` | Request status. `0` means the call succeeded. |

### Notes

- Get the `keyword` value from [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights) or [TikTok Creator Search Insights Trend](/apis/tiktok/app-v3/creator-search-insights-trend).
- Page through results with `offset` and `count`. `count` defaults to 20 and `offset` defaults to 0. Check `has_more` and `cursor` to see if another page exists.
- The top-level `aweme_list` array was empty in the sample. The videos appear in `search_item_list`.
- Call [TikTok Video Details](/apis/tiktok/app-v3/one-video) to get full data for a single video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-videos.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-videos
