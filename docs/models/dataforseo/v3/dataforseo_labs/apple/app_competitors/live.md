# DataForSEO App Store App Competitors API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/apple/app_competitors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Find App Store apps that compete with an iOS app for the same search keywords, with intersecting keyword counts and positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/apple/app_competitors/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/apple/app_competitors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/apple/app_competitors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/apple/app_competitors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/apple/app_competitors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_id` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Returns App Store apps that rank for the same search keywords as a given iOS app. It needs an `app_id`, plus `location_code` and `language_code` to pick the market. Each competitor comes with keyword overlap counts and ranking position buckets.

### Use cases

- Find which apps compete most directly with your iOS app in the US App Store.
- Spot competitors that rank in the top 3 for keywords where your app sits on page two or lower.
- Compare the size of each competitor's full keyword footprint with the overlap it shares with your app.
- Build a shortlist of apps to track for App Store optimization.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/apple/app_competitors/live" \
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
        "function": "app_competitors",
        "language_code": "en",
        "limit": 10,
        "location_code": 2840,
        "se_type": "apple"
      },
      "id": "11030829-1614-0450-0000-463134de4fb2",
      "path": [
        "v3"
      ],
      "result": [
        {
          "app_id": "6448311069",
          "items": [
            {
              "app_id": "6448311069",
              "avg_position": 42.38784221624124,
              "competitor_metrics": {
                "app_store_search_organic": {
                  "count": 58333,
                  "pos_1": 3070,
                  "pos_11_100": 47684,
                  "pos_2_3": 2119,
                  "pos_4_10": 5460,
                  "search_volume": 169541763
                }
              },
              "full_metrics": {
                "app_store_search_organic": {
                  "count": 58333,
                  "pos_1": 3070,
                  "pos_11_100": 47684,
                  "pos_2_3": 2119,
                  "pos_4_10": 5460,
                  "search_volume": 169541763
                }
              },
              "intersections": 58333,
              "se_type": "apple",
              "sum_position": 2472610
            }
          ],
          "items_count": 10,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "apple",
          "total_count": 546167
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "10.3257 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "10.3379 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].app_id` | App Store ID of the competitor app. The first item in the sample is the queried app itself. |
| `tasks[].result[].items[].intersections` | Number of keywords where both the queried app and this competitor rank. |
| `tasks[].result[].items[].avg_position / sum_position` | Average and summed ranking position of the competitor across the shared keywords. A lower average means a better rank. |
| `tasks[].result[].items[].competitor_metrics.app_store_search_organic.count` | Number of shared keywords the competitor ranks for in App Store organic search. |
| `tasks[].result[].items[].competitor_metrics.app_store_search_organic.pos_1 / pos_2_3 / pos_4_10 / pos_11_100` | Number of shared keywords where the competitor ranks at position 1, 2 to 3, 4 to 10, and 11 to 100. |
| `tasks[].result[].items[].competitor_metrics.app_store_search_organic.search_volume` | Combined search volume of the shared keywords. |
| `tasks[].result[].items[].full_metrics.app_store_search_organic` | Same count, position bucket and `search_volume` fields, but for all keywords the competitor ranks for, not only the shared ones. |
| `tasks[].result[].total_count` | Total number of competitor apps found for the target app. |
| `tasks[].result[].items_count` | Number of items returned in this response. |

### Notes

- `app_id` is the numeric App Store ID, for example `6448311069`. Find it in the app's App Store URL or through [DataForSEO App Store App Listings Search](/apis/dataforseo/v3/app_data/apple/app_listings/search/live).
- `location_code` `2840` and `language_code` `en` select the US English market.
- Use `limit` to set how many competitors come back. `total_count` shows how many exist in all.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/apple/app_competitors/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/apple/app_competitors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/apple/app_competitors/live
