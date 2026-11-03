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

Returns a paged list of trend insight reports from Douyin Index. Each report has a title, type, author, release date, summary, view and download counts, and PDF file links. All inputs are optional, and you can filter by keyword, report type, product, category ID and release year.

### Use cases

- Find Douyin industry reports on a topic such as beauty or technology by passing a `search` keyword.
- Build a list of the newest trend reports by reading `display_time` and paging through `report_list`.
- Compare how often reports are viewed or downloaded to see which research topics draw the most interest.
- Collect the PDF links in `post_files` to archive reports for offline review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/report-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `business` | string | No | comma-separated product list |
| `category` | string | No | top-level category ID, default "6" |
| `current_page` | string | No | Page number |
| `page_size` | string | No | Page size |
| `report_time` | string | No | comma-separated year list, e.g. "2024,2023" |
| `search` | string | No | keyword search |
| `type` | string | No | report type, empty for all |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "report_list": [
    {
      "author": "抖音",
      "business": [
        "抖音"
      ],
      "category": "6",
      "coop_institution": "",
      "cover": [
        {
          "cover_url": "https://lf3-trendinsight.bytetos.com/obj/ad-count-platform/b0ac1d2d984baafc",
          "height": "338",
          "width": "600"
        }
      ],
      "create_user": "8961757",
      "display_time": "2026-06-15",
      "download_cnt": "549",
      "id": "1092",
      "industry": [
        "美妆/日化"
      ],
      "introduction": "2026年抖音美妆春夏宝藏，经过百万用户投稿、专业评审团打分、专业时尚媒体背书三方权威评选，选出TOP120宝藏好物和TOP10宝藏妆容。这个春夏的美妆护肤答案…",
      "keywords": "抖音 时尚 美妆"
    }
  ],
  "total_num": "447"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `report_list[]` | One report per item. The list holds one page of results. |
| `total_num` | Total number of reports that match the filters, returned as a string. Use it to work out how many pages exist. |
| `report_list[].id` | ID of the report. |
| `report_list[].title` | Report title. |
| `report_list[].type` | Report type, such as `行业洞察` (industry insight) or `趋势洞察` (trend insight). |
| `report_list[].display_time` | Release date of the report in `YYYY-MM-DD` format. |
| `report_list[].introduction` | Short summary of the report. It can contain line breaks. |
| `report_list[].industry[] / report_list[].business[]` | Industry tags and product tags attached to the report. Either list can be empty. |
| `visit_cnt / download_cnt` | Number of views and downloads for the report, returned as strings. Both appear under `report_list[]`. |
| `report_list[].post_files[].file_name / post_files[].file_url` | File name and storage path of the report PDF. `file_image` holds a preview image for the file. |

### Notes

- Pass years to `report_time` as a comma-separated list, for example `2024,2023`.
- Leave `type` empty to get all report types. Otherwise use one of `行业洞察`, `产品洞察`, `用户洞察` or `趋势洞察`.
- Page with `current_page` and `page_size`. Compare `total_num` with the page size to know when to stop.
- To open one report, take its `id` and call [Douyin Trend Report Detail](/apis/douyin/index/report-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/report-search.json`](../../../../catalog/models/douyin/index/report-search.json) · Store page: https://www.sandbase.ai/model/douyin/index/report-search
