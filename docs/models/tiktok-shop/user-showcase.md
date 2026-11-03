# TikTok Shop User Showcase API: pricing, parameters and code examples

`tiktok-shop/user-showcase` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List the TikTok Shop products a creator showcases (title, price, rating, and sales per product).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/user-showcase", "handle": "mrtiktokreviews"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/user-showcase', {'handle': 'mrtiktokreviews'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/user-showcase", {
  "handle": "mrtiktokreviews"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/user-showcase", sandbase.Params{
	"handle": "mrtiktokreviews",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/user-showcase` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination token for retrieving subsequent product pages.  |
| `handle` | string | yes | The handle of the TikTok user (e.g. mrtiktokreviews).  |
| `region` | string |  | Geographical region for proxy placement (defaults to US).  |

## Details

This API returns the TikTok Shop products a creator showcases on their profile. Each product has a title, price, discount, rating, review count, and units sold. It needs the creator's TikTok `handle`.

### Use cases

- Track which products a TikTok creator promotes and how well each one sells.
- Compare `soldCount` and `rating` across a creator's showcase to find their top performing items.
- Monitor price and discount changes on products a creator features.
- Build a list of seller IDs and product URLs from a creator's showcase for further research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/user-showcase" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "mrtiktokreviews"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | The handle of the TikTok user (e.g. mrtiktokreviews). |
| `cursor` | string | No | Pagination token for retrieving subsequent product pages. |
| `region` | string | No | Geographical region for proxy placement (defaults to US). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_eL5R6xsw_RY1c_-LVf6VnQ",
    "products": [
      {
        "currency": "USD",
        "discountPct": 50,
        "imageUrl": "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/8d1f118…",
        "originalPrice": "30",
        "price": "15",
        "productId": "1729401442164511030",
        "rating": 4.4,
        "reviewCount": 36828,
        "sellerId": "7495079418085345590",
        "soldCount": 544937,
        "title": "BASED Hair Texture Powder | Instant Volume & Texture | Lightweight, Matte Finish…",
        "url": "https://www.tiktok.com/shop/pdp/1729401442164511030"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.products[].title` | Product name as listed on TikTok Shop. |
| `data.products[].productId` | ID of the product. Use it to look up the product in other TikTok Shop APIs. |
| `data.products[].price / data.products[].originalPrice` | Current price and the price before the discount. Both are strings, such as `"15"` and `"30"`. |
| `data.products[].discountPct` | Discount as a percentage, such as `50` for a product that dropped from `30` to `15`. |
| `data.products[].currency` | Currency code of the prices, such as `USD`. |
| `data.products[].rating / data.products[].reviewCount` | Average product rating and the number of reviews. |
| `data.products[].soldCount` | Number of units sold for the product. |
| `data.products[].sellerId` | ID of the seller that lists the product. |
| `data.products[].url / data.products[].imageUrl` | Link to the product page on TikTok Shop and a product image URL. |
| `data.nextCursor` | Token for the next page of products. |

### Notes

- Use the handle without the `@`, for example `mrtiktokreviews`.
- To get the next page, pass `data.nextCursor` from the response as `cursor` in the next request, with the same `handle`.
- Pass `productId` to [TikTok Shop Product](/apis/tiktok-shop/product) for product details, or to [TikTok Shop Product Reviews](/apis/tiktok-shop/product-reviews) for its reviews.
- Pass `sellerId` to [TikTok Shop Store Products](/apis/tiktok-shop/shop-products) to see the other products from that seller.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/user-showcase.json`](../../../catalog/models/tiktok-shop/user-showcase.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/user-showcase
