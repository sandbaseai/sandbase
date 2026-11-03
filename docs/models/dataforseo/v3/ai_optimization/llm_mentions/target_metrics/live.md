# DataForSEO LLM Mentions Target Metrics API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.101 per call · **Modes:** sync

Mention counts and AI search volume for a domain or keyword in AI answers, with breakdowns by platform, location and source.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.101**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

Returns total mentions and AI search volume for a domain or keyword across AI answers on Google AI Overviews and ChatGPT. It needs a `target` array with a `domain` or `keyword`, plus optional `location_code`, `language_code` and `platform`.

### Use cases

- Measure how often `nike.com` appears in AI answers compared with a competitor's domain.
- Split a brand's AI visibility between Google and ChatGPT to decide where to focus.
- Find which sites AI answers cite when they mention your brand.
- See which brand entity categories, such as products or athletes, drive most of your mentions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live" \
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
        "function": "target_metrics",
        "language_code": "en",
        "location_code": 2840,
        "target": [
          {
            "domain": "nike.com"
          }
        ]
      },
      "id": "11030828-2190-0651-0000-e0e568e4529b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 112588,
                "key": "product",
                "mentions": 4728
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 7600,
                "key": "Nike",
                "mentions": 956
              }
            ],
            "language": [
              {
                "ai_search_volume": 117869892,
                "key": "en",
                "mentions": 156756
              }
            ],
            "location": [
              {
                "ai_search_volume": 117869892,
                "key": 2840,
                "mentions": 156756
              }
            ],
            "platform": [
              {
                "ai_search_volume": 117007800,
                "key": "google",
                "mentions": 131908
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 715412,
                "key": "www.nike.com",
                "mentions": 18936
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 117647608,
                "key": "www.nike.com",
                "mentions": 148208
              }
            ],
            "total": {
              "ai_search_volume": 117869892,
              "mentions": 156756
            }
          },
          "items": [],
          "items_count": 0,
          "offset": 0,
          "total_count": 0
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0540 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0639 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].aggregated_metrics.total` | Total `mentions` and `ai_search_volume` for the target across all platforms in the requested location and language. |
| `aggregated_metrics.platform[]` | Mentions and AI search volume per platform. The `key` is `google` or `chat_gpt`. |
| `aggregated_metrics.sources_domain[]` | Domains that AI answers used as sources when they mentioned the target. Each row has the domain in `key`, plus `mentions` and `ai_search_volume`. |
| `aggregated_metrics.search_results_domain[]` | Domains that appeared in search results tied to the target's mentions, with `mentions` and `ai_search_volume` per domain. |
| `aggregated_metrics.brand_entities_category[]` | Mentions and AI search volume grouped by entity category, such as `product`, `brand` or `athlete`. |
| `aggregated_metrics.brand_entities_title[]` | Mentions and AI search volume grouped by entity title, such as `Nike` or `sportswear company`. |
| `aggregated_metrics.location[] / aggregated_metrics.language[]` | Mentions and AI search volume for each location code and language code. The `key` holds the code, for example `2840` or `en`. |
| `tasks[].result[].items / items_count / total_count` | The detail list. In this response it is empty and the counts are `0`, so the metrics sit in `aggregated_metrics`. |
| `tasks[].id` | Task ID in a UUID-style format for the call. |

### Notes

- Send up to 10 entries in `target`. Each entry holds one `domain` or one `keyword`.
- Omit `platform` to get both Google and ChatGPT. Set it to `google` or `chat_gpt` to get one.
- Each breakdown row has `key`, `mentions` and `ai_search_volume`. The `key` for `location` is a number, and for the other breakdowns it is a string.
- For a single target with fewer fields, try [DataForSEO LLM Mentions Target Metrics Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/target_metrics_lite/live). To compare several targets, try [DataForSEO LLM Mentions Multi-Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live).

### Pricing

Billed at the actual cost of each call, about $0.101 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live
