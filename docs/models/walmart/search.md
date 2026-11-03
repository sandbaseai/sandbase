# Walmart Search API: pricing, parameters and code examples

`walmart/search` · data API · Walmart · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Walmart products by keyword with price, rating, reviews, seller and fulfillment badges, plus sorting, price filters and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "walmart/search", "query": "laptop"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('walmart/search', {'query': 'laptop'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("walmart/search", {
  "query": "laptop"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "walmart/search", sandbase.Params{
	"query": "laptop",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/walmart/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string \\| number \\| boolean |  | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page` value is `100`.  |
| `sort` | string \\| number \\| boolean |  | Sorting. (e.g. `price_low`, `price_high`, `best_seller`, `best_match`, `rating_high`, `new`). **Note:** `best_seller`, `rating_high`, and `new` are not supported for `walmart.com.mx`.  |
| `facet` | string \\| number \\| boolean |  | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `\|\|`. The key and value are separated by `:`  |
| `nd_en` |  |  | Show results with NextDay delivery only. Set to `true` to enable or `false` (default) to disable. **Note:** not supported for `walmart.com.mx`.  |
| `query` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular Walmart search. Either a `query` or a `cat_id` parameter is required.  |
| `cat_id` | string \\| number \\| boolean |  | Category on Walmart Search. (e.g. `0` (default) is all departments, `976759_976787` is 'Cookies', etc.). Either a `query` or a `cat_id` parameter is required. **Note:** not supported for `walmart.com.mx`.  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `spelling` |  |  | Activate spelling fix. `true` (default) includes spelling fix, `false` searches without spelling fix.  |
| `store_id` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only. Head to the Walmart Stores Locations for a full list of supported stores. It's possible for the product pricing to differ between stores.  |
| `max_price` | string \\| number \\| boolean |  | Upper bound of price range query.  |
| `min_price` | string \\| number \\| boolean |  | Lower bound of price range query.  |
| `soft_sort` | string \\| number \\| boolean |  | Enables sort by relevance. Walmart is by default showing results sorted by relevance and using the `sort` option. Set to `false` to disable sort by Relevance. **Note:** not supported for `walmart.com.mx`.  |
| `walmart_domain` | string \\| number \\| boolean |  | The Walmart domain to use. It defaults to `walmart.com`. Head to the Walmart Stores for a full list of supported stores per domain.  |
| `include_filters` |  |  | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default).  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Returns one page of Walmart search results for a keyword. Each result has the title, price, rating, review count, seller and shipping flags. The only required input is `query`, such as `laptop`.

### Use cases

- Track the price and `was_price` discount of laptops from different sellers.
- Compare ratings and review counts across products for a keyword.
- Build a list of product IDs to feed into product page or review lookups.
- Check which sellers appear for a search term and whether results are sponsored.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/walmart/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "laptop"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | ['string', 'number', 'boolean'] | Yes | The search query. You can use anything that you would use in a regular Walmart search. Either a `query` or a `cat_id` parameter is required. |
| `cat_id` | ['string', 'number', 'boolean'] | No | Category on Walmart Search. (e.g. `0` (default) is all departments, `976759_976787` is 'Cookies', etc.). Either a `query` or a `cat_id` parameter is required. **Note:** not supported for `walmart.com.mx`. |
| `device` | ['string', 'number', 'boolean'] | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `facet` | ['string', 'number', 'boolean'] | No | Items filtering based on their attributes. The structure is a list of `key:value` pairs separated by `//`. The key and value are separated by `:` |
| `include_filters` | string | No | Include `filters` to the JSON response. Set to `true` to enable or `false` to disable (default). |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `max_price` | ['string', 'number', 'boolean'] | No | Upper bound of price range query. |
| `min_price` | ['string', 'number', 'boolean'] | No | Lower bound of price range query. |
| `nd_en` | string | No | Show results with NextDay delivery only. Set to `true` to enable or `false` (default) to disable. **Note:** not supported for `walmart.com.mx`. |
| `page` | ['string', 'number', 'boolean'] | No | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Maximum `page` value is `100`. |
| `soft_sort` | ['string', 'number', 'boolean'] | No | Enables sort by relevance. Walmart is by default showing results sorted by relevance and using the `sort` option. Set to `false` to disable sort by Relevance. **Note:** not supported for `walmart.com.mx`. |
| `sort` | ['string', 'number', 'boolean'] | No | Sorting. (e.g. `price_low`, `price_high`, `best_seller`, `best_match`, `rating_high`, `new`). **Note:** `best_seller`, `rating_high`, and `new` are not supported for `walmart.com.mx`. |
| `spelling` | string | No | Activate spelling fix. `true` (default) includes spelling fix, `false` searches without spelling fix. |
| `store_id` | ['string', 'number', 'boolean'] | No | Store ID to filter the products by the specific store only. Head to the Walmart Stores Locations for a full list of supported stores. It's possible for the product pricing to differ between stores. |
| `walmart_domain` | ['string', 'number', 'boolean'] | No | The Walmart domain to use. It defaults to `walmart.com`. Head to the Walmart Stores for a full list of supported stores per domain. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "free_shipping": false,
      "free_shipping_with_walmart_plus": false,
      "muliple_options_available": false,
      "multiple_options_available": false,
      "out_of_stock": false,
      "price_per_unit": {
        "currency": "USD",
        "unit": "each"
      },
      "primary_offer": {
        "currency": "USD",
        "offer_id": "44B94199498A3672AA257F39DA66AA0F",
        "offer_price": 197,
        "was_price": 219
      },
      "product_id": "1V55QUSDTIGB",
      "product_page_url": "https://www.walmart.com/ip/ASUS-Chromebook-CX15-Laptop-15-6-FHD-NanoEdge-Display…",
      "product_type": "Laptop Computers",
      "rating": 4.3,
      "reviews": 1941
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
    "other_pages": {
      "10": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "11": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "12": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "13": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "2": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "3": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "4": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "5": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "6": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "7": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "8": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…",
      "9": "https://www.walmart.com/search?adSlot=WSpread&affinityOverride=default&cat_id=0&…"
    }
  },
  "search_information": {
    "location": {
      "city": "Orlando",
      "postal_code": "32837",
      "province_code": "FL",
      "store_id": "2881"
    },
    "organic_results_state": "Results for exact spelling",
    "query_displayed": "laptop",
    "time_taken": 0.995,
    "total_results": 25259
  },
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:45:08 UTC",
    "id": "6ae99104951d73c01c846a84",
    "processed_at": "2026-11-03 07:45:08 UTC",
    "status": "Success",
    "total_time_taken": 4.24,
    "walmart_url": "https://www.walmart.com/search?query=laptop"
  },
  "search_parameters": {
    "device": "desktop",
    "engine": "walmart",
    "query": "laptop",
    "walmart_domain": "walmart.com"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/walmart/search",
      "queryParams": {
        "cat_id": "0",
        "device": "desktop",
        "page": "2",
        "query": "laptop",
        "sort": "best_match",
        "spelling": "true",
        "walmart_domain": "walmart.com"
      }
    },
    "next_link": {
      "endpoint": "/walmart/search",
      "queryParams": {
        "cat_id": "0",
        "device": "desktop",
        "page": "2",
        "query": "laptop",
        "sort": "best_match",
        "spelling": "true",
        "walmart_domain": "walmart.com"
      }
    },
    "other_pages": {
      "10": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "10",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "11": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "11",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "12": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "12",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "13": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "13",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "2": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "2",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "3": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "3",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "4": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "4",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "5": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "5",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "6": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "6",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "7": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "7",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "8": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "8",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      },
      "9": {
        "endpoint": "/walmart/search",
        "queryParams": {
          "cat_id": "0",
          "device": "desktop",
          "page": "9",
          "query": "laptop",
          "sort": "best_match",
          "spelling": "true",
          "walmart_domain": "walmart.com"
        }
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].title` | Product title as shown in the search result. |
| `organic_results[].primary_offer.offer_price / organic_results[].primary_offer.was_price` | Current price and previous price of the main offer. `was_price` only appears when the item is discounted. |
| `organic_results[].primary_offer.currency` | Currency code of the offer, such as `USD`. |
| `organic_results[].rating / organic_results[].reviews` | Average rating and number of reviews for the product. |
| `organic_results[].seller_name / organic_results[].seller_id` | Name and ID of the seller that holds the main offer. |
| `organic_results[].us_item_id` | Walmart item ID. It matches the `product_id` value in `serpapi_product_page_url.queryParams`. |
| `organic_results[].sponsored` | `true` when the result is a paid placement. |
| `organic_results[].free_shipping / organic_results[].two_day_shipping / organic_results[].out_of_stock` | Flags for free shipping, two-day shipping and stock status. |
| `search_information.total_results` | Number of results Walmart reports for the query. |
| `serpapi_pagination.next` | Endpoint and query parameters for the next page of results. |

### Notes

- Set `page` to move through results. The response lists page links such as `2` and `3` under `serpapi_pagination.other_pages`. The maximum `page` value is `100`.
- Use `organic_results[].serpapi_product_page_url.queryParams.product_id` (the same value as `us_item_id`) to look up one product with [Walmart Product Page](/apis/walmart/scrape/product).
- Use the same item ID with [Walmart Product Reviews](/apis/walmart/product-reviews) to read reviews.
- The `product_id` field at the top of each result is a different value from `us_item_id`. Use `us_item_id` for follow-up calls.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/walmart/search.json`](../../../catalog/models/walmart/search.json) · Store page: https://www.sandbase.ai/model/walmart/search
