# DataForSEO Google Play Keywords for App API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/keywords_for_app/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

List the Google Play search keywords an Android app ranks for, with positions and search volume, by app ID, location and language.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keywords_for_app/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keywords_for_app/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keywords_for_app/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keywords_for_app/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_app/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_id` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns the Google Play search keywords an Android app ranks for, with the app's rank position for each keyword. It needs an `app_id` (the package name, such as `com.openai.chatgpt`), plus a `location_code` and `language_code`.

### Use cases

- Find which search terms bring a competitor's Android app into Google Play results.
- Track an app's `rank_absolute` for branded and generic keywords such as `chatgpt`.
- Build a keyword list for app store optimization from terms where your app ranks low.
- Open the `check_url` for a keyword to view the matching Google Play search page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keywords_for_app/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "com.openai.chatgpt", "location_code": 2840, "language_code": "en", "limit": 10}'
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
        "app_id": "com.openai.chatgpt",
        "function": "keywords_for_app",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030829-1614-0451-0000-ff512e712e2d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_id": "com.openai.chatgpt",
          "items": [
            {
              "keyword_data": {
                "keyword": "chat-gpt",
                "keyword_info": {
                  "categories": null,
                  "competition": null,
                  "competition_level": null,
                  "cpc": null,
                  "high_top_of_page_bid": null,
                  "last_updated_time": "2026-09-15 16:41:40 +00:00",
                  "low_top_of_page_bid": null,
                  "monthly_searches": null
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "google"
              },
              "ranked_serp_element": {
                "check_url": "https://play.google.com/store/search?c=apps&q=chat-gpt&hl=en&gl=us&price=0",
                "last_updated_time": "2026-09-15 16:41:37 +00:00",
                "previous_updated_time": null,
                "se_results_count": null,
                "se_type": "google",
                "serp_item": {
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
                }
              },
              "se_type": "google"
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 110288
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "9.2958 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "9.3399 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword_data.keyword` | The search term the app ranks for. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.rank_absolute` | The app's position in the Google Play results for that keyword. A value of `1` means the first result. |
| `tasks[].result[].items[].ranked_serp_element.check_url` | The Google Play search URL for that keyword, with the language and country already set. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.app_id / tasks[].result[].items[].ranked_serp_element.serp_item.developer` | The ID of the ranked app and the name of its developer. |
| `tasks[].result[].items[].ranked_serp_element.serp_item.is_free / tasks[].result[].items[].ranked_serp_element.serp_item.price.current` | Whether the app is free and its current price, with the currency in `price.currency`. |
| `tasks[].result[].items[].keyword_data.keyword_info.monthly_searches / tasks[].result[].items[].keyword_data.keyword_info.cpc` | Search volume and cost per click for the keyword. In this response both are `null`, so they may be empty for some keywords. |
| `tasks[].result[].items[].ranked_serp_element.last_updated_time` | Timestamp of when this ranking entry was last updated, such as `2026-09-15 16:41:37 +00:00`. |
| `tasks[].result[].total_count` | Total number of keywords found for the app. The response here shows `110288`. |
| `tasks[].result[].items_count` | Number of keyword rows returned in this response. |

### Notes

- Get the `app_id` from the Google Play listing URL, where it follows `id=`. You can also find it with [DataForSEO Google Play App Listings Search](/apis/dataforseo/v3/app_data/google/app_listings/search/live).
- `location_code` `2840` and `language_code` `en` were used in the example request.
- Use `limit` to set how many keywords come back. `total_count` shows how many exist in total.
- Rows are not shown sorted by `rank_absolute` in the example, so sort the list yourself if you need the best ranks first.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_app/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keywords_for_app/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keywords_for_app/live
