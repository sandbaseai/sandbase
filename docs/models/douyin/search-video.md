# Douyin Video Search API: pricing, parameters and code examples

`douyin/search-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Douyin (TikTok China) videos by keyword with sort, publish-time, duration, and page filters; later pages require the previous search ID. Use it to support content discovery and trend research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-video", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-video', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-video", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-video", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `keyword` | string | yes | The search keyword.  |
| `duration` | string |  | Filter by video duration. one of: `_0`, `_1`, `_2`, `_3`; default `"_0"` |
| `searchId` | string |  | Search ID; required for pages > 1. Use data.business_config.next_page.search_id from the previous response, and stop paging when data.business_config.has_more is 0.  |
| `sortType` | string |  | Sorting criteria for search results. one of: `_0`, `_1`, `_2`; default `"_0"` |
| `publishTime` | string |  | Filter by video publish time range. one of: `_0`, `_1`, `_7`, `_180`; default `"_0"` |

## Details

This API searches Douyin (TikTok China) videos by keyword and returns a page of video cards with author and video data. It needs a `keyword`. You can add sort, publish-time, duration and page filters.

### Use cases

- Collect the top videos for a keyword such as `美食` to see what content ranks for a topic.
- Narrow results by `publishTime` or `duration` to find recent or short videos on a theme.
- Read the related search words to find nearby topics for content planning.
- Page through results with `searchId` to build a larger sample of videos for one keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `duration` | string | No | Filter by video duration. |
| `page` | integer | No | Page number (starting from 1). |
| `publishTime` | string | No | Filter by video publish time range. |
| `searchId` | string | No | Search ID; required for pages > 1. Use data.business_config.next_page.search_id from the previous response, and stop paging when data.business_config.has_more is 0. |
| `sortType` | string | No | Sorting criteria for search results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "backtrace": "IkaLj8XdHuweIxXXPkc8sidQSsMXb6T3fn9mjfhw5PfXD2xtVJo0IKVmFCGv2EeA0mM8iBpE70nJW78A…",
    "card_count": 12,
    "extra": {
      "guide_search_words": [
        {
          "attached_text": null,
          "id": "6541600883447174408",
          "query_id": "6598250706661020941",
          "type": "recom",
          "word": "附近"
        }
      ],
      "is_filter_search": 1,
      "req_start_ts": 1793691135764
    },
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": {},
    "general_search_config": {
      "keyword": "美食"
    },
    "has_more": 1,
    "is_filter_search": 1,
    "keyword": "美食"
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_video",
      "data": {
        "aweme_info": {
          "activity_video_type": 0,
          "admire_auth": {
            "admire_button": 1,
            "author_can_admire": 0,
            "exit_admire_in_aweme_post": 0,
            "is_admire": 0,
            "is_click_admire_icon_recently": 0,
            "is_fifty_admire_author_stable_fans": 0,
            "is_iron_fans_in_aweme_post": 0,
            "is_show_admire_button": 0
          },
          "ai_follow_images": null,
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
              "uri": "168x168/aweme-avatar/tos-cn-avt-0015_484e0c9cd090bb5eae97a26efe02fdb4",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_484e0c9cd090bb5eae97a2…"
              ],
              "width": 720
            },
            "avatar_300x300": {
              "height": 720,
              "uri": "300x300/aweme-avatar/tos-cn-avt-0015_484e0c9cd090bb5eae97a26efe02fdb4",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_484e0c9cd090bb5eae97a2…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 3857513138626052
        },
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_video",
        "card_info": {
          "search_autoplay_business": "153_dy"
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
        "dcm": "search.natural.aweme_video.7587446290642177329.20261103153215AEBEFC69712236CCF36…",
        "search_id": "20261103153215AEBEFC69712236CCF36D"
      },
      "type": 1
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "20261103153215AEBEFC69712236CCF36D",
    "now": 1793691136000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "guide_search_words": [
      {
        "attached_text": null,
        "id": "6541600883447174408",
        "query_id": "6598250706661020941",
        "type": "recom",
        "word": "附近"
      }
    ],
    "hidden_filter": false
  },
  "log": {
    "impr_id": "20261103153215AEBEFC69712236CCF36D",
    "search_id": "20261103153215AEBEFC69712236CCF36D",
    "search_keyword": "美食"
  },
  "log_pb": {
    "impr_id": "20261103153215AEBEFC69712236CCF36D"
  },
  "mock_recall_path": "/aweme/v2/search/item/",
  "path": "/aweme/v2/search/item/",
  "render_info": [
    {
      "render_extra": {
        "card_type_name": "video_search_video",
        "type": 8119168
      },
      "render_id": "0",
      "render_type": 0,
      "ui_info": {
        "card_exposure_ratio": [
          0.5
        ]
      }
    }
  ],
  "status_code": 0,
  "struct": {
    "children": [
      {
        "children": [
          {
            "data_id": "0",
            "fp": "",
            "id": "0",
            "render_id": "0"
          }
        ],
        "fp": "",
        "id": "000",
        "layout_info": {
          "item_gap": "2"
        },
        "layout_type": 2
      }
    ],
    "fp": "",
    "id": "00",
    "layout_type": 1
  },
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[].data.aweme_info` | The video object for one search result. It holds the video and its author. |
| `business_data[].data.aweme_info.author.avatar_168x168.url_list[]` | Image URLs for the author's avatar at 168x168 size. `avatar_300x300` holds the larger version. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the user who posted the video. |
| `business_data[].log.dcm` | Tracking string for the result. The video ID appears inside it after `aweme_video`, followed by the search ID. |
| `business_data[].log.search_id` | ID of this search. It matches `business_config.next_page.search_id`. |
| `business_config.has_more` | Shows whether more results exist. `1` means more pages, `0` means stop. |
| `business_config.next_page.search_id` | Search ID to send as `searchId` when you request the next page. |
| `business_config.next_page.cursor` | Position of the next page in the result list. In this response it is `12`, the same as `card_count`. |
| `business_config.extra.guide_search_words[].word` | Related search suggestions for the keyword, such as `做法` and `吃播`. |
| `status_code / success` | Result status of the call. `0` and `true` mean the request succeeded. |

### Notes

- For page 2 and later, set `page` and pass `business_config.next_page.search_id` from the previous response as `searchId`. Stop when `business_config.has_more` is `0`.
- The response is the platform's original data structure, so the video list sits in `business_data`, not in a `data` wrapper.
- To get full details for a video found here, call [Douyin Single Video Details](/apis/douyin/app-v3/one-video) with its video ID.
- For trending queries to use as keywords, see [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/search-video.json`](../../../catalog/models/douyin/search-video.json) · Store page: https://www.sandbase.ai/model/douyin/search-video
