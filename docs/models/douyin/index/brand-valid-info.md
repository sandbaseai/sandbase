# Douyin Brand Valid Information API: pricing, parameters and code examples

`douyin/index/brand-valid-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns brand details including brand ID and category information on Douyin. Queries are filtered using comma-separated brand keywords.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-valid-info", "keyword_list": "华为"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-valid-info', {'keyword_list': '华为'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-valid-info", {
  "keyword_list": "华为"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-valid-info", sandbase.Params{
	"keyword_list": "华为",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-valid-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword_list` | string | yes | Brand name list, comma separated  |

## Details

Look up brand metadata and category IDs on Douyin using `keyword_list`.

### Use cases

- Verify recognized brand names and extract their associated brand IDs.
- Map brands to their corresponding Douyin category classifications.
- Prepare brand identifiers for subsequent Douyin Index trend lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-valid-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_list": "华为"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword_list` | string | Yes | Brand name list, comma separated |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "keyword_info": [
    {
      "brand_info": [
        {
          "brand_id": "9117",
          "brand_name": "华为",
          "category_id": "11",
          "category_name": "手机"
        }
      ]
    }
  ]
}
```

### Notes

- Pass multiple brand names to `keyword_list` as a comma-separated string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-valid-info.json`](../../../../catalog/models/douyin/index/brand-valid-info.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-valid-info
