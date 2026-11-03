# TikTok Shop ID by Share Link API: pricing, parameters and code examples

`tiktok/shop-web/shop-id-by-share-link` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a TikTok Shop share URL into its corresponding store identifiers. Returns the numeric shop ID and internal store app link using a valid share link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/shop-id-by-share-link", "share_link": "https://vt.tiktok.com/ZT2AHoGsE/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/shop-id-by-share-link', {'share_link': 'https://vt.tiktok.com/ZT2AHoGsE/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/shop-id-by-share-link", {
  "share_link": "https://vt.tiktok.com/ZT2AHoGsE/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/shop-id-by-share-link", sandbase.Params{
	"share_link": "https://vt.tiktok.com/ZT2AHoGsE/",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/shop-id-by-share-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_link` | string | yes | Share link  |

## Details

Resolves a TikTok Shop share link into the numeric shop ID and an in-app store link. It needs one input, `share_link`, which is a TikTok Shop share URL such as `https://vt.tiktok.com/ZT2AHoGsE/`.

### Use cases

- Convert a shortened shop share URL into a numeric `shop_id` you can store in a database.
- Deduplicate shop links collected from different campaigns by comparing their `shop_id` values.
- Pull the `sellerId` out of a shared store link to identify the seller behind it.
- Turn a share URL into a store ID before you look up that shop's products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/shop-id-by-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://vt.tiktok.com/ZT2AHoGsE/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "shop_id": "7495832087428237549",
  "shop_link": "snssdk1180://ec/store?sellerId=7495832087428237549&store_page_version=2&trackPar…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shop_id` | Numeric ID of the TikTok Shop, returned as a string. It is the same value as `sellerId` inside `shop_link`. |
| `shop_link` | In-app deep link to the store page, using the `snssdk1180://ec/store` scheme. The query string holds `sellerId`, `store_page_version` and URL-encoded `trackParams`. |

### Notes

- Pass the full share URL in `share_link`, for example a short `vt.tiktok.com` link.
- `shop_id` is a string of digits. Keep it as a string to avoid precision loss in your code.
- To list products for the shop, call [TikTok Seller Products List](/apis/tiktok/shop-web/seller-products-list) or [TikTok Shop Seller Products (V2)](/apis/tiktok/shop-web/seller-products-list-v2).
- For a product share link instead of a shop link, use [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/shop-id-by-share-link.json`](../../../../catalog/models/tiktok/shop-web/shop-id-by-share-link.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/shop-id-by-share-link
