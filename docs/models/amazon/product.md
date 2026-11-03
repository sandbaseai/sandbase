# Amazon Product API: pricing, parameters and code examples

`amazon/product` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get an Amazon product by ASIN: title, brand, price, rating, reviews, images, variants, availability, purchase options, about-this-item and description.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/product", "asin": "B0CP9YB3Q4"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/product', {'asin': 'B0CP9YB3Q4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/product", {
  "asin": "B0CP9YB3Q4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/product", sandbase.Params{
	"asin": "B0CP9YB3Q4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/amazon/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string \\| number \\| boolean | yes | The Amazon Standard Identification Number (ASIN) of the product you want to retrieve. This is a unique identifier assigned to each product on Amazon.  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `language` | string \\| number \\| boolean |  | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a…  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `amazon_domain` | string \\| number \\| boolean |  | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains.  |
| `other_sellers` | string \\| number \\| boolean |  | Include results from other sellers.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_location` | string \\| number \\| boolean |  | Shipping country. To filter the shipping products by a selected country.  |
| `all_related_products` |  |  | Set to `true` to retrieve all items in `related_products` and `related_product_sections`, not just the first page. May yield better results but with a longer response time. Defaults to `false`.  |

## Details

Returns the Amazon product page for one ASIN as structured JSON. It includes title, rating, review count, images, variants, purchase options, specifications and related products. The only required input is `asin`.

### Use cases

- Track coupons, badges and stock status of a single ASIN.
- Collect specifications such as brand, capacity, material and UPC for catalog matching.
- Map every size and color variant of a product to its own ASIN.
- Read best sellers rank and review counts to compare a product against its category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | ['string', 'number', 'boolean'] | Yes | The Amazon Standard Identification Number (ASIN) of the product you want to retrieve. This is a unique identifier assigned to each product on Amazon. |
| `all_related_products` | string | No | Set to `true` to retrieve all items in `related_products` and `related_product_sections`, not just the first page. May yield better results but with a longer response time. Defaults to `false`. |
| `amazon_domain` | ['string', 'number', 'boolean'] | No | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains. |
| `delivery_zip` | ['string', 'number', 'boolean'] | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `device` | ['string', 'number', 'boolean'] | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `language` | ['string', 'number', 'boolean'] | No | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a full |
| `other_sellers` | ['string', 'number', 'boolean'] | No | Include results from other sellers. |
| `shipping_location` | ['string', 'number', 'boolean'] | No | Shipping country. To filter the shipping products by a selected country. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about_item": [
    "YOUR DREAM TUMBLER: Whichever way your day flows, the H2.0 FlowState tumbler kee…"
  ],
  "bought_together": [
    {
      "delivery": [
        "Get it as soon as Sunday, Nov 8"
      ],
      "extracted_price": 37.51,
      "position": 1,
      "price": "$37.51",
      "stock": "In Stock",
      "thumbnail": "https://images-na.ssl-images-amazon.com/images/I/51-U5dEbEBL._AC_UL116_SR116,116…",
      "title": "STANLEY Quencher H2.0 Tumbler with Handle and Straw 30 oz | Flowstate 3-Position…"
    }
  ],
  "item_specifications": {
    "brand": "STANLEY",
    "capacity": "30 fluid ounces",
    "color": "Rose Quartz 2.0",
    "material": "Stainless Steel",
    "special_feature": "Rotating"
  },
  "product_description": [
    {
      "image": "https://m.media-amazon.com/images/S/aplus-media-library-service-media/1dea9f7a-4…",
      "position": 1,
      "title": "The one and only - Quencher Flowstate H2.0 Tumbler"
    }
  ],
  "product_details": {
    "age_range_description": "Adult",
    "asin": "B0CP9YB3Q4",
    "best_sellers_rank": [
      {
        "extracted_rank": 7,
        "link": "https://www.amazon.com/gp/bestsellers/kitchen/ref=pd_zg_ts_kitchen",
        "link_text": "See Top 100 in Kitchen & Dining",
        "text": "#7 in Kitchen & Dining (See Top 100 in Kitchen & Dining)"
      }
    ],
    "brand_name": "STANLEY",
    "capacity": "30 fluid ounces",
    "color": "Rose Quartz 2.0",
    "customer_reviews": "4.7 out of 5 stars",
    "finish_types": "Brushed",
    "global_trade_identification_number": "00041604414831",
    "included_components": "Lid, Straw",
    "item_dimensions_w_x_h": "5.43\"W x 12.52\"H",
    "item_type_name": "Tumbler"
  },
  "product_results": {
    "asin": "B0CP9YB3Q4",
    "badges": [
      "Amazon's Choice"
    ],
    "bought_last_month": "5K+ bought in past month",
    "categories": [
      {
        "link": "https://www.amazon.com/home-garden-kitchen-furniture-bedding/b/ref=dp_bc_1?ie=UT…",
        "name": "Home & Kitchen",
        "node": "1055398",
        "position": 1,
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "node": "1055398"
          }
        }
      }
    ],
    "coupons": [
      {
        "discount": "$8.29",
        "terms_link": "https://www.amazon.com/promotion/details/popup/AQ28VQOKL3OQB?ref=cxcw_bxgx_tc_AQ…",
        "text": "Apply $8.29 coupon"
      }
    ],
    "delivery": [
      "FREE delivery Sunday, November 8"
    ],
    "description": "This Quencher H2.0 is generously sized (but not oversized) with an easy-carry, c…",
    "extracted_price": 37.51,
    "link": "https://www.amazon.com/STANLEY-Flowstate-3-Position-Compatible-Insulated/dp/B0CP…",
    "link_clean": "https://www.amazon.com/dp/B0CP9YB3Q4/",
    "price": "$37.51",
    "promotions": [
      {
        "currency": "$",
        "discount": "$8.29",
        "extracted_discount": 8.29,
        "text": "Apply $8.29 coupon",
        "type": "coupon"
      }
    ]
  },
  "purchase_options": {
    "buy_new": {
      "caption": "Buy New",
      "delivery": [
        "FREE delivery Sunday, November 8"
      ],
      "extracted_price": 37.51,
      "features": {
        "payment": {
          "details": {
            "content": "We work hard to protect your security and privacy. Our payment security system e…",
            "heading": "Your transaction is secure"
          },
          "link": {
            "link": "https://www.amazon.com/gp/help/customer/display.html?nodeId=201909010",
            "text": "Learn more"
          },
          "text": "Secure transaction"
        },
        "returns": {
          "details": {
            "content": "For the 2026 holiday season, eligible items purchased between November 1 and Dec…",
            "heading": "FREE refund/replacement until Jan 31, 2027"
          },
          "link": {
            "link": "https://www.amazon.com/gp/help/customer/display.html/?nodeId=GKQNFKFK5CF3C54B",
            "text": "See exceptions"
          },
          "text": "FREE refund/replacement until Jan 31, 2027"
        },
        "shipper_seller": {
          "details": {
            "content": "Amazon.com",
            "heading": "Shipper / Seller"
          },
          "text": "Amazon.com"
        }
      },
      "price": "$37.51",
      "stock": "In Stock"
    },
    "buy_used": {
      "caption": "Used - Like New",
      "delivery": [
        "FREE delivery Sunday, November 8 on orders shipped by Amazon over $35"
      ],
      "extracted_price": 24.38,
      "features": {
        "ships_from": "Amazon",
        "sold_by": "Amazon Resale"
      },
      "price": "$24.38",
      "stock": "In Stock"
    }
  },
  "related_product_sections": [
    {
      "items": [
        {
          "asin": "B0DCDZP98B",
          "delivery": [
            "Get it as soon as Sunday, Nov 8"
          ],
          "extracted_price": 40,
          "link": "https://www.amazon.com/STANLEY-Quencher-ProTour-Flipstraw-Tumbler/dp/B0DCDZP98B/…",
          "link_clean": "https://www.amazon.com/STANLEY-Quencher-ProTour-Flipstraw-Tumbler/dp/B0DCDZP98B/",
          "position": 1,
          "price": "$40.00",
          "rating": 4.7
        }
      ],
      "title": "Customers who viewed this item also viewed"
    }
  ],
  "related_products": [
    {
      "asin": "B0DCDZP98B",
      "delivery": [
        "Get it as soon as Sunday, Nov 8"
      ],
      "extracted_price": 40,
      "link": "https://www.amazon.com/STANLEY-Quencher-ProTour-Flipstraw-Tumbler/dp/B0DCDZP98B/…",
      "link_clean": "https://www.amazon.com/STANLEY-Quencher-ProTour-Flipstraw-Tumbler/dp/B0DCDZP98B/",
      "position": 1,
      "price": "$40.00",
      "rating": 4.7,
      "reviews": 21948,
      "serpapi_link": {
        "endpoint": "/amazon/product",
        "queryParams": {
          "amazon_domain": "amazon.com",
          "asin": "B0DCDZP98B",
          "device": "desktop"
        }
      },
      "thumbnail": "https://images-na.ssl-images-amazon.com/images/I/51L-q8h+bwL._AC_UL165_SR165,165…",
      "title": "STANLEY Quencher ProTour Flipstraw Tumbler, 30 oz, Rose Quartz | Built-In Straw …"
    }
  ],
  "reviews_information": {
    "summary": {
      "customer_reviews": {
        "1 star": 3,
        "2 star": 1,
        "3 star": 2,
        "4 star": 7,
        "5 star": 87
      },
      "insights": [
        {
          "examples": [
            {
              "link": "https://www.amazon.com/portal/customer-reviews/srp/-/R3GE9HCZ0GT0ZE",
              "position": 1,
              "snippet": "...I have one and it’s perfect. Keeps my water cold for hours and hours. Solid c…"
            }
          ],
          "mentions": {
            "negative": 1759,
            "positive": 10504,
            "total": 12200
          },
          "sentiment": "positive",
          "summary": "Customers find the tumbler to be fantastic and absolutely perfect, with one cust…",
          "title": "Quality"
        }
      ],
      "text": "Customers love this tumbler's beautiful appearance and appreciate its 30oz size,…"
    }
  },
  "search_metadata": {
    "amazon_product_url": "https://www.amazon.com/dp/B0CP9YB3Q4/?",
    "cached": true,
    "created_at": "2026-11-03 07:25:30 UTC",
    "id": "6ae98c6ab69cbef313330fcf",
    "processed_at": "2026-11-03 07:25:30 UTC",
    "status": "Success",
    "total_time_taken": 8.76
  },
  "search_parameters": {
    "amazon_domain": "amazon.com",
    "asin": "B0CP9YB3Q4",
    "device": "desktop",
    "engine": "amazon_product"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_results.title / product_results.asin` | Product title and its ASIN. Long titles are cut off. |
| `product_results.rating / product_results.reviews` | Average star rating and total number of reviews. |
| `product_results.stock` | Availability text, for example `In Stock`. |
| `product_results.promotions[]` | Active promotions. Each row has a `type` (such as `coupon`), a `text` label and the discount as `extracted_discount`. |
| `product_results.variants[].items[]` | Options for each variant group such as Size or Color. Each item has a `name` and an `asin`. The `selected` flag marks the current product. |
| `product_results.variant_combinations[]` | Size and color pairs in `dimensions`. Each pair has its own `asin`, or is marked `unavailable`. |
| `product_results.categories[]` | Category path of the product. Each row has a `name`, a `node` ID and a `position`. |
| `product_details.best_sellers_rank[]` | Sales rank in each category, with `extracted_rank` as a number and a `text` label. |
| `item_specifications.brand / item_specifications.capacity / item_specifications.color / item_specifications.material` | Short specification values for the product, such as brand and capacity. |
| `purchase_options.buy_new / purchase_options.buy_used` | Offer details for new and used buying: `stock`, `delivery` and seller information in `features`. |

### Notes

- Find the ASIN in the product page URL after `/dp/`, for example `B0CP9YB3Q4`.
- Set `amazon_domain` to read another Amazon site. It defaults to `amazon.com`.
- Each variant item has its own `asin`. Pass that value as `asin` to call this API again for that item.
- To find ASINs first, use [Amazon Search](/apis/amazon/search) or [Amazon Best Sellers](/apis/amazon/best-sellers).

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/product.json`](../../../catalog/models/amazon/product.json) · Store page: https://www.sandbase.ai/model/amazon/product
