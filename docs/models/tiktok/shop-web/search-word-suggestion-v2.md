# TikTok Shop Search Keyword Suggestions (V2) API: pricing, parameters and code examples

`tiktok/shop-web/search-word-suggestion-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns e-commerce search keyword suggestions based on an input query. Supports filtering by target region and language code.

## Pricing

- **$0.0015 per call** (USD)
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

Use this endpoint to retrieve search keyword suggestions optimized for TikTok Shop using `search_word`.

### Use cases

- Populate autocomplete recommendations in product search boxes.
- Discover popular search terms across different regional markets.
- Research relevant search keywords for product catalog tagging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/search-word-suggestion-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "coffee"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Search keyword (required) |
| `lang` | string | No | Language code (en-US/zh-CN etc.) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Notes

- `search_word` is required to supply the query keyword.
- `region` supports values such as US, GB, SG, MY, PH, TH, VN, and ID.
- `lang` accepts standard language codes such as en-US or zh-CN.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/search-word-suggestion-v2.json`](../../../../catalog/models/tiktok/shop-web/search-word-suggestion-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/search-word-suggestion-v2
