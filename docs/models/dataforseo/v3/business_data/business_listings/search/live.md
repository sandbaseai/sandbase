# DataForSEO Business Listings Search API: pricing, parameters and code examples

`dataforseo/v3/business_data/business_listings/search/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0156 per call · **Modes:** sync

Search Google Maps business listings by category, name or location radius, with ratings, contact details and work hours.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0156**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/business_listings/search/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/business_listings/search/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/business_listings/search/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/business_listings/search/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/business_listings/search/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of listings to return.  |
| `title` | string |  | Optional business name to match.  |
| `categories` | array |  | Array of business category ids, e.g. ["pizza_restaurant"].  |
| `location_coordinate` | string |  | "latitude,longitude,radius_km".  |

## Details

Returns Google Maps business listings that match a category, a business name, or a location radius. You send category ids such as `pizza_restaurant` and a `location_coordinate` string in the form `latitude,longitude,radius_km`.

### Use cases

- Build a lead list of every pizza restaurant within 10 km of a point in New York.
- Map competitors in a category around a planned store location.
- Filter venues by attributes such as wheelchair access, delivery or takeout.
- Count how many businesses of one category exist in an area using `total_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/business_listings/search/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"categories": ["pizza_restaurant"], "location_coordinate": "40.7128,-74.0060,10", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `categories` | array | No | Array of business category ids, e.g. ["pizza_restaurant"]. |
| `limit` | integer | No | Maximum number of listings to return. |
| `location_coordinate` | string | No | "latitude,longitude,radius_km". |
| `title` | string | No | Optional business name to match. |

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
        "function": "search",
        "limit": 10,
        "location_coordinate": "40.7128,-74.0060,10"
      },
      "id": "11030828-2190-0544-0000-95f7a3fdbe54",
      "path": [
        "v3"
      ],
      "result": [
        {
          "count": 10,
          "items": [
            {
              "additional_categories": [
                "Bar"
              ],
              "address": "70 Hudson St, Hoboken, NJ 07030",
              "address_info": {
                "address": "70 Hudson St",
                "borough": null,
                "city": "Hoboken",
                "country_code": "US",
                "region": "New Jersey",
                "zip": "07030"
              },
              "attributes": {
                "available_attributes": {
                  "accessibility": [
                    "has_wheelchair_accessible_entrance"
                  ],
                  "amenities": [
                    "has_restroom_unisex"
                  ],
                  "atmosphere": [
                    "feels_casual"
                  ],
                  "children": [
                    "has_childrens_menu"
                  ],
                  "crowd": [
                    "popular_with_students"
                  ],
                  "dining_options": [
                    "serves_breakfast"
                  ],
                  "highlights": [
                    "has_fast_service"
                  ],
                  "offerings": [
                    "serves_alcohol"
                  ]
                },
                "unavailable_attributes": {
                  "accessibility": [
                    "has_wheelchair_accessible_parking"
                  ],
                  "planning": [
                    "accepts_reservations"
                  ],
                  "service_options": [
                    "has_delivery"
                  ]
                }
              },
              "category": "Bar & grill",
              "category_ids": [
                "bar_and_grill"
              ],
              "check_url": "https://www.google.com/maps?cid=10011767498971649037&hl=en&gl=US",
              "cid": "10011767498971649037"
            }
          ],
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 1627
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.7087 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.7481 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Number of listings that match the search. This can be larger than the number of items returned. |
| `tasks[].result[].count` | Number of items returned in this response. |
| `tasks[].result[].items[].category / additional_categories` | Main category name of the listing and a list of extra category names. |
| `tasks[].result[].items[].category_ids` | Category ids for the listing. You can reuse them in the `categories` request parameter. |
| `tasks[].result[].items[].address` | Full address as one string. |
| `tasks[].result[].items[].address_info` | Address split into `address`, `borough`, `city`, `region`, `zip` and `country_code`. `borough` can be `null`. |
| `tasks[].result[].items[].attributes.available_attributes` | Features the business has, grouped by topic such as `accessibility`, `dining_options`, `offerings` and `service_options`. |
| `tasks[].result[].items[].attributes.unavailable_attributes` | Features the business does not have, grouped the same way. The value is `null` when none are listed. |
| `tasks[].result[].items[].cid` | Google Maps customer id of the listing, as a string. |
| `tasks[].result[].items[].check_url` | Google Maps link that opens the listing. |
| `tasks[].result[].offset_token` | Token for the next page of results. |

### Notes

- Set `limit` to control how many listings come back. The example request used `10`.
- The response has `offset` set to `0` and an `offset_token`. Use the token to continue a long result list.
- Pick category ids from the `category_ids` values in the response. [DataForSEO Business Listings Categories Aggregation](/apis/dataforseo/v3/business_data/business_listings/categories_aggregation/live) shows how categories are grouped.
- Pass a `cid` or `check_url` to [DataForSEO Google Business Listing Info](/apis/dataforseo/v3/business_data/google/my_business_info/live/advanced) for more detail on one business.

### Pricing

Billed at the actual cost of each call, about $0.0156 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/business_listings/search/live.json`](../../../../../../../catalog/models/dataforseo/v3/business_data/business_listings/search/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/business_listings/search/live
