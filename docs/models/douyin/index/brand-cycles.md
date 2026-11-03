# Douyin Brand Popularity Cycles API: pricing, parameters and code examples

`douyin/index/brand-cycles` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-cycles", "brand_name": "华为", "end_date": "20260412", "start_date": "20260406"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-cycles', {'brand_name': '华为', 'end_date': '20260412', 'start_date': '20260406'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-cycles", {
  "brand_name": "华为",
  "end_date": "20260412",
  "start_date": "20260406"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-cycles", sandbase.Params{
	"brand_name": "华为",
	"end_date": "20260412",
	"start_date": "20260406",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-cycles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_name` | string |  | Platform one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `brand_name` | string | yes | Brand info  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Returns periodic brand popularity and cycle analysis data for a brand on Douyin. You send `brand_name`, `start_date` and `end_date`, and can set `app_name` to `aweme` or `toutiao`.

### Use cases

- Check how a brand's popularity moves across a chosen week or month.
- Compare a brand's cycle data on `aweme` with the same range on `toutiao`.
- Line up a campaign's dates against the brand's popularity cycles.
- Pull cycle data for several brands over the same date range to compare them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-cycles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_name": "华为", "end_date": "20260412", "start_date": "20260406"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `brand_name` | string | Yes | Brand info |
| `end_date` | string | Yes | End date YYYYMMDD |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform |

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
| `BaseResp` | Status object. It appears in the response from the sample request. |
| `BaseResp.StatusCode` | Numeric status of the call. The sample request returned `-1`, which came with an error message. |
| `BaseResp.StatusMessage` | Text message for the status. The sample request returned `系统异常`, meaning system exception. |

### Notes

- Write `start_date` and `end_date` as YYYYMMDD, for example `20260406`.
- `app_name` accepts `aweme` or `toutiao`. It defaults to `aweme`.
- The sample request for `华为` from `20260406` to `20260412` returned only `BaseResp` with `StatusCode` `-1`. Check this field before you read any data.
- Use [Douyin Brand Search Suggestions](/apis/douyin/index/brand-suggest) to find a brand name to pass as `brand_name`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Hot Videos Time Scope](/apis/douyin/index/brand-hot-videos-time-scope): Returns the queryable time scope for Douyin brand hot videos.

---
Machine-readable: [`catalog/models/douyin/index/brand-cycles.json`](../../../../catalog/models/douyin/index/brand-cycles.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-cycles
