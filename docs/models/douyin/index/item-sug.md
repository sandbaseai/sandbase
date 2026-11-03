# Douyin Video Search Suggestions API: pricing, parameters and code examples

`douyin/index/item-sug` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search suggestions and related video items based on a keyword query. Includes video titles, URLs, like counts, and author nicknames.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-sug", "query": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-sug', {'query': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-sug", {
  "query": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-sug", sandbase.Params{
	"query": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-sug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |

## Details

Look up auto-complete suggestions and related Douyin video items using the `query` parameter.

### Use cases

- Display search keyword auto-complete options in a video search interface.
- Discover trending video titles associated with specific search terms.
- Retrieve video preview metadata including URLs and engagement metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-sug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "category_name": "科技",
      "likes": "404231",
      "nickname": "<user>",
      "title": "找了陌生人上门喂猫遛狗，被家里机器人全程盘问 #我系二白  #机器人二白  #人工智能 #上门喂猫 #机器人看家",
      "url": "https://www.douyin.com/video/7691553968815623478"
    }
  ]
}
```

### Notes

- Requires a search keyword provided in the `query` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-sug.json`](../../../../catalog/models/douyin/index/item-sug.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-sug
