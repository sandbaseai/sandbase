# Amazon Product Details API: pricing, parameters and code examples

`amazon/product-detail` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog review, product comparison, or downstream commerce analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/product-detail", "asin": "B0D1XD1ZV3"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/product-detail', {'asin': 'B0D1XD1ZV3'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/product-detail", {
  "asin": "B0D1XD1ZV3"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/product-detail", sandbase.Params{
	"asin": "B0D1XD1ZV3",
})
```

Same call via the path form: `POST /v1/api/amazon/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string | yes | ASIN (Amazon Standard Identification Number).  |
| `country` | string |  | Country code for the Amazon product. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |

## Details

This API returns the details of one Amazon listing, including bullet points, variations, delivery text, stock message, and badge flags. It needs an `asin` and optionally a `country` code for the marketplace, which defaults to `US`.

### Use cases

- Check a known listing's stock message and delivery estimate in a chosen country marketplace.
- Compare the bullet points and brand byline of two ASINs during catalog review.
- Map a variation ASIN to its `parent_asin` to group related listings.
- Read the `customers_say` summary to get a quick view of customer feedback on a product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0D1XD1ZV3"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string | Yes | ASIN (Amazon Standard Identification Number). |
| `country` | string | No | Country code for the Amazon product. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about_product": [
    "INTELLIGENT NOISE CONTROL — Active Noise Cancellation removes up to 2x more back…"
  ],
  "all_product_variations": {
    "B0D1XD1ZV3": {
      "style": "Without AppleCare+"
    }
  },
  "aplus_images": [],
  "aplus_text": null,
  "asin": "B0D1XD1ZV3",
  "best_sellers_rank": null,
  "brand_store_id": "77D9E1F7-0337-4282-9DB6-B6B8FB2DC98D",
  "buy_boxes": [],
  "carousel_products": null,
  "category": {
    "id": "aps",
    "name": "All Departments"
  },
  "category_path": [],
  "climate_pledge_friendly": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `asin / landing_asin / parent_asin` | The ASIN of the requested listing, the ASIN of the landing page, and the ASIN of the parent product that groups its variations. |
| `about_product[]` | The bullet points from the listing, as a list of strings. |
| `all_product_variations` | Variations of the product, keyed by ASIN. Each entry holds the variation attributes, such as `style`. |
| `product_byline` | The byline text shown with the listing, such as `Visit the Apple Store`. |
| `product_availability` | The stock message shown on the page, such as how many units are left. |
| `delivery / delivery_time / primary_delivery_time` | The delivery text shown on the page, and the delivery date range split out as its own value. |
| `is_prime / is_best_seller / is_amazon_choice / climate_pledge_friendly` | Boolean flags for Prime status and badges on the listing. |
| `customers_say` | A short text summary of what customers say about the product. |
| `country / currency / domain / marketplace_id` | The marketplace the data came from: the country code, the currency code, the Amazon domain, and the marketplace ID. |
| `has_video / has_aplus / has_brandstory` | Boolean flags that show whether the listing has a video, A+ content, or a brand story. |

### Notes

- Pass `country` as a code such as `US`, `DE`, or `JP`. If you omit it, the request uses `US`.
- Use [Amazon Product Search](/apis/amazon/search-products) to find other listings, then pass each `asin` to this API.
- Some fields can be `null` or an empty list when the listing has no such data, for example `best_sellers_rank`, `buy_boxes`, and `aplus_text`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/product-detail.json`](../../../catalog/models/amazon/product-detail.json) · Store page: https://www.sandbase.ai/model/amazon/product-detail
