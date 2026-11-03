# DataForSEO LLM Mentions Top Domains Lite API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The domains most often mentioned in AI answers that match a keyword or domain, with counts only.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the domains that appear most often in AI answers for a keyword or domain you give it. Each row has a mention count and an AI search volume, with no further detail. You send a `target` array, and you can add a location, language, platform and `limit`.

### Use cases

- Find which sites AI Overviews cite most for a topic such as `running shoes`.
- Check whether a competitor domain ranks among the most cited sources in AI answers.
- Build a short list of outreach or content targets based on the domains that AI answers rely on.
- Compare the top cited domains on Google and ChatGPT by setting `platform`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live" \
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
        "function": "top_mentioned_domains_lite",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0658-0000-e0a90058156b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": null,
          "items": [
            {
              "domain": "www.youtube.com",
              "language": "en",
              "location": 2840,
              "metrics": {
                "ai_search_volume": 57882560,
                "mentions": 99648
              },
              "platform": "google"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 10143
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0213 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0306 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | The domain that AI answers mention for the target, for example `www.youtube.com`. |
| `tasks[].result[].items[].metrics.mentions` | How many times this domain is mentioned in AI answers that match the target. |
| `tasks[].result[].items[].metrics.ai_search_volume` | AI search volume linked to the answers that mention this domain. Higher values mean the mentions sit on more searched topics. |
| `tasks[].result[].items[].platform` | The AI platform where the mentions were found, such as `google`. |
| `tasks[].result[].items[].location / tasks[].result[].items[].language` | The location code (`2840`) and language code (`en`) used for this row. |
| `tasks[].result[].items_count` | Number of items returned in this response. |
| `tasks[].result[].total_count` | Total number of matching domains, not only the rows returned. |
| `tasks[].result[].offset` | Position of the first returned item in the full list. |
| `tasks[].result[].aggregated_metrics` | Aggregate totals block. It is `null` in this response. |
| `tasks[].id` | ID of the task that served the call. |

### Notes

- Items are ordered from the highest `metrics.mentions` down in this response.
- Use `limit` to set how many domains come back. Compare `items_count` with `total_count` to see how many more exist.
- Omit `platform` to get rows for both Google and ChatGPT. Set it to `google` or `chat_gpt` to get one.
- For full metrics on each domain, call [DataForSEO LLM Mentions Top Domains](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live). For specific pages instead of domains, use [DataForSEO LLM Mentions Top Pages Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live
