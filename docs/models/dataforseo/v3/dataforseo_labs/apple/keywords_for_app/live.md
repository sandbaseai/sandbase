# DataForSEO App Store Keywords for App API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

List the App Store search keywords an iOS app ranks for, with positions and search volume, by app ID, location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_id` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns the App Store search keywords that an iOS app ranks for in a given country and language. It needs an `app_id`, a `location_code` and a `language_code`. Each row gives the keyword, the app's rank for it and the app's listing data.

### Use cases

- Find the search terms that already bring an iOS app into the top results in the US store.
- Track an app's `rank_absolute` for branded and generic terms such as `gmail` or `facebook`.
- Compare the keyword lists of two competing apps to find terms one app ranks for and the other does not.
- Build a keyword target list for App Store optimization from the terms an established app ranks for.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "6448311069", "location_code": 2840, "language_code": "en", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_id` | string | No |  |
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
        "app_id": "6448311069",
        "function": "keywords_for_app",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "apple"
      },
      "id": "11030828-2190-0451-0000-22a2046caa83",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_id": "6448311069",
          "items": [
            {
              "keyword_data": {
                "keyword": "google",
                "keyword_info": {
                  "categories": null,
                  "competition": null,
                  "competition_level": null,
                  "cpc": null,
                  "high_top_of_page_bid": null,
                  "last_updated_time": "2026-09-15 13:09:45 +00:00",
                  "low_top_of_page_bid": null,
                  "monthly_searches": null
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "apple"
              },
              "ranked_serp_element": {
                "check_url": null,
                "last_updated_time": "2026-09-15 13:09:44 +00:00",
                "previous_updated_time": null,
                "se_results_count": 250,
                "se_type": "apple",
                "serp_item": {
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
                  "rank_absolute": 9,
                  "rank_group": 9,
                  "rating": {
                    "rating_max": 5,
                    "rating_type": "Max5",
                    "value": 4.83,
                    "votes_count": 10292460
                  }
                }
              },
              "se_type": "apple"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "apple",
          "total_count": 58333
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.0758 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.0815 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword_data.keyword` | The search term the app ranks for. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.rank_absolute / rank_group` | The app's rank in the results for that keyword. In this response both values are the same. |
| `tasks[].result[].items[].ranked_serp_element.se_results_count` | The number of results found for the keyword. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches` | Monthly search volume for the keyword. It is `null` for all rows in this sample, so check for `null` before use. |
| `tasks[].result[].items[].keyword_data.keyword_info.cpc / competition / competition_level` | Ad cost and competition values for the keyword. They are `null` in this sample. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.rating.value / votes_count` | The app's average rating (out of `rating_max`) and the number of ratings. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.is_free / price.current` | Whether the app is free and its current price in `price.currency`. |
| `tasks[].result[].items[].ranked_serp_element.last_updated_time` | Timestamp of the ranking record, such as `2026-09-15 13:09:44 +00:00`. |
| `tasks[].result[].total_count / items_count` | `total_count` is the number of ranked keywords found for the app. `items_count` is the number of rows returned in this response. |

### Notes

- Set `limit` to control how many keyword rows come back. The sample request used `10`, and `total_count` showed 58333 keywords for this app.
- `location_code` `2840` and `language_code` `en` were used in the sample request.
- To find an `app_id`, search App Store listings with [DataForSEO App Store App Listings Search](/apis/dataforseo/v3/app_data/apple/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/apple/keywords_for_app/live
