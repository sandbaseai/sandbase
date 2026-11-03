# TikTok Shop Search API: pricing, parameters and code examples

`tiktok-shop/search` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00095 per call · **Modes:** sync

Search TikTok Shop products by keyword across 15 countries: price, sales, rating, and seller info per product, in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00095**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/search", "query": "phone case"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/search', {'query': 'phone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/search", {
  "query": "phone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/search", sandbase.Params{
	"query": "phone case",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum products to return, honoured on US searches up to 30. Other countries and larger values return every product TikTok Shop gives for the query, typically about 30 and occasionally more than 50. The price per call… range 1– |
| `query` | string | yes | Search keyword for TikTok Shop products (e.g. wireless earbuds).  |
| `country` | string |  | Country code of the TikTok Shop market to search (e.g. US). one of: `US`, `VN`, `TH`, `PH`, `MY`, `ID`, `GB`, `SG`, `ES`, `MX`, `DE`, `IT` …; default `"US"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `currency`, and it is served only by a source that returns every one…  |

## Details

Returns a list of TikTok Shop products that match a search keyword. Each product has a price, a sold count, the shop name, and a product link. You send a `query` and can pick a `country` market.

### Use cases

- Compare prices for the same product type across competing TikTok Shop sellers.
- Spot fast-selling products in a niche by sorting results on `soldCount`.
- Build a list of shops that sell in a category by collecting `shopName` and `sellerId`.
- Run the same `query` with different `country` values to check which markets carry a product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "phone case"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword for TikTok Shop products (e.g. wireless earbuds). |
| `country` | string | No | Country code of the TikTok Shop market to search (e.g. US). |
| `limit` | integer | No | Maximum products to return, honoured on US searches up to 30. Other countries and larger values return every product TikTok Shop gives for the query, typically about 30 and occasionally more than 50. The price per call i |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `currency`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "currency": "USD",
        "image": "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/b369a4c…",
        "price": 1.89,
        "productId": "1732493173845955041",
        "sellerId": "7494773196461475297",
        "shopName": "L-PureShell",
        "soldCount": 29,
        "title": "Magnetic Fit Slim Clear-1 Protector Cover for iPhone 17,16 Pro Max,16,15,14,13,1…",
        "url": "https://www.tiktok.com/shop/pdp/1732493173845955041"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Product title as listed in the shop. Long titles may be cut. |
| `data.items[].price / data.items[].currency` | Listed price of the product and the currency code for that price, such as `USD`. |
| `data.items[].soldCount` | Number of units sold for the product. |
| `data.items[].rating` | Product rating, for example `4.7`. Some products have no `rating` in the response. |
| `data.items[].productId` | ID of the product on TikTok Shop. Use it to look up more product detail. |
| `data.items[].shopName / data.items[].sellerId` | Name and ID of the shop that sells the product. |
| `data.items[].url` | Link to the product page on TikTok Shop. |
| `data.items[].image` | Link to the product image. |
| `found` | `true` when the search returned products. |

### Notes

- Pass the `productId` to [TikTok Shop Product](/apis/tiktok-shop/product) for full product detail, or to [TikTok Shop Product Reviews](/apis/tiktok-shop/product-reviews) for reviews.
- Use `sellerId` with [TikTok Shop Store Products](/apis/tiktok-shop/shop-products) to list more products from the same shop.
- Set `limit` to cap the number of products. It is honoured only on US searches up to 30. Other countries return every product found.
- `rating` is missing on some products, so handle items without it. To require `currency` or `reviewCount` in the output, list them in `requireFields`.

### Pricing

Billed at the actual cost of each call, about $0.00095 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/search.json`](../../../catalog/models/tiktok-shop/search.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/search
