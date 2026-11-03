# DataForSEO LLM Mentions Top Brand Categories API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.105 per call · **Modes:** sync

The brand categories most often mentioned in AI answers that match a keyword or domain, with mention counts and AI search volume.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.105**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of items to return.  |
| `target` | array |  | Array of up to 10 entities, each with one `domain` or one `keyword` (optional `search_filter`, `search_scope`, `match_type`).  |
| `platform` | string |  | Optional: "google" (AI Overviews) or "chat_gpt". Omit for both.  |
| `language_code` | string |  | Language code; default "en".  |
| `location_code` | integer |  | Location code; default 2840 (United States).  |

## Details

This API returns the brand categories (such as `product`, `brand` and `company`) most often mentioned in AI answers that match a keyword or domain. Each category comes with a mention count and an AI search volume. It needs a `target` array with up to 10 entries, each holding one `keyword` or one `domain`.

### Use cases

- Check whether AI answers about "running shoes" mention mostly products, brands or companies.
- Find which brand names and product names appear most inside each category for a keyword.
- See which websites AI answers cite as sources for each brand category.
- Compare category mix across `platform` values or locations to plan content for AI search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live" \
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
        "function": "top_mentioned_brand_categories",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "target": [
          {
            "keyword": "running shoes"
          }
        ]
      },
      "id": "11030828-2190-0656-0000-e909915b5cae",
      "path": [
        "v3"
      ],
      "result": [
        {
          "aggregated_metrics": {
            "brand_entities_category": [
              {
                "ai_search_volume": 144624,
                "key": "product",
                "mentions": 7520
              }
            ],
            "brand_entities_title": [
              {
                "ai_search_volume": 5963,
                "key": "Nike",
                "mentions": 775
              }
            ],
            "language": [
              {
                "ai_search_volume": 353618,
                "key": "en",
                "mentions": 17726
              }
            ],
            "location": [
              {
                "ai_search_volume": 353618,
                "key": 2840,
                "mentions": 17726
              }
            ],
            "platform": [
              {
                "ai_search_volume": 353618,
                "key": "chat_gpt",
                "mentions": 17726
              }
            ],
            "search_results_domain": [
              {
                "ai_search_volume": 52067,
                "key": "runrepeat.com",
                "mentions": 2895
              }
            ],
            "sources_domain": [
              {
                "ai_search_volume": 24341,
                "key": "www.reddit.com",
                "mentions": 2750
              }
            ],
            "total": {
              "ai_search_volume": 353618,
              "mentions": 17726
            }
          },
          "items": [
            {
              "brand_category": "product",
              "brand_entities_category": [
                {
                  "ai_search_volume": 144624,
                  "key": "product",
                  "mentions": 7520
                }
              ],
              "brand_entities_title": [
                {
                  "ai_search_volume": 6837,
                  "key": "HOKA Bondi 9",
                  "mentions": 219
                }
              ],
              "language": [
                {
                  "ai_search_volume": 144624,
                  "key": "en",
                  "mentions": 7520
                }
              ],
              "location": [
                {
                  "ai_search_volume": 144624,
                  "key": 2840,
                  "mentions": 7520
                }
              ],
              "platform": [
                {
                  "ai_search_volume": 144624,
                  "key": "chat_gpt",
                  "mentions": 7520
                }
              ],
              "search_results_domain": [
                {
                  "ai_search_volume": 39673,
                  "key": "runrepeat.com",
                  "mentions": 2098
                }
              ],
              "sources_domain": [
                {
                  "ai_search_volume": 28186,
                  "key": "runrepeat.com",
                  "mentions": 1296
                }
              ]
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
      "time": "0.0237 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0339 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].brand_category` | Name of the brand category for this item, for example `product`, `brand` or `company`. |
| `tasks[].result[].items[].brand_entities_category[].key / mentions / ai_search_volume` | Categories that appear together with this category, each with a mention count and an AI search volume. The entry that matches the item's own category carries its main totals. |
| `tasks[].result[].items[].brand_entities_title[].key` | Name of a specific brand or product mentioned in this category, such as `Nike` or `HOKA Bondi 9`. Each entry has its own `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].sources_domain[].key` | Domain that AI answers cite as a source for this category. Each entry has `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].search_results_domain[].key` | Domain that appears in search results tied to this category. Each entry has `mentions` and `ai_search_volume`. |
| `tasks[].result[].items[].platform[].key` | AI platform the numbers come from, such as `chat_gpt`. Sibling lists `language` and `location` show the language code and location code. |
| `tasks[].result[].aggregated_metrics` | The same breakdown lists (categories, brand titles, domains, platform, language, location) summed over all categories for the target. |
| `tasks[].result[].aggregated_metrics.total.mentions / ai_search_volume` | Total mention count and total AI search volume across all categories for the target. |
| `tasks[].result[].total_count` | Number of categories available for this target. |
| `tasks[].result[].items_count` | Number of items returned in this response. |

### Notes

- Set `limit` to cap the number of items returned. The response also shows `offset` (here `0`) and `total_count`, so you can see how many items exist.
- Location is a numeric code in `location_code` (for example `2840`) and language is a code in `language_code` (for example `en`). The same values come back as `key` in the `location` and `language` lists.
- Omit `platform` to get both Google AI Overviews and ChatGPT, or set it to `google` or `chat_gpt` to narrow the result.
- For a lighter version of this data, use [DataForSEO LLM Mentions Top Brand Categories Lite](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live). For individual brand rankings, use [DataForSEO LLM Mentions Top Brands](/apis/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brands/live).

### Pricing

Billed at the actual cost of each call, about $0.105 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live
