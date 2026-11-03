# DataForSEO App Store App Intersection API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/apple/app_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Compare up to 20 App Store apps and get the search keywords they rank for together, with each app's position.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/apple/app_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/apple/app_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/apple/app_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/apple/app_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/apple/app_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_ids` | object |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

This API compares up to 20 App Store apps and returns the search keywords where the apps rank together. Each keyword row shows every app's rank, rating and price. You send the apps as an `app_ids` object, plus a `location_code` and `language_code`.

### Use cases

- Find the shared keywords where a rival app outranks yours, such as `chat gpt` or `google gemini`.
- Compare the ratings and vote counts of competing apps on the same search terms.
- Build a keyword list for App Store search optimization from terms your competitors already rank for.
- Check how many keywords a set of apps share by reading `total_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/apple/app_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_ids": {"1": "6448311069", "2": "6473753684"}, "location_code": 2840, "language_code": "en", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_ids` | object | No |  |
| `language_code` | string | No |  |
| `limit` | integer | No |  |
| `location_code` | integer | No |  |

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
        "app_ids": {
          "1": "6448311069",
          "2": "6473753684"
        },
        "function": "app_intersection",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "apple"
      },
      "id": "11030829-1614-0452-0000-7f029e691b71",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_ids": {
            "1": "6448311069",
            "2": "6473753684"
          },
          "items": [
            {
              "intersection_result": {
                "1": {
                  "app_id": "6448311069",
                  "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/1e/d2/2c/1ed22c36-78c3-54c…",
                  "is_free": true,
                  "position": "left",
                  "price": {
                    "currency": "USD",
                    "current": 0,
                    "displayed_price": "",
                    "is_price_range": false,
                    "max_value": 0,
                    "regular": 0
                  },
                  "rank_absolute": 1,
                  "rank_group": 1,
                  "rating": {
                    "rating_max": 5,
                    "rating_type": "Max5",
                    "value": 4.83,
                    "votes_count": 10356877
                  }
                },
                "2": {
                  "app_id": "6473753684",
                  "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/04/a7/5f/04a75ff9-c075-e3b…",
                  "is_free": true,
                  "position": "left",
                  "price": {
                    "currency": "USD",
                    "current": 0,
                    "displayed_price": "",
                    "is_price_range": false,
                    "max_value": 0,
                    "regular": 0
                  },
                  "rank_absolute": 4,
                  "rank_group": 4,
                  "rating": {
                    "rating_max": 5,
                    "rating_type": "Max5",
                    "value": 4.72,
                    "votes_count": 264290
                  }
                }
              },
              "keyword_data": {
                "keyword": "chat gpt",
                "keyword_info": {
                  "categories": null,
                  "competition": null,
                  "competition_level": null,
                  "cpc": null,
                  "high_top_of_page_bid": null,
                  "last_updated_time": "2026-09-17 03:51:27 +00:00",
                  "low_top_of_page_bid": null,
                  "monthly_searches": null
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "apple",
                "serp_info": {
                  "check_url": null,
                  "last_updated_time": "2026-09-17 03:51:27 +00:00",
                  "previous_updated_time": null,
                  "se_results_count": 245,
                  "se_type": "apple",
                  "serp_item_types": null
                }
              },
              "se_type": "apple"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "apple",
          "total_count": 3244
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "11.2218 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "11.2476 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of shared keywords found for the apps. Compare it with `items_count` to see how many rows this response returned. |
| `tasks[].result[].items[].keyword_data.keyword` | The search keyword where the compared apps rank together. |
| `tasks[].result[].items[].intersection_result.1.app_id / tasks[].result[].items[].intersection_result.2.app_id` | The App Store ID of each compared app. The keys `1` and `2` match the keys you sent in `app_ids`. |
| `tasks[].result[].items[].intersection_result.1.rank_absolute / tasks[].result[].items[].intersection_result.1.rank_group` | The app's position in the App Store results for this keyword. The same fields exist under each app key. |
| `tasks[].result[].items[].intersection_result.1.rating.value / tasks[].result[].items[].intersection_result.1.rating.votes_count` | The app's average rating and the number of votes behind it. `rating.rating_max` gives the top of the scale, which is 5 here. |
| `tasks[].result[].items[].intersection_result.1.is_free / tasks[].result[].items[].intersection_result.1.price.current` | Whether the app is free and its current price. `price.currency` gives the currency. |
| `tasks[].result[].items[].intersection_result.1.icon` | URL of the app icon image. |
| `tasks[].result[].items[].keyword_data.serp_info.se_results_count` | Number of results for the keyword in the App Store search. |
| `tasks[].result[].items[].keyword_data.keyword_info.last_updated_time` | Timestamp of the last update of the keyword data, in the form `2026-09-17 03:51:27 +00:00`. |

### Notes

- Send `app_ids` as an object with numeric string keys, such as `{"1": "6448311069", "2": "6473753684"}`. The values are App Store app IDs.
- Use `limit` to set how many keyword rows come back. Compare `items_count` with `total_count` to see how many rows remain.
- In this response, the `keyword_info` fields such as `monthly_searches`, `cpc` and `competition` are `null`, so do not rely on them for volume data.
- To find app IDs, try [DataForSEO App Store App Listings Search](/apis/dataforseo/v3/app_data/apple/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/apple/app_intersection/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/apple/app_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/apple/app_intersection/live
