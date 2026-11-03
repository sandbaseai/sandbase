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

Query Toutiao creators across the Xingtu marketplace using a search `keyword` along with optional filters for metrics, tags, and audience profiles.

### Use cases

- Find Toutiao creators by nickname, Toutiao ID, or content topic.
- Filter creators by follower counts, play completion rates, and expected performance metrics.
- Sort creator search results by platform score or custom ranking fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-toutiao-creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Toutiao ID or content word |
| `tag` | string | No | Creator category IDs, comma-separated |
| `page` | integer | No | Page number, default 1 |
| `gender` | string | No | Creator gender, 1=male, 2=female |
| `cpe_max` | string | No | Maximum expected CPE |
| `cpe_min` | string | No | Minimum expected CPE |
| `cpm_max` | string | No | Maximum expected CPM |
| `cpm_min` | string | No | Minimum expected CPM |
| `fans_max` | string | No | Maximum followers |
| `fans_min` | string | No | Minimum followers |
| `price_max` | string | No | Maximum creator price |
| `price_min` | string | No | Minimum creator price |
| `sort_type` | integer | No | Sort type, 1=asc, 2=desc, default 2 |
| `price_type` | string | No | Price tier by video length |
| `sort_field` | string | No | Sort field, default `score` (comprehensive sort) |
| `extra_filter` | string | No | Extra profile filters (JSON array) for audience/fans profile, region, etc. |
| `persona_tags` | string | No | Persona IDs. |
| `task_category` | integer | No | Cooperation target |
| `author_list_id` | string | No | Featured creator list ID |
| `marketing_target` | integer | No | Marketing target |
| `expected_play_max` | string | No | Maximum expected plays |
| `expected_play_min` | string | No | Minimum expected plays |
| `first_industry_id` | string | No | Industry ID |
| `interact_rate_max` | string | No | Maximum interaction rate, 0-1 decimal |
| `interact_rate_min` | string | No | Minimum interaction rate, 0-1 decimal |
| `play_over_rate_max` | string | No | Maximum play-completion rate, 0-1 decimal |
| `play_over_rate_min` | string | No | Minimum play-completion rate, 0-1 decimal |
| `burst_text_rate_max` | string | No | Maximum viral-post rate, 0-1 decimal |
| `burst_text_rate_min` | string | No | Minimum viral-post rate, 0-1 decimal |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "authors": [
    {
      "star_id": "6729826071128047630",
      "attribute_datas": {
        "article_interate_rate": "0.0409",
        "auth_type": "0",
        "author_status": "0",
        "author_type": "1",
        "core_user_id": "4042405212",
        "id": "6729826071128047630"
      }
    }
  ]
}
```

### Notes

- The required `keyword` parameter matches creator nicknames, Toutiao IDs, or content words.
- Set `gender` to `1` for male or `2` for female.
- Pagination uses `page` (default 1), and `sort_type` defaults to `2` for descending order.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-toutiao-creator.json`](../../../../catalog/models/douyin/xingtu-v2/search-toutiao-creator.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-toutiao-creator
