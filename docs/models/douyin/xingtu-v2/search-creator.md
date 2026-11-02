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

Use this endpoint to search for marketplace creators by providing a `keyword` alongside optional performance and audience filters.

### Use cases

- Discover Douyin short-video creators by niche keywords or account identifiers.
- Filter creators by performance metrics such as expected plays and interaction rates.
- Screen potential brand partners based on follower thresholds and industry categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword: nickname, Douyin ID, Xingtu ID or content word |
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
| `first_industry_id` | integer | No | Industry ID, 0=unlimited |
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
      "star_id": "6829360684279529485",
      "attribute_datas": {
        "author_ecom_level": "L0",
        "author_level_game": "Lv1",
        "author_level_other": "Lv1",
        "author_status": "1",
        "author_thin_mid_word_association_index": "{}",
        "author_type": "1"
      }
    }
  ]
}
```

### Notes

- Search via `keyword` supports nicknames, Douyin IDs, Xingtu IDs, or content words.
- Pagination is controlled using the `page` parameter, defaulting to 1.
- Sort order is managed by `sort_field` (defaults to score) and `sort_type` (1 for ascending, 2 for descending).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-creator.json`](../../../../catalog/models/douyin/xingtu-v2/search-creator.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-creator
