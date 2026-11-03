# Douyin Content Creative Duration API: pricing, parameters and code examples

`douyin/index/content-creative-duration` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the video duration distribution for a specified Douyin category. Breaks down content duration patterns across weekly or monthly periods.

## Pricing

- **$0.001 per call** (USD)
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

Returns the video duration distribution for one Douyin category over a week or a month. You send a category `tag_id`, an `end_date`, and optionally a `period`.

### Use cases

- Check which video length ranges are most common in a single Douyin category.
- Compare duration patterns between a weekly window and a monthly window for the same category.
- Plan video runtimes for a category using its recent duration mix.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-duration" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "tag_id": "2027"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD, must align with period |
| `tag_id` | string | Yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID) |
| `period` | string | No | "week" (end_date must be a Sunday) or "month" (end_date must be month-end) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": -1,
    "StatusMessage": "end_date非当前周期最后一天"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `BaseResp` | Status block for the call. The response you get when the request is rejected contains only this object. |
| `BaseResp.StatusCode` | Result code. `-1` means the request failed. A failed call returns no duration data. |
| `BaseResp.StatusMessage` | Reason for the failure, in Chinese. The value `end_date非当前周期最后一天` means `end_date` is not the last day of the period. |

### Notes

- The sample request with `end_date` set to `1735660799` returned `StatusCode` `-1`. Send `end_date` as `YYYYMMDD` instead, for example `20241229`.
- With `period` set to `week`, `end_date` must be a Sunday. With `month`, it must be the last day of the month.
- `tag_id` must be a specific category ID. `0` for all categories is not accepted.
- To find dates that have data, call [Douyin Content Guide Valid Dates](/apis/douyin/index/content-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-duration.json`](../../../../catalog/models/douyin/index/content-creative-duration.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-duration
