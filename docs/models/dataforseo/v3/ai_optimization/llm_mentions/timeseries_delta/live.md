# DataForSEO LLM Mentions Change Over Time API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.104 per call · **Modes:** sync

Change in mention count and AI search volume for a domain or keyword between periods.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.104**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `date_to` | string |  | End date, "yyyy-mm-dd".  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `date_from` | string |  | Start date, "yyyy-mm-dd" (from 2025-08-01).  |
| `group_range` | string |  | "day", "week", "month" or "year".  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | string |  | Location code; default 2840 (United States).  |

## Details

Returns the change in LLM mention count and AI search volume for a domain or keyword, grouped by day, week, month or year. It needs a `target` array (up to 10 entities), a `date_from` and a `date_to`. You can limit results to Google AI Overviews or ChatGPT with `platform`.

### Use cases

- Track whether nike.com gained or lost mentions in AI answers from one month to the next.
- Spot sudden swings in AI search volume tied to a brand or keyword after a campaign or product launch.
- Compare Google AI Overviews and ChatGPT trends by running the same request with each `platform` value.
- Feed monthly deltas into a dashboard that reports AI visibility for a domain.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": [{"domain": "nike.com"}], "date_from": "2026-07-01", "date_to": "2026-10-01", "group_range": "month"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_from` | string | No | Start date, "yyyy-mm-dd" (from 2025-08-01). |
| `date_to` | string | No | End date, "yyyy-mm-dd". |
| `group_range` | string | No | "day", "week", "month" or "year". |
| `language_code` | string | No | Language code; default "en". |
| `location_code` | string | No | Location code; default 2840 (United States). |
| `platform` | string | No | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both. |
| `target` | array | No | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "ai_optimization",
        "date_from": "2026-07-01",
        "date_to": "2026-10-01",
        "function": "timeseries_delta",
        "group_range": "month",
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0663-0000-afb6aa3768b2",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "date": "2026-07-01",
              "delta_ai_search_volume": 21282273,
              "delta_mentions": 28463
            }
          ],
          "items_count": 4
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.4089 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.4191 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].date` | Start date of the period for this row, in `yyyy-mm-dd` format. With `group_range` set to `month`, each row starts on the first day of a month. |
| `tasks[].result[].items[].delta_mentions` | Change in the number of mentions for the target in that period. A negative value means mentions fell. |
| `tasks[].result[].items[].delta_ai_search_volume` | Change in AI search volume for the target in that period. A negative value means it fell. |
| `tasks[].result[].items_count` | Number of items counted for the result. |
| `tasks[].data.target` | Echo of the `target` entities sent in the request. |
| `tasks[].data.date_from / tasks[].data.date_to` | Date range the task used, echoed from the request. |
| `tasks[].data.group_range` | Period size used to group the rows, echoed from the request. |
| `tasks[].id` | Task ID in UUID-style format. |

### Notes

- Set `target` to an array of objects, each with one `domain` or one `keyword`. Example: `[{"domain": "nike.com"}]`.
- `date_from` can be no earlier than 2025-08-01. Dates use `yyyy-mm-dd`.
- `location_code` defaults to 2840 (United States) and `language_code` defaults to `en`. Omit `platform` to include both Google and ChatGPT.
- In the sample, `items_count` is 4 while three rows are shown, because the response was trimmed. For absolute values per period, call [DataForSEO LLM Mentions History](/apis/dataforseo/v3/ai_optimization/llm_mentions/historical/live).

### Pricing

Billed at the actual cost of each call, about $0.104 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live
