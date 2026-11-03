# Douyin Content Consumer Portrait API: pricing, parameters and code examples

`douyin/index/content-consumer-portrait` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns consumer viewer portrait data for audience members watching videos in a specified Douyin category over a given week or month.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-consumer-portrait", "end_date": "example", "tag_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-consumer-portrait', {'end_date': 'example', 'tag_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-consumer-portrait", {
  "end_date": "example",
  "tag_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-consumer-portrait", sandbase.Params{
	"end_date": "example",
	"tag_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-consumer-portrait` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "week" (end_date must be a Sunday) or "month" (end_date must be month-end, e.g. 20260331) one of: `week`, `month` |
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD, must align with period  |

## Details

Fetch demographic and viewer profile data for users who consume content in a category using `tag_id` and `end_date`.

### Use cases

- Analyze the viewer demographic breakdown for a specific video category.
- Evaluate consumer audience shifts across weekly or monthly reporting cycles.
- Compare Douyin category viewership profiles against content creator personas.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-consumer-portrait" \
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

- The `tag_id` parameter is required and does not accept 0; a specific category identifier is necessary.
- When `period` is set to "week", `end_date` must fall on a Sunday.
- When `period` is set to "month", `end_date` must be the final day of that month.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-consumer-portrait.json`](../../../../catalog/models/douyin/index/content-consumer-portrait.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-consumer-portrait
