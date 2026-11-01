# TikTok Shop ID by Share Link

`tiktok/shop-web/shop-id-by-share-link` · api · TikTok

Resolves a TikTok Shop share URL into its corresponding store identifiers. Returns the numeric shop ID and internal store app link using a valid share link.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve a TikTok store identifier by submitting a valid TikTok Shop URL in `share_link`. The endpoint returns the numeric `shop_id` along with a deep link to the store.

### Use cases

- Extract numeric store IDs from shortened TikTok share links.
- Convert shared store links into internal TikTok app deep links.
- Look up store identifiers to query additional shop metadata.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/shop-id-by-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://vt.tiktok.com/ZT2AHoGsE/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "shop_id": "7495832087428237549",
  "shop_link": "snssdk1180://ec/store?sellerId=7495832087428237549&store_page_version=2&trackParams=%7B%2…"
}
```

### Notes

- Requires a valid TikTok store URL in `share_link`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/shop-id-by-share-link.json`](../../../../catalog/models/tiktok/shop-web/shop-id-by-share-link.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/shop-id-by-share-link
