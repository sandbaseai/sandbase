# Douyin Index Keyword Valid Dates API: pricing, parameters and code examples

`douyin/index/keyword-valid-date` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the valid date ranges available for specified search terms in the Douyin Index. Queries accept a comma-separated list of keywords to identify data availability periods.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/keyword-valid-date", "keyword_list": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/keyword-valid-date', {'keyword_list': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/keyword-valid-date", {
  "keyword_list": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/keyword-valid-date", sandbase.Params{
	"keyword_list": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/keyword-valid-date` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword_list` | string | yes | Keyword list, comma separated  |

## Details

Returns Douyin Index date availability for each keyword you send. It needs `keyword_list`, a comma-separated string of search terms. The response is keyed by keyword and gives a valid day and a valid week day for each one.

### Use cases

- Check the valid day for a keyword before you request its index trend.
- Check the valid week day for a keyword before you run a weekly query.
- Compare `origin_keyword` with `real_keyword` to see whether a keyword text changed.
- Check several tracked keywords in one call to set the date limits of a date picker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/keyword-valid-date" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_list": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword_list` | string | Yes | Keyword list, comma separated |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "人工智能": {
    "keyword_types": [
      0
    ],
    "origin_keyword": "人工智 能",
    "real_keyword": "人工智能",
    "status": 0,
    "valid_category_list": [],
    "valid_day": "20211018",
    "valid_week_day": "20211024"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `人工智能.valid_day` | Valid date for daily data, in `YYYYMMDD` format. The sample value is `20211018`. The top-level key is the keyword you sent. |
| `人工智能.valid_week_day` | Valid date for weekly data, in `YYYYMMDD` format. The sample value is `20211024`. |
| `人工智能.origin_keyword` | The original keyword text. In the sample it is `人工智 能`, with a space inside the term, although the request had none. |
| `人工智能.real_keyword` | The keyword text used for the lookup. In the sample it is `人工智能`, without a space. |
| `人工智能.keyword_types` | List of numeric type codes for the keyword. The sample contains `0`. The response does not explain what each code means. |
| `人工智能.status` | Numeric status code for the keyword. The sample returns `0`. |
| `人工智能.valid_category_list` | List of valid categories for the keyword. It is empty in the sample. |

### Notes

- The response has one top-level object per keyword, named after that keyword. The sample uses `人工智能`.
- Send several terms in one call by joining them with commas in `keyword_list`.
- `valid_day` and `valid_week_day` are strings in `YYYYMMDD` format.
- To see the latest valid dates for each Douyin Index data type, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/keyword-valid-date.json`](../../../../catalog/models/douyin/index/keyword-valid-date.json) · Store page: https://www.sandbase.ai/model/douyin/index/keyword-valid-date
