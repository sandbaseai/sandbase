# Douyin Relation Word Analysis API: pricing, parameters and code examples

`douyin/index/relation-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search and content relation word graphs and rankings for a keyword. Query by target keyword, platform selection, and weekly date intervals.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/relation-word", "end_date": "example", "keyword": "example", "start_date": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/relation-word', {'end_date': 'example', 'keyword': 'example', 'start_date': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/relation-word", {
  "end_date": "example",
  "keyword": "example",
  "start_date": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/relation-word", sandbase.Params{
	"end_date": "example",
	"keyword": "example",
	"start_date": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/relation-word` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The keyword to analyze  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao` |
| `end_date` | string | yes | End date (**must be a Sunday**), format YYYYMMDD  |
| `start_date` | string | yes | Start date (recommend Monday), format YYYYMMDD  |

## Details

This API returns search and content relation word graphs and rankings on Douyin or Toutiao for a keyword. It needs a `keyword`, a `start_date` and an `end_date`. `app_name` is optional and selects the platform.

### Use cases

- Find which words people connect to a topic such as `人工智能` in a given week.
- Compare the related words for one keyword on Douyin (`aweme`) and Toutiao (`toutiao`).
- Check how the word associations around a brand or topic change between weekly periods.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/relation-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "start_date": "1730044800"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date (**must be a Sunday**), format YYYYMMDD |
| `keyword` | string | Yes | The keyword to analyze |
| `start_date` | string | Yes | Start date (recommend Monday), format YYYYMMDD |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 500,
    "StatusMessage": "日期格式需满足%Y%m%d，且关联分析终止日期为周日"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `BaseResp` | Status wrapper that the response returns. Check it first to see whether the call worked. |
| `BaseResp.StatusCode` | Numeric result code. `500` means the request failed, as in the sample response. |
| `BaseResp.StatusMessage` | Text reason for the result. The sample says the date must be in `%Y%m%d` format and the end date must be a Sunday. |

### Notes

- The sample request used values like `1735660799` for `start_date` and `end_date`, and the API rejected them. Send dates as `YYYYMMDD`, for example `20241229`.
- `end_date` must be a Sunday. Use a Monday for `start_date` so the range covers whole weeks.
- Use [Douyin Relation Analysis Valid Dates](/apis/douyin/index/valid-date-for-relation) to find dates that work for relation analysis.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/relation-word.json`](../../../../catalog/models/douyin/index/relation-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/relation-word
