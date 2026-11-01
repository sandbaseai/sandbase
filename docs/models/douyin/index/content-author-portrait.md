# Douyin Content Author Portrait

`douyin/index/content-author-portrait` · api · Douyin

Returns demographic profiles of creators posting within a specific category, including gender, age, region, and activity times based on category ID and selected period.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-author-portrait", "end_date": "1735660799", "tag_id": "2027"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-author-portrait', {'end_date': '1735660799', 'tag_id': '2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-author-portrait", {
  "end_date": "1735660799",
  "tag_id": "2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-author-portrait", sandbase.Params{
	"end_date": "1735660799",
	"tag_id": "2027",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-author-portrait` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "week" (end_date must be a Sunday) or "month" (end_date must be month-end, e.g. 20260331) one of: `week`, `month` |
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD, must align with period  |

## Details

Query creator audience demographics for a specific category using `tag_id`, `end_date`, and `period`.

### Use cases

- Analyze demographic distributions of creators posting in a target category.
- Inspect creator activity schedules across weekly or monthly intervals.
- Evaluate geographic and age profiles of authors for market research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-author-portrait" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "tag_id": "2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (required, does NOT support 0=all, must pass a specific category ID) |
| `end_date` | string | Yes | End date YYYYMMDD, must align with period |
| `period` | string | No | "week" (end_date must be a Sunday) or "month" (end_date must be month-end, e.g. 20260331) |

### Notes

- `tag_id` requires a specific category ID and does not accept 0 for all categories.
- `period` accepts either "week" or "month".
- `end_date` must align with `period` (a Sunday for weekly intervals or the last day of the month for monthly intervals).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-author-portrait.json`](../../../../catalog/models/douyin/index/content-author-portrait.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-author-portrait
