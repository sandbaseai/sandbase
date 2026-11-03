# DataForSEO LLM Mentions Top Brand Categories Lite API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The brand categories most often mentioned in AI answers that match a keyword or domain, with counts only.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the brand categories most often mentioned in AI answers that match a keyword or domain. It needs a `target` array with one `keyword` or `domain` per entry. Each row gives counts only, per platform.

### Use cases

- Check which brand categories, such as `product` or `company`, appear most in ChatGPT answers about "running shoes".
- Compare mention counts across categories to see how AI answers frame a topic.
- Run the same keyword with `platform` set to `google` and then `chat_gpt` to compare AI Overviews with ChatGPT.
- Track a competitor domain and see which brand categories it is tied to in AI answers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live" \
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
        "function": "top_mentioned_brand_categories_lite",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0661-0000-8bee54578b78",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": null,
          "items": [
            {
              "brand_category": "product",
              "language": "en",
              "location": 2840,
              "metrics": {
                "ai_search_volume": 144624,
                "mentions": 7520
              },
              "platform": "chat_gpt"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 230
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0208 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0320 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].brand_category` | The brand category label, for example `product`, `brand` or `company`. |
| `tasks[].result[].items[].metrics.mentions` | How many times this brand category was mentioned in AI answers matching the target. |
| `tasks[].result[].items[].metrics.ai_search_volume` | The AI search volume value attached to this brand category. |
| `tasks[].result[].items[].platform` | The AI platform the row comes from, for example `chat_gpt`. |
| `tasks[].result[].items[].location / tasks[].result[].items[].language` | The location code and language code the row applies to, matching the request. |
| `tasks[].result[].items_count` | Number of items returned in this response. |
| `tasks[].result[].total_count` | Total number of matching items available for the target. |
| `tasks[].result[].offset` | Offset of the first returned item in the full list. |

### Notes

- Set `target` to an array of up to 10 entries, each with one `keyword` or one `domain`.
- Use `limit` to cap the rows returned. Compare `items_count` with `total_count` to see how many rows remain.
- Omit `platform` to get rows for both platforms, or set it to `google` or `chat_gpt` for one.
- For brand names instead of categories, see [DataForSEO LLM Mentions Top Brands Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live
