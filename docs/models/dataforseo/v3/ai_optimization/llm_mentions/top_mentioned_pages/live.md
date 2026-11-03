# DataForSEO LLM Mentions Top Pages API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The pages most often mentioned in AI answers that match a keyword or domain, with mention counts and AI search volume.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the web pages that AI answers mention most often for a keyword or domain. Each page comes with mention counts and AI search volume, split by platform, language, and location. You send up to 10 `target` entities, each with one `keyword` or one `domain`.

### Use cases

- Find which guides and articles Google AI Overviews and ChatGPT cite most for a keyword like `running shoes`.
- Check which pages on a competitor domain get the most AI mentions.
- Build a content plan from the top cited pages and the domains they draw on.
- Compare how much a page is cited on `google` versus `chat_gpt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live" \
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
        "function": "top_mentioned_pages",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0654-0000-df4892dec4a0",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 677856,
                "key": "product",
                "mentions": 32000
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 33984,
                "key": "Nike",
                "mentions": 2784
              }
            ],
            "language": [
              {
                "ai_search_volume": 911679776,
                "key": "en",
                "mentions": 1655328
              }
            ],
            "location": [
              {
                "ai_search_volume": 911679776,
                "key": 2840,
                "mentions": 1655328
              }
            ],
            "platform": [
              {
                "ai_search_volume": 908206080,
                "key": "google",
                "mentions": 1524864
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 482144,
                "key": "runrepeat.com",
                "mentions": 15392
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 530975392,
                "key": "www.youtube.com",
                "mentions": 850944
              }
            ],
            "total": {
              "ai_search_volume": 275022918,
              "mentions": 332775
            }
          },
          "items": [
            {
              "brand_entities_category": [
                {
                  "ai_search_volume": 40,
                  "key": "brand",
                  "mentions": 1
                }
              ],
              "brand_entities_title": [
                {
                  "ai_search_volume": 40,
                  "key": "running and walking shoes",
                  "mentions": 1
                }
              ],
              "language": [
                {
                  "ai_search_volume": 333120,
                  "key": "en",
                  "mentions": 832
                }
              ],
              "location": [
                {
                  "ai_search_volume": 333120,
                  "key": 2840,
                  "mentions": 832
                }
              ],
              "page": "https://runrepeat.com/guides/best-all-day-wear-walking-shoes",
              "platform": [
                {
                  "ai_search_volume": 331840,
                  "key": "google",
                  "mentions": 800
                }
              ],
              "search_results_domain": [
                {
                  "ai_search_volume": 40,
                  "key": "www.wsj.com",
                  "mentions": 1
                }
              ],
              "sources_domain": [
                {
                  "ai_search_volume": 333120,
                  "key": "runrepeat.com",
                  "mentions": 832
                }
              ]
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 46051
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0212 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0403 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Number of matching pages found for the target. Use it to judge how many results exist beyond `limit`. |
| `tasks[].result[].items_count / offset` | Number of pages returned in this response, and the position this page of results starts from. |
| `tasks[].result[].items[].page` | Full URL of the page that AI answers mention. |
| `tasks[].result[].items[].platform[].key` | Platform name, such as `google` or `chat_gpt`. The `mentions` and `ai_search_volume` beside it count only that platform. |
| `tasks[].result[].items[].platform[].mentions / ai_search_volume` | Mentions of this page on the platform, and the AI search volume tied to those mentions. |
| `tasks[].result[].items[].sources_domain[].key` | Domain of a source that appears in answers mentioning this page. It often includes the page's own domain. |
| `tasks[].result[].items[].brand_entities_title[].key` | Name of a brand or product entity that appears alongside this page. The list can be empty. |
| `tasks[].result[].items[].language[] / location[]` | Mentions and AI search volume for the page by language code and by location code. `key` holds the code, for example `en` or `2840`. |
| `tasks[].result[].aggregated_metrics.total` | Total `mentions` and `ai_search_volume` for the whole target. |
| `tasks[].result[].aggregated_metrics.sources_domain[]` | Domains that appear most as sources across the whole target, with their mention counts and AI search volume. |

### Notes

- Set `limit` to control how many pages come back. The response also includes `offset` and `total_count`.
- Leave out `platform` to get both `google` and `chat_gpt`. Set it to one value to limit the results to that platform.
- `location_code` 2840 is the United States and `language_code` `en` is English. Both are the defaults.
- For a cheaper version of this data, use [DataForSEO LLM Mentions Top Pages Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live). To rank domains instead of pages, use [DataForSEO LLM Mentions Top Domains](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live
