# Douyin Creative Keyword Related Videos API: pricing, parameters and code examples

`douyin/index/content-creative-keyword-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos associated with a specific trending keyword in a category. Filters include category ID, target keyword, analysis period, and end date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-keyword-items", "end_date": "1735660799", "keyword": "人工智能", "tag_id": "2027"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-keyword-items', {'end_date': '1735660799', 'keyword': '人工智能', 'tag_id': '2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-keyword-items", {
  "end_date": "1735660799",
  "keyword": "人工智能",
  "tag_id": "2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-keyword-items", sandbase.Params{
	"end_date": "1735660799",
	"keyword": "人工智能",
	"tag_id": "2027",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-keyword-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "1" / "3" / "7" days one of: `1`, `3`, `7` |
| `tag_id` | string | yes | Category ID (same as category_id in fetch_item_query)  |
| `keyword` | string | yes | Hot keyword (typically from fetch_content_creative_keywords)  |
| `end_date` | string | yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3  |

## Details

Look up videos contributing to a trending keyword using `keyword`, category identifier `tag_id`, `end_date`, and an optional `period`.

### Use cases

- Inspect videos that drive volume for a trending creative keyword.
- Analyze creative formats associated with trending terms across categories.
- Track top-performing content over 1, 3, or 7-day intervals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-keyword-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "tag_id": "2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (same as category_id in fetch_item_query) |
| `keyword` | string | Yes | Hot keyword (typically from fetch_content_creative_keywords) |
| `end_date` | string | Yes | End date YYYYMMDD. |
| `period` | string | No | "1" / "3" / "7" days |

### Notes

- `end_date` must be in YYYYMMDD format and must fall on a Sunday when `period` is 7.
- `period` accepts values of 1, 3, or 7 days.
- `tag_id` represents the category ID corresponding to category query endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-keyword-items.json`](../../../../catalog/models/douyin/index/content-creative-keyword-items.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-keyword-items
