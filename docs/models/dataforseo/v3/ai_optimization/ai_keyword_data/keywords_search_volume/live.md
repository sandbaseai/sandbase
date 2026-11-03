# DataForSEO AI Keyword Search Volume API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0102 per call · **Modes:** sync

Estimated search volume of keywords inside AI tools such as ChatGPT and AI Overviews.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0102**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Array of keywords (up to 1,000).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the estimated monthly search volume of each keyword inside AI tools such as ChatGPT and AI Overviews. You send a list of keywords with a `location_code` and a `language_code`.

### Use cases

- Compare how often people search for a brand term in AI tools, such as `chatgpt` versus `seo tools`.
- Track month-by-month changes in AI search demand for a keyword list.
- Rank a list of candidate topics by AI search volume before planning content.
- Check whether a keyword gets more AI search volume in one country or language than in another.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["chatgpt", "seo tools"], "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | Array of keywords (up to 1,000). |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

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
        "function": "keywords_search_volume",
        "keywords": [
          "chatgpt"
        ],
        "language_code": "en",
        "location_code": 2840
      },
      "id": "11030828-2190-0619-0000-8b011fff2650",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "ai_monthly_searches": [
                {
                  "ai_search_volume": 286430,
                  "month": 10,
                  "year": 2026
                }
              ],
              "ai_search_volume": 286430,
              "keyword": "chatgpt"
            }
          ],
          "items_count": 2,
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1202 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1303 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword from your request that this row describes. |
| `tasks[].result[].items[].ai_search_volume` | Estimated AI search volume for the keyword. It matches the most recent entry in `ai_monthly_searches`. |
| `tasks[].result[].items[].ai_monthly_searches[].ai_search_volume` | Estimated AI search volume for one month. |
| `tasks[].result[].items[].ai_monthly_searches[].month / tasks[].result[].items[].ai_monthly_searches[].year` | The calendar month (1 to 12) and year that the monthly volume belongs to. |
| `tasks[].result[].items_count` | Number of keyword rows in `items`. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the volumes apply to, echoed from the request. |
| `tasks[].id` | Task ID in the form of a UUID-style string. |
| `tasks[].status_code / tasks[].status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Send up to 1,000 keywords in one `keywords` array.
- Use `location_code` such as `2840` for the United States and `language_code` such as `en`.
- `ai_monthly_searches` lists months from newest to oldest in the sample response.
- To see how AI tools answer a keyword, call [DataForSEO ChatGPT Search Answer](/apis/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced). To see which brands and domains AI answers mention, try [DataForSEO LLM Mentions Search](/apis/dataforseo/v3/ai_optimization/llm_mentions/search_mentions/live).

### Pricing

Billed at the actual cost of each call, about $0.0102 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live
