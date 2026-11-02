# Douyin Brand Search Suggestions API: pricing, parameters and code examples

`douyin/index/brand-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of brand auto-complete suggestions based on a query keyword. Results include brand identifiers, names, categories, and logo image links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-suggest", "keyword": "华为"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-suggest', {'keyword': '华为'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-suggest", {
  "keyword": "华为"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-suggest", sandbase.Params{
	"keyword": "华为",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Brand name keyword  |

## Details

Retrieve brand search auto-complete suggestions on Douyin using the `keyword` parameter.

### Use cases

- Populate brand autocomplete dropdowns in search interfaces.
- Resolve query strings to standard Douyin brand IDs and categories.
- Display matching brand logos and category labels in discovery tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "华为"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Brand name keyword |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "suggestion_list": [
    {
      "brand_id": "9117",
      "brand_name": "华为",
      "category_id": "11",
      "category_name": "手机",
      "logo_url": "https://p1.douyinpic.com/large/ad-brand/9117.jpg"
    }
  ]
}
```

### Notes

- Requires `keyword` to query matching brand names.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-suggest.json`](../../../../catalog/models/douyin/index/brand-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-suggest
