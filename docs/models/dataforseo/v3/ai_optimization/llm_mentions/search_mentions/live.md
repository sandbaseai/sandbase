# DataForSEO LLM Mentions Search API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

AI answers (Google AI Overviews, ChatGPT) that mention a domain or keyword, with the question, answer and sources.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns AI answers from Google AI Overviews and ChatGPT that mention a target domain or keyword. You send a `target` array (for example `[{"domain": "nike.com"}]`) and get back matching answers with search volume and response dates.

### Use cases

- Find which AI answers cite your domain so you can see what topics trigger a mention.
- Rank mentioning answers by `ai_search_volume` to spot the highest-demand questions that include a competitor brand.
- Read answer text to check how an AI engine describes a brand or product line.
- Page through all mentions of a keyword to build a list of AI answer topics for content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": [{"domain": "nike.com"}], "location_code": 2840, "language_code": "en", "limit": 5}'
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
        "function": "search_mentions",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0650-0000-4e44062da464",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "ai_search_volume": 5000000,
              "answer": "The **Nike Tiempo** lineup features `modern soccer cleats and footwear` , includ…",
              "brand_entities": null,
              "fan_out_queries": null,
              "first_response_at": "2026-07-30 03:37:45 +00:00",
              "is_web_search_based": true,
              "language_code": "en",
              "last_response_at": "2026-11-02 22:58:29 +00:00"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "search_after_token": "eyJDdXJy…",
          "total_count": 156932
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "5.4625 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "5.4981 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].answer` | Text of the AI answer that mentions the target. It uses Markdown, including bold text and links. |
| `tasks[].result[].items[].ai_search_volume` | Search volume figure attached to the question behind the answer. Larger values mean the question is asked more often. |
| `tasks[].result[].items[].first_response_at / last_response_at` | Timestamps of the first and last time this answer was seen. They use the format `YYYY-MM-DD HH:MM:SS +00:00`. |
| `tasks[].result[].items[].is_web_search_based` | Shows whether the answer was built from a web search (`true`) or not. |
| `tasks[].result[].items[].language_code` | Language of the answer, such as `en`. |
| `tasks[].result[].items[].brand_entities / fan_out_queries` | Extra lists of brands and related queries for the answer. Both are `null` in this sample. |
| `tasks[].result[].items_count` | Number of items returned in this call. |
| `tasks[].result[].total_count` | Total number of mentions that match the target. It is much larger than `items_count` when you set a small `limit`. |
| `tasks[].result[].offset` | Position of the first returned item within the full result set. |
| `tasks[].result[].search_after_token` | Token returned with the result. Use it to continue from where this page ended. |

### Notes

- The `target` array takes up to 10 entities. Each entity has one `domain` or one `keyword`.
- Set `platform` to `google` or `chat_gpt` to limit results to one engine. Omit it to get both.
- Use `limit` to set the page size. `total_count` shows how many mentions exist overall.
- For aggregate counts instead of single answers, try [DataForSEO LLM Mentions Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live) or [DataForSEO LLM Mentions Top Pages](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live
