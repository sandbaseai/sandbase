# Meijer Product Page API: pricing, parameters and code examples

`meijer/scrape/product` · data API · Meijer · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Extract structured data from a Meijer product page URL: price, availability and product details, optionally localized by ZIP code.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meijer/scrape/product", "url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meijer/scrape/product', {'url': 'https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meijer/scrape/product", {
  "url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meijer/scrape/product", sandbase.Params{
	"url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/meijer/scrape/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Meijer page URL, e.g. https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html  |
| `zipCode` | string |  | ZIP or postal code used for localized pricing and availability.  |

## Details

Returns structured data for one Meijer product page, including name, brand, UPC, category, images and fulfillment flags. It needs the full product page `url`, and accepts an optional `zipCode` for localized results.

### Use cases

- Look up the UPC and brand of a Meijer product from its page URL to match it against another catalog.
- Check whether an item is eligible for curbside pickup or home delivery.
- Collect product images and descriptions to fill a product database.
- Check whether an item is active, age restricted or eligible for food stamps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/meijer/scrape/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Meijer page URL, e.g. https://www.meijer.com/shopping/product/highlighters-4pk/71928356637.html |
| `zipCode` | string | No | ZIP or postal code used for localized pricing and availability. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "product": {
    "brandDescription": "Meijer",
    "brandName": "MEIJER",
    "category": "HARDLINES,SCHOOL HOME OFFICE,WRITING INSTRUMENTS,HIGHLIGHTERS",
    "colorGeneral": "Assorte",
    "colorSpecific": null,
    "countryOfOrigin": null,
    "descriptiveFeatures": "Thin Chisel Tip Highlighters Assorted 4PK",
    "disclaimer": "Statements regarding dietary supplements have not been evaluated by the Food and…",
    "eventType": null,
    "hasMPerks": false,
    "ingredients": null,
    "isAlcohol": false
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product.productName` | Display name of the product on the Meijer page. |
| `product.productId / product.upc` | Meijer's internal product ID and the product's UPC barcode number. `upcTypeName` gives the barcode type, such as `UPCA`. |
| `product.brandName / product.brandDescription` | Brand of the product. |
| `product.category` | Comma-separated category path from broad department to specific type. |
| `product.productDescription / product.productDetails / product.descriptiveFeatures` | Short descriptive text for the product, in different lengths and wording. |
| `product.productMedia[].url` | Image URL. Each entry also has `width` and `height`, so you can pick a size, and `isDefault` marks default images. |
| `product.isCurbsideEligible / product.isHomeDeliveryAvailable` | Whether the item can be ordered for curbside pickup or home delivery. |
| `product.isFoodStampEligible / product.isAlcohol / product.isProductAgeRestricted` | Eligibility and restriction flags for the item. |
| `product.productStatus / product.isBusinessActive` | Listing status of the product. The sample value for `productStatus` is `ACT`. |
| `product.soldByUnit / product.unitOfMeasureQuantity` | Unit the item is sold in and the quantity per unit. The sample shows `EA` and `1`. |

### Notes

- Copy the `url` from a Meijer product page. The number before `.html` in the sample URL matches the `upc` value in the response.
- Add `zipCode` to localize the result. Fields that are not set for a product come back as `null`.
- The sample response has no price field. Product details and fulfillment flags are present.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/meijer/scrape/product.json`](../../../../catalog/models/meijer/scrape/product.json) · Store page: https://www.sandbase.ai/model/meijer/scrape/product
