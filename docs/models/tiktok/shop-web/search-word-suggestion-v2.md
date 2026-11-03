# TikTok Shop Search Keyword Suggestions (V2) API: pricing, parameters and code examples

`tiktok/shop-web/search-word-suggestion-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns e-commerce search keyword suggestions based on an input query. Supports filtering by target region and language code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/search-word-suggestion-v2", "search_word": "coffee"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/search-word-suggestion-v2', {'search_word': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/search-word-suggestion-v2", {
  "search_word": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/search-word-suggestion-v2", sandbase.Params{
	"search_word": "coffee",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/search-word-suggestion-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string |  | Language code (en-US/zh-CN etc.) default `"en-US"` |
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `search_word` | string | yes | Search keyword (required)  |

## Details

Returns a list of TikTok Shop search keyword suggestions for a starting query. You send `search_word`, and you can set `region` and `lang` to match a market.

### Use cases

- Fill a product search box with autocomplete suggestions for a partial keyword.
- Expand a seed word like `coffee` into related shopping queries for keyword research.
- Compare the suggestions returned for different `region` values to see how shoppers phrase searches in each market.
- Pick search phrases to feed into a product search call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/search-word-suggestion-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Search keyword (required) |
| `lang` | string | No | Language code (en-US/zh-CN etc.) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    "coffee table"
  ],
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the call. `0` means the request succeeded. |
| `message` | Text status of the call. It shows `success` when the request worked. |
| `data` | List of suggested search keywords as plain strings. The list is ordered as returned. |
| `data[]` | One suggested search phrase, such as `coffee table` or `coffee maker machine`. |

### Notes

- `search_word` is the only required parameter. `region` defaults to `US` and `lang` defaults to `en-US`.
- The response is a flat list of strings. It has no counts, scores or IDs for each suggestion.
- Pass a suggestion into [TikTok Shop Product Search](/apis/tiktok/shop-web/search-products-list) to find products for that phrase.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/search-word-suggestion-v2.json`](../../../../catalog/models/tiktok/shop-web/search-word-suggestion-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/search-word-suggestion-v2
