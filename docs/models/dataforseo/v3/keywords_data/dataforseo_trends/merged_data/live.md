# DataForSEO Keyword Trend Overview API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.006 per call (free daily quota) · **Modes:** sync

Get trend series, subregion, and demographic data for keywords in one call. DataForSEO Trends merged data for up to 5 keywords: the interest-over-time graph, subregion interests, and demographic split in one response.

## Pricing

- **$0.006 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google-style trend data for one or more keywords in a single response: a weekly interest-over-time series, interest by subregion, and an age and gender split. It needs a `keywords` list and a `location_code`.

### Use cases

- Check whether interest in a product keyword peaks in a given season before planning a campaign.
- Find which US states show the highest relative interest in a keyword to pick regions for ads.
- Profile the age and gender mix of people searching a keyword to shape ad targeting.
- Plot the weekly trend line of a keyword in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |
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
        "api": "keywords_data",
        "function": "merged_data",
        "keywords": [
          "running shoes"
        ],
        "location_code": 2840,
        "se": "dataforseo_trends"
      },
      "id": "11030829-1614-0575-0000-c3ca73a11911",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:29:21 +00:00",
          "items": [
            {
              "averages": [
                50
              ],
              "data": [
                {
                  "date_from": "2025-11-09",
                  "date_to": "2025-11-15",
                  "timestamp": 1762646400,
                  "values": [
                    51
                  ]
                }
              ],
              "keywords": [
                "running shoes"
              ],
              "position": 1,
              "type": "dataforseo_trends_graph"
            }
          ],
          "items_count": 3,
          "keywords": [
            "running shoes"
          ],
          "language_code": null,
          "location_code": 2840,
          "type": "trends"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.5718 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.6095 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].type` | Block type. The response has `dataforseo_trends_graph`, `subregion_interests` and `demography` items. |
| `tasks[].result[].items[].keywords` | The keywords the item covers. |
| `tasks[].result[].items[].averages` | Average interest value for each keyword over the whole graph period. |
| `tasks[].result[].items[].data[].date_from / date_to` | Start and end dates of one weekly point in the graph. |
| `tasks[].result[].items[].data[].timestamp` | Unix timestamp for that weekly point. |
| `tasks[].result[].items[].data[].values` | Interest value for each keyword in that week. The sample values run up to 100. |
| `tasks[].result[].items[].interests[].values[].geo_name / value` | Subregion name and the interest value for the keyword there. `geo_id` can be `null`. |
| `tasks[].result[].items[].demography.age[].values[].type / value` | Age group, such as `18-24`, and the interest value for that group. |
| `tasks[].result[].items[].demography.gender[].values[].type / value` | Gender (`female` or `male`) and the interest value for it. |
| `tasks[].result[].items_count` | Number of blocks in the result. |

### Notes

- Find `location_code` values in the DataForSEO location list. `2840` is the United States.
- Each block in `items` is a separate type. Check `type` before you read its fields.
- `interests_comparison` and `demography_comparison` are `null` in the sample with one keyword.

### Pricing

$0.006 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/dataforseo_trends/merged_data/live
