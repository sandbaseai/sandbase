# Douyin Topic Search Suggestions API: pricing, parameters and code examples

`douyin/index/topic-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns autocomplete topic suggestions based on a search query. Supports filtering by target platform such as Douyin or Toutiao.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/topic-suggest", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/topic-suggest', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/topic-suggest", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/topic-suggest", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/topic-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Topic keyword  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao`; default `"aweme"` |

## Details

Look up topic suggestions for a given `keyword` string. You can also specify `app_name` to target Douyin or Toutiao.

### Use cases

- Populate autocomplete dropdowns for topic search inputs.
- Discover valid topic names and IDs matching user queries.
- Target topic suggestions specifically for Douyin or Toutiao.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/topic-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Topic keyword |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "topic_list": [
    {
      "topic_id": "1576073697445901",
      "topic_name": "人工智能"
    }
  ]
}
```

### Notes

- The `app_name` parameter accepts aweme for Douyin or toutiao for Toutiao.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/topic-suggest.json`](../../../../catalog/models/douyin/index/topic-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/index/topic-suggest
