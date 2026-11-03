# Target Search API: pricing, parameters and code examples

`target/search` · data API · Target · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Target products by keyword with TCIN, brand, price, sale price, rating, reviews and pickup, delivery and shipping availability.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "target/search", "q": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('target/search', {'q': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("target/search", {
  "q": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "target/search", sandbase.Params{
	"q": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/target/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The query you want to search. You can use anything that you would use in a regular Target search (e.g., `coffee`, `65 inch tv`, or `lego star wars`).  |
| `page` | string \\| number \\| boolean |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Target returns up to 24 results per page, plus…  |
| `sort` |  |  | The sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `featured` - Featured `price_low` - Price: low to high `price_high` - Price: high to low `rating_high` - Guest rating…  |
| `facet` | string \\| number \\| boolean |  | The filters to apply, like Target's filters (e.g., deals, brands, sizes, colors, or guest ratings). It's a comma-separated list of filter IDs (e.g., `5tdv0,4yagy` for Sale and Dark Roast). Filter IDs are available in…  |
| `spelling` |  |  | Whether to fix the spelling of misspelled queries, like Target. It can be set to `true` (default) to search for the spelling fix (e.g., `coffee` for `cofee`), as shown in `search_information.spelling_fix`, or `false`…  |
| `store_id` | string \\| number \\| boolean |  | The Target store to get prices and availability for, like the store selected on Target (e.g., `1375` for Mpls Nicollet Mall, MN). The store ID is the number at the end of the store's page URL on Target (e.g.,…  |
| `max_price` | string \\| number \\| boolean |  | The maximum price of the products, in US dollars (e.g., `50`).  |
| `min_price` | string \\| number \\| boolean |  | The minimum price of the products, in US dollars (e.g., `10`).  |
| `category_id` | string \\| number \\| boolean |  | The category to search in (e.g., `hz89j` for Kitchen & Dining). Category IDs are available in the `Category` filter of the results when `include_filters` is set to `true`.  |
| `delivery_zip` | string \\| number \\| boolean |  | The US ZIP code to deliver to (e.g., `10001`). It's used for the shipping dates and the same day delivery availability. It defaults to the location of the store.  |
| `include_filters` |  |  | Whether to include the `filters` of the search in the JSON response, with the IDs to use in `facet` and `category_id`. It can be set to `true` or `false` (default).  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Target Search returns Target product listings for a keyword query. Each result includes the TCIN, brand, price, rating, review count and fulfillment status for the selected store. The only required input is `q`.

### Use cases

- Track prices and sale prices for a product type such as wireless earbuds across result pages.
- Compare brands by rating and review count for a keyword.
- Check whether products are available for store pickup, same day delivery or shipping at a given store.
- Build a list of TCINs to look up product details or monitor changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/target/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "wireless earbuds"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | ['string', 'number', 'boolean'] | Yes | The query you want to search. You can use anything that you would use in a regular Target search (e.g., `coffee`, `65 inch tv`, or `lego star wars`). |
| `category_id` | ['string', 'number', 'boolean'] | No | The category to search in (e.g., `hz89j` for Kitchen & Dining). Category IDs are available in the `Category` filter of the results when `include_filters` is set to `true`. |
| `delivery_zip` | ['string', 'number', 'boolean'] | No | The US ZIP code to deliver to (e.g., `10001`). It's used for the shipping dates and the same day delivery availability. It defaults to the location of the store. |
| `facet` | ['string', 'number', 'boolean'] | No | The filters to apply, like Target's filters (e.g., deals, brands, sizes, colors, or guest ratings). It's a comma-separated list of filter IDs (e.g., `5tdv0,4yagy` for Sale and Dark Roast). Filter IDs are available in `fi |
| `include_filters` | string | No | Whether to include the `filters` of the search in the JSON response, with the IDs to use in `facet` and `category_id`. It can be set to `true` or `false` (default). |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `max_price` | ['string', 'number', 'boolean'] | No | The maximum price of the products, in US dollars (e.g., `50`). |
| `min_price` | ['string', 'number', 'boolean'] | No | The minimum price of the products, in US dollars (e.g., `10`). |
| `page` | ['string', 'number', 'boolean'] | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Target returns up to 24 results per page, plus sp |
| `sort` | string | No | The sorting of the results. It defaults to `relevance`. Available options: `relevance` - Relevance `featured` - Featured `price_low` - Price: low to high `price_high` - Price: high to low `rating_high` - Guest rating `be |
| `spelling` | string | No | Whether to fix the spelling of misspelled queries, like Target. It can be set to `true` (default) to search for the spelling fix (e.g., `coffee` for `cofee`), as shown in `search_information.spelling_fix`, or `false` to  |
| `store_id` | ['string', 'number', 'boolean'] | No | The Target store to get prices and availability for, like the store selected on Target (e.g., `1375` for Mpls Nicollet Mall, MN). The store ID is the number at the end of the store's page URL on Target (e.g., `https://ww |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "badges": [
        "Highly rated"
      ],
      "brand": "JLab",
      "extracted_price": 14.99,
      "fulfillment": {
        "in_store": "IN_STOCK",
        "pickup": "IN_STOCK",
        "pickup_date": "2026-11-03",
        "same_day_delivery": "IN_STOCK",
        "shipping": "IN_STOCK",
        "shipping_date": "2026-11-10"
      },
      "link": "https://www.target.com/p/jlab-go-air-pop-true-wireless-bluetooth-earbuds/-/A-848…",
      "parent_tcin": "84826951",
      "position": 1,
      "price": "$14.99",
      "price_note": "When purchased online",
      "rating": 4.3,
      "reviews": 8006,
      "sponsored": true
    }
  ],
  "popular_filters": [
    {
      "facet": "m2tvk",
      "id": "m2tvk",
      "name": "Heyday",
      "serpapi_link": {
        "endpoint": "/target/search",
        "queryParams": {
          "facet": "m2tvk",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "thumbnail": "https://target.scene7.com/is/image/Target/328x328heyday141445-180822_15349758438…"
    }
  ],
  "search_information": {
    "query_displayed": "wireless earbuds",
    "store_id": "1771",
    "store_name": "Cedar Rapids South",
    "total_results": 351
  },
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:43:31 UTC",
    "id": "6ae990a3ff782343f03cff0b",
    "processed_at": "2026-11-03 07:43:31 UTC",
    "status": "Success",
    "target_url": "https://www.target.com/s?searchTerm=wireless+earbuds",
    "total_time_taken": 2
  },
  "search_parameters": {
    "engine": "target",
    "q": "wireless earbuds",
    "store_id": "1771"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/target/search",
      "queryParams": {
        "page": "2",
        "q": "wireless earbuds",
        "store_id": "1771"
      }
    },
    "other_pages": {
      "10": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "10",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "11": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "11",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "2": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "2",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "3": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "3",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "4": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "4",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "5": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "5",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "6": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "6",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "7": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "7",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "8": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "8",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      },
      "9": {
        "endpoint": "/target/search",
        "queryParams": {
          "page": "9",
          "q": "wireless earbuds",
          "store_id": "1771"
        }
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].tcin / organic_results[].parent_tcin` | The TCIN of the listed item. `parent_tcin` appears on items with color or style variants and identifies the parent product. |
| `organic_results[].title / organic_results[].brand` | The product name and its brand. |
| `organic_results[].price / organic_results[].extracted_price` | The current price as display text (such as `$14.99`) and as a number. |
| `organic_results[].old_price / organic_results[].extracted_old_price` | The price before the discount, as text and as a number. These appear only on sale items, which also carry a `tag` such as `Sale`. |
| `organic_results[].rating / organic_results[].reviews` | The average guest rating and the number of reviews. |
| `organic_results[].fulfillment` | Availability by method: `in_store`, `pickup`, `same_day_delivery` and `shipping`, with values like `IN_STOCK`. It also holds `pickup_date`, `shipping_date` and `free_shipping` when present. |
| `organic_results[].sponsored` | Whether the result is a sponsored placement. |
| `organic_results[].swatches[]` | Variants of the product, each with a `name`, `tcin` and `thumbnail`. |
| `search_information.total_results` | The number of products that match the search. |
| `popular_filters[].facet` | A filter ID that you can pass in the `facet` parameter, with its `name` such as a brand or price range. |

### Notes

- Use `page` to move through results. The `serpapi_pagination.next` object holds the query parameters for the next page.
- Set `include_filters` to `true` to get the filter and category IDs that you can pass in `facet` and `category_id`.
- Results use the store in `search_information.store_id`. Pass `store_id` to get prices and availability for another store.
- Dates such as `pickup_date` and `shipping_date` use the `YYYY-MM-DD` format.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/target/search.json`](../../../catalog/models/target/search.json) · Store page: https://www.sandbase.ai/model/target/search
