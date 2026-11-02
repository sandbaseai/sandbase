# Douyin Video Comparison Analysis API: pricing, parameters and code examples

`douyin/index/item-analysis` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comparison analysis and metric trends for a Douyin video relative to benchmarks or similar content over a date range, based on the specified video ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-analysis", "end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-analysis', {'end_date': '20260710', 'item_id': '7660090930283744575', 'start_date': '20260704'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-analysis", {
  "end_date": "20260710",
  "item_id": "7660090930283744575",
  "start_date": "20260704"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-analysis", sandbase.Params{
	"end_date": "20260710",
	"item_id": "7660090930283744575",
	"start_date": "20260704",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID (Douyin aweme id, numeric string)  |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

This endpoint retrieves comparative performance analysis and trends for a Douyin video identified by `item_id`. Queries require a date window defined by `start_date` and `end_date`.

### Use cases

- Benchmark video performance against similar content.
- Track metric accumulation trends across a specified date range.
- Evaluate engagement indicators for Douyin items over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID (Douyin aweme id, numeric string) |
| `end_date` | string | Yes | End date YYYYMMDD |
| `start_date` | string | Yes | Start date YYYYMMDD |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "detail": {
    "comment_acc": {
      "trend": [
        {
          "datetime": "20260705",
          "value": "0"
        }
      ]
    }
  }
}
```

### Notes

- Pass `item_id` as a numeric Douyin aweme ID string.
- Format `start_date` and `end_date` as YYYYMMDD strings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-analysis.json`](../../../../catalog/models/douyin/index/item-analysis.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-analysis
