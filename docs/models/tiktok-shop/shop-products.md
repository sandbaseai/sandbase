# TikTok Shop Store Products API: pricing, parameters and code examples

`tiktok-shop/shop-products` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List every product of a TikTok Shop store by URL (title, price, sales, and rating per product plus shop-level stats) with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/shop-products", "url": "https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/shop-products', {'url': 'https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/shop-products", {
  "url": "https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/shop-products", sandbase.Params{
	"url": "https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/shop-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok Shop store URL (e.g. https://www.tiktok.com/shop/store/...).  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |
| `region` | string |  | Two-letter country code of the store's market (e.g. US).  |
| `sortBy` | string |  | Product ordering within the store. one of: `top`, `new_releases`; default `"top"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `shopRating`, and it is served only by a source that returns every…  |

## Details

This API returns the products of a TikTok Shop store, with title, price, sold count, and rating for each product. It also returns shop-level stats such as the shop name, shop rating, and total units sold. It needs a TikTok Shop store URL.

### Use cases

- Track a competitor store's best sellers and see how their prices change over time.
- Build a catalog of every product a brand sells on TikTok Shop.
- Compare discounts across a store by checking `price` against `originalPrice`.
- Find a store's newest listings by setting `sortBy` to `new_releases`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/shop-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok Shop store URL (e.g. https://www.tiktok.com/shop/store/...). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `region` | string | No | Two-letter country code of the store's market (e.g. US). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `shopRating`, and it is served only by a source that returns every one |
| `sortBy` | string | No | Product ordering within the store. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hasMore": true,
    "nextCursor": "cur_up8aGtbgaWa2lUhcuYJUcQ",
    "productCount": 53,
    "products": [
      {
        "currency": "USD",
        "discountPct": 21,
        "image": "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/2bc69aa…",
        "originalPrice": 24.7,
        "price": 19.47,
        "productId": "1729527313880355335",
        "rating": 4.5,
        "reviewCount": 94624,
        "sellerId": "7495794203056835079",
        "soldCount": 1306640,
        "title": "Goli Ashwagandha & Vitamin D Gummy - Mixed Berry, KSM-66, Vegan, Plant Based, No…",
        "url": "https://www.tiktok.com/shop/pdp/1729527313880355335"
      }
    ],
    "shopName": "Goli Nutrition",
    "shopRating": 4.6,
    "soldCount": 5815669
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.shopName` | Display name of the store. |
| `data.shopRating` | Average rating of the whole shop. |
| `data.soldCount` | Total units sold by the shop, as a shop-level figure. |
| `data.productCount` | Number of products the store lists. |
| `data.products[].title / data.products[].url` | Product title and the link to its TikTok Shop product page. |
| `data.products[].price / data.products[].originalPrice` | Current price and the price before discount, in the currency given in `currency`. |
| `data.products[].discountPct` | Discount as a percentage off `originalPrice`. |
| `data.products[].rating / data.products[].reviewCount` | Average rating of the product and the number of reviews behind it. |
| `data.products[].soldCount` | Units sold for this product. |
| `data.products[].productId / data.products[].sellerId` | Product ID and the ID of the store that sells it. |

### Notes

- Copy the store URL from the TikTok Shop store page. It ends with the store name and a numeric ID, which matches `sellerId` in the products.
- When `data.hasMore` is `true`, pass `data.nextCursor` as `cursor` in the next request to get the next page.
- `sortBy` accepts `top` (default) or `new_releases`.
- To get details for one product, pass its `productId` or `url` to [TikTok Shop Product](/apis/tiktok-shop/product), or read its reviews with [TikTok Shop Product Reviews](/apis/tiktok-shop/product-reviews).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/shop-products.json`](../../../catalog/models/tiktok-shop/shop-products.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/shop-products
