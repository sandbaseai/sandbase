# Douyin Xingtu Creator Search API: pricing, parameters and code examples

`douyin/xingtu-v2/search-creator` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Searches Douyin Xingtu short-video creators by keyword, with filtering across metrics like follower count, interaction rate, and category tags.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/search-creator", "first_industry_id": 0, "keyword": "人工智能", "marketing_target": 1, "page": 1, "sort_field": "score", "sort_type": 2, "task_category": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/search-creator', {'first_industry_id': 0, 'keyword': '人工智能', 'marketing_target': 1, 'page': 1, 'sort_field': 'score', 'sort_type': 2, 'task_category': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/search-creator", {
  "first_industry_id": 0,
  "keyword": "人工智能",
  "marketing_target": 1,
  "page": 1,
  "sort_field": "score",
  "sort_type": 2,
  "task_category": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/search-creator", sandbase.Params{
	"first_industry_id": 0,
	"keyword": "人工智能",
	"marketing_target": 1,
	"page": 1,
	"sort_field": "score",
	"sort_type": 2,
	"task_category": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/search-creator` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag` |  |  | Creator category IDs, comma-separated  |
| `page` | integer |  | Page number, default 1 default `1` |
| `gender` |  |  | Creator gender, 1=male, 2=female  |
| `cpe_max` |  |  | Maximum expected CPE  |
| `cpe_min` |  |  | Minimum expected CPE  |
| `cpm_max` |  |  | Maximum expected CPM  |
| `cpm_min` |  |  | Minimum expected CPM  |
| `keyword` | string | yes | Search keyword: nickname, Douyin ID, Xingtu ID or content word  |
| `fans_max` |  |  | Maximum followers  |
| `fans_min` |  |  | Minimum followers  |
| `price_max` |  |  | Maximum creator price  |
| `price_min` |  |  | Minimum creator price  |
| `sort_type` | integer |  | Sort type, 1=asc, 2=desc, default 2 default `2` |
| `price_type` |  |  | Price tier by video length  |
| `sort_field` | string |  | Sort field, default `score` (comprehensive sort) default `"score"` |
| `extra_filter` |  |  | Extra profile filters (JSON array) for audience/fans profile, region, etc.  |
| `persona_tags` |  |  | Persona IDs. Comma=match any, semicolon=group AND  |
| `task_category` | integer |  | Cooperation target default `1` |
| `author_list_id` |  |  | Featured creator list ID  |
| `marketing_target` | integer |  | Marketing target default `1` |
| `expected_play_max` |  |  | Maximum expected plays  |
| `expected_play_min` |  |  | Minimum expected plays  |
| `first_industry_id` | integer |  | Industry ID, 0=unlimited default `0` |
| `interact_rate_max` |  |  | Maximum interaction rate, 0-1 decimal  |
| `interact_rate_min` |  |  | Minimum interaction rate, 0-1 decimal  |
| `play_over_rate_max` |  |  | Maximum play-completion rate, 0-1 decimal  |
| `play_over_rate_min` |  |  | Minimum play-completion rate, 0-1 decimal  |
| `burst_text_rate_max` |  |  | Maximum viral-post rate, 0-1 decimal  |
| `burst_text_rate_min` |  |  | Minimum viral-post rate, 0-1 decimal  |

## Details

Searches Douyin Xingtu creators by keyword and returns a page of matching creators. Each result has a Xingtu creator ID, account attributes, recent videos with play counts, and price quotes. The only required input is `keyword`, which can be a nickname, Douyin ID, Xingtu ID or content word.

### Use cases

- Build a shortlist of Douyin creators who post about a topic such as artificial intelligence.
- Compare the quoted prices of creators for different video types before a campaign.
- Find recent videos with play counts to judge whether a creator's content matches a brand.
- Collect `star_id` values to feed into creator detail and audience lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Douyin ID, Xingtu ID or content word |
| `author_list_id` | string | No | Featured creator list ID |
| `burst_text_rate_max` | string | No | Maximum viral-post rate, 0-1 decimal |
| `burst_text_rate_min` | string | No | Minimum viral-post rate, 0-1 decimal |
| `cpe_max` | string | No | Maximum expected CPE |
| `cpe_min` | string | No | Minimum expected CPE |
| `cpm_max` | string | No | Maximum expected CPM |
| `cpm_min` | string | No | Minimum expected CPM |
| `expected_play_max` | string | No | Maximum expected plays |
| `expected_play_min` | string | No | Minimum expected plays |
| `extra_filter` | string | No | Extra profile filters (JSON array) for audience/fans profile, region, etc. |
| `fans_max` | string | No | Maximum followers |
| `fans_min` | string | No | Minimum followers |
| `first_industry_id` | integer | No | Industry ID, 0=unlimited |
| `gender` | string | No | Creator gender, 1=male, 2=female |
| `interact_rate_max` | string | No | Maximum interaction rate, 0-1 decimal |
| `interact_rate_min` | string | No | Minimum interaction rate, 0-1 decimal |
| `marketing_target` | integer | No | Marketing target |
| `page` | integer | No | Page number, default 1 |
| `persona_tags` | string | No | Persona IDs. Comma=match any, semicolon=group AND |
| `play_over_rate_max` | string | No | Maximum play-completion rate, 0-1 decimal |
| `play_over_rate_min` | string | No | Minimum play-completion rate, 0-1 decimal |
| `price_max` | string | No | Maximum creator price |
| `price_min` | string | No | Minimum creator price |
| `price_type` | string | No | Price tier by video length |
| `sort_field` | string | No | Sort field, default `score` (comprehensive sort) |
| `sort_type` | integer | No | Sort type, 1=asc, 2=desc, default 2 |
| `tag` | string | No | Creator category IDs, comma-separated |
| `task_category` | integer | No | Cooperation target |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "authors": [
    {
      "attribute_datas": {
        "author_avatar_frame_icon": "0",
        "author_ecom_level": "L0",
        "author_level_game": "Lv1",
        "author_level_other": "Lv1",
        "author_status": "1",
        "author_thin_mid_word_association_index": "{}",
        "author_type": "1",
        "avatar_uri": "https://p26.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_a055f1ce0…"
      },
      "extra_data": {
        "assign_live_restrict_tip": "当前账号暂无法向该达人发起任务",
        "assign_live_restricted": true,
        "content_query_from_word": "",
        "content_query_score": 0,
        "debug_info": "",
        "demander_behavior": {
          "added_author_list": false,
          "cooperated": false,
          "viewd_author_page": false
        },
        "recall_from": [
          "1_0"
        ],
        "recall_return_infos": {}
      },
      "items": [
        {
          "item_id": "7345410490002197796",
          "video_tag": 3,
          "vv": 7053
        }
      ],
      "star_id": "6829360684279529485",
      "task_infos": [
        {
          "online_status": 1,
          "platform_source": 1,
          "price_infos": [
            {
              "end_time": "2145916800",
              "platform_source": 1,
              "price": 2000,
              "price_extra_info": {},
              "start_time": "1609430400",
              "task_category": 1,
              "video_type": 2,
              "video_type_status": 1
            }
          ],
          "task_category": 1,
          "task_status": 1
        }
      ]
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "extra_data": {
    "intent_score": 0.14355403184890747,
    "is_cpm_project_search": false,
    "is_intent_consistent": false,
    "search_author_count": 0,
    "search_item_count": 0,
    "search_session_id": "77038443…",
    "speaker_live_base_dis": []
  },
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 84
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | Xingtu ID of the creator. Use it as the creator identifier in other Xingtu APIs. |
| `authors[].attribute_datas.author_ecom_level` | Creator's e-commerce level, for example `L0`. |
| `authors[].attribute_datas.author_level_game / authors[].attribute_datas.author_level_other` | Creator level labels for the game category and for other categories, for example `Lv1`. |
| `authors[].attribute_datas.avatar_uri` | URL of the creator's avatar image. |
| `authors[].items[].item_id` | ID of a recent video by the creator that matched the search. |
| `authors[].items[].vv` | Play count of that video, as given by `vv`. |
| `authors[].task_infos[].price_infos[].price` | Quoted price for the creator under the given `video_type`. An empty `task_infos` list means no price info was returned for that creator. |
| `authors[].task_infos[].price_infos[].video_type` | Code for the video type the price applies to, for example `2`, `71` or `91`. |
| `authors[].extra_data.demander_behavior.cooperated / authors[].extra_data.demander_behavior.added_author_list` | Flags showing whether the calling account has already worked with the creator or added them to a list. |
| `pagination.has_more / pagination.total_count` | Whether more pages exist and the total number of matching creators. |

### Notes

- Pass `page` to move through results. The response shows `pagination.limit` of 20 per page and `pagination.page` for the current page.
- Price `start_time` and `end_time` values are Unix timestamps in seconds, returned as strings.
- `star_id` is a 19-digit string. Keep it as a string to avoid rounding.
- Call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) with a `star_id` for the creator's profile, or [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution) for audience data.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-creator.json`](../../../../catalog/models/douyin/xingtu-v2/search-creator.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-creator
