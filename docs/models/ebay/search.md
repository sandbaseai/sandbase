# eBay Search API: pricing, parameters and code examples

`ebay/search` · data API · eBay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search eBay listings by keyword with price, condition, shipping, bids, time left and seller, plus condition, format, price and location filters.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ebay/search", "_nkw": "iphone 15"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ebay/search', {'_nkw': 'iphone 15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ebay/search", {
  "_nkw": "iphone 15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ebay/search", sandbase.Params{
	"_nkw": "iphone 15",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ebay/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `_dmd` | string \\| number \\| boolean |  | The visual layout for displaying results. The available options are 'Grid' and 'List'.  |
| `_ipg` | string \\| number \\| boolean |  | The maximum number of results to return. There are three options: `60` (default), `120` and `240` results.  |
| `_nkw` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular eBay search. `_nkw` parameter is optional when `category_id` parameter is specified.  |
| `_pgn` | string \\| number \\| boolean |  | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.).  |
| `_sop` | string \\| number \\| boolean |  | Results sorted by different options in the eBay. The default option is 'Best Match'. Head to the eBay sort options for a full list of supported sort options.  |
| `_blrs` | string \\| number \\| boolean |  | The exclusion of results from an auto-corrected query when the original query is spelled wrong. The recommended value for this parameter is `spell_auto_correct`. Omit `_blrs` if you want the search to include results…  |
| `_sasl` | string \\| number \\| boolean |  | The seller username(s) to filter results by. You can specify multiple sellers separated by commas (e.g. `iRobot,samsung`). Use with `_saslop` to control whether to include or exclude items from the specified seller(s).  |
| `_udhi` | string \\| number \\| boolean |  | The highest price of items that should be included in the results (e.g. `20` will only return items that have lower price than `20`).  |
| `_udlo` | string \\| number \\| boolean |  | The lowest price of items that should be included in the results (e.g. `10` will only return items that have higher price than `10`).  |
| `_salic` | string \\| number \\| boolean |  | The location based on country. Head to the eBay location options for a full list of supported countries.  |
| `_stpos` | string \\| number \\| boolean |  | The ZIP or Postal code. You can use it to filter the shipping products by a selected area.  |
| `_saslop` |  |  | Whether to include or exclude items from the seller(s) specified in `_sasl`. Available options: `1` - Only show items from sellers (default) `2` - Don't show items from sellers  |
| `show_only` | string |  | The list of filters you can apply to the results. Available options **(case-sensitive)**: `FR` - Free returns `RPA` - Returns accepted `AS` - Authorized seller `Savings` - Deals and savings `SaleItems` - Sale items…  |
| `LH_PrefLoc` | string \\| number \\| boolean |  | The preferred location. The available options are 'Domestic', 'Regional', and 'Worldwide'.  |
| `category_id` | string \\| number \\| boolean |  | The ID of a category where you want your search to be concentrated. ID values are accessible inside `categories` array, located in our JSON output (e.g. `categories[1].id`). You can search using `category_id` parameter…  |
| `ebay_domain` | string \\| number \\| boolean |  | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported eBay domains.  |
| `buying_format` |  |  | The buying format you can apply to the results. Available options **(case-sensitive)**: `Auction` - Auction `BIN` - Buy It Now `BO` - Accepts Offers  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `popular_filters` | string \\| number \\| boolean |  | Allows filtering items based on their attributes. The structure is a list of `key=value` pairs separated by `&` (e.g. `Brand=Nespresso&Size=L`). To pass multiple values for the same filter, join them with `\|` (e.g.…  |
| `LH_ItemCondition` | string \\| number \\| boolean |  | One or multiple product conditions to limit the search to. Condition is represented via numeric ID, e.g. `1000` for `New`. Multiple IDs should be joined with `\|` delimiter, e.g. `1000\|3000`. List of supported IDs can…  |

## Details

Returns eBay search results for a keyword: listings with price, condition, shipping, seller, and buying format, plus category, filter, and pagination data. The only required input is the search query in `_nkw`, or a `category_id`.

### Use cases

- Track asking prices for a product such as the iPhone 15 across new, used, and refurbished listings.
- Compare sellers by feedback percentage and review count before choosing where to buy.
- Find discounted listings by comparing `price` with `old_price`.
- Build a catalog of listing IDs, then fetch full item details for each one.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ebay/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"_nkw": "iphone 15"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `_nkw` | ['string', 'number', 'boolean'] | Yes | The search query. You can use anything that you would use in a regular eBay search. `_nkw` parameter is optional when `category_id` parameter is specified. |
| `LH_ItemCondition` | ['string', 'number', 'boolean'] | No | One or multiple product conditions to limit the search to. Condition is represented via numeric ID, e.g. `1000` for `New`. Multiple IDs should be joined with `/` delimiter, e.g. `1000/3000`. List of supported IDs can be  |
| `LH_PrefLoc` | ['string', 'number', 'boolean'] | No | The preferred location. The available options are 'Domestic', 'Regional', and 'Worldwide'. |
| `_blrs` | ['string', 'number', 'boolean'] | No | The exclusion of results from an auto-corrected query when the original query is spelled wrong. The recommended value for this parameter is `spell_auto_correct`. Omit `_blrs` if you want the search to include results for |
| `_dmd` | ['string', 'number', 'boolean'] | No | The visual layout for displaying results. The available options are 'Grid' and 'List'. |
| `_ipg` | ['string', 'number', 'boolean'] | No | The maximum number of results to return. There are three options: `60` (default), `120` and `240` results. |
| `_pgn` | ['string', 'number', 'boolean'] | No | The page number. It's used for pagination. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). |
| `_salic` | ['string', 'number', 'boolean'] | No | The location based on country. Head to the eBay location options for a full list of supported countries. |
| `_sasl` | ['string', 'number', 'boolean'] | No | The seller username(s) to filter results by. You can specify multiple sellers separated by commas (e.g. `iRobot,samsung`). Use with `_saslop` to control whether to include or exclude items from the specified seller(s). |
| `_saslop` | string | No | Whether to include or exclude items from the seller(s) specified in `_sasl`. Available options: `1` - Only show items from sellers (default) `2` - Don't show items from sellers |
| `_sop` | ['string', 'number', 'boolean'] | No | Results sorted by different options in the eBay. The default option is 'Best Match'. Head to the eBay sort options for a full list of supported sort options. |
| `_stpos` | ['string', 'number', 'boolean'] | No | The ZIP or Postal code. You can use it to filter the shipping products by a selected area. |
| `_udhi` | ['string', 'number', 'boolean'] | No | The highest price of items that should be included in the results (e.g. `20` will only return items that have lower price than `20`). |
| `_udlo` | ['string', 'number', 'boolean'] | No | The lowest price of items that should be included in the results (e.g. `10` will only return items that have higher price than `10`). |
| `buying_format` | string | No | The buying format you can apply to the results. Available options **(case-sensitive)**: `Auction` - Auction `BIN` - Buy It Now `BO` - Accepts Offers |
| `category_id` | ['string', 'number', 'boolean'] | No | The ID of a category where you want your search to be concentrated. ID values are accessible inside `categories` array, located in our JSON output (e.g. `categories[1].id`). You can search using `category_id` parameter w |
| `ebay_domain` | ['string', 'number', 'boolean'] | No | The eBay domain to use. It defaults to `ebay.com`. Head to the eBay domains for a full list of supported eBay domains. |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `popular_filters` | ['string', 'number', 'boolean'] | No | Allows filtering items based on their attributes. The structure is a list of `key=value` pairs separated by `&` (e.g. `Brand=Nespresso&Size=L`). To pass multiple values for the same filter, join them with `/` (e.g. `Bran |
| `show_only` | string | No | The list of filters you can apply to the results. Available options **(case-sensitive)**: `FR` - Free returns `RPA` - Returns accepted `AS` - Authorized seller `Savings` - Deals and savings `SaleItems` - Sale items `Lots |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "categories": [
    {
      "link": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_oac=1",
      "name": "All"
    }
  ],
  "inline_results": [
    {
      "items": [
        {
          "link": "https://www.ebay.com/sch/i.html?_nkw=Apple+iPhone+13&_sacat=9355&_productid=1004…",
          "thumbnail": "https://i.ebayimg.com/images/g/Mr0AAOSwCmBn4A4q/s-l500.jpg",
          "title": "Apple iPhone 13"
        }
      ],
      "title": "Best selling products"
    }
  ],
  "organic_results": [
    {
      "buying_format": "buy_it_now",
      "buying_format_text": "Buy It Now",
      "condition": "Apple iPhone 15",
      "epid": "8062766781",
      "extensions": [
        "eBay Refurbished"
      ],
      "extracted_quantity_sold": 817,
      "link": "https://www.ebay.com/itm/257285303938?_skw=iphone+15&epid=8062766781&itmmeta=01M…",
      "location": "Located in United States",
      "old_price": {
        "discount": "$371.99",
        "extracted": 799,
        "raw": "$799.00"
      },
      "price": {
        "extracted": 371.99,
        "raw": "$371.99"
      },
      "product_id": "257285303938",
      "quantity_sold": "817+ sold"
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=2",
    "other_pages": {
      "1": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=1",
      "10": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=10&rt=nc",
      "2": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=2",
      "3": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=3",
      "4": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=4",
      "5": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=5&rt=nc",
      "6": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=6&rt=nc",
      "7": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=7&rt=nc",
      "8": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=8&rt=nc",
      "9": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&_pgn=9&rt=nc"
    }
  },
  "popular_filters": [
    {
      "link": "https://www.ebay.com/sch/i.html?_nkw=iphone+15&Network=Unlocked",
      "name": "Unlocked",
      "parameter": "Network=Unlocked",
      "serpapi_link": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "popular_filters": "Network=Unlocked"
        }
      }
    }
  ],
  "related_searches": [
    {
      "link": "https://www.ebay.com/sch/i.html?_nkw=iphone+16&_sop=12",
      "query": "iphone 16"
    }
  ],
  "search_information": {
    "organic_results_state": "Results for exact spelling",
    "query_displayed": "iphone 15",
    "total_results": 41000
  },
  "search_metadata": {
    "cached": false,
    "created_at": "2026-11-03 07:33:08 UTC",
    "ebay_url": "https://www.ebay.com/sch/i.html?_nkw=iphone+15",
    "id": "6ae98e34c8ef264ace9bcb6a",
    "processed_at": "2026-11-03 07:33:08 UTC",
    "status": "Success",
    "total_time_taken": 1.69
  },
  "search_parameters": {
    "_nkw": "iphone 15",
    "engine": "ebay"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/ebay/search",
      "queryParams": {
        "_nkw": "iphone 15",
        "_pgn": "2"
      }
    },
    "next_link": {
      "endpoint": "/ebay/search",
      "queryParams": {
        "_nkw": "iphone 15",
        "_pgn": "2"
      }
    },
    "other_pages": {
      "1": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "1"
        }
      },
      "10": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "10"
        }
      },
      "2": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "2"
        }
      },
      "3": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "3"
        }
      },
      "4": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "4"
        }
      },
      "5": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "5"
        }
      },
      "6": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "6"
        }
      },
      "7": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "7"
        }
      },
      "8": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "8"
        }
      },
      "9": {
        "endpoint": "/ebay/search",
        "queryParams": {
          "_nkw": "iphone 15",
          "_pgn": "9"
        }
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].title` | Listing title as shown on eBay. |
| `organic_results[].price.extracted / organic_results[].price.raw` | Current listing price as a number and as the displayed text, for example `$371.99`. |
| `organic_results[].old_price.extracted` | Earlier price shown as crossed out, when the listing has one. Compare it with `price` to find discounts. |
| `organic_results[].condition` | Condition label of the listing, such as `Pre-Owned`. Some listings show a product name here instead. |
| `organic_results[].buying_format / organic_results[].buying_format_text` | Buying format of the listing, for example `buy_it_now` and `Buy It Now`. |
| `organic_results[].shipping` | Shipping text, such as `Free delivery in 1-2 days`. It can also be an object with `extracted` and `raw` when a delivery cost applies. |
| `organic_results[].seller.username / organic_results[].seller.positive_feedback_in_percentage / organic_results[].seller.reviews` | Seller name, positive feedback percentage, and number of seller reviews. |
| `organic_results[].product_id` | eBay item ID of the listing. Pass it to the product API. |
| `categories[].id` | Category ID that you can pass as `category_id` to narrow the search. |
| `popular_filters[].parameter` | Filter value that you can pass in the `popular_filters` request parameter, such as `Network=Unlocked`. |

### Notes

- Pass `organic_results[].product_id` as `product_id` to [eBay Product](/apis/ebay/product) to get details for one listing.
- For the next page, set `_pgn` to the next page number. Use `_ipg` to set the page size to `60`, `120`, or `240`.
- `search_information.total_results` gives the total number of matching listings.
- The `inline_results` array holds extra groups of items, such as best selling products and sponsored picks, with fewer fields than `organic_results`.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/ebay/search.json`](../../../catalog/models/ebay/search.json) · Store page: https://www.sandbase.ai/model/ebay/search
