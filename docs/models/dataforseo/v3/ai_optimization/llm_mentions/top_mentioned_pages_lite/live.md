# DataForSEO LLM Mentions Top Pages Lite API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The pages most often mentioned in AI answers that match a keyword or domain, with counts only.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the web pages that AI answers mention most often for a keyword or domain. It needs a `target` array with up to 10 entries, each holding one `keyword` or one `domain`. The Lite version returns counts only.

### Use cases

- Find which pages AI Overviews cite most often for a keyword such as `running shoes`.
- Check which of your own pages show up in AI answers for a topic, and how often.
- Spot competitor guides that AI answers favor, so you can plan content to match them.
- Rank pages by `ai_search_volume` to pick the topics that reach the most AI search traffic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": [{"keyword": "running shoes"}], "location_code": 2840, "language_code": "en", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code; default "en". |
| `limit` | integer | No | Maximum number of items to return. |
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
        "function": "top_mentioned_pages_lite",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0659-0000-f098322af8a4",
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
                "ai_search_volume": 1836800,
                "mentions": 800
              },
              "page": "https://runrepeat.com/guides/best-running-shoes",
              "platform": "google"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 46142
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0176 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0796 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].page` | The URL of the page that AI answers mention. |
| `tasks[].result[].items[].platform` | The AI platform where the mentions were found. The sample shows `google`. |
| `tasks[].result[].items[].metrics.mentions` | How many times the page is mentioned in AI answers for the target. |
| `tasks[].result[].items[].metrics.ai_search_volume` | The AI search volume tied to the page's mentions. Higher values mean more AI search activity around the page. |
| `tasks[].result[].items[].location / tasks[].result[].items[].language` | The location code and language code the row applies to, such as `2840` and `en`. |
| `tasks[].result[].items_count` | The number of items returned in this response. |
| `tasks[].result[].total_count` | The total number of matching pages. It can be much larger than `items_count`. |
| `tasks[].result[].offset` | The position in the full result list where this response starts. |

### Notes

- Pass the keyword or domain in `target`, for example `[{"keyword": "running shoes"}]`. Use `limit` to cap the number of rows.
- Set `platform` to `google` or `chat_gpt` to limit results to one platform. Omit it to get both.
- `aggregated_metrics` is `null` in this response, so use `items[]` for the data.
- For the version of this data with more detail per page, call [DataForSEO LLM Mentions Top Pages](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live). For domain-level counts, call [DataForSEO LLM Mentions Top Domains Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live
