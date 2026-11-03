# eBay Product API: pricing, parameters and code examples

`ebay/product` · data API · eBay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Get an eBay product by product ID: title, price, condition, quantity sold, item specifics, media, shipping, returns and seller details.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/product", "product_id": "326405504746"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ebay/product', {'product_id': '326405504746'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ebay/product", {
  "product_id": "326405504746"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ebay/product", sandbase.Params{
	"product_id": "326405504746",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ebay/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string \\| number \\| boolean |  | The language to use for the search. Normally, it defaults to `en-US`, but some locales use localized interface (Japan, Argentina etc.) so override might be helpful. This parameter available only for `United States`…  |
| `locale` | string \\| number \\| boolean |  | From where you want the search to originate from. Head to the eBay locales for a full list of supported locales.  |
| `product_id` | string \\| number \\| boolean | yes | An ID of the product to get results for. Normally, it can be found in product link from search results: `https://www.ebay.com/itm/{product_id}`  |
| `ebay_domain` | string \\| number \\| boolean |  | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported domains.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_country` | string \\| number \\| boolean |  | The shipping country to use for shipping data calculation. Head to the eBay shipping countries for a full list of supported countries.  |

## Details

Returns the details of one eBay listing: title, price, condition, quantity sold, item specifics, images, shipping, returns and variations. It needs a `product_id`, the number in an eBay item link.

### Use cases

- Track the Buy It Now price and discount of a listing over time.
- Check how many units a listing has sold and how many people watch it.
- Pull item specifics, images and variation options to rebuild a listing in another catalog.
- Compare shipping cost, ship-from location and return terms across sellers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ebay/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "326405504746"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | ['string', 'number', 'boolean'] | Yes | An ID of the product to get results for. Normally, it can be found in product link from search results: `https://www.ebay.com/itm/{product_id}` |
| `ebay_domain` | ['string', 'number', 'boolean'] | No | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported domains. |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `lang` | ['string', 'number', 'boolean'] | No | The language to use for the search. Normally, it defaults to `en-US`, but some locales use localized interface (Japan, Argentina etc.) so override might be helpful. This parameter available only for `United States` eBay  |
| `locale` | ['string', 'number', 'boolean'] | No | From where you want the search to originate from. Head to the eBay locales for a full list of supported locales. |
| `shipping_country` | ['string', 'number', 'boolean'] | No | The shipping country to use for shipping data calculation. Head to the eBay shipping countries for a full list of supported countries. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "product_results": {
    "additional_services": [
      {
        "id": "909078495197-0",
        "price": {
          "amount": 54.99,
          "currency": "USD"
        },
        "snippets": [
          {
            "text": "Add peace of mind with a protection plan"
          }
        ],
        "title": "1-year protection plan",
        "type": "warranty"
      }
    ],
    "banner_status": "In 135 carts",
    "buy": {
      "buy_it_now": {
        "additional_info": [
          {
            "text": "Save US $300.00 (33% off)"
          }
        ],
        "price": {
          "amount": 599.99,
          "currency": "USD"
        }
      },
      "options": [
        "buy_it_now"
      ]
    },
    "categories": [
      {
        "link": "https://www.ebay.com/b/Electronics/bn_7000259124",
        "title": "Electronics"
      }
    ],
    "condition": "Used",
    "full_description_link": "https://itm.ebaydesc.com/itmdesc/326405504746?t=1773602404000&category=9355&sell…",
    "media": [
      {
        "image": [
          {
            "link": "https://i.ebayimg.com/images/g/15UAAeSwhA5pjPL6/s-l140.jpg",
            "size": {
              "height": 140,
              "width": 140
            }
          }
        ],
        "type": "image"
      }
    ],
    "payment_methods": {
      "financing": [
        {
          "snippet_groups": [
            [
              {
                "text": "Select PayPal Credit at checkout to have the option to pay over time."
              }
            ]
          ],
          "title": "Paypal Credit"
        }
      ],
      "payments": [
        {
          "title": "PayPal"
        }
      ]
    },
    "product_id": "326405504746",
    "product_link": "http://www.ebay.com/itm/326405504746",
    "quantity": {
      "availability_signal": "Last one",
      "available_per_buyer": {
        "max": 2,
        "min": 1
      },
      "sold": 60
    },
    "returns": [
      [
        {
          "snippets": [
            {
              "text": "No returns, but backed by"
            }
          ],
          "title": "Returns"
        }
      ]
    ]
  },
  "related_products": [
    {
      "image_link": "https://i.ebayimg.com/thumbs/images/g/ZdkAAeSwr9Jqvbb5/s-l500.jpg",
      "price": {
        "amount": 635.97,
        "currency": "USD"
      },
      "product_id": "298722439938",
      "product_link": "https://www.ebay.com/itm/298722439938"
    }
  ],
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:33:08 UTC",
    "ebay_product_url": "https://www.ebay.com/itm/326405504746",
    "id": "6ae98e342070378e07b84f3b",
    "processed_at": "2026-11-03 07:33:08 UTC",
    "status": "Success",
    "total_time_taken": 19.01
  },
  "search_parameters": {
    "ebay_domain": "ebay.com",
    "engine": "ebay_product",
    "product_id": "326405504746"
  },
  "seller_results": {
    "bio": "Welcome to The Coco Store, your ultimate destination for entertainment and fando…",
    "joined_at": "Joined Jan 2008",
    "logo_link": "https://i.ebayimg.com/images/g/LIkAAOSweKdhLD7o/s-l140.jpg",
    "name": "The Coco Store",
    "popular_categories": {
      "list": [
        {
          "category_id": "24229432011",
          "link": "https://www.ebay.com/str/cocosmartphones/iPhone-5S-SE/_i.html?store_cat=24229432…",
          "title": "iPhone 5S/SE"
        }
      ],
      "see_all_link": "https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering…"
    },
    "positive_feedback": 99.8,
    "profile_link": "https://www.ebay.com/str/cocosmartphones",
    "rating": 42312,
    "serpapi_link": {
      "endpoint": "/ebay/seller",
      "queryParams": {
        "ebay_domain": "ebay.com",
        "seller_id": "cocosmartphones",
        "type": "store"
      }
    },
    "sold_count": 131000,
    "type": "store",
    "username": "cocosmartphones"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_results.title / product_results.condition` | Listing title and item condition, such as `Used`. |
| `product_results.buy.buy_it_now.price.amount / product_results.buy.buy_it_now.price.currency` | Buy It Now price and its currency code. |
| `product_results.buy.buy_it_now.additional_info[].text` | Discount text shown next to the price, such as the amount saved and percent off. |
| `product_results.quantity.sold / product_results.quantity.availability_signal` | Number of units sold and the stock message shown on the page, such as `Last one`. |
| `product_results.watch_count / product_results.banner_status` | Number of watchers and the banner text shown on the listing, such as how many carts hold the item. |
| `product_results.specifications.groups[].sections[].fields[]` | Item specifics as `title`, `type` and `value` rows, such as `Processor`. |
| `product_results.shipping.options[]` | Shipping choices with `via` (service name), `price` and `each_additional_price`. |
| `product_results.shipping.from / product_results.shipping.status` | Where the item ships from and whether shipping is `available`. |
| `product_results.variations.menus[] / product_results.variations.combinations[]` | Menus list the choices, such as storage and color. Combinations give a `variation_id`, `price` and stock state for each choice set via `menu_option_ids`. |
| `related_products[]` | Other listings with `product_id`, `price` and `product_link`. Some also have `title` and `condition`. |

### Notes

- Take `product_id` from a listing link in the form `https://www.ebay.com/itm/{product_id}`. Use [eBay Search](/apis/ebay/search) to find listings first.
- Set `shipping_country` to calculate shipping data for another country. Set `ebay_domain` to use a different eBay site.
- Use `json_restrictor` to return only the fields you need and shrink the payload.
- Prices are objects with `amount` and `currency`. Each variation has its own `variation_id`.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/ebay/product.json`](../../../catalog/models/ebay/product.json) · Store page: https://www.sandbase.ai/model/ebay/product
