# Douyin Content Creative Keywords API: pricing, parameters and code examples

`douyin/index/content-creative-keywords` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creative hot keywords for a specified category from the Douyin index. Filter keywords by category ID, end date, and time intervals of one, three, or seven days.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-keywords", "end_date": "example", "tag_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-keywords', {'end_date': 'example', 'tag_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-keywords", {
  "end_date": "example",
  "tag_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-keywords", sandbase.Params{
	"end_date": "example",
	"tag_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "1"=last 1 day, "3"=last 3 days, "7"=last 7 days one of: `1`, `3`, `7` |
| `tag_id` | string | yes | Category ID (same as category_id in fetch_item_query)  |
| `end_date` | string | yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3  |

## Details

Use this endpoint to inspect trending creative keywords for a Douyin category by supplying `tag_id` and `end_date`. You can also adjust the timeframe using `period`.

### Use cases

- Discover trending creative topics within specific Douyin categories.
- Track keyword momentum over 1-day, 3-day, or 7-day intervals.
- Gather content ideation signals for targeted video categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "tag_id": "2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | string | Yes | Category ID (same as category_id in fetch_item_query) |
| `end_date` | string | Yes | End date YYYYMMDD. |
| `period` | string | No | "1"=last 1 day, "3"=last 3 days, "7"=last 7 days |

### Notes

- `tag_id` uses the category ID format from category queries.
- Supported `period` values are "1" (1 day), "3" (3 days), and "7" (7 days).
- `end_date` must fall on a Sunday when `period` is set to "7".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-keywords.json`](../../../../catalog/models/douyin/index/content-creative-keywords.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-keywords
