# DataForSEO LLM Mentions Multi-Target Metrics API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.102 per call · **Modes:** sync

Mention metrics for 2 to 10 domains or keywords side by side, for share-of-voice comparisons in AI answers.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.102**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of 2 to 10 objects, each with a `key` label and a `target` array of domain or keyword entities.  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

Returns LLM mention counts and AI search volume for 2 to 10 targets in one call. Each target is a labeled group of domains or keywords, and the response gives totals plus a per-target breakdown by platform, language, location, source domain and brand entity.

### Use cases

- Compare how often Nike and Adidas appear in Google AI Overviews and ChatGPT answers.
- Check which domains AI answers cite most often when they mention each competitor.
- Split a brand's mentions by platform to see where it appears more often.
- Build a share-of-voice table for a set of competitors from the `mentions` and `ai_search_volume` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": [{"key": "nike", "target": [{"domain": "nike.com"}]}, {"key": "adidas", "target": [{"domain": "adidas.com"}]}], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code; default "en". |
| `location_code` | integer | No | Location code; default 2840 (United States). |
| `platform` | string | No | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both. |
| `targets` | array | No | Array of 2 to 10 objects, each with a `key` label and a `target` array of domain or keyword entities. |

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
        "function": "multi_target_metrics",
        "language_code": "en",
        "location_code": 2840,
        "targets": [
          {
            "key": "nike",
            "target": [
              {
                "domain": "nike.com"
              }
            ]
          }
        ]
      },
      "id": "11030828-2190-0652-0000-69973a20683e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 135562,
                "key": "product",
                "mentions": 5788
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 8580,
                "key": "Nike",
                "mentions": 935
              }
            ],
            "language": [
              {
                "ai_search_volume": 137745073,
                "key": "en",
                "mentions": 216373
              }
            ],
            "location": [
              {
                "ai_search_volume": 137745073,
                "key": 2840,
                "mentions": 216373
              }
            ],
            "platform": [
              {
                "ai_search_volume": 136695320,
                "key": "google",
                "mentions": 185713
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 701873,
                "key": "www.nike.com",
                "mentions": 18950
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 101825425,
                "key": "www.nike.com",
                "mentions": 148275
              }
            ],
            "total": {
              "ai_search_volume": 137745073,
              "mentions": 216373
            }
          },
          "items": [
            {
              "brand_entities_category": [
                {
                  "ai_search_volume": 112090,
                  "key": "product",
                  "mentions": 4795
                }
              ],
              "brand_entities_title": [
                {
                  "ai_search_volume": 8292,
                  "key": "Nike",
                  "mentions": 905
                }
              ],
              "key": "nike",
              "language": [
                {
                  "ai_search_volume": 102075470,
                  "key": "en",
                  "mentions": 156932
                }
              ],
              "location": [
                {
                  "ai_search_volume": 102075470,
                  "key": 2840,
                  "mentions": 156932
                }
              ],
              "platform": [
                {
                  "ai_search_volume": 101220080,
                  "key": "google",
                  "mentions": 132043
                }
              ],
              "search_results_domain": [
                {
                  "ai_search_volume": 701873,
                  "key": "www.nike.com",
                  "mentions": 18950
                }
              ],
              "sources_domain": [
                {
                  "ai_search_volume": 101825425,
                  "key": "www.nike.com",
                  "mentions": 148275
                }
              ]
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
      "time": "0.0764 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1111 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].key` | The label you gave the target in the request, such as `nike` or `adidas`. Use it to match each row to its target. |
| `tasks[].result[].items[].platform[]` | Mentions and AI search volume for that target on each platform, such as `google` and `chat_gpt`. The platform name is in `key`. |
| `tasks[].result[].items[].sources_domain[]` | Domains that AI answers cited as sources for this target. Each row has the domain in `key`, with `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].search_results_domain[]` | Domains found in search results tied to this target, with `mentions` and `ai_search_volume` for each. |
| `tasks[].result[].items[].brand_entities_title[]` | Brand or entity names that appear alongside this target, with their `mentions` and `ai_search_volume`. Rival brands can show up here. |
| `tasks[].result[].items[].brand_entities_category[]` | The same brand entities grouped by category, such as `product`, `brand` and `athlete`. |
| `tasks[].result[].items[].language[] / tasks[].result[].items[].location[]` | The same metrics split by language code and location code. The code is in `key`. |
| `tasks[].result[].aggregated_metrics.total` | Combined `mentions` and `ai_search_volume` across all targets in the request. |
| `tasks[].result[].aggregated_metrics.platform[] / tasks[].result[].aggregated_metrics.sources_domain[]` | The same breakdowns as the per-target rows, but combined across all targets. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | Number of target rows returned and the total number of targets. |

### Notes

- Each entry in `targets` needs a `key` label and a `target` array, for example `[{"domain": "nike.com"}]`. The `key` comes back unchanged in `items[].key`.
- Set `platform` to `google` or `chat_gpt` to limit the metrics to one platform. Leave it out to get both.
- The `location` rows use the numeric code in `key`, such as `2840`. The `language` rows use the code, such as `en`.
- For a single target with more detail, see [DataForSEO LLM Mentions Target Metrics](/apis/dataforseo/v3/ai_optimization/llm_mentions/target_metrics/live). For the pages and domains behind the mentions, see [DataForSEO LLM Mentions Search](/apis/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live).

### Pricing

Billed at the actual cost of each call, about $0.102 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/multi_target_metrics/live
