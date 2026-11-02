# Douyin Trend Report Search API: pricing, parameters and code examples

`douyin/index/report-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trend insight reports from Douyin Index. Supports filtering by keyword, report type, product line, category ID, and release year.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/report-search", "business": "", "category": "6", "current_page": "1", "page_size": "16", "report_time": "", "search": "", "type": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/report-search', {'business': '', 'category': '6', 'current_page': '1', 'page_size': '16', 'report_time': '', 'search': '', 'type': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/report-search", {
  "business": "",
  "category": "6",
  "current_page": "1",
  "page_size": "16",
  "report_time": "",
  "search": "",
  "type": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/report-search", sandbase.Params{
	"business": "",
	"category": "6",
	"current_page": "1",
	"page_size": "16",
	"report_time": "",
	"search": "",
	"type": "",
})
```

Same call via the path form: `POST /v1/api/douyin/index/report-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | report type, empty for all one of: ``, `行业洞察`, `产品洞察`, `用户洞察`, `趋势洞察`; default `""` |
| `search` | string |  | keyword search default `""` |
| `business` | string |  | comma-separated product list default `""` |
| `category` | string |  | top-level category ID, default "6" default `"6"` |
| `page_size` | string |  | Page size default `"16"` |
| `report_time` | string |  | comma-separated year list, e.g. "2024,2023" default `""` |
| `current_page` | string |  | Page number default `"1"` |

## Details

Queries trend insight reports from Douyin Index using `search` keywords, `type`, and `report_time` filters.

### Use cases

- Discover industry and consumer insight reports published on Douyin.
- Filter historical trend research by release year and category ID.
- Search report titles and metadata for marketing intelligence.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/report-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | string | No | report type, empty for all |
| `search` | string | No | keyword search |
| `business` | string | No | comma-separated product list |
| `category` | string | No | top-level category ID, default "6" |
| `page_size` | string | No | Page size |
| `report_time` | string | No | comma-separated year list, e.g. "2024,2023" |
| `current_page` | string | No | Page number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "report_list": [
    {
      "author": "抖音",
      "category": "6",
      "display_time": "2026-06-15",
      "id": "1092",
      "keywords": "抖音 时尚 美妆",
      "title": "2026年抖音美妆春夏宝藏",
      "type": "行业洞察",
      "visit_cnt": "2979"
    }
  ]
}
```

### Notes

- Specify multiple release years as a comma-separated list in `report_time`.
- Leave `type` empty to return all report types, or specify a single category.
- Manage pagination using `current_page` and `page_size`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/report-search.json`](../../../../catalog/models/douyin/index/report-search.json) · Store page: https://www.sandbase.ai/model/douyin/index/report-search
