# DataForSEO Google AI Mode Answer API: pricing, parameters and code examples

`dataforseo/v3/serp/google/ai_mode/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Fetch Google AI Mode's generated answer and cited sources for a query. Google AI Mode response for a keyword and location.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/ai_mode/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/ai_mode/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/ai_mode/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/ai_mode/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/ai_mode/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the answer that Google AI Mode generates for a search query, split into text blocks with the sources and links it cites. You send a `keyword`, a `location_code` and a `language_code`.

### Use cases

- Check which sources Google AI Mode cites when someone searches for a product category such as `running shoes`.
- Track how the AI Mode answer text for a keyword changes between locations or languages.
- Collect product names and links that AI Mode recommends for a shopping query.
- Compare the AI Mode answer with the ChatGPT or Gemini answer for the same keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/ai_mode/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
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
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "keyword": "running shoes",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-1abd4755a2d0",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/search?q=running%20shoes&hl=en&gl=US&udm=50&uule=w+CAIQIF…",
          "datetime": "2026-11-03 08:29:32 +00:00",
          "item_types": [
            "ai_overview"
          ],
          "items": [
            {
              "items": [
                {
                  "images": null,
                  "links": null,
                  "markdown": "Whether you are logging daily miles, recovering from a long run, or hunting for …",
                  "position": "left",
                  "references": null,
                  "text": "Whether you are logging daily miles, recovering from a long run, or hunting for …",
                  "title": null,
                  "type": "ai_overview_element"
                }
              ],
              "markdown": "Whether you are logging daily miles, recovering from a long run, or hunting for …",
              "page": 1,
              "position": "left",
              "rank_absolute": 1,
              "rank_group": 1,
              "rectangle": null,
              "references": [
                {
                  "domain": "www.google.com",
                  "position": "right",
                  "source": "Google",
                  "text": "The Saucony Hurricane 26 is a max Cushion Stability shoe Designed for Runners wh…",
                  "title": "Saucony Men's Hurricane 26",
                  "type": "ai_overview_reference",
                  "url": "https://www.google.com/search?q=product&prds=pvt:hg,pvo:29,productid:10559705419…"
                }
              ]
            }
          ],
          "items_count": 1,
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.4163 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.4850 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].check_url` | Google search URL for the query, location and language. Open it to compare the data with the live page. |
| `tasks[].result[].datetime` | Time the result was captured, in the format `2026-11-03 08:29:32 +00:00`. |
| `tasks[].result[].item_types` | Types of blocks found in the result. Here the value is `ai_overview`. |
| `tasks[].result[].items[].markdown` | Full AI Mode answer as Markdown. Long answers may be cut off in the text. |
| `tasks[].result[].items[].items[].text / markdown` | Plain text and Markdown version of one answer element, such as an intro line, a sentence or a list section. |
| `tasks[].result[].items[].items[].links[].title / url / domain` | Links that appear inside one answer element. In this response they are Google Shopping product links, with the product name in `title`. |
| `tasks[].result[].items[].items[].references[].title / url / domain / source` | Source cited for one answer element. `source` names the site or publisher, and `text` gives a snippet from it. |
| `tasks[].result[].items[].references[]` | All sources cited for the whole answer, with `title`, `url`, `domain`, `source` and a `text` snippet. |
| `tasks[].result[].items[].rank_absolute / rank_group` | Position of the answer block among the results. `1` means the first block. |
| `tasks[].result[].items_count` | Number of top-level answer blocks in the result. |

### Notes

- The `keyword` is free text. Look up location codes and language codes in the DataForSEO docs; `2840` is the United States.
- Some `links` and `references` values are `null` when an answer element has no cited sources.
- To compare with other AI answers for the same keyword, call [DataForSEO ChatGPT Search Answer](/apis/dataforseo/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced) or [DataForSEO Gemini Search Answer](/apis/dataforseo/v3/ai_optimization/gemini/llm_scraper/live/advanced).

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/ai_mode/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/ai_mode/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/ai_mode/live/advanced
