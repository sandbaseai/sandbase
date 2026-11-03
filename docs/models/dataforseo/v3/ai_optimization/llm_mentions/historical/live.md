# DataForSEO LLM Mentions History API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/historical/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.101 per call · **Modes:** sync

Monthly mention counts and AI search volume for a domain or keyword since August 2025.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.101**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/historical/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/historical/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/historical/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/historical/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/historical/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns monthly LLM mention counts and AI search volume for a domain or keyword, starting in August 2025. It needs a `target` array with up to 10 entries, each holding one `domain` or one `keyword`.

### Use cases

- Track how often AI answers mention nike.com each month and spot rises or drops.
- Compare AI search volume for a brand domain against the number of times it is mentioned.
- Build a monthly chart of a brand's visibility in Google AI Overviews or ChatGPT by setting `platform`.
- Check a keyword's mention trend in a given country and language by changing `location_code` and `language_code`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/historical/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": [{"domain": "nike.com"}], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code; default "en". |
| `location_code` | integer | No | Location code; default 2840 (United States). |
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
        "function": "historical",
        "language_code": "en",
        "location_code": 2840,
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0662-0000-ec731a7905a2",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "metrics": {
                "ai_search_volume": 23700880,
                "mentions": 812
              },
              "month": 11,
              "year": 2026
            }
          ],
          "items_count": 16
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.1371 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.1477 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One row per month for the target. Rows are listed newest first in the sample. |
| `tasks[].result[].items[].year / month` | Calendar year and month number (1 to 12) that the row covers. |
| `tasks[].result[].items[].metrics.mentions` | Number of LLM mentions of the target in that month. |
| `tasks[].result[].items[].metrics.ai_search_volume` | AI search volume figure for the target in that month. |
| `tasks[].result[].items_count` | Number of monthly rows returned in `items`. |
| `tasks[].data.target` | The target entities the task ran for, echoed from the request. |
| `tasks[].data.location_code / language_code` | The location and language the task used. |
| `tasks[].id` | Task ID in UUID-style format. |
| `tasks[].status_code / status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Pass `platform` as `google` or `chat_gpt` to limit the data to one platform. Omit it to cover both.
- `month` is a plain number and `year` is a separate field, so build dates from the two values.
- For a single snapshot of a target instead of a monthly series, try [DataForSEO LLM Mentions Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live).
- To see month-over-month changes directly, use [DataForSEO LLM Mentions Change Over Time](/apis/dataforseo/v3/ai_optimization/llm_mentions/timeseries_delta/live).

### Pricing

Billed at the actual cost of each call, about $0.101 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/historical/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/historical/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/historical/live
