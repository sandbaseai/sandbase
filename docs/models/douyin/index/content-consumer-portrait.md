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

Returns viewer portrait data for the audience watching videos in one Douyin category over a week or a month. You send a specific `tag_id` and an `end_date`, and you can set `period` to `week` or `month`.

### Use cases

- Check who watches a single Douyin video category before you plan content for it.
- Compare the viewer portrait of one category across weekly or monthly periods.
- Pull the audience profile of a category to support a brand or ad targeting brief.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-consumer-portrait" \
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
| `period` | string | No | "week" (end_date must be a Sunday) or "month" (end_date must be month-end, e.g. 20260331) |

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
| `BaseResp` | Status block returned with the request result. |
| `BaseResp.StatusCode` | Result code. The sample call returned `-1`, which marks a failed request. |
| `BaseResp.StatusMessage` | Text reason for the result. The sample call returned a message saying `end_date` is not the last day of the current period. |

### Notes

- The sample call failed because `end_date` was `1735660799`, which is not a `YYYYMMDD` date. Send a value such as `20260331`.
- With `period` set to `week`, `end_date` must be a Sunday. With `period` set to `month`, `end_date` must be the last day of the month.
- `tag_id` must be a specific category ID. The value `0` for all categories is not accepted.
- To find dates that have data, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-consumer-portrait.json`](../../../../catalog/models/douyin/index/content-consumer-portrait.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-consumer-portrait
