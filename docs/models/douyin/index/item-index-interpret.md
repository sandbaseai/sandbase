# Douyin Video Index Interpretation

`douyin/index/item-index-interpret` · api · Douyin

Returns index breakdown metrics for a specified Douyin video across a date range. It provides sub-index interpretations using a video ID with start and end dates.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-index-interpret", "end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-index-interpret', {'end_date': '20260710', 'item_id': '7660090930283744575', 'start_date': '20260704'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-index-interpret", {
  "end_date": "20260710",
  "item_id": "7660090930283744575",
  "start_date": "20260704"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-index-interpret", sandbase.Params{
	"end_date": "20260710",
	"item_id": "7660090930283744575",
	"start_date": "20260704",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-index-interpret` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID (Douyin aweme id, numeric string)  |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Fetch index breakdown details for a Douyin video by providing the `item_id`, `start_date`, and `end_date`.

### Use cases

- Analyze sub-index breakdowns for a specific Douyin video.
- Track video index performance across a defined date window.
- Pair with video index queries to interpret metric changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-index-interpret" \
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

### Notes

- The `item_id` corresponds to the Douyin aweme ID as a numeric string.
- Dates for `start_date` and `end_date` must follow the YYYYMMDD format.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-index-interpret.json`](../../../../catalog/models/douyin/index/item-index-interpret.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-index-interpret
