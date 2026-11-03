# DataForSEO Google Play App Competitors API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/app_competitors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Find Google Play apps that compete with an app for the same search keywords, with intersecting keyword counts and average positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/app_competitors/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/app_competitors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/app_competitors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/app_competitors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/app_competitors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_id` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns Google Play apps that rank for the same search keywords as a target app. The input is an `app_id` (the Google Play package name), plus a `location_code` and `language_code`. Each competitor row has its shared keyword count, average position, and ranking breakdowns.

### Use cases

- Find the apps that compete most closely with your own app in Google Play search.
- Compare how many keywords a rival shares with your app and where it ranks on them.
- Spot large apps that take top positions on keywords you also target.
- Build a competitor list to track before you plan app store keyword work.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/app_competitors/live" \
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
        "function": "app_competitors",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "google"
      },
      "id": "11030829-1614-0450-0000-4a467efa5efd",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_id": "com.openai.chatgpt",
          "items": [
            {
              "app_id": "com.openai.chatgpt",
              "avg_position": 14.569327578703032,
              "competitor_metrics": {
                "google_play_search_organic": {
                  "count": 110288,
                  "pos_1": 4038,
                  "pos_11_100": 71762,
                  "pos_2_3": 3874,
                  "pos_4_10": 30614,
                  "search_volume": 33996424
                }
              },
              "full_metrics": {
                "google_play_search_organic": {
                  "count": 110288,
                  "pos_1": 4038,
                  "pos_11_100": 71762,
                  "pos_2_3": 3874,
                  "pos_4_10": 30614,
                  "search_volume": 33996424
                }
              },
              "intersections": 110288,
              "se_type": "google",
              "sum_position": 1606822
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "google",
          "total_count": 156883
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.1442 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.1522 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.tasks[].result[].items[].app_id` | Package name of the competing app. The first row can be the target app itself. |
| `tasks[].result[].items[].intersections` | Number of search keywords where both the target app and this competitor rank. |
| `tasks[].result[].items[].avg_position / sum_position` | Average ranking position of the competitor across the shared keywords, and the sum of those positions. |
| `tasks[].result[].items[].competitor_metrics.google_play_search_organic.count` | Number of shared keywords where this competitor ranks in Google Play organic search. |
| `tasks[].result[].items[].competitor_metrics.google_play_search_organic.pos_1 / pos_2_3 / pos_4_10 / pos_11_100` | Number of shared keywords where the competitor ranks at position 1, 2 to 3, 4 to 10, and 11 to 100. |
| `tasks[].result[].items[].competitor_metrics.google_play_search_organic.search_volume` | Search volume value summed for the shared keywords. |
| `tasks[].result[].items[].full_metrics.google_play_search_organic` | Same ranking counts for the competitor across all its keywords, not only those shared with the target app. |
| `tasks[].result[].total_count` | Total number of competing apps found for the target app. |
| `tasks[].result[].items_count` | Number of competitor rows returned in this response. |

### Notes

- Use the Google Play package name for `app_id`, such as `com.openai.chatgpt`. It is the same ID the response returns in `app_id`.
- `location_code` `2840` and `language_code` `en` were used in the example request.
- Set `limit` to control how many competitors come back. Compare `items_count` with `total_count` to see how many more exist.
- To look up apps by name or category first, use [DataForSEO Google Play App Listings Search](/apis/dataforseo/v3/app_data/google/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/app_competitors/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/app_competitors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/app_competitors/live
