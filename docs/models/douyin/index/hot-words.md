# Douyin Hot Search Keywords API: pricing, parameters and code examples

`douyin/index/hot-words` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of current trending search keywords and their growth rates on Douyin or Toutiao. Results can be filtered by the target platform application.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/hot-words", "app_name": "aweme"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/hot-words', {'app_name': 'aweme'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/hot-words", {
  "app_name": "aweme"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/hot-words", sandbase.Params{
	"app_name": "aweme",
})
```

Same call via the path form: `POST /v1/api/douyin/index/hot-words` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao`; default `"aweme"` |

## Details

Retrieve current trending search terms on Douyin or Toutiao using the optional `app_name` parameter. The response includes keywords alongside their respective growth rates.

### Use cases

- Track trending topics across Douyin and Toutiao platforms.
- Analyze search keyword growth rates for content research.
- Identify popular search queries for marketing campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/hot-words" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "hot_words": [
    {
      "growth_rate": 100,
      "keyword": "美食"
    }
  ]
}
```

### Notes

- `app_name` accepts `aweme` for Douyin or `toutiao` for Toutiao.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/hot-words.json`](../../../../catalog/models/douyin/index/hot-words.json) · Store page: https://www.sandbase.ai/model/douyin/index/hot-words
