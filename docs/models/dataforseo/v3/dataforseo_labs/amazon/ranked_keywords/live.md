# DataForSEO Amazon Ranked Keywords API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

List keywords an Amazon product (ASIN) ranks for, with positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string |  | Amazon product ASIN.  |
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the keywords an Amazon product ranks for in Amazon search, based on its ASIN. Each row has the keyword, its search volume, and details about the product's listing in that search. You also pass a location code and a language code.

### Use cases

- Find the search terms that already bring shoppers to your product page, so you can add them to the listing title and bullets.
- Sort a competitor's ASIN by `search_volume` to see which keywords drive its visibility.
- Spot keywords where the product shows up as an Amazon's Choice or best seller badge holder.
- Compare the keyword sets of two ASINs to find gaps in your own listing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `asin` | string | No | Amazon product ASIN. |
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
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
        "api": "dataforseo_labs",
        "asin": "B0CP9YB3Q4",
        "function": "ranked_keywords",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0377-0000-e243bfa7269d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "asin": "B0CP9YB3Q4",
          "items": [
            {
              "keyword_data": {
                "keyword": "stanley on sale",
                "keyword_info": {
                  "last_updated_time": "2026-10-03 18:09:37 +00:00",
                  "se_type": "amazon",
                  "search_volume": 411
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "amazon"
              },
              "ranked_serp_element": {
                "check_url": "https://www.amazon.com/s?k=stanley+on+sale&crid=FNBAP1KX53HO&sprefix=stanley%2Bo…",
                "last_updated_time": "2026-09-13 08:26:55 +00:00",
                "previous_updated_time": "2026-07-14 20:53:00 +00:00",
                "se_results_count": 15268,
                "se_type": "amazon",
                "serp_item": {
                  "asin": "B0CP9YB3Q4",
                  "bought_past_month": 8000,
                  "currency": "USD",
                  "delivery_info": null,
                  "domain": "www.amazon.com",
                  "image_url": "https://m.media-amazon.com/images/I/51-U5dEbEBL._AC_UL320_.jpg",
                  "is_amazon_choice": false,
                  "is_best_seller": true
                },
                "serp_item_types": [
                  "amazon_serp"
                ]
              },
              "se_type": "amazon"
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "total_count": 3201
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.3482 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.3817 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].asin` | The ASIN the keywords were looked up for. |
| `tasks[].result[].total_count` | Total number of ranked keywords found for the ASIN. Compare it with `items_count` to see how many rows were returned in this call. |
| `tasks[].result[].items_count` | Number of keyword rows returned in this response. |
| `tasks[].result[].items[].keyword_data.keyword` | The search keyword the product ranks for. |
| `tasks[].result[].items[].keyword_data.keyword_info.search_volume` | Search volume for the keyword on Amazon. |
| `tasks[].result[].items[].ranked_serp_element.se_results_count` | Number of results Amazon shows for this keyword. |
| `tasks[].result[].items[].ranked_serp_element.check_url` | Amazon search URL for the keyword. Open it to see the results page. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.bought_past_month` | Count of purchases of the product in the past month, as shown on the listing. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.is_amazon_choice / tasks[].result[].items[].ranked_serp_element.serp_item.is_best_seller` | Whether the listing carried the Amazon's Choice or Best Seller badge for that keyword. |
| `tasks[].result[].items[].ranked_serp_element.last_updated_time / tasks[].result[].items[].ranked_serp_element.previous_updated_time` | Timestamps of the latest and the previous check of this ranking, in `YYYY-MM-DD HH:MM:SS +00:00` format. |

### Notes

- Find the ASIN in the product page URL on Amazon, where it appears after `/dp/`.
- Set `limit` to control how many rows come back, up to 100. Compare `total_count` with `items_count` to see if more keywords exist.
- Use `location_code` (for example `2840` for the United States) and `language_code` (for example `en`) to pick the Amazon market.
- Results sit in `tasks[].result`. A `status_code` of `20000` means the call succeeded.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/ranked_keywords/live
