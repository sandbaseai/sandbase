# TikTok Shop Product Category List API: pricing, parameters and code examples

`tiktok/shop-web/products-category-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the available product categories for TikTok Shop across supported regional marketplaces. Allows filtering the taxonomy by the specified region code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/products-category-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/products-category-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/products-category-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/products-category-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/products-category-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |

## Details

Returns the TikTok Shop product category tree for one regional marketplace. It takes an optional `region` code and defaults to `US`. Each top-level category lists its child categories.

### Use cases

- Build a category picker that mirrors the TikTok Shop taxonomy for a given market.
- Map your own catalog categories to TikTok Shop `category_id` values.
- Compare which top-level categories exist across the supported regions.
- Download category names and images to label product research dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/products-category-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "children": [
      {
        "children": [],
        "self": {
          "category_id": "849032",
          "category_level": 2,
          "category_name": "Hand & Foot Care",
          "category_name_en": "hand-foot-care",
          "image_url": "https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/dc05090b19cd43e…",
          "is_leaf": false,
          "parent_category_id": "601450"
        }
      }
    ],
    "self": {
      "category_id": "601450",
      "category_level": 1,
      "category_name": "Beauty & Personal Care",
      "category_name_en": "beauty-personal-care",
      "image_url": "https://lf16-tiktok-common.tiktokcdn-us.com/obj/tiktok-web-common-tx/i18n_ecom_f…",
      "is_leaf": false,
      "parent_category_id": "0"
    }
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `self.category_id` | ID of the top-level category as a string. Use it to match or store the category. |
| `self.category_name / self.category_name_en` | Display name of the category, and a lowercase hyphenated version of the name. The second form looks like a URL slug, for example `beauty-personal-care`. |
| `self.category_level` | Depth in the tree. Top-level categories show `1` and their children show `2`. |
| `self.parent_category_id` | `category_id` of the parent. Top-level categories show `0`. |
| `self.is_leaf` | Shows whether the category has no further subcategories. Every category in the sample shows `false`. |
| `self.image_url` | URL of an image for the category. |
| `children[]` | List of child category nodes under a top-level category. Each node has the same `self` and `children` shape. |
| `children[].self.category_id / children[].self.category_name` | ID and display name of each level 2 category. |
| `children[].self.parent_category_id` | Links the child back to the top-level `self.category_id`. |
| `children[].children[]` | Nested list for deeper levels. It is empty in the sample, even though `children[].self.is_leaf` shows `false`. |

### Notes

- The response is a JSON array of top-level category nodes, not an object.
- Pass `region` as one of `US`, `GB`, `SG`, `MY`, `PH`, `TH`, `VN` or `ID`. If you omit it, the request uses `US`.
- `category_id` values are strings, so keep them as strings when you store them.
- Level 2 nodes come back with an empty `children` list even when `is_leaf` is `false`, so do not assume the tree stops at level 2.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/products-category-list.json`](../../../../catalog/models/tiktok/shop-web/products-category-list.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/products-category-list
