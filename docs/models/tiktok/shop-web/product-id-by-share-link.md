# TikTok Shop Product ID by Share Link API: pricing, parameters and code examples

`tiktok/shop-web/product-id-by-share-link` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the TikTok Shop product identifier extracted from a provided product share link. Takes a required share URL to resolve the associated product ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-id-by-share-link", "share_link": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-id-by-share-link', {'share_link': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-id-by-share-link", {
  "share_link": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-id-by-share-link", sandbase.Params{
	"share_link": "test",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-id-by-share-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_link` | string | yes | Share link  |

## Details

Returns the TikTok Shop product ID for a product share link. Send the full share URL in `share_link`. The response also includes a `product_link` deep link for the TikTok app.

### Use cases

- Convert a TikTok Shop share link copied from the app into a numeric product ID.
- Normalize affiliate share links into product IDs before storing them in a product database.
- Feed the resolved `product_id` into a product detail call to get price and seller data.
- Deduplicate a list of shared links by comparing the product IDs they resolve to.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-id-by-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://affiliate-us.tiktok.com/api/v1/share/AJ4hS3OdXmSg"}'
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
  "product_id": "8651224669119091502",
  "product_link": "snssdk1180://lynxview?bundle=partner-product-page%2Ftemplate.js&channel=tea_prod…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_id` | The TikTok Shop product ID that the share link points to. It is returned as a string of digits. |
| `product_link` | A TikTok app deep link (`snssdk1180://` scheme) for the product page. It carries URL-encoded query parameters such as the page bundle and channel. |

### Notes

- Pass the full share URL in `share_link`, for example `https://affiliate-us.tiktok.com/api/v1/share/AJ4hS3OdXmSg`.
- Keep `product_id` as a string, because the value is a long number.
- Pass `product_id` to [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail) or [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3) to get full product data.
- For a share link that points to a shop instead of a product, use [TikTok Shop ID by Share Link](/apis/tiktok/shop-web/shop-id-by-share-link).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-id-by-share-link.json`](../../../../catalog/models/tiktok/shop-web/product-id-by-share-link.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-id-by-share-link
