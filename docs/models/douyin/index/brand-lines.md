# Douyin Brand Trend Lines API: pricing, parameters and code examples

`douyin/index/brand-lines` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns brand trend line metrics and popularity trends over time for a specified brand name and date range across supported platforms.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-lines", "app_name": "aweme", "brand_name": "华为", "end_date": "20260412", "start_date": "20260406"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-lines', {'app_name': 'aweme', 'brand_name': '华为', 'end_date': '20260412', 'start_date': '20260406'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-lines", {
  "app_name": "aweme",
  "brand_name": "华为",
  "end_date": "20260412",
  "start_date": "20260406"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-lines", sandbase.Params{
	"app_name": "aweme",
	"brand_name": "华为",
	"end_date": "20260412",
	"start_date": "20260406",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-lines` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_name` | string |  | Platform one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `brand_name` | string | yes | Brand info  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Fetch historical brand popularity trends by passing `brand_name`, `start_date`, and `end_date`, with an optional `app_name` filter.

### Use cases

- Track brand popularity metrics across Douyin or Toutiao over time.
- Compare brand trend fluctuations within specific date ranges.
- Analyze marketing campaign reach and brand visibility shifts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-lines" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_name": "华为", "end_date": "20260412", "start_date": "20260406"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `brand_name` | string | Yes | Brand info |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform |

### Notes

- `start_date` and `end_date` require date formats in YYYYMMDD.
- `app_name` accepts either aweme or toutiao.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-lines.json`](../../../../catalog/models/douyin/index/brand-lines.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-lines
