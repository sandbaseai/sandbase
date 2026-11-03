# DataForSEO LLM Mentions New and Lost API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.104 per call · **Modes:** sync

New and lost mentions of a domain or keyword in AI answers per period.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.104**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` with the body above minus `model`.

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

This API returns, for each period between two dates, how many mentions of a domain or keyword appeared in AI answers for the first time and how many dropped out. It needs a `target` array (for example a `domain`), a `date_from` and `date_to` range, and a `group_range`.

### Use cases

- Track whether nike.com gains or loses visibility in AI answers from one month to the next.
- Compare `new_mentions` and `lost_mentions` to see if a content or PR push changed how often a brand is cited.
- Check the change in AI search volume tied to new and lost mentions to judge how big each shift is.
- Run the same query with `platform` set to `google` and then `chat_gpt` to see which platform drives the change.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live" \
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
        "function": "timeseries_new_lost",
        "group_range": "month",
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0664-0000-52ceb8f4aca1",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "date": "2026-07-01",
              "lost_ai_search_volume": 28526277,
              "lost_mentions": 42288,
              "new_ai_search_volume": 49808730,
              "new_mentions": 70751
            }
          ],
          "items_count": 4
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "5.5894 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "5.6206 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].date` | Start date of the period for this row, in `yyyy-mm-dd` format. With `group_range` set to `month`, each row is one month. |
| `tasks[].result[].items[].new_mentions` | Number of mentions of the target that are new in this period. |
| `tasks[].result[].items[].lost_mentions` | Number of mentions of the target that were present before and are gone in this period. |
| `tasks[].result[].items[].new_ai_search_volume / tasks[].result[].items[].lost_ai_search_volume` | AI search volume linked to the new mentions and to the lost mentions. Compare the two to see the net change for the period. |
| `tasks[].result[].items_count` | Count of items reported for the result. |
| `tasks[].data` | Echo of the request: `target`, `date_from`, `date_to`, `group_range` and `function`. |
| `tasks[].id` | Task ID returned for this call. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means the call succeeded. |

### Notes

- Subtract `lost_mentions` from `new_mentions` in each row to get the net change for that period.
- `date_from` can be no earlier than `2025-08-01`. `group_range` accepts `day`, `week`, `month` or `year`.
- Omit `platform` to cover both Google AI Overviews and ChatGPT, or set it to `google` or `chat_gpt` to limit the data to one.
- For a view of mention changes with other metrics, see [DataForSEO LLM Mentions Change Over Time](/apis/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live) or [DataForSEO LLM Mentions History](/apis/dataforseo/v3/ai_optimization/llm_mentions/historical/live).

### Pricing

Billed at the actual cost of each call, about $0.104 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/timeseries_new_lost/live
