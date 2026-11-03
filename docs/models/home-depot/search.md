# Home Depot Search API: pricing, parameters and code examples

`home-depot/search` · data API · Home Depot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Home Depot products by keyword with price, brand, model number, rating, delivery and pickup availability, filters and pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "home-depot/search", "q": "cordless drill"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('home-depot/search', {'q': 'cordless drill'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("home-depot/search", {
  "q": "cordless drill"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "home-depot/search", sandbase.Params{
	"q": "cordless drill",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/home-depot/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular The Home Depot search.  |
| `ps` | string \\| number \\| boolean |  | Determines the number of items per page. There are scenarios where The Home Depot overrides the `ps` value. By default, The Home Depot returns `24` (maximum allowed value) results.  |
| `nao` | string \\| number \\| boolean |  | Defines offset for products result. A single page contains 24 products. First page offset is 0, second -> 24, third -> 48 and so on.  |
| `page` | string \\| number \\| boolean |  | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). This parameter is common for both US and CA…  |
| `sort` |  |  | Results sorted by different options in Home Depot Canada. It can be set to: `price-asc`: Price Low to High, `price-desc`: Price High to Low, `reviewAvgRating`: Top Rated, `relevance`: Recommended (Default)  |
| `store` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only in Home Depot Canada. The default store is Gatineau (`7140`). See all Home Depot Canada stores  |
| `filter` | string \\| number \\| boolean |  | Used to pass filter tokens divided by dash (-) in Home Depot Canada. Filter tokens can be obtained from API response  |
| `minmax` | string \\| number \\| boolean |  | Defines lower and upper bound for price in CAD. Parameter is only used in the Home Depot Canada. Example: `price:[100 TO 500]`(Between $100 to $500) Example: `price:[100 TO *]`(Minimum $100) Example: `price:[0 TO…  |
| `country` | string \\| number \\| boolean |  | The country to use for the Home Depot search. Only United States(`us`), and Canada(`ca`) are supported.  |
| `hd_sort` |  |  | Results sorted by different options in Home Depot US. It can be set to: `top_sellers`: Top Sellers, `price_low_to_high`: Price Low to High, `price_high_to_low`: Price High to Low, `top_rated`: Top Rated, `best_match`:…  |
| `pagesize` | string \\| number \\| boolean |  | Determines the number of items per page in the Home Depot Canada. By default, the Home Depot Canada returns `40` (maximum allowed value) results.  |
| `store_id` | string \\| number \\| boolean |  | Store ID to filter the products by the specific store only. See all Home Depot stores  |
| `lowerbound` | string \\| number \\| boolean |  | Defines lower bound for price in USD.  |
| `upperbound` | string \\| number \\| boolean |  | Defines upper bound for price in USD.  |
| `delivery_zip` | string \\| number \\| boolean |  | ZIP Postal code. To filter the shipping products by a selected area.  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `hd_filter_tokens` | string \\| number \\| boolean |  | Used to pass filter tokens divided by comma. Filter tokens can be obtained from API response  |

## Details

Returns a page of Home Depot products that match a keyword, with price, brand, model number, rating, review count, and delivery and pickup details for each item. It also returns filter options, category breadcrumbs, and pagination links. The only required input is the search query `q`.

### Use cases

- Compare prices and discounts for one tool category across brands, using `price`, `price_was` and `percentage_off`.
- Check which products a nearby store has in stock for pickup by passing `store_id` and reading `pickup.quantity`.
- Collect model numbers and product IDs for a keyword, then pull full details or reviews for each item.
- Build a category or brand breakdown of a search using the facet counts in `filters`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/home-depot/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "cordless drill"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | ['string', 'number', 'boolean'] | Yes | The search query. You can use anything that you would use in a regular The Home Depot search. |
| `country` | ['string', 'number', 'boolean'] | No | The country to use for the Home Depot search. Only United States(`us`), and Canada(`ca`) are supported. |
| `delivery_zip` | ['string', 'number', 'boolean'] | No | ZIP Postal code. To filter the shipping products by a selected area. |
| `filter` | ['string', 'number', 'boolean'] | No | Used to pass filter tokens divided by dash (-) in Home Depot Canada. Filter tokens can be obtained from API response |
| `hd_filter_tokens` | ['string', 'number', 'boolean'] | No | Used to pass filter tokens divided by comma. Filter tokens can be obtained from API response |
| `hd_sort` | string | No | Results sorted by different options in Home Depot US. It can be set to: `top_sellers`: Top Sellers, `price_low_to_high`: Price Low to High, `price_high_to_low`: Price High to Low, `top_rated`: Top Rated, `best_match`: Be |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `lowerbound` | ['string', 'number', 'boolean'] | No | Defines lower bound for price in USD. |
| `minmax` | ['string', 'number', 'boolean'] | No | Defines lower and upper bound for price in CAD. Parameter is only used in the Home Depot Canada. Example: `price:[100 TO 500]`(Between $100 to $500) Example: `price:[100 TO *]`(Minimum $100) Example: `price:[0 TO 500]`(M |
| `nao` | ['string', 'number', 'boolean'] | No | Defines offset for products result. A single page contains 24 products. First page offset is 0, second -> 24, third -> 48 and so on. |
| `page` | ['string', 'number', 'boolean'] | No | Value is used to get the items on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). This parameter is common for both US and CA sea |
| `pagesize` | ['string', 'number', 'boolean'] | No | Determines the number of items per page in the Home Depot Canada. By default, the Home Depot Canada returns `40` (maximum allowed value) results. |
| `ps` | ['string', 'number', 'boolean'] | No | Determines the number of items per page. There are scenarios where The Home Depot overrides the `ps` value. By default, The Home Depot returns `24` (maximum allowed value) results. |
| `sort` | string | No | Results sorted by different options in Home Depot Canada. It can be set to: `price-asc`: Price Low to High, `price-desc`: Price High to Low, `reviewAvgRating`: Top Rated, `relevance`: Recommended (Default) |
| `store` | ['string', 'number', 'boolean'] | No | Store ID to filter the products by the specific store only in Home Depot Canada. The default store is Gatineau (`7140`). See all Home Depot Canada stores |
| `store_id` | ['string', 'number', 'boolean'] | No | Store ID to filter the products by the specific store only. See all Home Depot stores |
| `upperbound` | ['string', 'number', 'boolean'] | No | Defines upper bound for price in USD. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "filters": [
    {
      "key": "Get It Fast",
      "value": [
        {
          "count": "94",
          "link": "https://www.homedepot.com/b/Tools-Power-Tools-Drills/Cordless/Pick-Up-Today/N-5y…",
          "name": "Pick Up Today",
          "value": "1z175a5"
        }
      ]
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=24",
    "other_pages": {
      "2": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=24",
      "3": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=48",
      "4": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=72",
      "5": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=96"
    }
  },
  "products": [
    {
      "badges": [
        "bestseller"
      ],
      "brand": "DEWALT",
      "collection": "https://www.homedepot.com/collection/Tools/DEWALT-ATOMIC-Compact-20-Volt-Collect…",
      "delivery": {
        "free": true,
        "free_delivery_threshold": false
      },
      "link": "https://www.homedepot.com/p/DEWALT-Atomic-20V-Max-Lithium-Ion-Brushless-Cordless…",
      "model_number": "DCF809D1",
      "percentage_off": 45,
      "pickup": {
        "distance": 0,
        "quantity": 23,
        "store_name": "Bangor"
      },
      "position": 1,
      "price": 99,
      "price_badge": "New-Lower-Price",
      "price_saving": 80
    }
  ],
  "search_information": {
    "results_state": "Results for exact spelling",
    "store_id": "2414",
    "store_name": "Bangor",
    "total_results": 931
  },
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:34:42 UTC",
    "home_depot_url": "https://www.homedepot.com/b/N-5yc1v/Ntt-cordless+drill?Nao=0",
    "id": "6ae98e9213181178a6dd9cb0",
    "processed_at": "2026-11-03 07:34:42 UTC",
    "status": "Success",
    "total_time_taken": 1.28
  },
  "search_parameters": {
    "country": "us",
    "delivery_zip": "04401",
    "engine": "home_depot",
    "nao": "0",
    "ps": 24,
    "q": "cordless drill",
    "store_id": "2414"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/home-depot/search",
      "queryParams": {
        "country": "us",
        "delivery_zip": "04401",
        "nao": "24",
        "ps": "24",
        "q": "cordless drill",
        "store_id": "2414"
      }
    },
    "next_link": {
      "endpoint": "/home-depot/search",
      "queryParams": {
        "country": "us",
        "delivery_zip": "04401",
        "nao": "24",
        "ps": "24",
        "q": "cordless drill",
        "store_id": "2414"
      }
    },
    "other_pages": {
      "2": {
        "endpoint": "/home-depot/search",
        "queryParams": {
          "country": "us",
          "delivery_zip": "04401",
          "nao": "24",
          "ps": "24",
          "q": "cordless drill",
          "store_id": "2414"
        }
      },
      "3": {
        "endpoint": "/home-depot/search",
        "queryParams": {
          "country": "us",
          "delivery_zip": "04401",
          "nao": "48",
          "ps": "24",
          "q": "cordless drill",
          "store_id": "2414"
        }
      },
      "4": {
        "endpoint": "/home-depot/search",
        "queryParams": {
          "country": "us",
          "delivery_zip": "04401",
          "nao": "72",
          "ps": "24",
          "q": "cordless drill",
          "store_id": "2414"
        }
      },
      "5": {
        "endpoint": "/home-depot/search",
        "queryParams": {
          "country": "us",
          "delivery_zip": "04401",
          "nao": "96",
          "ps": "24",
          "q": "cordless drill",
          "store_id": "2414"
        }
      }
    }
  },
  "taxonomy": [
    {
      "link": "https://www.homedepot.com/b/Tools/N-5yc1vZc1xy",
      "title": "Tools"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `products[].title / products[].brand` | Product name and brand as shown in the listing. |
| `products[].model_number / products[].product_id` | The manufacturer model number and the Home Depot product ID. Use `product_id` to look up the item in other calls. |
| `products[].price / products[].price_was / products[].price_saving / products[].percentage_off` | Current price, previous price, the amount saved, and the discount percent. The last three appear only on discounted items. |
| `products[].rating / products[].reviews` | Average review rating and the number of reviews. |
| `products[].pickup.store_name / products[].pickup.quantity / products[].pickup.distance` | The store used for pickup, the quantity it lists, and its distance value. |
| `products[].delivery.free / products[].delivery.schedule_delivery` | Delivery flags for the item. Which flags appear varies by product. |
| `products[].badges / products[].price_badge` | Labels such as `bestseller` and `exclusive`, and a price label such as `New-Lower-Price`. |
| `filters[].key / filters[].value[].name / filters[].value[].count / filters[].value[].value` | Filter groups, such as Category, with each option's name, result count, and filter token. |
| `search_information.total_results / search_information.store_name` | Total number of matching products and the store the search ran against. |
| `pagination.next / serpapi_pagination.next.queryParams.nao` | Link to the next page and the offset value for the next request. |

### Notes

- Page through results with `nao` (offset). A page holds 24 products, so use `0`, `24`, `48` and so on. The `serpapi_pagination.other_pages` object lists the parameters for each page.
- Pass values from `filters[].value[].value` as `hd_filter_tokens` to narrow a US search. Use `hd_sort` to change the order.
- Use `products[].product_id` with [Home Depot Product](/apis/home-depot/product) for full product details, or [Home Depot Product Reviews](/apis/home-depot/product-reviews) for customer reviews.
- The response echoes the `store_id` and `delivery_zip` used. Set both to get pickup and delivery data for a specific area.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/home-depot/search.json`](../../../catalog/models/home-depot/search.json) · Store page: https://www.sandbase.ai/model/home-depot/search
