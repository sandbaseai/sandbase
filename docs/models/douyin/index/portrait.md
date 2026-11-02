# Douyin Keyword Crowd Portrait API: pricing, parameters and code examples

`douyin/index/portrait` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns crowd portrait analysis for a specific keyword over a defined date range. Allows querying data for Douyin or Toutiao platforms.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/portrait", "end_date": "example", "keyword": "example", "start_date": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/portrait', {'end_date': 'example', 'keyword': 'example', 'start_date': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/portrait", {
  "end_date": "example",
  "keyword": "example",
  "start_date": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/portrait", sandbase.Params{
	"end_date": "example",
	"keyword": "example",
	"start_date": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/portrait` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The keyword to analyze  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Query crowd portrait metrics for a targeted `keyword` across a timeframe set by `start_date` and `end_date`.

### Use cases

- Analyze audience demographics interested in specific search terms.
- Compare audience interest between Douyin and Toutiao platforms.
- Evaluate keyword audience trends across selected date ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/portrait" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "start_date": "1730044800"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The keyword to analyze |
| `end_date` | string | Yes | End date YYYYMMDD |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Notes

- The `app_name` parameter supports `aweme` for Douyin and `toutiao` for Toutiao.
- Both `start_date` and `end_date` require the YYYYMMDD date format.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/portrait.json`](../../../../catalog/models/douyin/index/portrait.json) · Store page: https://www.sandbase.ai/model/douyin/index/portrait
