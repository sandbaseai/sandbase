# DataForSEO Merchant Amazon Sellers API: pricing, parameters and code examples

`dataforseo/v3/merchant/amazon/sellers/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0033 per call · **Modes:** sync

Retrieves real-time Amazon seller information and merchant data across e-commerce listings. Returns merchant profiles, ratings, and seller metrics for competitive analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0033**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/merchant/amazon/sellers/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/merchant/amazon/sellers/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/merchant/amazon/sellers/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/merchant/amazon/sellers/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/merchant/amazon/sellers/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string |  | Amazon product ASIN.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the list of sellers that offer a given Amazon product, with the condition, price and delivery details of each offer. It needs a product `asin`, plus an optional `location_code` and `language_code`.

### Use cases

- Compare new and used offer prices for one ASIN across all sellers.
- Check which offer holds the top position and what delivery date it promises.
- Find coupons attached to a seller offer on a target product.
- Track how many sellers list a competitor product over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/merchant/amazon/sellers/live/advanced" \
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
        "function": "sellers",
        "language_code": "en_US",
        "location_code": 2840,
        "os": "windows",
        "se": "amazon"
      },
      "id": "11030829-1614-0646-0000-4326915d97c1",
      "path": [
        "v3"
      ],
      "result": [
        {
          "asin": "B0CP9YB3Q4",
          "check_url": "https://www.amazon.com/dp/B0CP9YB3Q4/ref=olp_aod_redir_impl1?_encoding=UTF8&aod=…",
          "datetime": "2026-11-03 08:30:10 +00:00",
          "image": "https://m.media-amazon.com/images/I/31CNE+44-xL.jpg",
          "item_types": [
            "amazon_seller_main_item"
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
              "condition": "New",
              "condition_description": null,
              "delivery_info": {
                "delivery_date_from": "2026-11-08T00:00:00+00:00",
                "delivery_date_to": null,
                "delivery_message": "FREE delivery Sunday, November 8 Or Prime members get FREE delivery Friday, Nove…",
                "delivery_price": null,
                "fastest_delivery_date_from": "2026-11-06T00:00:00+00:00",
                "fastest_delivery_date_to": null
              },
              "percentage_discount": null,
              "position": "left",
              "price": {
                "currency": "USD",
                "current": 37.51,
                "displayed_price": "$37.51",
                "is_price_range": false,
                "max_value": null,
                "regular": null
              },
              "rank_absolute": 1
            }
          ],
          "items_count": 8,
          "language_code": "en_US"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "34.1572 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "34.1804 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].asin` | The ASIN of the product the seller offers belong to. |
| `tasks[].result[].check_url` | Amazon page URL that lists the offers for this product. |
| `tasks[].result[].items_count` | Number of seller offers found for the product. |
| `tasks[].result[].items[].rank_absolute` | Position of the offer in the list. `1` is the first (main) offer. |
| `tasks[].result[].items[].condition` | Condition of the item in the offer, for example `New` or `Used - Very Good`. |
| `tasks[].result[].items[].price.current / tasks[].result[].items[].price.displayed_price` | Current offer price as a number and as the text shown on Amazon. |
| `tasks[].result[].items[].price.currency` | Currency code of the price, for example `USD`. |
| `tasks[].result[].items[].delivery_info.delivery_message` | Delivery text shown for the offer, including free shipping and Prime terms. |
| `tasks[].result[].items[].delivery_info.delivery_date_from / tasks[].result[].items[].delivery_info.fastest_delivery_date_from` | Standard and fastest delivery dates in ISO 8601 format. |
| `tasks[].result[].items[].applicable_vouchers[].text` | Coupon text for the offer. The `fixed_discount` field holds the coupon amount. |

### Notes

- Take the `asin` from an Amazon product URL, where it follows `/dp/`.
- Use `location_code` `2840` for the United States.
- `applicable_vouchers` is `null` when an offer has no coupon.
- The response lists only a few items in this sample, so compare `items_count` with the length of `items` to see how many offers came back.

### Pricing

Billed at the actual cost of each call, about $0.0033 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/sellers/live/advanced
