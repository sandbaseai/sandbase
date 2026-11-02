# Douyin Relation Word Analysis API: pricing, parameters and code examples

`douyin/index/relation-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns search and content relation word graphs and rankings for a keyword. Query by target keyword, platform selection, and weekly date intervals.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve search and content relation word analysis for a target `keyword` across Douyin or Toutiao. Provide `start_date` and `end_date` to define the analysis period.

### Use cases

- Analyze search and content keywords associated with a specific term.
- Map relation word graphs to identify emerging topic associations.
- Compare keyword relations across Douyin and Toutiao platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/relation-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "start_date": "1730044800"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The keyword to analyze |
| `end_date` | string | Yes | End date (must be a Sunday), format YYYYMMDD |
| `start_date` | string | Yes | Start date (recommend Monday), format YYYYMMDD |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Notes

- `end_date` must be a Sunday in YYYYMMDD format, with `start_date` recommended to be a Monday.
- Set `app_name` to `aweme` for Douyin or `toutiao` for Toutiao.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/relation-word.json`](../../../../catalog/models/douyin/index/relation-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/relation-word
