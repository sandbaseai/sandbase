# AliExpress Reviews API: pricing, parameters and code examples

`aliexpress/reviews` · data API · AliExpress · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Get one page of buyer reviews for an AliExpress product by id, with rating, text, buyer country, date, bought variant and photos for each review, plus the product's total reviews, average rating and star distribution, in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aliexpress/reviews", "productId": "3256807039224587"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aliexpress/reviews', {'productId': '3256807039224587'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aliexpress/reviews", {
  "productId": "3256807039224587"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aliexpress/reviews", sandbase.Params{
	"productId": "3256807039224587",
})
```

Same call via the path form: `POST /v1/api/aliexpress/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of 20 reviews in AliExpress's default order. Each page is billed as one request. default `1`; range 1– |
| `productId` | string | yes | AliExpress product id, the number in the product URL (https://www.aliexpress.com/item/<id>.html), e.g. 3256807039224587. The AliExpress Search SKU returns it as productId.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `helpfulVotes`, and it is served only by a source that returns every…  |

## Details

Get one page of buyer reviews for an AliExpress product by id, with rating, text, buyer country, date, bought variant and photos for each review, plus the product's total reviews, average rating and star distribution, in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "aliexpress/reviews", "productId": "3256807039224587"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `productId` | string | Yes | AliExpress product id, the number in the product URL (https://www.aliexpress.com/item/<id>.html), e.g. 3256807039224587. The AliExpress Search SKU returns it as productId. |
| `page` | integer | No | 1-based page of 20 reviews in AliExpress's default order. Each page is billed as one request. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `helpfulVotes`, and it is served only by a source that returns every o |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/aliexpress/reviews.json`](../../../catalog/models/aliexpress/reviews.json) · Store page: https://www.sandbase.ai/model/aliexpress/reviews
