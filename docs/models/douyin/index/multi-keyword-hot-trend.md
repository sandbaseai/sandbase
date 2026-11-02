# Douyin Multi Keyword Hot Trend API: pricing, parameters and code examples

`douyin/index/multi-keyword-hot-trend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0045 per call (free daily quota) · **Modes:** sync

Returns hot trend data for multiple keywords over a specified date range. Filter by platform and geographical region to compare trend metrics.

## Pricing

- **$0.0045 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/multi-keyword-hot-trend", "app_name": "aweme", "end_date": "20260922", "keyword_list": "车载防水折叠垃圾桶 悬挂式,汽车座椅缝隙储物盒,车门内侧水杯架 卡扣式,免打孔承重挂钩,厨房洞洞板挂架 调料收纳,创意牙签盒 棉签盒,收纳盒,手工编织收纳筐,束口收纳袋,布艺收纳笔筒", "region": "", "start_date": "20260729"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/multi-keyword-hot-trend', {'app_name': 'aweme', 'end_date': '20260922', 'keyword_list': '车载防水折叠垃圾桶 悬挂式,汽车座椅缝隙储物盒,车门内侧水杯架 卡扣式,免打孔承重挂钩,厨房洞洞板挂架 调料收纳,创意牙签盒 棉签盒,收纳盒,手工编织收纳筐,束口收纳袋,布艺收纳笔筒', 'region': '', 'start_date': '20260729'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/multi-keyword-hot-trend", {
  "app_name": "aweme",
  "end_date": "20260922",
  "keyword_list": "车载防水折叠垃圾桶 悬挂式,汽车座椅缝隙储物盒,车门内侧水杯架 卡扣式,免打孔承重挂钩,厨房洞洞板挂架 调料收纳,创意牙签盒 棉签盒,收纳盒,手工编织收纳筐,束口收纳袋,布艺收纳笔筒",
  "region": "",
  "start_date": "20260729"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/multi-keyword-hot-trend", sandbase.Params{
	"app_name": "aweme",
	"end_date": "20260922",
	"keyword_list": "车载防水折叠垃圾桶 悬挂式,汽车座椅缝隙储物盒,车门内侧水杯架 卡扣式,免打孔承重挂钩,厨房洞洞板挂架 调料收纳,创意牙签盒 棉签盒,收纳盒,手工编织收纳筐,束口收纳袋,布艺收纳笔筒",
	"region": "",
	"start_date": "20260729",
})
```

Same call via the path form: `POST /v1/api/douyin/index/multi-keyword-hot-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region list, comma separated  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao` |
| `end_date` | string | yes | End date, format YYYYMMDD  |
| `start_date` | string | yes | Start date, format YYYYMMDD  |
| `keyword_list` | string | yes | Keyword list, comma separated  |

## Details

Query hot trend index metrics for multiple search terms using `keyword_list`, `start_date`, and `end_date`.

### Use cases

- Compare popularity trends across multiple related keywords over time.
- Analyze search momentum on Douyin or Toutiao platforms.
- Evaluate regional interest patterns for targeted keyword sets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/multi-keyword-hot-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "<end_date>", "keyword_list": "<keyword_list>", "start_date": "<start_date>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date, format YYYYMMDD |
| `start_date` | string | Yes | Start date, format YYYYMMDD |
| `keyword_list` | string | Yes | Keyword list, comma separated |
| `region` | string | No | Region list, comma separated |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Notes

- Set `app_name` to `aweme` for Douyin or `toutiao` for Toutiao.
- Specify dates in YYYYMMDD format using `start_date` and `end_date`.
- Provide multiple entries as comma-separated strings for `keyword_list` and `region`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/multi-keyword-hot-trend.json`](../../../../catalog/models/douyin/index/multi-keyword-hot-trend.json) · Store page: https://www.sandbase.ai/model/douyin/index/multi-keyword-hot-trend
