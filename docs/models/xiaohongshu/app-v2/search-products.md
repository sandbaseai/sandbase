# Xiaohongshu (RED) Product Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-products` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Xiaohongshu product search results based on a target keyword. Includes product card details, goods identifiers, stock status, and item titles across paginated listings.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-products", "keyword": "OpenAI", "page": 1, "search_id": "", "source": "explore_feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-products', {'keyword': 'OpenAI', 'page': 1, 'search_id': '', 'source': 'explore_feed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-products", {
  "keyword": "OpenAI",
  "page": 1,
  "search_id": "",
  "source": "explore_feed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-products", sandbase.Params{
	"keyword": "OpenAI",
	"page": 1,
	"search_id": "",
	"source": "explore_feed",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |

## Details

Search Xiaohongshu product listings by supplying a search query in `keyword`. Supports pagination across result pages using `page` and `search_id`.

### Use cases

- Search for e-commerce items on Xiaohongshu using custom keywords.
- Track product stock availability and listing titles across search feeds.
- Collect product cards and IDs for market research and item discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `source` | string | No | Source, default "explore_feed" |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "module": {
      "data": [
        {
          "card_name": "cosmos_search_goods_card",
          "card_type": "dsl",
          "id": "cosmos_search_goods_card_1",
          "content": {
            "goods_type": "normal",
            "id": "69ca2e68fcd43f0001a0185d",
            "link": "xhsdiscover://goods_detail/69ca2e68fcd43f0001a0185d?listing_image=https%3A%2F%2Fmall-i8.x…",
            "stock_status": 1,
            "title": "OpenAI PPT-以智能为笔，绘就未来图景"
          }
        }
      ]
    }
  }
}
```

### Notes

- `page` starts from 1 for paginated queries.
- Pass `search_id` from the initial search response to navigate subsequent pages.
- `source` defaults to "explore_feed".

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-products.json`](../../../../catalog/models/xiaohongshu/app-v2/search-products.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-products
