# DataForSEO LLM Mentions Top Domains API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The domains most often mentioned in AI answers that match a keyword or domain, with mention counts and AI search volume.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the domains that AI answers mention most often for a keyword or domain target. Each domain comes with mention counts and AI search volume, split by platform, location, language and more. It needs a `target` array with up to 10 entries, each holding one `keyword` or one `domain`.

### Use cases

- Find which sites AI answers cite most often for a topic such as `running shoes`.
- Compare how often a domain appears in Google AI Overviews versus ChatGPT answers.
- See which review and community sites (for example YouTube or Reddit) shape AI answers in your niche.
- Spot the brands and products that AI answers tie to a given domain.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live" \
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
        "function": "top_mentioned_domains",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0653-0000-b9331f4b0a2a",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 491776,
                "key": "product",
                "mentions": 25024
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 27328,
                "key": "Nike",
                "mentions": 2272
              }
            ],
            "language": [
              {
                "ai_search_volume": 728047328,
                "key": "en",
                "mentions": 1239296
              }
            ],
            "location": [
              {
                "ai_search_volume": 728047328,
                "key": 2840,
                "mentions": 1239296
              }
            ],
            "platform": [
              {
                "ai_search_volume": 725368320,
                "key": "google",
                "mentions": 1134368
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 378368,
                "key": "runrepeat.com",
                "mentions": 12736
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 57886432,
                "key": "www.youtube.com",
                "mentions": 99904
              }
            ],
            "total": {
              "ai_search_volume": 591286891,
              "mentions": 1022141
            }
          },
          "items": [
            {
              "brand_entities_category": [
                {
                  "ai_search_volume": 1568,
                  "key": "product",
                  "mentions": 96
                }
              ],
              "brand_entities_title": [
                {
                  "ai_search_volume": 41,
                  "key": "track and distance running documentary YouTube channel",
                  "mentions": 1
                }
              ],
              "domain": "www.youtube.com",
              "language": [
                {
                  "ai_search_volume": 57886432,
                  "key": "en",
                  "mentions": 99904
                }
              ],
              "location": [
                {
                  "ai_search_volume": 57886432,
                  "key": 2840,
                  "mentions": 99904
                }
              ],
              "platform": [
                {
                  "ai_search_volume": 57882560,
                  "key": "google",
                  "mentions": 99648
                }
              ],
              "search_results_domain": [
                {
                  "ai_search_volume": 1792,
                  "key": "www.adidas.com",
                  "mentions": 96
                }
              ],
              "sources_domain": [
                {
                  "ai_search_volume": 57886432,
                  "key": "www.youtube.com",
                  "mentions": 99904
                }
              ]
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 9591
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0242 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0528 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | A domain that AI answers mention for the target. Items appear in the order returned, with the largest mention counts first in this sample. |
| `tasks[].result[].items[].sources_domain[].key` | A source domain that appears in answers that mention this item's domain, including the domain itself. |
| `tasks[].result[].items[].sources_domain[].mentions / tasks[].result[].items[].sources_domain[].ai_search_volume` | Number of mentions for that source domain, and its AI search volume. |
| `tasks[].result[].items[].platform[].key` | Platform for the breakdown row, such as `google` or `chat_gpt`. Each row has `mentions` and `ai_search_volume` for that platform. |
| `tasks[].result[].items[].brand_entities_title[].key` | Name or description of a brand, product or entity mentioned alongside the domain, such as `Nike`. |
| `tasks[].result[].items[].brand_entities_category[].key` | Category of the mentioned entity, such as `product`, `brand` or `local_business`. |
| `tasks[].result[].items[].search_results_domain[].key` | A domain that shows up in search results linked to this item's domain, with its own `mentions` and `ai_search_volume`. |
| `tasks[].result[].aggregated_metrics.total` | Total `mentions` and `ai_search_volume` across all matching data for the target. |
| `tasks[].result[].aggregated_metrics.platform[]` | Totals for the whole target split by platform (`google` and `chat_gpt` in this response). |
| `tasks[].result[].total_count / tasks[].result[].items_count / tasks[].result[].offset` | `total_count` is the number of matching domains. `items_count` is how many came back in this call. `offset` is the start position of the page. |

### Notes

- Set `limit` to control how many domains come back. This call used `limit` 5 and returned 5 items out of a `total_count` of 9591.
- Every breakdown list (`platform`, `location`, `language`) uses a `key`, `mentions` and `ai_search_volume` row. A `location` key is the numeric code, for example `2840`.
- Set `platform` to `google` or `chat_gpt` to limit results to one platform. Omit it to get both.
- For a lighter response, try [DataForSEO LLM Mentions Top Domains Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live). For specific pages, call [DataForSEO LLM Mentions Top Pages](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_pages/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_domains/live
