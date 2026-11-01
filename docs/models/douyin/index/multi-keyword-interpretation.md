# Douyin Multi-Keyword Index Interpretation

`douyin/index/multi-keyword-interpretation` · api · Douyin

Returns index interpretation metrics for multiple keywords across selected time periods. Includes comparison metrics like period-over-period and year-over-year differences.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/multi-keyword-interpretation", "app_name": "aweme", "end_date": "20260412", "keyword_list": "人工智能,华为", "region": "", "start_date": "20251015"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/multi-keyword-interpretation', {'app_name': 'aweme', 'end_date': '20260412', 'keyword_list': '人工智能,华为', 'region': '', 'start_date': '20251015'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/multi-keyword-interpretation", {
  "app_name": "aweme",
  "end_date": "20260412",
  "keyword_list": "人工智能,华为",
  "region": "",
  "start_date": "20251015"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/multi-keyword-interpretation", sandbase.Params{
	"app_name": "aweme",
	"end_date": "20260412",
	"keyword_list": "人工智能,华为",
	"region": "",
	"start_date": "20251015",
})
```

Same call via the path form: `POST /v1/api/douyin/index/multi-keyword-interpretation` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region filter, comma separated, empty for all default `""` |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date, YYYYMMDD  |
| `start_date` | string | yes | Start date, YYYYMMDD  |
| `keyword_list` | string | yes | Comma separated keywords  |

## Details

Fetch comparative index interpretation data for multiple topics by supplying `keyword_list`, `start_date`, and `end_date`.

### Use cases

- Compare content index changes between current and previous periods for multiple topics.
- Monitor year-over-year search and content index differences for targeted brand terms.
- Track trend performance across Douyin and Toutiao platforms simultaneously.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/multi-keyword-interpretation" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260412", "keyword_list": "人工智能,华为", "start_date": "20251015"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date, YYYYMMDD |
| `start_date` | string | Yes | Start date, YYYYMMDD |
| `keyword_list` | string | Yes | Comma separated keywords |
| `region` | string | No | Region filter, comma separated, empty for all |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword_index_interpretations": [
    {
      "keyword": "人工智能",
      "current_period": {
        "content_index": "6286798"
      },
      "last_period": {
        "content_index": "22432607"
      },
      "last_period_diff": {
        "content_diff": -0.7197473303036067
      },
      "last_year_diff": {
        "content_diff": -0.29883205556881526
      },
      "overview": {
        "content_index": 6286798
      }
    }
  ]
}
```

### Notes

- Set `app_name` to "aweme" for Douyin or "toutiao" for Toutiao.
- Pass multiple terms in `keyword_list` as a comma-separated string.
- Use `region` with comma-separated values to filter by specific geographic areas, or leave it empty for all regions.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/multi-keyword-interpretation.json`](../../../../catalog/models/douyin/index/multi-keyword-interpretation.json) · Store page: https://www.sandbase.ai/model/douyin/index/multi-keyword-interpretation
