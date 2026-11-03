# DataForSEO LLM Mentions Top Brands Lite API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The brands most often mentioned in AI answers that match a keyword or domain, with counts only.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the brands that AI answers mention most often for a keyword or domain, ranked by mention count. Send a `target` array with a `keyword` or `domain`, plus optional location, language and platform. Each brand comes back with counts only.

### Use cases

- Find which shoe brands ChatGPT names most often for the keyword `running shoes`.
- Compare how often AI answers mention each brand in a product category to see who leads.
- Check which brands show up for a competitor's domain in AI answers.
- Pull a short top-brand list for a market by changing `location_code` and `language_code`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live" \
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
        "function": "top_mentioned_brands_lite",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0660-0000-2581ca029d4d",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": null,
          "items": [
            {
              "brand": "Nike",
              "language": "en",
              "location": 2840,
              "metrics": {
                "ai_search_volume": 4297,
                "mentions": 554
              },
              "platform": "chat_gpt"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 28749
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0230 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0683 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].brand` | Name of the brand mentioned in AI answers, such as `Nike`. |
| `tasks[].result[].items[].metrics.mentions` | Number of AI answers that mention the brand for the given target. |
| `tasks[].result[].items[].metrics.ai_search_volume` | AI search volume value for the brand. Higher numbers go with brands that have more mentions in this sample. |
| `tasks[].result[].items[].platform` | Platform the row comes from, such as `chat_gpt`. |
| `tasks[].result[].items[].location / language` | Location code and language code the row applies to, such as `2840` and `en`. |
| `tasks[].result[].items_count` | Number of brand rows in this response. |
| `tasks[].result[].total_count` | Total number of brand rows available for the target. It can be far larger than `items_count`. |
| `tasks[].result[].offset` | Position of the first returned row in the full list. It is `0` here. |
| `tasks[].data` | Echo of the request values the task ran with, including `target`, `limit`, `location_code` and `language_code`. |
| `tasks[].id` | Task ID in the form of a UUID-style string. |

### Notes

- Each `target` entry takes one `keyword` or one `domain`. You can send up to 10 entries.
- Set `platform` to `google` or `chat_gpt` to limit results to one platform. Leave it out to get both.
- Use `limit` to cap the rows returned. Compare `items_count` with `total_count` to see how many more rows exist.
- For more detail per brand, try [DataForSEO LLM Mentions Top Brands](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live
