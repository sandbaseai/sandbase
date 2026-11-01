# Douyin Brand Radar Chart

`douyin/index/brand-radar-chart` · api · Douyin

Returns multi-dimensional brand radar chart scores across Douyin or Toutiao. Query by brand name and a custom date range in YYYYMMDD format.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-radar-chart", "app_name": "aweme", "brand_name": "华为", "end_date": "20260412", "start_date": "20251015"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-radar-chart', {'app_name': 'aweme', 'brand_name': '华为', 'end_date': '20260412', 'start_date': '20251015'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-radar-chart", {
  "app_name": "aweme",
  "brand_name": "华为",
  "end_date": "20260412",
  "start_date": "20251015"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-radar-chart", sandbase.Params{
	"app_name": "aweme",
	"brand_name": "华为",
	"end_date": "20260412",
	"start_date": "20251015",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-radar-chart` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_name` | string |  | Platform selection one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `brand_name` | string | yes | Brand name  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Query multi-dimensional brand radar score data by specifying `brand_name`, `start_date`, and `end_date`.

### Use cases

- Analyze multi-dimensional performance scores for target brands.
- Compare brand presence across Douyin and Toutiao platforms.
- Track shifts in brand score metrics over custom date intervals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-radar-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_name": "华为", "end_date": "20260412", "start_date": "20251015"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `brand_name` | string | Yes | Brand name |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform selection |

### Notes

- `start_date` and `end_date` require the YYYYMMDD format.
- `app_name` accepts either aweme or toutiao to filter by platform.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-radar-chart.json`](../../../../catalog/models/douyin/index/brand-radar-chart.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-radar-chart
