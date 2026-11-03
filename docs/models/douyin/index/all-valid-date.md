# Douyin Index Valid Dates API: pricing, parameters and code examples

`douyin/index/all-valid-date` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the latest valid dates available for each data type in Douyin Index. Helps verify data availability before querying index metrics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/all-valid-date"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/all-valid-date', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/all-valid-date", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/all-valid-date", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/all-valid-date` with the body above minus `model`.

## Details

Returns the latest valid date for each data type in Douyin Index, split into brand, keyword and POI groups. It needs no input. Call it with an empty JSON body `{}`.

### Use cases

- Check that the newest day is available for keyword data before you request a keyword trend.
- Pick the latest weekly date for brand data when you build a weekly brand report.
- Use the monthly POI date to choose the end month for a POI query.
- Run it at the start of a scheduled job to set the end date of each query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/all-valid-date" \
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
  "brand_latest_day": "20261102",
  "brand_latest_week": "20261024",
  "keyword_latest_day": "20261102",
  "keyword_latest_week": "20261102",
  "poi_latest_day": "20261101",
  "poi_latest_month": "202610",
  "poi_latest_week": "20261101"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `brand_latest_day / brand_latest_week` | Latest valid day and latest valid week for brand data. |
| `keyword_latest_day / keyword_latest_week` | Latest valid day and latest valid week for keyword data. |
| `poi_latest_day / poi_latest_week` | Latest valid day and latest valid week for POI data. |
| `poi_latest_month` | Latest valid month for POI data. |
| `BaseResp.StatusCode` | Status code of the call. `0` appears in a normal response. |
| `BaseResp.StatusMessage` | Status text of the call. It is an empty string in a normal response. |

### Notes

- Day and week values use the `YYYYMMDD` format, for example `20261102`. The month value uses `YYYYMM`, for example `202610`.
- The week values are dates, not week numbers. In the sample, `brand_latest_week` is `20261024` while `keyword_latest_week` is `20261102`, so the data types differ.
- For keyword-specific dates, call [Douyin Index Keyword Valid Dates](/apis/douyin/index/keyword-valid-date). For brand-specific dates, call [Douyin Brand Valid Information](/apis/douyin/index/brand-valid-info).
- For content guide dates, call [Douyin Content Guide Valid Dates](/apis/douyin/index/content-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.
- [Douyin Brand Hot Videos Time Scope](/apis/douyin/index/brand-hot-videos-time-scope): Returns the queryable time scope for Douyin brand hot videos.

---
Machine-readable: [`catalog/models/douyin/index/all-valid-date.json`](../../../../catalog/models/douyin/index/all-valid-date.json) · Store page: https://www.sandbase.ai/model/douyin/index/all-valid-date
