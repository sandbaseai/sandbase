# DataForSEO Bing Search Volume History API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/bing/search_volume_history/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Get monthly Bing search volume history for up to 1000 keywords. Bing Ads search volume history for a keyword list.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/search_volume_history/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/search_volume_history/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/search_volume_history/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/search_volume_history/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/search_volume_history/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns monthly Bing search volume history for each keyword you send. It needs a `keywords` list, plus a `location_code` and a `language_code`. Volumes come back per device type.

### Use cases

- Chart how Bing demand for a product term such as "running shoes" changes from month to month.
- Compare desktop, mobile and tablet search volume for the same keyword to plan device-specific Bing Ads bids.
- Spot seasonal peaks in Bing search interest before you set campaign budgets.
- Build a keyword research report that tracks Bing volume trends for a list of terms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/search_volume_history/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |
| `language_code` | string | No | Language code, e.g. "en". |
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
        "function": "search_volume_history",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "location_code": 2840,
        "se": "bing"
      },
      "id": "11030829-1614-0262-0000-5e0703863dce",
      "path": [
        "v3"
      ],
      "result": [
        {
          "device": [
            "desktop"
          ],
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840,
          "period": "monthly",
          "searches": {
            "desktop": [
              {
                "day": 1,
                "month": 10,
                "search_volume": 38889,
                "year": 2026
              }
            ],
            "mobile": [
              {
                "day": 1,
                "month": 10,
                "search_volume": 6908,
                "year": 2026
              }
            ],
            "non_smartphones": null,
            "tablet": [
              {
                "day": 1,
                "month": 10,
                "search_volume": 294,
                "year": 2026
              }
            ]
          }
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.2650 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.2965 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].keyword` | The keyword the volume history belongs to. |
| `tasks[].result[].period` | The time step of the history. The value `monthly` means one data point per month. |
| `tasks[].result[].device` | The device types listed for this keyword. A device in this list can still have `null` data in `searches`. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the volumes apply to. They match the values in your request. |
| `tasks[].result[].searches.desktop[]` | Monthly search volume points for desktop searches. |
| `tasks[].result[].searches.mobile[]` | Monthly search volume points for mobile searches. |
| `tasks[].result[].searches.tablet[]` | Monthly search volume points for tablet searches. |
| `tasks[].result[].searches.non_smartphones` | Volume points for non-smartphone devices. The value is `null` in this response, so no data came back for it. |
| `tasks[].result[].searches.desktop[].year / tasks[].result[].searches.desktop[].month / tasks[].result[].searches.desktop[].day` | The date of the data point. The `day` is `1` in this response, so each point marks the start of a month. The same keys appear in the `mobile` and `tablet` lists. |
| `tasks[].result[].searches.desktop[].search_volume` | The search volume for that month and device. The same key appears in the `mobile` and `tablet` lists. |

### Notes

- Send `keywords` as a list of strings. Use `location_code` such as `2840` for the United States and `language_code` such as `en`.
- Each device list is sorted from the newest month to the oldest in this response.
- Check each device list for `null` before you read it, because a device such as `non_smartphones` can have no data.
- The `tasks[].id` value identifies the task, and `tasks[].result_count` tells you how many keyword results came back.

### Pricing

$0.09 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/search_volume_history/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/search_volume_history/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/search_volume_history/live
