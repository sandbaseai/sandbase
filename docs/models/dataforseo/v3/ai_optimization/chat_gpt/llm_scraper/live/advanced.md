# DataForSEO ChatGPT Search Answer API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Get ChatGPT's answer to a query as a signed-out user would see it. ChatGPT (chatgpt.com) response for a keyword, location, and language as the public web UI shows it.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns ChatGPT's answer to a search query as a signed-out user sees it on chatgpt.com. Send a `keyword`, a `location_code` and a `language_code`. The response lists the answer blocks in order, with the brands and source pages ChatGPT shows.

### Use cases

- Track which products and brands ChatGPT names for a buying query such as `best running shoes 2026`.
- Find which websites ChatGPT cites as sources for a topic, and check whether your domain is one of them.
- Compare ChatGPT answers for the same keyword across different locations and languages.
- See the extra queries ChatGPT ran behind the scenes to build its answer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "best running shoes 2026", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
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
        "device": "desktop",
        "function": "live",
        "keyword": "best running shoes 2026",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "chat_gpt"
      },
      "id": "11030828-2190-0629-0000-168fbde78531",
      "path": [
        "v3"
      ],
      "result": [
        {
          "brand_entities": [
            {
              "category": "product",
              "markdown": "ASICS Superblast 3",
              "title": "ASICS Superblast 3",
              "type": "chat_gpt_brand_entity",
              "urls": null
            }
          ],
          "check_url": "https://chatgpt.com/?prompt=best%20running%20shoes%202026",
          "datetime": "2026-11-03 08:28:50 +00:00",
          "fan_out_queries": [
            "best running shoes 2026 reviews daily trainers stability race shoes"
          ],
          "item_types": [
            "chat_gpt_text"
          ],
          "items": [
            {
              "brand_entities": null,
              "markdown": "The best running shoes of **2026** depend on whether you want comfort, speed, cu…",
              "rank_absolute": 1,
              "rank_group": 1,
              "sources": null,
              "type": "chat_gpt_text"
            }
          ],
          "items_count": 17,
          "keyword": "best running shoes 2026"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "16.7166 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "16.8346 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | Answer blocks in the order ChatGPT shows them. Each block has a `type` such as `chat_gpt_text`, `chat_gpt_images` or `chat_gpt_products`. |
| `tasks[].result[].items[].markdown` | The text of the block in Markdown. Product blocks can include a price and a short list of pros. |
| `tasks[].result[].items[].rank_absolute / rank_group` | `rank_absolute` is the block position in the whole answer. `rank_group` is its position among blocks of the same group. |
| `tasks[].result[].items[].sources[].title / domain / source_name` | Title, domain and publisher name of a page cited for that block. |
| `tasks[].result[].items[].sources[].publication_date` | Publication date of the cited page, when ChatGPT shows one. It is `null` otherwise. |
| `tasks[].result[].brand_entities[].title / category` | Name and category (for example `product`) of each brand or product mentioned in the answer. |
| `tasks[].result[].fan_out_queries` | Related search queries ChatGPT used to build the answer. |
| `tasks[].result[].check_url` | A chatgpt.com link that opens the same prompt in the web UI. |
| `tasks[].result[].item_types / items_count` | The block types present in the answer and the total number of items. |
| `tasks[].result[].datetime` | Time the answer was captured, in the format `2026-11-03 08:28:50 +00:00`. |

### Notes

- Results are in `tasks[].result`. Each call returns one task with its own `id`.
- Many `brand_entities[].urls`, `sources`, and `markdown` values are `null`, so check for `null` before you read them.
- Use `location_code` `2840` for the United States and `language_code` `en` for English.
- To get a plain model answer without the web UI layout, call [DataForSEO ChatGPT LLM Response](/apis/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live). For the same kind of answer from Gemini, use [DataForSEO Gemini Search Answer](/apis/dataforseo/v3/ai_optimization/gemini/llm_scraper/live/advanced).

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced
