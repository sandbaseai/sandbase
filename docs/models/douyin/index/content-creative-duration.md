# Douyin Content Creative Duration

`douyin/index/content-creative-duration` · api · Douyin

Returns the video duration distribution for a specified Douyin category. Breaks down content duration patterns across weekly or monthly periods.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-duration", "end_date": "example", "tag_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-duration', {'end_date': 'example', 'tag_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-duration", {
  "end_date": "example",
  "tag_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-duration", sandbase.Params{
	"end_date": "example",
	"tag_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-duration` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "week" (end_date must be a Sunday) or "month" (end_date must be month-end) one of: `week`, `month` |
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD, must align with period  |

## Details

Query video length distribution metrics for a specific Douyin category using `tag_id`, `end_date`, and optional `period`.

### Use cases

- Analyze preferred video lengths for creators within a target category.
- Benchmark video duration patterns across weekly or monthly reporting windows.
- Identify optimal video runtimes based on category-level creative trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-duration" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "tag_id": "2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (required, does NOT support 0=all, must pass a specific category ID) |
| `end_date` | string | Yes | End date YYYYMMDD, must align with period |
| `period` | string | No | "week" (end_date must be a Sunday) or "month" (end_date must be month-end) |

### Notes

- `tag_id` requires a specific category ID and does not support 0 for all categories.
- `end_date` must be formatted as YYYYMMDD and align with `period` (Sunday for week, month-end for month).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-duration.json`](../../../../catalog/models/douyin/index/content-creative-duration.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-duration
