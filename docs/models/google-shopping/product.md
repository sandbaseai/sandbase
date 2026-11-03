# Google Shopping Product Details API: pricing, parameters and code examples

`google-shopping/product` · data API · Google Shopping · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

One Google Shopping product's merchant offers, prices, specifications, reviews and related products.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-shopping/product", "q": "coffee maker"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-shopping/product', {'q': 'coffee maker'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-shopping/product", {
  "q": "coffee maker"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-shopping/product", sandbase.Params{
	"q": "coffee maker",
})
```

Same call via the path form: `POST /v1/api/google-shopping/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Required search term from the shopping request that found the product. Google resolves the product page against it as well as the identifiers.  |
| `gl` | string |  | Two-letter country code used to localize results.  |
| `hl` | string |  | Language code such as en, en-GB, or de. default `"en"` |
| `prds` | string |  | Google product selector token from a previous response. Mutually exclusive with gpcid and its companion document IDs.  |
| `uule` | string |  | Pre-encoded Google location token. Mutually exclusive with location.  |
| `gpcid` | string |  | Product cluster ID from a shopping result. Required unless prds is supplied; follow litescrape_product_link for a ready-made request.  |
| `device` | string |  | Google device layout. Each device is served Google's real layout for it. one of: `desktop`, `tablet`, `mobile`; default `"desktop"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `location` | string |  | Human-readable search location, such as Austin, Texas. At most 63 UTF-8 bytes. Mutually exclusive with uule.  |
| `image_docid` | string |  | Optional image document ID from the same shopping result; use with gpcid.  |
| `google_domain` | string |  | Google domain used for the request. default `"google.com"` |
| `headline_offer_docid` | string |  | Optional headline offer document ID from the same shopping result; use with gpcid.  |

## Details

Returns details for one Google Shopping product, including its title, description, specifications and thumbnail images. You pass a search term `q` and a product cluster ID `gpcid`, usually with the companion document IDs from the same shopping result.

### Use cases

- Pull the specification list for a coffee maker to build a side-by-side comparison table.
- Fetch the product description and images to fill a catalog page for an item found in a shopping search.
- Check which product title and `gpcid` Google resolves for a search term and ID pair.
- Collect thumbnail URLs for a product to show in a price-tracking dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-shopping/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee maker", "gpcid": "3753285529675071078", "headline_offer_docid": "2823574139643882398", "image_docid": "5002652757944012799"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Required search term from the shopping request that found the product. Google resolves the product page against it as well as the identifiers. |
| `device` | string | No | Google device layout. Each device is served Google's real layout for it. |
| `gl` | string | No | Two-letter country code used to localize results. |
| `google_domain` | string | No | Google domain used for the request. |
| `gpcid` | string | No | Product cluster ID from a shopping result. Required unless prds is supplied; follow litescrape_product_link for a ready-made request. |
| `headline_offer_docid` | string | No | Optional headline offer document ID from the same shopping result; use with gpcid. |
| `hl` | string | No | Language code such as en, en-GB, or de. |
| `image_docid` | string | No | Optional image document ID from the same shopping result; use with gpcid. |
| `location` | string | No | Human-readable search location, such as Austin, Texas. At most 63 UTF-8 bytes. Mutually exclusive with uule. |
| `prds` | string | No | Google product selector token from a previous response. Mutually exclusive with gpcid and its companion document IDs. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the cal |
| `uule` | string | No | Pre-encoded Google location token. Mutually exclusive with location. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "offers": null,
  "product_result": {
    "description": "Kickstart your mornings with the invigorating aroma of freshly brewed coffee, th…",
    "gpcid": "3753285529675071078",
    "headline_offer_docid": "2823574139643882398",
    "image_docid": "5002652757944012799",
    "specifications": [
      {
        "name": "Capacity",
        "value": "10 cups"
      }
    ],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSE-TeJ2k_-GjVS30DtuitDDc…",
    "thumbnails": [
      "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSE-TeJ2k_-GjVS30DtuitDDc…"
    ],
    "title": "Starfrit 10-Cup Drip Coffee Maker"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_result.title` | Product name as Google Shopping shows it. |
| `product_result.description` | Text description of the product. Long descriptions may be cut off in the sample. |
| `product_result.gpcid` | Product cluster ID of the product. It matches the `gpcid` you sent. |
| `product_result.headline_offer_docid / product_result.image_docid` | Document IDs for the headline offer and the product image. Use them with `gpcid` in later requests. |
| `product_result.specifications[].name` | Name of a product attribute, such as `Capacity` or `Depth`. |
| `product_result.specifications[].value` | Value of that attribute, written with its unit, such as `10 cups` or `7.97 in`. |
| `product_result.thumbnail` | URL of the main product thumbnail image. |
| `product_result.thumbnails[]` | URLs of additional thumbnail images for the product. |
| `offers` | Merchant offers for the product. This is `null` in this response, so no offers were returned for this request. |

### Notes

- Get `gpcid`, `headline_offer_docid` and `image_docid` from one result of the same shopping search, for example with [Google Shopping Search](/apis/google-shopping/search).
- Send `q` with every request. It is the only required parameter.
- Use either `prds` or `gpcid` with its companion IDs, not both. `location` and `uule` are also mutually exclusive.
- The data is in `outputs[0].data`. The `offers` key can be `null`, so check it before you read it.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/google-shopping/product.json`](../../../catalog/models/google-shopping/product.json) · Store page: https://www.sandbase.ai/model/google-shopping/product
