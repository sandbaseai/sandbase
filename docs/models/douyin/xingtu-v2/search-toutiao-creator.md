# Douyin Toutiao Creator Search API: pricing, parameters and code examples

`douyin/xingtu-v2/search-toutiao-creator` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Toutiao image-text creator profiles matching a search keyword and filters such as follower count, interaction rate, and industry categories.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/search-toutiao-creator", "keyword": "人工智能", "marketing_target": 1, "page": 1, "sort_field": "score", "sort_type": 2, "task_category": 11}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/search-toutiao-creator', {'keyword': '人工智能', 'marketing_target': 1, 'page': 1, 'sort_field': 'score', 'sort_type': 2, 'task_category': 11})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/search-toutiao-creator", {
  "keyword": "人工智能",
  "marketing_target": 1,
  "page": 1,
  "sort_field": "score",
  "sort_type": 2,
  "task_category": 11
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/search-toutiao-creator", sandbase.Params{
	"keyword": "人工智能",
	"marketing_target": 1,
	"page": 1,
	"sort_field": "score",
	"sort_type": 2,
	"task_category": 11,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/search-toutiao-creator` with the body above minus `model`.

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
| `keyword` | string | yes | Search keyword: nickname, Toutiao ID or content word  |
| `fans_max` |  |  | Maximum followers  |
| `fans_min` |  |  | Minimum followers  |
| `price_max` |  |  | Maximum creator price  |
| `price_min` |  |  | Minimum creator price  |
| `sort_type` | integer |  | Sort type, 1=asc, 2=desc, default 2 default `2` |
| `price_type` |  |  | Price tier by video length  |
| `sort_field` | string |  | Sort field, default `score` (comprehensive sort) default `"score"` |
| `extra_filter` |  |  | Extra profile filters (JSON array) for audience/fans profile, region, etc.  |
| `persona_tags` |  |  | Persona IDs. Comma=match any, semicolon=group AND  |
| `task_category` | integer |  | Cooperation target default `11` |
| `author_list_id` |  |  | Featured creator list ID  |
| `marketing_target` | integer |  | Marketing target default `1` |
| `expected_play_max` |  |  | Maximum expected plays  |
| `expected_play_min` |  |  | Minimum expected plays  |
| `first_industry_id` |  |  | Industry ID  |
| `interact_rate_max` |  |  | Maximum interaction rate, 0-1 decimal  |
| `interact_rate_min` |  |  | Minimum interaction rate, 0-1 decimal  |
| `play_over_rate_max` |  |  | Maximum play-completion rate, 0-1 decimal  |
| `play_over_rate_min` |  |  | Minimum play-completion rate, 0-1 decimal  |
| `burst_text_rate_max` |  |  | Maximum viral-post rate, 0-1 decimal  |
| `burst_text_rate_min` |  |  | Minimum viral-post rate, 0-1 decimal  |

## Details

Returns a list of Toutiao image-text creators that match a search `keyword`, with each creator's `star_id`, profile attributes, and price list. The `keyword` can be a nickname, a Toutiao ID, or a content word. Optional filters narrow results by followers, interaction rate, price, and industry.

### Use cases

- Build a shortlist of Toutiao creators who write about a topic such as artificial intelligence.
- Compare the listed `price` of creators for the same task category before you contact them.
- Filter creators by `article_interate_rate` and expected views to find accounts with strong article engagement.
- Collect `star_id` values to feed into creator detail and audience APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-toutiao-creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Toutiao ID or content word |
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
| `first_industry_id` | string | No | Industry ID |
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
        "article_expected_vv": "17642",
        "article_interate_rate": "0.0409",
        "auth_info": "微头条首发创作者",
        "auth_type": "0",
        "author_avatar_frame_icon": "0",
        "author_status": "0",
        "author_type": "1",
        "avatar_uri": "https://sf3-cdn-tos.toutiaostatic.com/img/user-avatar/135a0f72919777e6f0dffc0c8c…"
      },
      "extra_data": {
        "assign_live_restrict_tip": "当前账号暂无法向该达人发起任务",
        "assign_live_restricted": true,
        "content_query_from_word": "",
        "content_query_score": 0,
        "debug_info": "",
        "recall_from": [
          "1_0"
        ],
        "recall_return_infos": {},
        "recommend_types": []
      },
      "items": [],
      "star_id": "6729826071128047630",
      "task_infos": [
        {
          "online_status": 1,
          "platform_source": 2,
          "price_infos": [
            {
              "end_time": "2145916800",
              "platform_source": 2,
              "price": 5000,
              "price_extra_info": {},
              "start_time": "1732982400",
              "task_category": 11,
              "video_type": 11,
              "video_type_status": 1
            }
          ],
          "task_category": 11,
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
    "has_more": false,
    "limit": 20,
    "page": 1,
    "total_count": 10
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | Creator ID in the Xingtu marketplace. Use it to look up the same creator in other Xingtu APIs. |
| `authors[].attribute_datas.auth_info` | Verification or title text shown on the creator profile, such as a teacher or technology creator label. |
| `authors[].attribute_datas.article_expected_vv` | Expected views per article for the creator, returned as a string. |
| `authors[].attribute_datas.article_interate_rate` | Article interaction rate as a decimal string. For example, `0.0409` is about 4.1%. |
| `authors[].attribute_datas.avatar_uri / authors[].attribute_datas.city / authors[].attribute_datas.core_user_id` | Avatar image URL, city, and user ID of the creator. `city` and `core_user_id` appear only on some creators. |
| `authors[].task_infos[].price_infos[].price` | Listed price for the task. An empty `task_infos` list means no price is listed. |
| `authors[].task_infos[].price_infos[].start_time / authors[].task_infos[].price_infos[].end_time` | Start and end of the price validity as Unix timestamps in seconds, returned as strings. |
| `authors[].extra_data.assign_live_restricted / authors[].extra_data.assign_live_restrict_tip` | Whether the current account is blocked from sending a task to this creator, and the reason text. |
| `pagination.has_more / pagination.page / pagination.limit / pagination.total_count` | Paging state: whether more pages exist, the current page, the page size, and the total number of matches. |

### Notes

- Send `page` to move through results. The response `pagination.limit` was 20 in this example.
- Use `authors[].star_id` as the creator ID in follow-up calls such as [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).
- Call [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution) to see the audience profile of a creator you shortlisted.
- The `items` list in each author was empty in this example, and some creators have no `task_infos`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-toutiao-creator.json`](../../../../catalog/models/douyin/xingtu-v2/search-toutiao-creator.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-toutiao-creator
