# DataForSEO Merchant Amazon ASIN API: pricing, parameters and code examples

`dataforseo/v3/merchant/amazon/asin/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns real-time Amazon product details for a single ASIN: title, brand, price, availability, rating and review count, images, bullet points, specifications, variants and buy-box seller.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/merchant/amazon/asin/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/merchant/amazon/asin/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/merchant/amazon/asin/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/merchant/amazon/asin/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/merchant/amazon/asin/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string |  | Amazon product ASIN.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns live Amazon product details for one ASIN, such as the store line, categories, coupons, description, specs and main image. You send an `asin` plus a `location_code` and `language_code`.

### Use cases

- Fill a product catalogue with the Amazon description, category path, spec text and image for each ASIN.
- Check which coupons are active on a competitor ASIN, including the fixed or percentage discount.
- Map an ASIN to its Amazon category breadcrumb to sort products into your own taxonomy.
- Open the `check_url` of an ASIN to confirm which page and language version was fetched.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/merchant/amazon/asin/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4", "location_code": 2840, "language_code": "en_US"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string | No | Amazon product ASIN. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "merchant",
        "asin": "B0CP9YB3Q4",
        "device": "desktop",
        "function": "asin",
        "language_code": "en_US",
        "location_code": 2840,
        "os": "windows",
        "se": "amazon"
      },
      "id": "11030829-1614-0648-0000-c639c92f9d82",
      "path": [
        "v3"
      ],
      "result": [
        {
          "asin": "B0CP9YB3Q4",
          "check_url": "https://www.amazon.com/dp/B0CP9YB3Q4?language=en_US",
          "datetime": "2026-11-03 08:30:05 +00:00",
          "item_types": [
            "amazon_product_info"
          ],
          "items": [
            {
              "applicable_vouchers": [
                {
                  "fixed_discount": 8.29,
                  "fixed_discount_currency": "USD",
                  "important_details": null,
                  "percentage_discount": null,
                  "text": "Apply $8.29 coupon",
                  "type": "amazon_applicable_vouchers_item"
                }
              ],
              "author": "Visit the STANLEY Store",
              "categories": [
                {
                  "category": "Home & Kitchen",
                  "url": "https://amazon.com/home-garden-kitchen-furniture-bedding/b/ref=dp_bc_1?ie=UTF8&n…"
                }
              ],
              "currency": "USD",
              "data_asin": "B0CP9YB3Q4",
              "description": "About this item  YOUR DREAM TUMBLER: Whichever way your day flows, the H2.0 Flow…",
              "details": "Product information\nItem details\nBrand Name\tSTANLEY\nRecommended Uses For Product…",
              "image_url": "https://m.media-amazon.com/images/I/51-U5dEbEBL._AC_SY300_SX300_QL70_FMwebp_.jpg"
            }
          ],
          "items_count": 1,
          "language_code": "en_US",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "27.3048 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "27.3292 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].asin` | The ASIN that was looked up. |
| `tasks[].result[].check_url` | The Amazon product page URL for this ASIN and language. Open it to compare the data with the live page. |
| `tasks[].result[].datetime` | Time the product page was fetched, for example `2026-11-03 08:30:05 +00:00`. |
| `tasks[].result[].items[].author` | The store or brand line shown on the product page, for example `Visit the STANLEY Store`. |
| `tasks[].result[].items[].categories[].category / url` | Each step of the Amazon category breadcrumb, with its name and a link to that category page. |
| `tasks[].result[].items[].currency` | Currency code used for money values on the item, for example `USD`. |
| `tasks[].result[].items[].applicable_vouchers[].text` | The coupon label shown on the page, for example `Apply $8.29 coupon`. |
| `tasks[].result[].items[].applicable_vouchers[].fixed_discount / fixed_discount_currency / percentage_discount` | The coupon value as a fixed amount with its currency, or as a percentage. The field that does not apply is `null`. |
| `tasks[].result[].items[].description` | Product description text, including the "About this item" bullet points. |
| `tasks[].result[].items[].details` | Product information table as plain text. Each row holds a label and a value separated by a tab, such as `Brand Name` and `Manufacturer`. |
| `tasks[].result[].items[].image_url` | URL of the main product image. |

### Notes

- Find the ASIN in the Amazon product URL after `/dp/`, for example `B0CP9YB3Q4` in `https://www.amazon.com/dp/B0CP9YB3Q4`.
- Use `location_code` `2840` for the United States. The sample call uses `en_US` for `language_code`.
- The product data sits in `tasks[].result[].items[]`. `items_count` tells you how many items came back for the ASIN.
- A `status_code` of `20000` on the response and on each task means the call succeeded.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [DataForSEO Merchant Amazon Products](/apis/dataforseo/v3/merchant/amazon/products/live/advanced): Returns Amazon search results for a keyword with ratings, sellers and positions.
- [DataForSEO Merchant Amazon Sellers](/apis/dataforseo/v3/merchant/amazon/sellers/live/advanced): Returns sellers and offers for an Amazon product.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/asin/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/asin/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/asin/live/advanced
