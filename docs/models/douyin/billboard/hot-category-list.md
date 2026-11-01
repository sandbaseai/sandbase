# Douyin Billboard Hot Category List

`douyin/billboard/hot-category-list` · api · Douyin

Returns category IDs and popularity metrics from Douyin hot list billboards. Supports filtering by billboard type, search keywords, and snapshot time ranges.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-category-list", "billboard_type": "rise"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-category-list', {'billboard_type': 'rise'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-category-list", {
  "billboard_type": "rise"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-category-list", sandbase.Params{
	"billboard_type": "rise",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-category-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Hot search term  |
| `end_date` | string |  | Snapshot end time  |
| `start_date` | string |  | Snapshot start time  |
| `snapshot_time` | string |  | Snapshot time  |
| `billboard_type` | string | yes | Billboard type  |

## Details

Retrieve category IDs and popularity data for Douyin hot lists by specifying `billboard_type`. You can also filter categories by `keyword` or snapshot time frames.

### Use cases

- Track popularity metrics across various Douyin hot list categories.
- Filter category trends by snapshot date ranges and specific keywords.
- Identify high-performing Douyin billboard categories for content research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-category-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"billboard_type": "<billboard_type>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `billboard_type` | string | Yes | Billboard type |
| `keyword` | string | No | Hot search term |
| `end_date` | string | No | Snapshot end time |
| `start_date` | string | No | Snapshot start time |
| `snapshot_time` | string | No | Snapshot time |

### Notes

- The `billboard_type` parameter is required.
- Time filters can be applied using `snapshot_time` or a range with `start_date` and `end_date`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-category-list.json`](../../../../catalog/models/douyin/billboard/hot-category-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-category-list
