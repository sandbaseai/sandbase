# Walmart Product Page API: pricing, parameters and code examples

`walmart/scrape/product` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Extract structured data from a Walmart product page URL: name, current and list price, stock, delivery estimate, ratings and seller details.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/scrape/product", "url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/scrape/product', {'url': 'https://www.walmart.com/ip/HP-14-Laptop/17581855155'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/scrape/product", {
  "url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/scrape/product", sandbase.Params{
	"url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/scrape/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Walmart page URL, e.g. https://www.walmart.com/ip/HP-14-Laptop/17581855155  |
| `country` | string |  | Walmart marketplace country code, e.g. 'us', 'ca', 'mx' (default 'us').  |
| `storeId` | string |  | Walmart store ID for localized inventory.  |
| `zipCode` | string |  | US zip code used to determine local product availability.  |

## Details

Returns structured data for one Walmart product page: name, price, availability, images, review count and seller details. It needs the full product page URL as `url`.

### Use cases

- Track the listed price of a specific Walmart laptop or other item over time.
- Check whether a product is in stock for a given store or zip code.
- Identify which third-party seller is listing an item and link to their seller page.
- Collect product names, descriptions and image URLs to build a catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/scrape/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.walmart.com/ip/HP-14-Laptop/17581855155"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Walmart page URL, e.g. https://www.walmart.com/ip/HP-14-Laptop/17581855155 |
| `country` | string | No | Walmart marketplace country code, e.g. 'us', 'ca', 'mx' (default 'us'). |
| `storeId` | string | No | Walmart store ID for localized inventory. |
| `zipCode` | string | No | US zip code used to determine local product availability. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "currency": "$",
  "description": "<p>Statement: Original Seal is opened for upgrade ONLY. If the computer has modi…",
  "price": "$599.99",
  "productAvailability": true,
  "productId": "17581855155",
  "productImages": [
    "https://i5.walmartimages.com/seo/HP-14-Laptop-Student-Business-Computer-Intel-N1…"
  ],
  "productName": "HP 14\" Laptop Student Business Computer, Intel N150 Processor, 1-Year Microsoft …",
  "reviewCount": 115,
  "sellerId": "974611902A77437FBB999DF11CCBF0BA",
  "sellerName": "82days Tech",
  "sellerUrl": "https://www.walmart.com/global/seller/102594305",
  "soldCount": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `productId` | Walmart product ID. It matches the number at the end of the product page URL. |
| `productName` | Full product title as shown on the page. |
| `price` | Current price as a string with the currency symbol, for example `$599.99`. |
| `currency` | Currency symbol used for the price. |
| `productAvailability` | Boolean. `true` means the product is available for the requested location. |
| `reviewCount` | Number of customer reviews for the product. |
| `productImages[]` | List of product image URLs. |
| `description` | Product description. It contains HTML markup and may be cut short. |
| `sellerName / sellerId / sellerUrl` | Name, ID and Walmart page URL of the seller listing the product. |
| `soldCount` | Units sold, when the page shows it. It is `null` when the page gives no value. |

### Notes

- Copy the `url` from a Walmart product page. The product ID is the last part of the path, for example `17581855155`.
- Use `country` to pick the marketplace, and use `storeId` or `zipCode` to localize availability.
- To find product URLs first, call [Walmart Search](/apis/walmart/search).
- To read customer reviews for the product, call [Walmart Product Reviews](/apis/walmart/product-reviews).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/walmart/scrape/product.json`](../../../../catalog/models/walmart/scrape/product.json) · Store page: https://www.sandbase.ai/model/walmart/scrape/product
