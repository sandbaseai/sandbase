# Douyin Content Volume Trend API: pricing, parameters and code examples

`douyin/index/content-publish-trend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns content posting volume trends over time for a specified category. Requires a category identifier alongside inclusive start and end dates.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-publish-trend", "end_date": "20260927", "start_date": "20260901", "tag_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-publish-trend', {'end_date': '20260927', 'start_date': '20260901', 'tag_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-publish-trend", {
  "end_date": "20260927",
  "start_date": "20260901",
  "tag_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-publish-trend", sandbase.Params{
	"end_date": "20260927",
	"start_date": "20260901",
	"tag_id": "1",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-publish-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD (inclusive)  |
| `start_date` | string | yes | Start date YYYYMMDD (inclusive)  |

## Details

Retrieves category-level content posting volume trends for Douyin over a designated timeframe using `tag_id`, `start_date`, and `end_date`.

### Use cases

- Track content supply heat fluctuations for specific categories over time.
- Compare posting frequency across different time windows.
- Analyze category momentum and video upload dynamics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-publish-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "start_date": "1730044800", "tag_id": "2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (required, does NOT support 0=all, must pass a specific category ID) |
| `end_date` | string | Yes | End date YYYYMMDD (inclusive) |
| `start_date` | string | Yes | Start date YYYYMMDD (inclusive) |

### Notes

- `tag_id` requires a specific category identifier and does not support 0 for all categories.
- `start_date` and `end_date` must be formatted as YYYYMMDD and are inclusive.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-publish-trend.json`](../../../../catalog/models/douyin/index/content-publish-trend.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-publish-trend
