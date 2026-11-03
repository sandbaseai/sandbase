# DataForSEO LLM Mentions Top Brands API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The brands most often mentioned in AI answers that match a keyword or domain, with mention counts and AI search volume.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

Returns the brands that AI answers mention most often for a keyword or domain. Each brand comes with mention counts, AI search volume, and breakdowns by category, platform, and source domain. You send a `target` array with one `keyword` or `domain` per entry.

### Use cases

- Find which shoe brands ChatGPT names most often for the keyword `running shoes`.
- Compare your brand's mention count against competitors in the same topic.
- See which domains and sources AI answers cite when they mention a given brand.
- Rank brands by AI search volume to pick topics worth targeting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live" \
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
        "function": "top_mentioned_brands",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0655-0000-e99750f35850",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 551800,
                "key": "product",
                "mentions": 28190
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 4284,
                "key": "Nike",
                "mentions": 553
              }
            ],
            "language": [
              {
                "ai_search_volume": 1217745,
                "key": "en",
                "mentions": 53128
              }
            ],
            "location": [
              {
                "ai_search_volume": 1217745,
                "key": 2840,
                "mentions": 53128
              }
            ],
            "platform": [
              {
                "ai_search_volume": 1217745,
                "key": "chat_gpt",
                "mentions": 53128
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 152203,
                "key": "runrepeat.com",
                "mentions": 8124
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 71189,
                "key": "www.reddit.com",
                "mentions": 6966
              }
            ],
            "total": {
              "ai_search_volume": 1217745,
              "mentions": 53128
            }
          },
          "items": [
            {
              "brand": "Nike",
              "brand_entities_category": [
                {
                  "ai_search_volume": 3495,
                  "key": "brand",
                  "mentions": 449
                }
              ],
              "brand_entities_title": [
                {
                  "ai_search_volume": 4284,
                  "key": "Nike",
                  "mentions": 553
                }
              ],
              "language": [
                {
                  "ai_search_volume": 4284,
                  "key": "en",
                  "mentions": 553
                }
              ],
              "location": [
                {
                  "ai_search_volume": 4284,
                  "key": 2840,
                  "mentions": 553
                }
              ],
              "platform": [
                {
                  "ai_search_volume": 4284,
                  "key": "chat_gpt",
                  "mentions": 553
                }
              ],
              "search_results_domain": [
                {
                  "ai_search_volume": 796,
                  "key": "www.nike.com",
                  "mentions": 120
                }
              ],
              "sources_domain": [
                {
                  "ai_search_volume": 780,
                  "key": "www.nike.com",
                  "mentions": 115
                }
              ]
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
      "time": "0.0219 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0609 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].brand` | Brand name, such as `Nike`. Items appear in order of mentions, highest first. |
| `tasks[].result[].items[].brand_entities_title[]` | Brands that appear together with this brand. Each row has the brand name in `key`, with `mentions` and `ai_search_volume`. The row matching the item's own brand gives its totals. |
| `tasks[].result[].items[].brand_entities_category[]` | How the AI answers classify this brand, with keys such as `brand`, `company`, `product` and `people`. Each row has `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].sources_domain[]` | Domains that AI answers cite as sources when they mention this brand. Each row has `key` (the domain), `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].search_results_domain[]` | Domains that appear in search results tied to answers mentioning this brand. Each row has `key`, `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].platform[] / language[] / location[]` | Splits the brand's mentions by `key`: AI platform such as `chat_gpt`, language code, and location code. Each row has `mentions` and `ai_search_volume`. |
| `tasks[].result[].aggregated_metrics.total` | Total `mentions` and `ai_search_volume` across all brands matching the target. |
| `tasks[].result[].aggregated_metrics.brand_entities_title[] / sources_domain[] / search_results_domain[]` | The same breakdowns for the whole target rather than one brand. Use them to see the top brands and domains overall. |
| `tasks[].result[].total_count` | Number of matching brands in total. `items_count` is the number returned in this response. |

### Notes

- Set `limit` to control how many brands come back. The response also includes `offset`, which was `0` here.
- Leave out `platform` to get both Google AI Overviews and ChatGPT. The sample response shows only `chat_gpt` in the platform breakdown.
- `location_code` `2840` is the United States and `language_code` `en` is English. The response echoes both in `location[].key` and `language[].key`.
- For a lighter version of this data, see [DataForSEO LLM Mentions Top Brands Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live). For domains instead of brands, see [DataForSEO LLM Mentions Top Domains](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live
