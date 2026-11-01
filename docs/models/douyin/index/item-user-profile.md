# Douyin Video Audience Profile

`douyin/index/item-user-profile` · api · Douyin

Returns the audience portrait and demographic breakdown for a Douyin video across a specified date range. Filter results using item ID and date parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-user-profile", "end_date": "example", "item_id": "example", "start_date": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-user-profile', {'end_date': 'example', 'item_id': 'example', 'start_date': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-user-profile", {
  "end_date": "example",
  "item_id": "example",
  "start_date": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-user-profile", sandbase.Params{
	"end_date": "example",
	"item_id": "example",
	"start_date": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID (Douyin aweme id, numeric string)  |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Retrieve audience profile data for a specific video by passing `item_id` along with `start_date` and `end_date`.

### Use cases

- Analyze viewer demographics for a specific Douyin video.
- Evaluate audience reach across designated date ranges.
- Compare viewer profiles across different video clips.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "item_id": "7692766887218950514", "start_date": "1730044800"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID (Douyin aweme id, numeric string) |
| `end_date` | string | Yes | End date YYYYMMDD |
| `start_date` | string | Yes | Start date YYYYMMDD |

### Notes

- `item_id` requires a numeric Douyin aweme ID string.
- `start_date` and `end_date` must use the YYYYMMDD format.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-user-profile.json`](../../../../catalog/models/douyin/index/item-user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-user-profile
