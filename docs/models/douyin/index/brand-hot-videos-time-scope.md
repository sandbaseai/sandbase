# Douyin Brand Hot Videos Time Scope API: pricing, parameters and code examples

`douyin/index/brand-hot-videos-time-scope` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the queryable time scope for Douyin brand hot videos. Allows systems to check valid date ranges before querying related brand analytics endpoints.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-hot-videos-time-scope"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-hot-videos-time-scope', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-hot-videos-time-scope", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-hot-videos-time-scope", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-hot-videos-time-scope` with the body above minus `model`.

## Details

Returns the date range you can query for Douyin brand hot videos. It needs no input. The response gives the first and last week of the range and the latest available day.

### Use cases

- Read `latest_day` to set the default end date in a brand hot video report.
- Limit a date picker to the range from `start_week` to `end_week`.
- Check a requested date against the range before you call a brand analytics endpoint.
- Run the call on a schedule to see when the range moves forward.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-hot-videos-time-scope" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "end_week": "20261101",
  "latest_day": "20261101",
  "start_week": "20260809"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `start_week` | First date of the queryable range, written as `YYYYMMDD` (for example `20260809`). |
| `end_week` | Last date of the queryable range, written as `YYYYMMDD`. |
| `latest_day` | Most recent day in the range, written as `YYYYMMDD`. |
| `BaseResp.StatusCode` | Status code of the call. `0` means the call succeeded. |
| `BaseResp.StatusMessage` | Status text. It is an empty string when the call succeeds. |

### Notes

- Send an empty JSON object `{}` as the body. The API has no request parameters.
- All dates use the compact `YYYYMMDD` format with no separators.
- For other valid date ranges in Douyin Index, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date).
- To look up a brand before you query its data, call [Douyin Brand Search Suggestions](/apis/douyin/index/brand-suggest).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-hot-videos-time-scope.json`](../../../../catalog/models/douyin/index/brand-hot-videos-time-scope.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-hot-videos-time-scope
