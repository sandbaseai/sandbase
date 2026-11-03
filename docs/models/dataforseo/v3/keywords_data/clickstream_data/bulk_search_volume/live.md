# DataForSEO Clickstream Bulk Search Volume API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Clickstream-based monthly search volume for up to 1,000 keywords in one request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Array of keywords (up to 1,000).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

This API returns monthly search volume estimates for a list of keywords, based on clickstream data. Send up to 1,000 keywords in `keywords` and a `location_code` such as `2840` for the United States.

### Use cases

- Rank a long list of candidate keywords by search volume in one call.
- Compare the demand for two product categories, such as coffee and tea, in the same country.
- Plot the recent monthly trend for each keyword to spot falling or rising interest.
- Filter a large keyword export down to terms with meaningful volume before deeper research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["coffee", "tea"], "location_code": 2840}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | Array of keywords (up to 1,000). |
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
        "function": "bulk_search_volume",
        "keywords": [
          "coffee"
        ],
        "location_code": 2840,
        "se": "clickstream_data"
      },
      "id": "11030829-1614-0591-0000-969020a1898d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "keyword": "coffee",
              "monthly_searches": [
                {
                  "month": 10,
                  "search_volume": 177126,
                  "year": 2026
                }
              ],
              "search_volume": 177126
            }
          ],
          "items_count": 2,
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.2405 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.2585 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword from your request that this row describes. |
| `tasks[].result[].items[].search_volume` | Estimated search volume for the keyword. It matches the most recent entry in `monthly_searches`. |
| `tasks[].result[].items[].monthly_searches[].year / tasks[].result[].items[].monthly_searches[].month` | Year and month number (1 to 12) of one monthly data point. |
| `tasks[].result[].items[].monthly_searches[].search_volume` | Estimated search volume for that keyword in that month. |
| `tasks[].result[].items_count` | Number of keyword rows in this result. |
| `tasks[].result[].location_code` | The location code the volumes apply to. |
| `tasks[].data.keywords` | The keywords the task received, echoed back from your request. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means it succeeded. |

### Notes

- Results sit in `tasks[].result`. A call sends one task, so read `tasks[0].result[0].items`.
- Months in `monthly_searches` are listed newest first.
- Use the `location_code` value from the request to match the results to a market. `2840` is the United States.
- `tasks[].id` is the task ID, a string like `11030829-1614-0591-0000-969020a1898d`.

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live
