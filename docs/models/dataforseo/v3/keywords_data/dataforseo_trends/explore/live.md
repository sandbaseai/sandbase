# DataForSEO Keyword Trend Explore API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/dataforseo_trends/explore/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0012 per call (free daily quota) · **Modes:** sync

Get keyword search trend series from an independent trends dataset. DataForSEO Trends explore for up to 5 keywords.

## Pricing

- **$0.0012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/dataforseo_trends/explore/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/dataforseo_trends/explore/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/dataforseo_trends/explore/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/dataforseo_trends/explore/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/dataforseo_trends/explore/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns a weekly search interest series for each keyword group you send, from the DataForSEO Trends dataset. You send a list of keywords and a `location_code`.

### Use cases

- Compare weekly search interest for up to 5 product keywords in the United States.
- Find the peak week for a seasonal keyword such as running shoes.
- Chart a keyword's interest over time in a dashboard using the weekly `timestamp` values.
- Check the average interest of a keyword before you plan content or ad spend.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/dataforseo_trends/explore/live" \
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
        "function": "explore",
        "keywords": [
          "running shoes"
        ],
        "location_code": 2840,
        "se": "dataforseo_trends"
      },
      "id": "11030829-1614-0570-0000-a953bf1b79ae",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:29:18 +00:00",
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
      "time": "0.9984 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.0165 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keywords` | The keywords the trend graph covers. |
| `tasks[].result[].items[].averages` | The average interest value over the whole period, one number per keyword. |
| `tasks[].result[].items[].data[].values` | Interest values for the week, one number per keyword in the same order as `keywords`. The sample shows a peak of `100`. |
| `tasks[].result[].items[].data[].date_from / tasks[].result[].items[].data[].date_to` | First and last day of the weekly period, as `YYYY-MM-DD`. |
| `tasks[].result[].items[].data[].timestamp` | Unix timestamp for the start of the weekly period. |
| `tasks[].result[].items[].type` | The item type. The value is `dataforseo_trends_graph` for the trend series. |
| `tasks[].result[].items_count` | Number of items in the result. |
| `tasks[].result[].location_code` | The location code used for the request. |
| `tasks[].result[].datetime` | Date and time of the result, with a UTC offset. |
| `tasks[].status_code / tasks[].status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Read the results from `tasks[].result`. Each call returns one task.
- Match each number in `values` and `averages` to the keyword at the same position in `keywords`.
- Use `location_code` `2840` for the United States.

### Pricing

$0.0012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/explore/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/explore/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/dataforseo_trends/explore/live
