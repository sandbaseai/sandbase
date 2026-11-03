# DataForSEO Keyword Trend by Region API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0024 per call (free daily quota) · **Modes:** sync

Get keyword interest split by subregion from an independent trends dataset. DataForSEO Trends subregion interest for up to 5 keywords.

## Pricing

- **$0.0024 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns relative search interest for each keyword, split by subregion (for example, US states) within one location. Send a `keywords` list and a `location_code`.

### Use cases

- Compare demand for `running shoes` across US states to pick regions for a local ad campaign.
- Find the subregions with the lowest interest to spot markets where a product is underserved.
- Build a regional heat map of keyword interest for a market research report.
- Check whether interest in a product term is concentrated in a few subregions or spread evenly.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live" \
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
        "function": "subregion_interests",
        "keywords": [
          "running shoes"
        ],
        "location_code": 2840,
        "se": "dataforseo_trends"
      },
      "id": "11030829-1614-0573-0000-8fe703a460b1",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:29:19 +00:00",
          "items": [
            {
              "interests": [
                {
                  "keyword": "running shoes",
                  "values": [
                    {
                      "geo_id": null,
                      "geo_name": "Alabama",
                      "value": 48
                    }
                  ]
                }
              ],
              "interests_comparison": null,
              "keywords": [
                "running shoes"
              ],
              "position": 1,
              "type": "subregion_interests"
            }
          ],
          "items_count": 1,
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
      "time": "0.9086 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.0052 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].interests[].keyword` | The keyword that the subregion values belong to. |
| `tasks[].result[].items[].interests[].values[].geo_name` | Name of the subregion, such as `Alabama`. |
| `tasks[].result[].items[].interests[].values[].value` | Interest score for the keyword in that subregion. Compare values within the same response. |
| `tasks[].result[].items[].interests[].values[].geo_id` | ID of the subregion. It is `null` in this response. |
| `tasks[].result[].items[].interests_comparison` | Comparison data between keywords. It is `null` in this response. |
| `tasks[].result[].items[].position` | Position of the item in the result list. |
| `tasks[].result[].items_count` | Number of items in the result. |
| `tasks[].result[].datetime` | Date and time of the result, in the format `2026-11-03 08:29:19 +00:00`. |
| `tasks[].result[].location_code / tasks[].result[].keywords` | The location and keywords the result was built for. They match the request. |
| `tasks[].status_code / tasks[].status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Results are in `tasks[].result`. Loop over `items[].interests[].values[]` to read each subregion.
- Use `location_code` `2840` for the United States. The sample response returns US state names in `geo_name`.
- The `language_code` field in the result is `null` for this request.

### Pricing

$0.0024 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/dataforseo_trends/subregion_interests/live
