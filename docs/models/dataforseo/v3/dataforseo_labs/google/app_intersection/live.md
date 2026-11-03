# DataForSEO Google Play App Intersection API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/app_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Compare up to 20 Google Play apps and get the search keywords they rank for together, with each app's position.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/app_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/app_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/app_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/app_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/app_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_ids` | object |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

This API compares two or more Google Play apps and returns the search keywords where they all rank. Each row shows every app's rank for that keyword. It needs `app_ids` (a map of numbered keys to Google Play package names), plus `location_code` and `language_code`.

### Use cases

- Find the shared search terms where a new AI assistant app competes with an established one on Google Play.
- Spot keywords where a competitor ranks above your app and target them in your store listing.
- Build a keyword list for app store optimization from the terms several rival apps all rank for.
- Check how many keywords two apps share by reading `total_count` for a given country and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/app_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_ids": {"1": "com.openai.chatgpt", "2": "com.anthropic.claude"}, "location_code": 2840, "language_code": "en", "limit": 10}'
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
          "1": "com.openai.chatgpt",
          "2": "com.anthropic.claude"
        },
        "function": "app_intersection",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030829-1614-0452-0000-9ceb600611fb",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_ids": {
            "1": "com.openai.chatgpt",
            "2": "com.anthropic.claude"
          },
          "items": [
            {
              "intersection_result": {
                "1": {
                  "app_id": "com.openai.chatgpt",
                  "developer": "OpenAI",
                  "developer_url": null,
                  "icon": "https://play-lh.googleusercontent.com/T9J8e9oxxPd600j_KPM4KK2GHfNpUpGBdTy8lHPXBX…",
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
                  "rank_absolute": 1
                },
                "2": {
                  "app_id": "com.anthropic.claude",
                  "developer": "Anthropic PBC",
                  "developer_url": null,
                  "icon": "https://play-lh.googleusercontent.com/YeFCFSW5LkBVdsEAL_fjzxDxTbhKz31j1uZUfDbSaC…",
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
                  "rank_absolute": 4
                }
              },
              "keyword_data": {
                "keyword": "chatgpt",
                "keyword_info": {
                  "categories": null,
                  "competition": null,
                  "competition_level": null,
                  "cpc": null,
                  "high_top_of_page_bid": null,
                  "last_updated_time": "2026-09-26 17:06:24 +00:00",
                  "low_top_of_page_bid": null,
                  "monthly_searches": null
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "google",
                "serp_info": {
                  "check_url": "https://play.google.com/store/search?c=apps&q=chatgpt&hl=en&gl=us&price=0",
                  "last_updated_time": "2026-09-26 17:06:23 +00:00",
                  "previous_updated_time": null,
                  "se_results_count": null,
                  "se_type": "google",
                  "serp_item_types": null
                }
              },
              "se_type": "google"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 10490
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.6692 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.6908 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of shared keywords found for the apps. `items_count` shows how many rows this response returned. |
| `tasks[].result[].items[].keyword_data.keyword` | The search keyword that all compared apps rank for. |
| `tasks[].result[].items[].intersection_result.1.rank_absolute / tasks[].result[].items[].intersection_result.2.rank_absolute` | The rank of the app in each slot for this keyword. The slot keys match the keys you sent in `app_ids`. |
| `tasks[].result[].items[].intersection_result.1.app_id / tasks[].result[].items[].intersection_result.2.app_id` | The Google Play package name of the app in that slot. |
| `tasks[].result[].items[].intersection_result.1.developer / tasks[].result[].items[].intersection_result.2.developer` | The developer name shown for the app. |
| `tasks[].result[].items[].intersection_result.1.is_free / tasks[].result[].items[].intersection_result.2.is_free` | Whether the app is free. The `price` object next to it holds `currency`, `current` and `regular` values. |
| `tasks[].result[].items[].keyword_data.serp_info.check_url` | A Google Play search URL for the keyword. Open it to see the results page for that term. |
| `tasks[].result[].items[].keyword_data.serp_info.last_updated_time / tasks[].result[].items[].keyword_data.keyword_info.last_updated_time` | Timestamps for when the search results and keyword data were last updated, in `YYYY-MM-DD HH:MM:SS +00:00` format. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches / tasks[].result[].items[].keyword_data.keyword_info.cpc` | Search volume and cost per click for the keyword. Both are `null` in this response, so do not rely on them for every keyword. |

### Notes

- Pass `app_ids` as an object such as `{"1": "com.openai.chatgpt", "2": "com.anthropic.claude"}`. The values are Google Play package names.
- Use `limit` to set how many keyword rows come back. `total_count` shows how many shared keywords exist beyond that.
- To find package names, search for apps with [DataForSEO Google Play App Listings Search](/apis/dataforseo/v3/app_data/google/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/app_intersection/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/app_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/app_intersection/live
