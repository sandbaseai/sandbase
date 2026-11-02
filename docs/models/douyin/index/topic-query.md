# Douyin Topic Search API: pricing, parameters and code examples

`douyin/index/topic-query` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns Douyin topic performance metrics matching a search term over a specific date range, including item counts, like counts, and view counts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/topic-query", "app_name": "aweme", "end_date": "20260412", "keyword": "人工智能", "start_date": "20260406"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/topic-query', {'app_name': 'aweme', 'end_date': '20260412', 'keyword': '人工智能', 'start_date': '20260406'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/topic-query", {
  "app_name": "aweme",
  "end_date": "20260412",
  "keyword": "人工智能",
  "start_date": "20260406"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/topic-query", sandbase.Params{
	"app_name": "aweme",
	"end_date": "20260412",
	"keyword": "人工智能",
	"start_date": "20260406",
})
```

Same call via the path form: `POST /v1/api/douyin/index/topic-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Topic keyword  |
| `app_name` | string |  | Platform one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Query topic metrics on Douyin by submitting a `keyword` alongside `start_date` and `end_date` date filters.

### Use cases

- Track engagement and total views for specific trend topics.
- Compare topic volume across Aweme and Toutiao platforms.
- Retrieve topic identifiers for historical performance monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/topic-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260412", "keyword": "人工智能", "start_date": "20260406"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Topic keyword |
| `end_date` | string | Yes | End date YYYYMMDD |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "topic_list": [
    {
      "digg_cnt": "3886643",
      "item_cnt": "26313",
      "play_read_cnt": "201528869",
      "topic_id": "1576073697445901",
      "topic_name": "人工智能"
    }
  ]
}
```

### Notes

- `start_date` and `end_date` must be formatted as YYYYMMDD.
- `app_name` filters by platform and supports `aweme` or `toutiao`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/topic-query.json`](../../../../catalog/models/douyin/index/topic-query.json) · Store page: https://www.sandbase.ai/model/douyin/index/topic-query
