# Amazon Search API: pricing, parameters and code examples

`amazon/search` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Amazon by keyword: organic results with ASIN, title, price, old price, rating, reviews, Prime and delivery info, plus sponsored products and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/search", "k": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/search', {'k': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/search", {
  "k": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/search", sandbase.Params{
	"k": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/amazon/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `k` | string \\| number \\| boolean | yes | The query you want to search. You can use anything that you would use in a regular Amazon search. This parameter can't be used with the `node` parameter.  |
| `s` |  |  | Sorting results. Available options: `relevanceblender` - Featured (default) `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low `review-rank` - Avg. Customer Review `date-desc-rank` - Newest…  |
| `dc` |  |  | The exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default).  |
| `rh` | string \\| number \\| boolean |  | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318031,p_n_cpf_eligible:21512497011,p_72:1248897011` to filter for products in **Coffee**…  |
| `node` | string \\| number \\| boolean |  | Specifies the category for Amazon search results. You can find the appropriate node value by browsing Amazon’s website and accessing a specific category. The node ID is typically included in the URL after the format…  |
| `page` | string \\| number \\| boolean |  | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `language` | string \\| number \\| boolean |  | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a…  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `amazon_domain` | string \\| number \\| boolean |  | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `shipping_location` | string \\| number \\| boolean |  | Shipping country. To filter the shipping products by a selected country.  |

## Details

Amazon Search returns search results from an Amazon site for a keyword. It also returns featured product groups, category links and filter options. The only required input is the search query in `k`.

### Use cases

- Monitor how much featured products for a keyword such as `wireless earbuds` cost and how far they dropped from the old amount.
- Collect ASINs from a search to feed into a product detail lookup.
- Find which products carry deal badges or the Climate Pledge Friendly flag for a keyword.
- Build filtered searches by reusing the `rh` values from the filter options, for example by age range or audio driver type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"k": "wireless earbuds"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `k` | ['string', 'number', 'boolean'] | Yes | The query you want to search. You can use anything that you would use in a regular Amazon search. This parameter can't be used with the `node` parameter. |
| `amazon_domain` | ['string', 'number', 'boolean'] | No | The Amazon domain to use. It defaults to `amazon.com`. Head to Amazon domains for a full list of supported Amazon domains. |
| `dc` | string | No | The exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `true` to exclude these results, or `false` to include them (default). |
| `delivery_zip` | ['string', 'number', 'boolean'] | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `device` | ['string', 'number', 'boolean'] | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `language` | ['string', 'number', 'boolean'] | No | The language to use for the Amazon search. It's a locale name represented as _. (e.g., on amazon.com `en_US` for English, `es_US` for Spanish, or on amazon.co.jp `ja_JP` for Japanese). Head to Amazon languages for a full |
| `node` | ['string', 'number', 'boolean'] | No | Specifies the category for Amazon search results. You can find the appropriate node value by browsing Amazon’s website and accessing a specific category. The node ID is typically included in the URL after the format `nod |
| `page` | ['string', 'number', 'boolean'] | No | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `rh` | ['string', 'number', 'boolean'] | No | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `,`. For example `n:16318031,p_n_cpf_eligible:21512497011,p_72:1248897011` to filter for products in **Coffee** departm |
| `s` | string | No | Sorting results. Available options: `relevanceblender` - Featured (default) `price-asc-rank` - Price: Low to High `price-desc-rank` - Price: High to Low `review-rank` - Avg. Customer Review `date-desc-rank` - Newest Arri |
| `shipping_location` | ['string', 'number', 'boolean'] | No | Shipping country. To filter the shipping products by a selected country. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "link": "https://www.amazon.com/pet-shops-dogs-cats-hamsters-kittens/b/?ie=UTF8&node=2619…",
      "name": "Pet Supplies",
      "node": "2619533011",
      "position": 1,
      "serpapi_link": {
        "endpoint": "/amazon/search",
        "queryParams": {
          "amazon_domain": "amazon.com",
          "device": "desktop",
          "node": "2619533011"
        }
      }
    }
  ],
  "featured_products": [
    {
      "products": [
        {
          "asin": "B0F5Q7BH7H",
          "badges": [
            "Ends in 34:26"
          ],
          "bought_last_month": "300+ bought in past month",
          "delivery": [
            "Join Prime to get FREE delivery Tomorrow, Nov 4Or Non-members get FREE delivery …"
          ],
          "extracted_old_price": 35.99,
          "extracted_price": 23.97,
          "link": "https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo2ODI1NzM3ODY0MjE4MTA5OjE3OTM2OT…",
          "link_clean": "https://www.amazon.com/dp/B0F5Q7BH7H/"
        }
      ],
      "title": "Today's deals"
    }
  ],
  "filters": {
    "age_range": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_feature_browse-bin%3A23549350…",
        "name": "Kid",
        "position": 1,
        "rh": "p_n_feature_browse-bin:23549350011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_feature_browse-bin:23549350011"
          }
        }
      }
    ],
    "audio_driver_size": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015506109111%3A122272120…",
        "name": "3 in & above",
        "position": 1,
        "rh": "p_n_g-101015506109111:122272120011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015506109111:122272120011"
          }
        }
      }
    ],
    "audio_driver_type": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015499549111%3A122268314…",
        "name": "Dynamic Driver",
        "position": 1,
        "rh": "p_n_g-101015499549111:122268314011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015499549111:122268314011"
          }
        }
      }
    ],
    "audio_latency": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015506076111%3A122272124…",
        "name": "Up to 19 ms",
        "position": 1,
        "rh": "p_n_g-101015506076111:122272124011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015506076111:122272124011"
          }
        }
      }
    ],
    "battery_charge_time": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015490467111%3A122265089…",
        "name": "Up to 1 h",
        "position": 1,
        "rh": "p_n_g-101015490467111:122265089011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015490467111:122265089011"
          }
        }
      }
    ],
    "battery_life": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015499813111%3A122268319…",
        "name": "Up to 9 h",
        "position": 1,
        "rh": "p_n_g-101015499813111:122268319011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015499813111:122268319011"
          }
        }
      }
    ],
    "brands": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_123%3A110955&dc&qid=1793690732&…",
        "name": "Apple",
        "position": 1,
        "rh": "p_123:110955",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_123:110955"
          }
        }
      }
    ],
    "cable_feature": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-1003285868111%3A23942863011…",
        "name": "Detachable",
        "position": 1,
        "rh": "p_n_g-1003285868111:23942863011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-1003285868111:23942863011"
          }
        }
      }
    ],
    "carrying_case_color": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015500219111%3A122269856…",
        "name": "Black",
        "position": 1,
        "rh": "p_n_g-101015500219111:122269856011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015500219111:122269856011"
          }
        }
      }
    ],
    "carrying_case_material": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-101015500290111%3A122269835…",
        "name": "Plastic",
        "position": 1,
        "rh": "p_n_g-101015500290111:122269835011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-101015500290111:122269835011"
          }
        }
      }
    ],
    "color": [
      {
        "image": "https://m.media-amazon.com/images/G/01/nav2/images/gui/clothingcolorsprite._CB43…",
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_feature_twenty-nine_browse-bi…",
        "name": "Black",
        "position": 1,
        "rh": "p_n_feature_twenty-nine_browse-bin:204376047011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_feature_twenty-nine_browse-bin:204376047011"
          }
        }
      }
    ],
    "compatible_devices": [
      {
        "link": "https://www.amazon.com/s?k=wireless+earbuds&rh=p_n_g-1003341941111%3A24003431011…",
        "name": "Cellphones",
        "position": 1,
        "rh": "p_n_g-1003341941111:24003431011",
        "serpapi_link": {
          "endpoint": "/amazon/search",
          "queryParams": {
            "amazon_domain": "amazon.com",
            "device": "desktop",
            "k": "wireless earbuds",
            "rh": "p_n_g-1003341941111:24003431011"
          }
        }
      }
    ]
  },
  "organic_results": [
    {
      "asin": "B0HP82ZCPC",
      "climate_pledge_friendly": true,
      "delivery": [
        "Join Prime to get FREE delivery Tomorrow, Nov 4"
      ],
      "extracted_price": 99.99,
      "link": "https://www.amazon.com/sspa/click?ie=UTF8&spc=MTozNTY4MDQxMzQ1NjA2MjI0OjE3OTM2OT…",
      "link_clean": "https://www.amazon.com/dp/B0HP82ZCPC/",
      "position": 1,
      "price": "$99.99",
      "purchase_options": [
        {
          "extracted_primary_price": 99.99,
          "primary_price": "$99.99"
        }
      ],
      "rating": 4.8,
      "reviews": 187,
      "save_with_coupon": "You pay $49.99 with coupon"
    }
  ],
  "related_searches": [
    {
      "link": "https://www.amazon.com/s?k=wireless+headphones&ref=rsl_sug_0_0&pd_rd_w=H7BDB&con…",
      "position": 1,
      "query": "wireless headphones"
    }
  ],
  "search_information": {
    "page": 1,
    "query_displayed": "wireless earbuds",
    "store": "gateway",
    "total_results": 27449
  },
  "search_metadata": {
    "amazon_url": "https://www.amazon.com/s?k=wireless+earbuds",
    "cached": true,
    "created_at": "2026-11-03 07:25:31 UTC",
    "id": "6ae98c6b21fa2ce99333cc5a",
    "processed_at": "2026-11-03 07:25:31 UTC",
    "status": "Success",
    "total_time_taken": 1.9
  },
  "search_parameters": {
    "amazon_domain": "amazon.com",
    "device": "desktop",
    "engine": "amazon",
    "k": "wireless earbuds"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/amazon/search",
      "queryParams": {
        "amazon_domain": "amazon.com",
        "device": "desktop",
        "k": "wireless earbuds",
        "page": "2"
      }
    }
  },
  "sponsored_brands": {
    "brands": [
      {
        "headline": "Listen, in every moment",
        "image": "https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/07e43f53-1c4d-4d02-bca4-…",
        "link": "https://sponsored-ads.amazon.com/clk/?_encoding=UTF8&p=eAFdUM1u00AYVFsBJSqiyqFIO…",
        "logo": "https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/fb97f2e1-e5b0-4098-8c53-…",
        "name": "TAGRY",
        "position": 1
      }
    ],
    "title": "Brands related to your search"
  },
  "video_results": [
    {
      "block_position": "top",
      "products": [
        {
          "asin": "B0CSXV3GK4",
          "bought_last_month": "10K+ bought in past month",
          "delivery": [
            "Join Prime to get FREE delivery Tomorrow, Nov 4"
          ],
          "extracted_old_price": 39.99,
          "extracted_price": 25.99,
          "link": "https://sponsored-ads.amazon.com/clk?p=eAHj8uR4M2PZdTYhXseQsAAXb0_vCAMX1yAlRkMrM…",
          "link_clean": "https://www.amazon.com/dp/B0CSXV3GK4/",
          "old_price": "$39.99"
        }
      ],
      "video_link": "https://sponsored-ads.amazon.com/clk?p=eAHj8uR4M2PZdTYhXseQsAAXb0_vCAMX1yAlRkMrM…",
      "video_src": "https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/dcefa0bd-d305-4123-9095-…",
      "video_thumbnail": "https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/dcefa0bd-d305-4123-9095-…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `featured_products[].title` | Name of a featured product group, such as `Today's deals` or `Seen on social media`. |
| `featured_products[].products[].asin` | The Amazon ASIN of the product. Use it to identify the product in other calls. |
| `featured_products[].products[].extracted_price / featured_products[].products[].extracted_old_price` | Current and previous listed amounts as numbers. Not every product has an old amount. |
| `featured_products[].products[].bought_last_month` | Text such as `10K+ bought in past month`. |
| `featured_products[].products[].badges` | Labels on the product, such as `Limited time deal`. |
| `featured_products[].products[].climate_pledge_friendly` | Set to `true` when the product has the Climate Pledge Friendly flag. |
| `featured_products[].products[].delivery` | Delivery messages for the product, including Prime and non-member delivery dates. |
| `featured_products[].products[].link_clean` | Short product page URL in the form `https://www.amazon.com/dp/<ASIN>/`. |
| `categories[].name / categories[].node` | Category name and its node ID. Pass the node ID in the `node` parameter to browse that category. |
| `filters.age_range[].name / filters.age_range[].rh` | Label of an age range filter option, such as `Kid` or `Adult`, and the `rh` value that applies it to the same search. Other filter groups, such as `filters.audio_driver_type`, use the same structure. |

### Notes

- Use either `k` or `node` in one call, not both.
- Each category and filter entry includes a `queryParams` object. It shows the parameters to send in a follow-up call to this API.
- Use `page` to get further result pages. The first page is `1`.
- To get details for one product, pass its ASIN to [Amazon Product](/apis/amazon/product) or [Amazon Product Details](/apis/amazon/product-detail).

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/search.json`](../../../catalog/models/amazon/search.json) · Store page: https://www.sandbase.ai/model/amazon/search
