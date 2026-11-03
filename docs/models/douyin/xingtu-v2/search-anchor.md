# Douyin Xingtu Anchor Search API: pricing, parameters and code examples

`douyin/xingtu-v2/search-anchor` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Douyin Xingtu anchors matching a specific query keyword, with filtering options for audience metrics, follower counts, and engagement rates.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/search-anchor", "keyword": "人工智能", "marketing_target": 3, "page": 1, "sort_field": "score", "sort_type": 2, "task_category": 6}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/search-anchor', {'keyword': '人工智能', 'marketing_target': 3, 'page': 1, 'sort_field': 'score', 'sort_type': 2, 'task_category': 6})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/search-anchor", {
  "keyword": "人工智能",
  "marketing_target": 3,
  "page": 1,
  "sort_field": "score",
  "sort_type": 2,
  "task_category": 6
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/search-anchor", sandbase.Params{
	"keyword": "人工智能",
	"marketing_target": 3,
	"page": 1,
	"sort_field": "score",
	"sort_type": 2,
	"task_category": 6,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/search-anchor` with the body above minus `model`.

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
| `keyword` | string | yes | Search keyword: nickname, Douyin ID, Xingtu ID or live content word  |
| `fans_max` |  |  | Maximum followers  |
| `fans_min` |  |  | Minimum followers  |
| `price_max` |  |  | Maximum creator price  |
| `price_min` |  |  | Minimum creator price  |
| `sort_type` | integer |  | Sort type, 1=asc, 2=desc, default 2 default `2` |
| `price_type` |  |  | Price tier by video length  |
| `sort_field` | string |  | Sort field, default `score` (comprehensive sort) default `"score"` |
| `extra_filter` |  |  | Extra profile filters (JSON array) for audience/fans profile, region, etc.  |
| `persona_tags` |  |  | Persona IDs. Comma=match any, semicolon=group AND  |
| `task_category` | integer |  | Cooperation target default `6` |
| `author_list_id` |  |  | Featured creator list ID  |
| `marketing_target` | integer |  | Marketing target default `3` |
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

This API searches Douyin Xingtu anchors by keyword and returns a paged list of matching creators. The only required input is `keyword`, which can be a nickname, Douyin ID, Xingtu ID or a live content word. Optional filters cover followers, price, CPE, CPM, interaction rate and more.

### Use cases

- Build a shortlist of Xingtu creators whose live content matches a topic such as `人工智能`.
- Narrow candidates by follower range with `fans_min` and `fans_max` before contacting them.
- Check whether your account can send a task to a creator, using the restriction flags on each result.
- Collect `star_id` values from search results to feed into creator detail APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-anchor" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Douyin ID, Xingtu ID or live content word |
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
        "author_avatar_frame_icon": "0",
        "author_status": "1",
        "author_type": "1",
        "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_02df7b1c9ab1…",
        "city": "",
        "core_user_id": "4089782058092311",
        "fans_increment_rate_within_15d": "0",
        "fans_increment_within_15d": "0"
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
      "star_id": "7535764710830899235",
      "task_infos": []
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
    "search_session_id": "77038444…",
    "speaker_live_base_dis": []
  },
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 1094
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | Xingtu ID of the creator. Use it as the creator identifier in other Xingtu APIs. |
| `authors[].attribute_datas.core_user_id` | Core user ID of the creator account. |
| `authors[].attribute_datas.avatar_uri` | URL of the creator avatar image. |
| `authors[].attribute_datas.city` | City shown on the creator profile. It can be an empty string. |
| `authors[].attribute_datas.author_status / authors[].attribute_datas.author_type` | Status and type codes of the creator. Values are returned as strings. |
| `authors[].attribute_datas.fans_increment_within_15d / authors[].attribute_datas.fans_increment_rate_within_15d` | Follower change and change rate over the last 15 days. Present on some results only. |
| `authors[].extra_data.assign_live_restricted` | `true` when your account cannot send a task to this creator. `assign_live_restrict_tip` holds the reason text. |
| `authors[].extra_data.content_query_score` | Relevance score of the creator's content for the keyword. It is `0` for results that matched on other grounds. |
| `pagination.has_more / pagination.total_count` | Whether more pages exist and how many creators match the search in total. |
| `pagination.page / pagination.limit` | Current page number and the number of creators per page (`20` in this response). |

### Notes

- Use `page` to move through results. The response shows `limit` as `20` per page.
- Some fields in `attribute_datas` appear only on certain creators, so check for missing keys.
- To get full profiles, pass a `star_id` to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).
- For audience data on a creator, call [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-anchor.json`](../../../../catalog/models/douyin/xingtu-v2/search-anchor.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-anchor
