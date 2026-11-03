# TikTok Shop Product API: pricing, parameters and code examples

`tiktok-shop/product` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch TikTok Shop product details (title, price, sales, seller, and ratings) from a product URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/product", "url": "https://www.tiktok.com/shop/pdp/goli-ashwagandha-gummies-with-vitamin-d-ksm-66-vegan-non-gmo/1729587769570529799"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/product', {'url': 'https://www.tiktok.com/shop/pdp/goli-ashwagandha-gummies-with-vitamin-d-ksm-66-vegan-non-gmo/1729587769570529799'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/product", {
  "url": "https://www.tiktok.com/shop/pdp/goli-ashwagandha-gummies-with-vitamin-d-ksm-66-vegan-non-gmo/1729587769570529799"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/product", sandbase.Params{
	"url": "https://www.tiktok.com/shop/pdp/goli-ashwagandha-gummies-with-vitamin-d-ksm-66-vegan-non-gmo/1729587769570529799",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok Shop product detail page URL (e.g. https://www.tiktok.com/shop/pdp/.../1729587769570529799).  |
| `region` | string |  | Two-letter country code for the proxy location used to access region-specific products (e.g. US, GB, FR). Defaults to US.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerLocation`, and it is served only by a source that returns…  |

## Details

Returns details for one TikTok Shop product: title, brand, category, current and original price, rating, review count, units sold, seller, images, and specifications. It needs the product detail page `url`, and an optional `region` country code for region-specific products.

### Use cases

- Track the `price` and `originalPrice` of a competitor's product to watch discounts.
- Compare `soldCount`, `rating`, and `reviewCount` across products to judge which ones sell well.
- Build a product catalog entry with the title, images, brand, and specifications.
- Identify the seller of a product by `sellerId`, `sellerName`, and `sellerLocation`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/shop/pdp/goli-ashwagandha-gummies-with-vitamin-d-ksm-66-vegan-non-gmo/1729587769570529799"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok Shop product detail page URL (e.g. https://www.tiktok.com/shop/pdp/.../1729587769570529799). |
| `region` | string | No | Two-letter country code for the proxy location used to access region-specific products (e.g. US, GB, FR). Defaults to US. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerLocation`, and it is served only by a source that returns every |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "brand": "Goli",
    "category": "Health",
    "currency": "USD",
    "images": [
      "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/b0d9acd…"
    ],
    "originalPrice": "$74.10",
    "price": "$58.47",
    "productId": "1729587769570529799",
    "rating": 4.7,
    "reviewCount": 71752,
    "sellerId": "7495794203056835079",
    "sellerLocation": "United States of America",
    "sellerName": "Goli Nutrition"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Product listing title as shown on TikTok Shop. |
| `data.price / data.originalPrice` | Current price and the original price, as formatted strings with a currency symbol (for example `$58.47`). Compare them to see the discount. |
| `data.currency` | Currency code for the prices, for example `USD`. |
| `data.soldCount` | Number of units sold for the product. |
| `data.rating / data.reviewCount` | Average rating and the number of reviews. |
| `data.sellerId / data.sellerName / data.sellerLocation` | Identifier, display name, and country of the seller. |
| `data.brand / data.category` | Brand name and category of the product. |
| `data.specifications[].name / data.specifications[].value` | Product attributes as name and value pairs, such as `Flavor` and `Container type`. |
| `data.images[]` | URLs of the product images. |
| `data.productId / data.url` | Product ID and the short canonical product page URL. |
| `found` | `true` when the product was found. |

### Notes

- Copy the `url` from a TikTok Shop product page. The product ID is the number at the end of the path, for example `1729587769570529799`.
- Use `region` with a two-letter code such as `GB` or `FR` to access region-specific products. It defaults to `US`.
- Use `requireFields` to demand fields such as `sellerLocation` or `specifications`. This can change which source serves the call, and so the price.
- To read customer reviews for the same product, call [TikTok Shop Product Reviews](/apis/tiktok-shop/product-reviews). To list more items from the same seller, call [TikTok Shop Store Products](/apis/tiktok-shop/shop-products).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/product.json`](../../../catalog/models/tiktok-shop/product.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/product
