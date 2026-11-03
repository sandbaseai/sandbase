# Bing Shopping Search API: pricing, parameters and code examples

`bing-shopping/search` · data API · Bing Shopping · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** async

Search Bing Shopping by keyword: product title, price, old price, seller, rating, reviews and shipping, with market and filter options.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing-shopping/search", "q": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing-shopping/search', {'q': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing-shopping/search", {
  "q": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing-shopping/search", sandbase.Params{
	"q": "wireless earbuds",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bing-shopping/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string \\| number \\| boolean | yes | The search query. You can use anything that you would use in a regular Bing Shopping search.  |
| `cc` | string \\| number \\| boolean |  | The country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.).  |
| `mkt` | string \\| number \\| boolean |  | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where…  |
| `device` | string \\| number \\| boolean |  | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `efirst` | string \\| number \\| boolean |  | Controls the offset of the shopping results. (e.g., `efirst=10` will move the 10th shopping result to the first position).  |
| `filters` | string \\| number \\| boolean |  | Allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as…  |
| `json_restrictor` | string \\| number \\| boolean |  | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Returns Bing Shopping results for a keyword search. Each result lists product details such as title, price, old price, seller, rating and reviews. The only required input is the search query `q`.

### Use cases

- Track the price and old price of competing products for a keyword like `wireless earbuds`.
- Compare which sellers appear for a product search in different markets using `cc` or `mkt`.
- Collect brand and price-range filter options to see how Bing groups a product category.
- Find related search terms to expand a keyword list for a shopping catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing-shopping/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "wireless earbuds"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | ['string', 'number', 'boolean'] | Yes | The search query. You can use anything that you would use in a regular Bing Shopping search. |
| `cc` | ['string', 'number', 'boolean'] | No | The country to search from. It follows the 2-character ISO_3166-1 format. (e.g., `us` for United States, `de` for Germany, `gb` for United Kingdom, etc.). |
| `device` | ['string', 'number', 'boolean'] | No | The device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `efirst` | ['string', 'number', 'boolean'] | No | Controls the offset of the shopping results. (e.g., `efirst=10` will move the 10th shopping result to the first position). |
| `filters` | ['string', 'number', 'boolean'] | No | Allows usage of a more complex filtering options such as filtering by date range `ex1:"ez5_18169_18230"` or using a specific display filters such as `ufn:"Wunderman+Thompson"+sid:"5bede9a2-1bda-9887-e6eb-30b1b8b6b513"+ca |
| `json_restrictor` | ['string', 'number', 'boolean'] | No | The fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |
| `mkt` | ['string', 'number', 'boolean'] | No | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where Bin |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ads_results": [
    {
      "displayed_link": "https://top10best.how",
      "extensions": [
        "Site visitors: Over 100K in the past month"
      ],
      "link": "https://www.bing.com/aclick?ld=e81eGxNvMkOi3NPQOgPVVOrjVUCUyOrCzsUAPumQ1mDJxSSD-…",
      "title": "Top 10 Best Wireless Earbuds - See Our #1 Pick Before You Buy"
    }
  ],
  "filters": [
    {
      "options": [
        {
          "link": "https://www.bing.com/shop?q=Available+nearby+wireless+earbuds&filters=gsfilter%3…",
          "serpapi_link": {
            "endpoint": "/bing/shopping",
            "queryParams": {
              "device": "desktop",
              "filters": "gsfilter%3A%22MSxCYXNpYywyPTEsVHw7%22+scenario%3A%2215%22+OriginalQuery%3A%22wir…",
              "q": "Available nearby wireless earbuds"
            }
          },
          "text": "Available nearby"
        }
      ],
      "type": "Show Only"
    }
  ],
  "inline_ads_results": [
    {
      "block_position": "top",
      "external_link": "https://tryravine.com/pages/pdp-eb-v1?tw_source=bing&tw_campaign=524067636&utm_t…",
      "extracted_old_price": 199.99,
      "extracted_price": 99.99,
      "link": "https://www.bing.com/aclick?ld=e84gDIRd-R5za9R0WhkK-gADVUCUwJkz2_wSCGjGmzY3YH6VV…",
      "old_price": "$199.99",
      "price": "$99.99",
      "seller": "Ravine",
      "tag": {
        "top": "SALE"
      },
      "thumbnail": "https://th.bing.com/th/id/OPHS.jaaPkVy9mb81dQ474C474?w=200&h=209&c=17&pid=21.1",
      "title": "Bluetooth Shooting Earbuds | Wireless Hunting Hearing Protection | Ravine Fieldo…"
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.bing.com/shop?q=wireless+earbuds&filters=scenario%3a%2215%22+LookupK…",
    "other_pages": {
      "2": "https://www.bing.com/shop?q=wireless+earbuds&filters=scenario%3a%2215%22+LookupK…",
      "3": "https://www.bing.com/shop?q=wireless+earbuds&filters=scenario%3a%2215%22+LookupK…",
      "4": "https://www.bing.com/shop?q=wireless+earbuds&filters=scenario%3a%2215%22+LookupK…",
      "5": "https://www.bing.com/shop?q=wireless+earbuds&filters=scenario%3a%2215%22+LookupK…"
    }
  },
  "related_searches": [
    {
      "highlighted_words": [
        "Apple"
      ],
      "link": "https://www.bing.com/shop?q=Apple+AirPods+Pro&FORM=SHOPA2",
      "serpapi_link": {
        "endpoint": "/bing/shopping",
        "queryParams": {
          "device": "desktop",
          "q": "Apple AirPods Pro"
        }
      },
      "text": "Apple AirPods Pro"
    }
  ],
  "search_metadata": {
    "bing_shopping_url": "https://www.bing.com/shop?q=wireless+earbuds",
    "cached": false,
    "created_at": "2026-11-03 07:26:43 UTC",
    "id": "6ae98cb34e12bd49d8426ebc",
    "processed_at": "2026-11-03 07:26:43 UTC",
    "status": "Success",
    "total_time_taken": 1.13
  },
  "search_parameters": {
    "device": "desktop",
    "engine": "bing_shopping",
    "q": "wireless earbuds"
  },
  "serpapi_pagination": {
    "current": 1,
    "next": {
      "endpoint": "/bing/shopping",
      "queryParams": {
        "device": "desktop",
        "efirst": "37",
        "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
        "q": "wireless earbuds"
      }
    },
    "next_link": {
      "endpoint": "/bing/shopping",
      "queryParams": {
        "device": "desktop",
        "efirst": "37",
        "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
        "q": "wireless earbuds"
      }
    },
    "other_pages": {
      "2": {
        "endpoint": "/bing/shopping",
        "queryParams": {
          "device": "desktop",
          "efirst": "37",
          "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
          "q": "wireless earbuds"
        }
      },
      "3": {
        "endpoint": "/bing/shopping",
        "queryParams": {
          "device": "desktop",
          "efirst": "73",
          "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
          "q": "wireless earbuds"
        }
      },
      "4": {
        "endpoint": "/bing/shopping",
        "queryParams": {
          "device": "desktop",
          "efirst": "109",
          "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
          "q": "wireless earbuds"
        }
      },
      "5": {
        "endpoint": "/bing/shopping",
        "queryParams": {
          "device": "desktop",
          "efirst": "145",
          "filters": "scenario:\"15\" LookupKey:\"e143c33b72324705a2a81cc606282447\" ParentRguid:\"e143c33b…",
          "q": "wireless earbuds"
        }
      }
    }
  },
  "shopping_results": [
    {
      "external_link": "https://www.macys.com/shop/product/sony-wf-1000xm6-truly-wireless-noise-cancelli…",
      "extracted_old_price": 328,
      "extracted_price": 298,
      "link": "https://www.bing.com/ck/a?!&&p=a15e83ffd043ae8ecadb51169f62df553726a2042071124e4…",
      "old_price": "$328.00",
      "price": "$298.00",
      "product_token": "KQg5Xnic…",
      "rating": 4.4,
      "reviews": "10K+",
      "seller": "Macy's",
      "serpapi_bing_product_api": {
        "endpoint": "/bing/product",
        "queryParams": {
          "product_token": "KQg5Xnic…"
        }
      },
      "thumbnails": [
        "https://th.bing.com/th?id=OPHS.x8x%2fz4CIrJyVng474C474&w=220&h=220&c=17&o=5&pid=…"
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shopping_results[]` | The organic product results for the query. Each item is one product listing. |
| `inline_ads_results[].title` | The product title of a sponsored product listing shown at the top of the results. |
| `inline_ads_results[].price / inline_ads_results[].old_price` | The current price and the earlier price as display strings, for example `$99.99` and `$199.99`. |
| `inline_ads_results[].extracted_price / inline_ads_results[].extracted_old_price` | The same current and old prices as plain numbers, ready for calculations. |
| `inline_ads_results[].seller` | The store that sells the sponsored product, for example `Walmart`. |
| `inline_ads_results[].rating / inline_ads_results[].reviews` | The product rating and the number of reviews. Some listings do not include them. |
| `ads_results[].title / ads_results[].link` | The title and tracking link of a text ad shown for the query. |
| `filters[].type / filters[].options[].text` | The filter group name, such as `Brand` or `Price`, and the label of each option in that group. |
| `related_searches[].text` | A related search phrase that Bing suggests for the query. |
| `pagination.current / pagination.other_pages` | The current page number and links to the other result pages. |

### Notes

- Each filter option and related search has a `serpapi_link.queryParams` object. Pass its `q` and `filters` values into a new request to apply that filter or search.
- To get the next page, use the `efirst` and `filters` values in `serpapi_pagination.next.queryParams`. In this response, page 2 uses `efirst` of `37` and page 3 uses `73`.
- The `search_parameters` object echoes the `q` and `device` values used for the call.

### Pricing

$0.015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bing-shopping/search.json`](../../../catalog/models/bing-shopping/search.json) · Store page: https://www.sandbase.ai/model/bing-shopping/search
