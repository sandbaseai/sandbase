# Douyin Index Video Search API: pricing, parameters and code examples

`douyin/index/item-query` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Douyin Index videos by keyword with filters for post date, duration, category, and label type. Returns video metadata and performance metrics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-query", "query": "sandbase"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-query', {'query': 'sandbase'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-query", {
  "query": "sandbase"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-query", sandbase.Params{
	"query": "sandbase",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (required), e.g. "food"  |
| `date_type` | integer |  | Publish date filter, default 0=any default `0` |
| `label_type` | integer |  | Video type (quality tag), default 0=any default `0` |
| `category_id` | string |  | Category ID (string), default "0"=all default `"0"` |
| `duration_type` | integer |  | Duration filter, default 0=any default `0` |

## Details

Search the Douyin Index video catalog using `query` alongside optional filters like `category_id`, `duration_type`, `date_type`, and `label_type`. Returns video details and engagement indicators.

### Use cases

- Search Douyin videos matching specific keywords and categories.
- Filter indexed video results by duration and post timeframe.
- Track video engagement metrics such as like counts and performance flags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required), e.g. "food" |
| `date_type` | integer | No | Publish date filter, default 0=any |
| `label_type` | integer | No | Video type (quality tag), default 0=any |
| `category_id` | string | No | Category ID (string), default "0"=all |
| `duration_type` | integer | No | Duration filter, default 0=any |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "createTime": "2026-09-08 21:42:33",
      "duration": 22,
      "isHighFansRiseRate": 0,
      "isHighLikeRate": 0,
      "isHighPlayOverRate": 0,
      "likes": "242510",
      "nickname": "<user>",
      "title": "#腋来香 #腋问 #腋总会 #可爱 #美食 @DOU+小助手",
      "url": "https://www.douyin.com/video/7683159416120892148"
    }
  ]
}
```

### Notes

- Set `date_type`, `label_type`, and `duration_type` to `0` for default unfiltered results.
- Pass `category_id` as a string, with `"0"` selecting all categories.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-query.json`](../../../../catalog/models/douyin/index/item-query.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-query
