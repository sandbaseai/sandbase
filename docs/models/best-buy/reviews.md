# Best Buy Reviews API: pricing, parameters and code examples

`best-buy/reviews` · data API · Best Buy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Pull a page of 10 customer reviews for any BestBuy.com product by URL, newest first or by relevance, helpfulness, or rating: rating, title, text, date, reviewer, and verified-buyer badge.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "best-buy/reviews", "url": "https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('best-buy/reviews', {'url': 'https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("best-buy/reviews", {
  "url": "https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "best-buy/reviews", sandbase.Params{
	"url": "https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564",
})
```

Same call via the path form: `POST /v1/api/best-buy/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Best Buy product page URL that carries the numeric Best Buy SKU, either the .../sku/6376564 form the Best Buy Search SKU returns or the older .../6376564.p?skuId=6376564 form.  |
| `page` | integer |  | 1-based page of 10 reviews; Best Buy serves at most 1000 pages. Each page is billed as one request; keep url and sort the same while walking pages. default `1`; range 1–1000 |
| `sort` | string |  | Review order: recent (newest first, the default), oldest, relevancy, helpful, rating_high, or rating_low (e.g. helpful). one of: `recent`, `oldest`, `relevancy`, `helpful`, `rating_high`, `rating_low`; default `"recent"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `rating`, and it is served only by a source that returns every one…  |

## Details

Pull a page of 10 customer reviews for any BestBuy.com product by URL, newest first or by relevance, helpfulness, or rating: rating, title, text, date, reviewer, and verified-buyer badge.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "best-buy/reviews", "url": "https://www.bestbuy.com/product/apple-airpods-5-true-wireless-active-noise-cancelling-earbuds-with-wireless-charging-case-white/JJGCQP634G/sku/6376564"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Best Buy product page URL that carries the numeric Best Buy SKU, either the .../sku/6376564 form the Best Buy Search SKU returns or the older .../6376564.p?skuId=6376564 form. |
| `page` | integer | No | 1-based page of 10 reviews; Best Buy serves at most 1000 pages. Each page is billed as one request; keep url and sort the same while walking pages. Default `1`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `rating`, and it is served only by a source that returns every one of  |
| `sort` | string | No | Review order: recent (newest first, the default), oldest, relevancy, helpful, rating_high, or rating_low (e.g. helpful). One of: `recent`, `oldest`, `relevancy`, `helpful`, `rating_high`, `rating_low`. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/best-buy/reviews.json`](../../../catalog/models/best-buy/reviews.json) · Store page: https://www.sandbase.ai/model/best-buy/reviews
