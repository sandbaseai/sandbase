# Amazon Seller Products API: pricing, parameters and code examples

`amazon/seller-products` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

List one Amazon seller's storefront by seller ID, a page at a time, and get ASIN, title, price, list price, rating, reviews count, image, coupon and sponsored, Prime, best seller and Amazon's Choice flags for each product in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/seller-products", "sellerId": "A1AU32JJ4K70WE"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/seller-products', {'sellerId': 'A1AU32JJ4K70WE'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/seller-products", {
  "sellerId": "A1AU32JJ4K70WE"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/seller-products", sandbase.Params{
	"sellerId": "A1AU32JJ4K70WE",
})
```

Same call via the path form: `POST /v1/api/amazon/seller-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of the seller's storefront. Each page is billed as one request. default `1`; range 1– |
| `region` | string |  | Amazon marketplace to read, as its domain (e.g. amazon.co.uk); omit it for amazon.com. one of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazon.se`, `amazon.pl`, `amazon.ca`, `amazon.com.mx`, `amazon.com.br` … |
| `sellerId` | string | yes | Amazon seller ID, the value after seller= in a seller page URL (https://www.amazon.com/sp?seller=<id>), e.g. A11V4PRB7HXYNG.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `listPrice`, and it is served only by a source that returns every…  |

## Details

List one Amazon seller's storefront by seller ID, a page at a time, and get ASIN, title, price, list price, rating, reviews count, image, coupon and sponsored, Prime, best seller and Amazon's Choice flags for each product in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "amazon/seller-products", "sellerId": "A1AU32JJ4K70WE"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sellerId` | string | Yes | Amazon seller ID, the value after seller= in a seller page URL (https://www.amazon.com/sp?seller=<id>), e.g. A11V4PRB7HXYNG. |
| `page` | integer | No | 1-based page of the seller's storefront. Each page is billed as one request. Default `1`. |
| `region` | string | No | Amazon marketplace to read, as its domain (e.g. amazon.co.uk); omit it for amazon.com. One of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazon.se`, `amazon.pl`, `ama |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `listPrice`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/amazon/seller-products.json`](../../../catalog/models/amazon/seller-products.json) · Store page: https://www.sandbase.ai/model/amazon/seller-products
