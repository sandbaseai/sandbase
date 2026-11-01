# TikTok Shop Product ID by Share Link

`tiktok/shop-web/product-id-by-share-link` · api · TikTok

Returns the TikTok Shop product identifier extracted from a provided product share link. Takes a required share URL to resolve the associated product ID.

## Pricing

- **$0.0015 per call** (USD)
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

Look up a TikTok Shop product identifier using a `share_link`. Resolves shared URLs into direct product IDs for downstream product queries.

### Use cases

- Resolve TikTok Shop share links into direct product identifiers.
- Automate product catalog indexing from shared TikTok product URLs.
- Extract item IDs for subsequent product detail queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-id-by-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "<share_link>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes | Share link |

### Notes

- Pass the full TikTok Shop product URL in the `share_link` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-id-by-share-link.json`](../../../../catalog/models/tiktok/shop-web/product-id-by-share-link.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-id-by-share-link
