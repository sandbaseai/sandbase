# Douyin Multi-Keyword Index Interpretation API: pricing, parameters and code examples

`douyin/index/multi-keyword-interpretation` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns index interpretation metrics for multiple keywords across selected time periods. Includes comparison metrics like period-over-period and year-over-year differences.

## Pricing

- **$0.001 per call** (USD)
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

Returns index metrics for each keyword in a comma separated list over a date range. Each keyword gets search, content and consume index values for the current period and the previous period, plus percentage differences against the previous period and the same period last year. It needs `keyword_list`, `start_date` and `end_date`.

### Use cases

- Compare search interest in two brand names such as `华为` and `人工智能` over the same half-year window.
- Check whether content volume for a topic fell or rose against the previous period before planning a video campaign.
- Spot keywords whose consume index grew year over year while their content index dropped.
- Build a dashboard table that ranks a keyword set by search index change.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/multi-keyword-interpretation" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260412", "keyword_list": "人工智能,华为", "start_date": "20251015"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date, YYYYMMDD |
| `keyword_list` | string | Yes | Comma separated keywords |
| `start_date` | string | Yes | Start date, YYYYMMDD |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |
| `region` | string | No | Region filter, comma separated, empty for all |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "keyword_index_interpretations": [
    {
      "current_period": {
        "consume_index": "12721157",
        "content_index": "5864262",
        "search_index": "345391408"
      },
      "keyword": "华为",
      "last_period": {
        "consume_index": "11416262",
        "content_index": "12861878",
        "search_index": "339348518"
      },
      "last_period_diff": {
        "consume_diff": 0.11430142370593815,
        "content_diff": -0.5440586514659833,
        "search_diff": 0.017807326920461233
      },
      "last_year_diff": {
        "consume_diff": 0.054911176596635455,
        "content_diff": -0.7390276463913172,
        "search_diff": -0.0010165791323027082
      },
      "overview": {
        "consume_index": 12721157,
        "content_index": 5864262,
        "search_index": 345391408
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword_index_interpretations[].keyword` | The keyword these metrics belong to. The list has one entry per keyword in the request. |
| `keyword_index_interpretations[].current_period.search_index / content_index / consume_index` | Search, content and consume index for the requested date range. Values are strings. |
| `keyword_index_interpretations[].last_period.search_index / content_index / consume_index` | The same three indexes for the previous period, used as the baseline for the period-over-period difference. |
| `keyword_index_interpretations[].last_period_diff.search_diff / content_diff / consume_diff` | Change against the previous period as a decimal ratio. For example `0.114` means about 11.4% higher, and `-0.544` means about 54.4% lower. |
| `keyword_index_interpretations[].last_year_diff.search_diff / content_diff / consume_diff` | Change against the same period last year, as a decimal ratio. Negative values mean a decline. |
| `keyword_index_interpretations[].overview.search_index / content_index / consume_index` | The current period indexes as numbers instead of strings. They match the `current_period` values. |
| `BaseResp.StatusCode` | Status of the call. `0` appears in the sample response, with an empty `StatusMessage`. |

### Notes

- Separate keywords with commas in `keyword_list`, for example `人工智能,华为`.
- Write `start_date` and `end_date` as `YYYYMMDD`, for example `20251015`.
- Set `app_name` to `aweme` for Douyin (default) or `toutiao` for Toutiao. Leave `region` empty for all regions.
- Call [Douyin Index Keyword Valid Dates](/apis/douyin/index/keyword-valid-date) to check which dates are valid, and [Douyin Index Area List](/apis/douyin/index/all-area) for `region` values.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/multi-keyword-interpretation.json`](../../../../catalog/models/douyin/index/multi-keyword-interpretation.json) · Store page: https://www.sandbase.ai/model/douyin/index/multi-keyword-interpretation
