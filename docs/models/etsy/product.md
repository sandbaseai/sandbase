# Etsy Product API: pricing, parameters and code examples

`etsy/product` · data API · Etsy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00187 per call · **Modes:** sync

Look up one Etsy listing by id and get its price, images, description, rating, reviews count, shop, category, variations, stock, ship-from country, favorites and materials in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00187**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "etsy/product", "listingId": "1810545592"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('etsy/product', {'listingId': '1810545592'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("etsy/product", {
  "listingId": "1810545592"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "etsy/product", sandbase.Params{
	"listingId": "1810545592",
})
```

Same call via the path form: `POST /v1/api/etsy/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `listingId` | string | yes | Etsy listing id, the number in the listing URL (https://www.etsy.com/listing/<id>/...), e.g. 1810545592. The Etsy Search and Etsy Shop Listings SKUs return it as listingId.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `materials`, and it is served only by a source that returns every…  |

## Details

Look up one Etsy listing by id and get its price, images, description, rating, reviews count, shop, category, variations, stock, ship-from country, favorites and materials in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "etsy/product", "listingId": "1810545592"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `listingId` | string | Yes | Etsy listing id, the number in the listing URL (https://www.etsy.com/listing/<id>/...), e.g. 1810545592. The Etsy Search and Etsy Shop Listings SKUs return it as listingId. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `materials`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, about $0.00187 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/etsy/product.json`](../../../catalog/models/etsy/product.json) · Store page: https://www.sandbase.ai/model/etsy/product
