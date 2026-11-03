# DataForSEO Amazon Bulk Search Volume API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Get Amazon search volume for up to 100 keywords at once by location and language, to size product demand on Amazon.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

This API returns the Amazon search volume for each keyword in a list of up to 100 keywords. You send `keywords`, a `location_code` and a `language_code`, and it returns one volume number per keyword.

### Use cases

- Compare demand for several product ideas on Amazon in one call before choosing what to sell.
- Rank a list of seller keywords by `search_volume` to decide which ones to target in listings and ads.
- Check the same keyword list for different locations by changing `location_code`.
- Track a keyword set over time by saving the volumes from each call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["wireless earbuds", "phone case"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No |  |
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
        "function": "bulk_search_volume",
        "keywords": [
          "wireless earbuds"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0397-0000-5727301a74d0",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "keyword": "phone case",
              "se_type": "amazon",
              "search_volume": 43608
            }
          ],
          "items_count": 2,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "total_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1181 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1642 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword that was looked up. The items may come back in a different order than the request. |
| `tasks[].result[].items[].search_volume` | The Amazon search volume for the keyword in the chosen location and language. A higher number means more demand. |
| `tasks[].result[].items[].se_type` | The search engine type for the row. It is `amazon` here. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | The number of keyword rows in the result. In the example both are `2`, matching the two keywords sent. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the volumes apply to. They echo the request values. |
| `tasks[].data.keywords` | The keyword list the task received. |
| `tasks[].id` | The unique ID of the task, in a UUID-like format. |
| `tasks[].status_code / tasks[].status_message` | The status of the task. `20000` with `Ok.` means the task succeeded. |
| `tasks_count / tasks_error` | The number of tasks in the request and how many of them failed. |

### Notes

- Send at most 100 strings in `keywords`. Use `location_code` such as `2840` and `language_code` such as `en`.
- Read the volumes from `tasks[0].result[0].items`. Match rows to your input by `keyword`, not by position.
- Check `tasks_error` and `tasks[].status_code` before you read the items.

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/bulk_search_volume/live
