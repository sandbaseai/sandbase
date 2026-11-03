# DataForSEO LLM Mentions Target Metrics Lite API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.102 per call · **Modes:** sync

Headline mention counts and AI search volume for a domain or keyword in AI answers.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.102**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns headline AI answer metrics for up to 10 targets, where each target is a domain or a keyword. It gives one row per platform with an AI search volume and a mention count. The request needs a `target` array, and `location_code`, `language_code` and `platform` are optional.

### Use cases

- Compare how often a brand domain such as `nike.com` appears in Google AI Overviews versus ChatGPT answers.
- Check a brand's AI visibility in a quick, low-detail call before you run a full report.
- Track a keyword's mention count in AI answers for one country and language.
- Screen a short list of competitor domains for AI exposure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live" \
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
        "function": "target_metrics_lite",
        "language_code": "en",
        "location_code": 2840,
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0657-0000-254bbcf374fe",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": null,
          "items": [
            {
              "language": "en",
              "location": 2840,
              "metrics": {
                "ai_search_volume": 101220080,
                "mentions": 132043
              },
              "platform": "google"
            }
          ],
          "items_count": 2,
          "offset": 0,
          "total_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0301 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0828 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One row per platform for the requested target. This response has a `google` row and a `chat_gpt` row. |
| `tasks[].result[].items[].platform` | The AI platform the metrics belong to. Seen values are `google` and `chat_gpt`. |
| `tasks[].result[].items[].metrics.mentions` | Number of mentions of the target on that platform. |
| `tasks[].result[].items[].metrics.ai_search_volume` | AI search volume for the target on that platform. |
| `tasks[].result[].items[].location / language` | The location code and language code the row covers. They match `location_code` and `language_code` in the request. |
| `tasks[].result[].items_count / total_count` | Number of rows returned and total rows available. Both are 2 here. |
| `tasks[].result[].aggregated_metrics` | Aggregated metrics block. It is `null` in this response. |
| `tasks[].data.target[]` | Echo of the targets you sent, such as `domain` set to `nike.com`. |
| `tasks[].id` | Task ID in a UUID-like string format. |
| `status_code / status_message` | Status of the call. `20000` with `Ok.` means success. |

### Notes

- Set `platform` to `google` or `chat_gpt` to get one row. Omit it to get both.
- Each target object holds one `domain` or one `keyword`. You can send up to 10 targets.
- For a fuller metric set, call [DataForSEO LLM Mentions Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live).
- To compare several targets in one view, use [DataForSEO LLM Mentions Multi-Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live).

### Pricing

Billed at the actual cost of each call, about $0.102 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live
