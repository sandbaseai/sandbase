# DataForSEO Google Play Bulk App Metrics API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get ranking metrics for up to 100 Google Play apps at once: keyword counts, position distribution and estimated search visibility.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_ids` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns keyword ranking metrics for Google Play apps, one item per app. Send a list of `app_ids` (Google Play package names) plus a `location_code` and `language_code`.

### Use cases

- Compare how many Google Play search keywords each competing app ranks for in the US.
- Track whether an app has more top 3 rankings than its rivals in a given market.
- Rank a list of apps by estimated search volume to find the most visible ones.
- Check app store search visibility in one request for up to 100 apps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_ids": ["com.openai.chatgpt"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_ids` | array | No |  |
| `language_code` | string | No |  |
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
        "app_ids": [
          "com.openai.chatgpt"
        ],
        "function": "bulk_app_metrics",
        "language_code": "en",
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030828-2190-0453-0000-51bae0baab66",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "app_id": "com.openai.chatgpt",
              "metrics": {
                "google_play_search_organic": {
                  "count": 110288,
                  "pos_1": 4038,
                  "pos_11_100": 71762,
                  "pos_2_3": 3874,
                  "pos_4_10": 30614,
                  "search_volume": 33996424
                }
              },
              "se_type": "google"
            }
          ],
          "items_count": 1,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 1
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.4160 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.4284 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].app_id` | The Google Play package name of the app, as you sent it in `app_ids`. |
| `tasks[].result[].items[].metrics.google_play_search_organic.count` | Total number of keywords the app ranks for in Google Play organic search for the chosen location and language. |
| `tasks[].result[].items[].metrics.google_play_search_organic.pos_1` | Number of keywords where the app ranks at position 1. |
| `tasks[].result[].items[].metrics.google_play_search_organic.pos_2_3` | Number of keywords where the app ranks at positions 2 to 3. |
| `tasks[].result[].items[].metrics.google_play_search_organic.pos_4_10` | Number of keywords where the app ranks at positions 4 to 10. |
| `tasks[].result[].items[].metrics.google_play_search_organic.pos_11_100` | Number of keywords where the app ranks at positions 11 to 100. |
| `tasks[].result[].items[].metrics.google_play_search_organic.search_volume` | Search volume summed over the keywords the app ranks for. Use it as a measure of search visibility. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | Number of app items returned and total number of items available for the request. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the metrics apply to. |

### Notes

- Use the Google Play package name as the app ID, for example `com.openai.chatgpt`. It is the `id` value in the Google Play store URL.
- The four position buckets (`pos_1`, `pos_2_3`, `pos_4_10`, `pos_11_100`) add up to `count` in this response.
- To find app IDs by name or category first, call [DataForSEO Google Play App Listings Search](/apis/dataforseo/v3/app_data/google/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live
