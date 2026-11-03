# Douyin Video Comparison Analysis API: pricing, parameters and code examples

`douyin/index/item-analysis` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comparison analysis and metric trends for a Douyin video relative to benchmarks or similar content over a date range, based on the specified video ID.

## Pricing

- **$0.001 per call** (USD)
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

Returns comparison analysis and metric trends for one Douyin video over a date range. You send the video's `item_id`, a `start_date` and an `end_date`.

### Use cases

- Compare a Douyin video's metric trends against benchmark or similar content.
- Track how a video's metrics change day by day across a chosen week or month.
- Check a video's performance over a campaign window before and after a push.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `item_id` | string | Yes | Video ID (Douyin aweme id, numeric string) |
| `start_date` | string | Yes | Start date YYYYMMDD |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": -1,
    "StatusMessage": "系统异常"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `BaseResp` | Status wrapper for the call. It holds the status code and a status message. |
| `BaseResp.StatusCode` | Numeric status of the call. The sample request returned `-1`, which came with an error message. |
| `BaseResp.StatusMessage` | Text message for the status. The sample request returned `系统异常`, which means system exception. |

### Notes

- `item_id` is the Douyin aweme ID as a numeric string, for example `7660090930283744575`. Use [Douyin Index Video Search](/apis/douyin/index/item-query) to find videos.
- Send `start_date` and `end_date` as `YYYYMMDD` strings, for example `20260704` and `20260710`.
- The sample request for `item_id` `7660090930283744575` from `20260704` to `20260710` returned only a `BaseResp` object with `StatusCode` `-1`. Check the dates with [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date) and retry if you see this.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-analysis.json`](../../../../catalog/models/douyin/index/item-analysis.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-analysis
