# Google Play Reviews API: pricing, parameters and code examples

`google-play/reviews` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Get Google Play reviews for a product with rating, sort, platform, and paging.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/reviews", "product_id": "com.duolingo"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/reviews', {'product_id': 'com.duolingo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/reviews", {
  "product_id": "com.duolingo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/reviews", sandbase.Params{
	"product_id": "com.duolingo",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-play/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code. Default 'us'.  |
| `hl` | string |  | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'.  |
| `num` | integer |  | Number of reviews, 1-199. Default 40. range 1–199 |
| `store` | string |  | Product catalog containing this identifier. Default 'apps'. one of: `apps`, `books`, `audiobooks`, `movies`, `tv` |
| `rating` | integer |  | Only reviews with this star rating, 1-5. range 1–5 |
| `sort_by` |  |  | 1 most relevant, 2 newest, 3 by rating. Default 1.  |
| `platform` | string |  | Platform the reviews belong to. Default 'phone'. one of: `phone`, `tablet`, `watch`, `chromebook`, `tv` |
| `product_id` | string | yes | Native Google Play product identifier, such as 'com.duolingo'.  |
| `next_page_token` | string |  | Returned review continuation. Keep product, store, language, country, platform, rating, sort order, and count the same.  |

## Details

Get Google Play reviews for a product with rating, sort, platform, and paging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "com.duolingo"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Native Google Play product identifier, such as 'com.duolingo'. |
| `gl` | string | No | Two-letter country code. Default 'us'. |
| `hl` | string | No | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'. |
| `next_page_token` | string | No | Returned review continuation. Keep product, store, language, country, platform, rating, sort order, and count the same. |
| `num` | integer | No | Number of reviews, 1-199. Default 40. |
| `platform` | string | No | Platform the reviews belong to. Default 'phone'. One of: `phone`, `tablet`, `watch`, `chromebook`, `tv`. |
| `rating` | integer | No | Only reviews with this star rating, 1-5. |
| `sort_by` | any | No | 1 most relevant, 2 newest, 3 by rating. Default 1. |
| `store` | string | No | Product catalog containing this identifier. Default 'apps'. One of: `apps`, `books`, `audiobooks`, `movies`, `tv`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-play/reviews.json`](../../../catalog/models/google-play/reviews.json) · Store page: https://www.sandbase.ai/model/google-play/reviews
