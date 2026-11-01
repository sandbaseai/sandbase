# Douyin Content Consumption Trend

`douyin/index/content-consume-trend` · api · Douyin

Returns content consumption metrics such as play counts and watch duration trends over time for a specified Douyin category within a selected date range.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-consume-trend", "end_date": "1735660799", "start_date": "1730044800", "tag_id": "2027"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-consume-trend', {'end_date': '1735660799', 'start_date': '1730044800', 'tag_id': '2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-consume-trend", {
  "end_date": "1735660799",
  "start_date": "1730044800",
  "tag_id": "2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-consume-trend", sandbase.Params{
	"end_date": "1735660799",
	"start_date": "1730044800",
	"tag_id": "2027",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-consume-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD (inclusive)  |
| `start_date` | string | yes | Start date YYYYMMDD (inclusive)  |

## Details

Access category-level consumption heat trends across a date window defined by `start_date` and `end_date` for a specific `tag_id`.

### Use cases

- Track viewership and play count trends for Douyin categories over time.
- Evaluate audience watch duration to measure category viewing heat.
- Compare consumption shifts across distinct date ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-consume-trend" \
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

- `tag_id` requires a specific category ID and does not support 0 for all categories.
- Specify both `start_date` and `end_date` in YYYYMMDD format (inclusive).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-consume-trend.json`](../../../../catalog/models/douyin/index/content-consume-trend.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-consume-trend
