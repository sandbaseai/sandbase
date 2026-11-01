# Douyin Xingtu Anchor Search

`douyin/xingtu-v2/search-anchor` · api · Douyin

Search Douyin Xingtu anchors matching a specific query keyword, with filtering options for audience metrics, follower counts, and engagement rates.

## Pricing

- **$0.0015 per call** (USD)
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

Query Douyin Xingtu anchors by providing a search term in `keyword`. Refine results using filters for follower counts, engagement rates, and industry categories.

### Use cases

- Find Douyin anchors matching brand campaign requirements.
- Filter potential creators by follower volume and audience engagement metrics.
- Identify relevant talent using specific niche keywords and industry tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-anchor" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Douyin ID, Xingtu ID or live content word |
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
      "star_id": "7481538995130728485",
      "attribute_datas": {
        "author_status": "1",
        "author_type": "1",
        "core_user_id": "1379225338382761",
        "fans_increment_rate_within_15d": "-0.027777777777777776",
        "id": "7481538995130728485",
        "nick_name": "<user>"
      }
    }
  ]
}
```

### Notes

- Set `gender` to 1 for male or 2 for female creators.
- Use `sort_type` with 1 for ascending order and 2 for descending order (default 2).
- Filter results using `page` for pagination, which defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-anchor.json`](../../../../catalog/models/douyin/xingtu-v2/search-anchor.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-anchor
