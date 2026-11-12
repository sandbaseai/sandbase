# Amazon Offers API: pricing, parameters and code examples

`amazon/offers` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

List every offer for one Amazon product by ASIN or product URL, the Buy Box first and then the other sellers, and get price, condition, seller name and ID, seller rating, Prime, delivery estimate and fulfillment for each in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/offers", "product": "B00000IZJB"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/offers', {'product': 'B00000IZJB'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/offers", {
  "product": "B00000IZJB"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/offers", sandbase.Params{
	"product": "B00000IZJB",
})
```

Same call via the path form: `POST /v1/api/amazon/offers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of the other sellers' offers, about 10 a page; page 1 also carries the Buy Box. Each page is billed as one request. default `1`; range 1– |
| `region` | string |  | Amazon marketplace the product ASIN belongs to (e.g. amazon.co.uk); a product URL sets it from its own domain. one of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazon.se`, `amazon.pl`, `amazon.ca`, `amazon.com.mx`, `amazon.com.br` … |
| `product` | string | yes | Amazon product ASIN (e.g. B006MIWDCC) or a product link on one of the marketplaces listed under region, such as https://www.amazon.co.uk/dp/<ASIN>, with the ASIN after /dp/, /gp/product/ or /product-reviews/. A link…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerId`, and it is served only by a source that returns every one…  |

## Details

List every offer for one Amazon product by ASIN or product URL, the Buy Box first and then the other sellers, and get price, condition, seller name and ID, seller rating, Prime, delivery estimate and fulfillment for each in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "amazon/offers", "product": "B00000IZJB"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product` | string | Yes | Amazon product ASIN (e.g. B006MIWDCC) or a product link on one of the marketplaces listed under region, such as https://www.amazon.co.uk/dp/<ASIN>, with the ASIN after /dp/, /gp/product/ or /product-reviews/. A link with |
| `page` | integer | No | 1-based page of the other sellers' offers, about 10 a page; page 1 also carries the Buy Box. Each page is billed as one request. Default `1`. |
| `region` | string | No | Amazon marketplace the product ASIN belongs to (e.g. amazon.co.uk); a product URL sets it from its own domain. One of: `amazon.com`, `amazon.co.uk`, `amazon.de`, `amazon.fr`, `amazon.it`, `amazon.es`, `amazon.nl`, `amazo |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerId`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/amazon/offers.json`](../../../catalog/models/amazon/offers.json) · Store page: https://www.sandbase.ai/model/amazon/offers
