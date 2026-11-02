# TikTok Shop Product Reviews API: pricing, parameters and code examples

`tiktok-shop/product-reviews` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00095 per call · **Modes:** sync

Fetch customer reviews for a TikTok Shop product by URL (rating, text, reviewer, country, and verified-buyer flag).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00095**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/product-reviews", "url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/product-reviews', {'url': 'https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/product-reviews", {
  "url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/product-reviews", sandbase.Params{
	"url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok Shop product URL (e.g. https://www.tiktok.com/shop/pdp/.../1729385633899532161).  |
| `page` | integer |  | 1-based results page. Use with hasMore in the output to paginate. default `1`; range 1– |
| `region` | string |  | Two-letter country code of the product's shop region (e.g. US). Strongly recommended for correct results.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `images`, and it is served only by a source that returns every one…  |

## Details

Fetch customer reviews for a TikTok Shop product by URL (rating, text, reviewer, country, and verified-buyer flag).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok Shop product URL (e.g. https://www.tiktok.com/shop/pdp/.../1729385633899532161). |
| `page` | integer | No | 1-based results page. Use with hasMore in the output to paginate. Default `1`. |
| `region` | string | No | Two-letter country code of the product's shop region (e.g. US). Strongly recommended for correct results. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `images`, and it is served only by a source that returns every one of  |

### Pricing

Billed at the actual cost of each call, usually $0.00095 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok-shop/product-reviews.json`](../../../catalog/models/tiktok-shop/product-reviews.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/product-reviews
