# Douyin Content Creative Topics API: pricing, parameters and code examples

`douyin/index/content-creative-topic` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending creative topics for a specific Douyin category. Filter results by category ID, evaluation period, ranking metric, and end date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-topic", "end_date": "20260405", "tag_id": "601"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-topic', {'end_date': '20260405', 'tag_id': '601'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-topic", {
  "end_date": "20260405",
  "tag_id": "601"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-topic", sandbase.Params{
	"end_date": "20260405",
	"tag_id": "601",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-topic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "1" / "3" / "7" one of: `1`, `3`, `7`; default `"7"` |
| `tag_id` | string | yes | Category ID (same as category_id in fetch_item_query)  |
| `end_date` | string | yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3  |
| `rank_type` | string |  | "index" or "rise" one of: `index`, `rise`; default `"index"` |

## Details

Fetch trending creative topics within a specific Douyin category by providing a `tag_id` and an `end_date`.

### Use cases

- Identify trending video topics within a target category.
- Track topic performance metrics like item count and like counts.
- Analyze rising versus overall indexed content themes over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-topic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260405", "tag_id": "601"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (same as category_id in fetch_item_query) |
| `end_date` | string | Yes | End date YYYYMMDD. |
| `period` | string | No | "1" / "3" / "7" |
| `rank_type` | string | No | "index" or "rise" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "topic_list": [
    {
      "digg_cnt": "171445435",
      "id": "1635669004810253",
      "item_cnt": "19739286",
      "name": "搞笑"
    }
  ]
}
```

### Notes

- The `end_date` must be formatted as YYYYMMDD and must fall on a Sunday when `period` is set to "7".
- `tag_id` corresponds to the category ID used in query operations.
- `rank_type` accepts either "index" or "rise".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-topic.json`](../../../../catalog/models/douyin/index/content-creative-topic.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-topic
