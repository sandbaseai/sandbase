# Shopify Store Products API: pricing, parameters and code examples

`shopify/products` · data API · Shopify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

List the products of any public Shopify store by its domain, a page at a time, with title, vendor, type, tags, price range, sale price, stock, images, options and every variant's SKU, price and stock. Filter by vendor, type, tag, title, SKU, price, sale, stock or recent arrivals. A domain that is not a public Shopify store comes back not found.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopify/products", "store": "allbirds.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shopify/products', {'store': 'allbirds.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shopify/products", {
  "store": "allbirds.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shopify/products", sandbase.Params{
	"store": "allbirds.com",
})
```

Same call via the path form: `POST /v1/api/shopify/products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of the store's product list. Each page is billed as one request. default `1`; range 1– |
| `tags` | array |  | Only products carrying at least one of these tags.  |
| `limit` | integer |  | Products the store is asked for per page (1-250, default 50). The filters below are applied to that page, so a filtered page can hold fewer, even none while hasMore is true. default `50`; range 1–250 |
| `store` | string | yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain.  |
| `vendor` | string |  | Only products whose vendor (brand) contains this text.  |
| `maxPrice` | number |  | Only products priced at or below this, in the store's currency. range 0– |
| `minPrice` | number |  | Only products priced at or above this, in the store's currency. range 0– |
| `onlyOnSale` | boolean |  | Only products with at least one discounted variant. default `false` |
| `onlyInStock` | boolean |  | Only products with at least one variant in stock. default `false` |
| `productType` | string |  | Only products whose product type contains this text, e.g. "Shoes".  |
| `skuContains` | string |  | Only products with a variant whose SKU code contains this text.  |
| `titleContains` | string |  | Only products whose title contains this text.  |
| `publishedWithinDays` | integer |  | Only products published to the store within the last this many days. range 1– |

## Details

List the products of any public Shopify store by its domain, a page at a time, with title, vendor, type, tags, price range, sale price, stock, images, options and every variant's SKU, price and stock. Filter by vendor, type, tag, title, SKU, price, sale, stock or recent arrivals. A domain that is not a public Shopify store comes back not found.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shopify/products", "limit": 10, "store": "allbirds.com"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `store` | string | Yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain. |
| `limit` | integer | No | Products the store is asked for per page (1-250, default 50). The filters below are applied to that page, so a filtered page can hold fewer, even none while hasMore is true. |
| `maxPrice` | number | No | Only products priced at or below this, in the store's currency. |
| `minPrice` | number | No | Only products priced at or above this, in the store's currency. |
| `onlyInStock` | boolean | No | Only products with at least one variant in stock. Default `false`. |
| `onlyOnSale` | boolean | No | Only products with at least one discounted variant. Default `false`. |
| `page` | integer | No | 1-based page of the store's product list. Each page is billed as one request. Default `1`. |
| `productType` | string | No | Only products whose product type contains this text, e.g. "Shoes". |
| `publishedWithinDays` | integer | No | Only products published to the store within the last this many days. |
| `skuContains` | string | No | Only products with a variant whose SKU code contains this text. |
| `tags` | array | No | Only products carrying at least one of these tags. |
| `titleContains` | string | No | Only products whose title contains this text. |
| `vendor` | string | No | Only products whose vendor (brand) contains this text. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/shopify/products.json`](../../../catalog/models/shopify/products.json) · Store page: https://www.sandbase.ai/model/shopify/products
