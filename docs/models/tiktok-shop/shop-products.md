# TikTok Shop Store Products

`tiktok-shop/shop-products` · api · TikTok Shop

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

List every product of a TikTok Shop store by URL (title, price, sales, and rating per product plus shop-level stats) with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/shop-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/shop/store/goli-nutrition/7495794203056835079"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok Shop store URL (e.g. https://www.tiktok.com/shop/store/...). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `region` | string | No | Two-letter country code of the store's market (e.g. US). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `shopRating`, and it is served only by a source that returns every one |
| `sortBy` | string | No | Product ordering within the store. One of: `top`, `new_releases`. Default `"top"`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/shop-products.json`](../../../catalog/models/tiktok-shop/shop-products.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/shop-products
