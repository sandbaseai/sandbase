# DataForSEO Business Listings Categories Aggregation API: pricing, parameters and code examples

`dataforseo/v3/business_data/business_listings/categories_aggregation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.048 per call · **Modes:** sync

Business category counts for a location or filter set, for local market sizing.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.048**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/business_listings/categories_aggregation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/business_listings/categories_aggregation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/business_listings/categories_aggregation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/business_listings/categories_aggregation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/business_listings/categories_aggregation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Maximum number of categories to return.  |
| `categories` | array |  | Optional array of category ids to aggregate.  |
| `location_coordinate` | string |  | "latitude,longitude,radius_km".  |

## Details

Returns business listing counts grouped by category for a location. Each category row includes the number of businesses, plus the most common related categories, attributes, and place topics. Send a `location_coordinate` as latitude, longitude and radius in km, and optionally a list of `categories`.

### Use cases

- Size a local market by counting how many pizza restaurants operate within 10 km of a point in New York.
- Find which categories most often overlap with a target category, such as `italian_restaurant` alongside `pizza_restaurant`.
- Compare how many businesses in an area offer delivery or takeout using the attribute counts.
- Spot popular menu or review topics in a category, such as `garlic knots`, to plan local content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/business_listings/categories_aggregation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"categories": ["pizza_restaurant"], "location_coordinate": "40.7128,-74.0060,10"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `categories` | array | No | Optional array of category ids to aggregate. |
| `limit` | string | No | Maximum number of categories to return. |
| `location_coordinate` | string | No | "latitude,longitude,radius_km". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "business_data",
        "categories": [
          "pizza_restaurant"
        ],
        "function": "categories_aggregation",
        "location_coordinate": "40.7128,-74.0060,10"
      },
      "id": "11030828-2190-0545-0000-9156cdc136bc",
      "path": [
        "v3"
      ],
      "result": [
        {
          "count": 100,
          "items": [
            {
              "aggregation": {
                "count": 1627,
                "top_attributes": {
                  "feels_casual": 1318,
                  "has_delivery": 1514,
                  "has_takeout": 1550,
                  "pay_credit_card": 1440,
                  "pay_debit_card": 1504,
                  "serves_comfort_food": 1372,
                  "serves_dine_in": 1440,
                  "serves_dinner": 1396
                },
                "top_categories": {
                  "bar": 104,
                  "chicken_wings_restaurant": 100,
                  "italian_restaurant": 516,
                  "meal_delivery": 209,
                  "meal_takeaway": 131,
                  "pasta_shop": 89,
                  "pizza_delivery_service": 425,
                  "pizza_restaurant": 1627
                },
                "top_countries": {
                  "US": 1627
                },
                "top_place_topics": {
                  "chicken parm": 116,
                  "crispy crust": 296,
                  "garlic knots": 453,
                  "grandma slice": 75,
                  "margarita pizza": 79,
                  "margherita pizza": 75,
                  "outdoor seating": 280,
                  "pie": 214
                },
                "websites_count": 1045
              },
              "categories": [
                "pizza_restaurant"
              ],
              "type": "business_category"
            }
          ],
          "offset": null,
          "offset_token": null,
          "total_count": 163
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.9609 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.9675 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of category rows that match the request. In the sample it is `163`. |
| `tasks[].result[].count` | Number of items returned in this response. In the sample it is `100`. |
| `tasks[].result[].items[].categories` | The category id this row aggregates, for example `pizza_restaurant`. |
| `tasks[].result[].items[].aggregation.count` | Number of business listings in this category within the search area. |
| `tasks[].result[].items[].aggregation.websites_count` | Number of those listings that have a website. |
| `tasks[].result[].items[].aggregation.top_categories` | Map of other category ids to the number of listings that also carry them. Use it to see which categories overlap. |
| `tasks[].result[].items[].aggregation.top_attributes` | Map of listing attributes such as `has_delivery` or `has_takeout` to the number of listings that have each one. |
| `tasks[].result[].items[].aggregation.top_place_topics` | Map of topics found for places in the category, such as `crispy crust`, to a count. |
| `tasks[].result[].items[].aggregation.top_countries` | Map of country codes to the number of listings in each country. |
| `tasks[].data.location_coordinate / tasks[].data.categories` | Echo of the filters the task ran with. |

### Notes

- Set `location_coordinate` as `"latitude,longitude,radius_km"`, for example `40.7128,-74.0060,10`.
- Use `limit` to cap how many category rows come back. `offset` and `offset_token` are `null` in this response, so there was no further page.
- To see the individual businesses behind these counts, call [Business Listings Search](/apis/dataforseo/v3/business_data/business_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.048 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/business_listings/categories_aggregation/live.json`](../../../../../../../catalog/models/dataforseo/v3/business_data/business_listings/categories_aggregation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/business_listings/categories_aggregation/live
