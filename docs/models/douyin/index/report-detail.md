# Douyin Trend Report Detail API: pricing, parameters and code examples

`douyin/index/report-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a Douyin trend insight report by report ID, including title, cover image, release time, business tags, body content, image assets, and PDF links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/report-detail", "report_id": "1092"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/report-detail', {'report_id': '1092'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/report-detail", {
  "report_id": "1092"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/report-detail", sandbase.Params{
	"report_id": "1092",
})
```

Same call via the path form: `POST /v1/api/douyin/index/report-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `report_id` | string | yes | Report ID (string), obtained from fetch_report_search or  |

## Details

Retrieve full details and downloadable assets for a Douyin trend insight report using its `report_id`.

### Use cases

- View full text and business tags of Douyin trend insight reports.
- Retrieve PDF download links and image assets for offline analysis.
- Display trend research summaries and covers within internal dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/report-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"report_id": "<report_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `report_id` | string | Yes | Report ID (string), obtained from fetch_report_search or |

### Notes

- Obtain the `report_id` from the report search endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/report-detail.json`](../../../../catalog/models/douyin/index/report-detail.json) · Store page: https://www.sandbase.ai/model/douyin/index/report-detail
