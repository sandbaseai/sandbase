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

Returns a list of brand auto-complete suggestions on Douyin for a brand name keyword. Each suggestion has a brand ID, brand name, category, and logo image link. The only input is `keyword`.

### Use cases

- Fill a brand search box with live suggestions as a user types.
- Convert a typed brand name such as `华为` into a `brand_id` for other Douyin Index calls.
- List every category a brand appears under, such as phones and home appliances.
- Show brand logos next to suggestion labels in a discovery tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "华为"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Brand name keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
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

### Response fields

| Field | Meaning |
|---|---|
| `suggestion_list` | List of brand suggestions that match `keyword`. Each item is one brand and category pair. |
| `suggestion_list[].brand_id` | ID of the brand, returned as a string. The same brand can appear in several items with the same ID. |
| `suggestion_list[].brand_name` | Display name of the brand. |
| `suggestion_list[].category_id / suggestion_list[].category_name` | ID and name of the category the brand is listed under, for example `手机` (phones) or `家用电器` (home appliances). |
| `suggestion_list[].logo_url` | Link to the brand logo image. |
| `BaseResp.StatusCode` | Status code of the response. `0` appears in a successful call. |
| `BaseResp.StatusMessage` | Status text. It is an empty string in a successful call. |

### Notes

- The same `brand_id` can repeat across items when the brand has more than one category, so group by `brand_id` if you need unique brands.
- Use the `brand_id` and `brand_name` from this response as input for brand analysis APIs such as [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles) or [Douyin Brand Trend Lines](/apis/douyin/index/brand-lines).
- Use [Douyin Brand Valid Information](/apis/douyin/index/brand-valid-info) to check brand details after you pick a suggestion.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-suggest.json`](../../../../catalog/models/douyin/index/brand-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-suggest
