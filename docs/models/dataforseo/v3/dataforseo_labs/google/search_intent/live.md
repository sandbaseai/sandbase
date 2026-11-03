# DataForSEO Google Search Intent API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/search_intent/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Classify up to 100 keywords by search intent (informational, navigational, commercial, transactional) with a probability for each label.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/search_intent/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/search_intent/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/search_intent/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/search_intent/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/search_intent/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  |   |
| `language_code` | string |  |   |

## Details

Returns the search intent of each keyword you send: informational, navigational, commercial or transactional. Each keyword gets a main intent label with a probability. The request needs a `keywords` array and a `language_code`.

### Use cases

- Sort a keyword list into content types, such as guides for informational terms and product pages for transactional terms.
- Filter a keyword research export to keep only terms with buying intent.
- Check whether a target keyword matches the type of page you plan to publish.
- Tag keywords in bulk before you build a content calendar or an ad campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/search_intent/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["buy running shoes", "how to tie shoes"], "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No |  |
| `language_code` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "dataforseo_labs",
        "function": "search_intent",
        "keywords": [
          "buy running shoes"
        ],
        "se_type": "google"
      },
      "id": "11030829-1614-0541-0000-d274e03b6bf6",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "keyword": "buy running shoes",
              "keyword_intent": {
                "label": "transactional",
                "probability": 1
              },
              "secondary_keyword_intents": null
            }
          ],
          "items_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1011 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1105 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword from your request that this row classifies. |
| `tasks[].result[].items[].keyword_intent.label` | The main search intent for the keyword. The example shows `transactional` for `buy running shoes` and `informational` for `how to tie shoes`. |
| `tasks[].result[].items[].keyword_intent.probability` | The probability for the main label, from 0 to 1. Both example keywords return `1`. |
| `tasks[].result[].items[].secondary_keyword_intents` | Other intents for the keyword. It is `null` when the keyword has no secondary intent. |
| `tasks[].result[].items_count` | The number of keyword rows in this result. |
| `tasks[].data.keywords` | The keywords the task processed, echoed from your request. |
| `tasks[].id` | The task ID for this call. |
| `tasks[].status_code / tasks[].status_message` | The status of the task. `20000` with `Ok.` means the task succeeded. |

### Notes

- Send up to 100 keywords in one request. Each keyword gets one row in `tasks[].result[].items[]`.
- Set `language_code` to a language code such as `en`.
- Check `tasks[].status_code` for each task, as well as the top-level `status_code`.
- Pair this with [DataForSEO AI Keyword Search Volume](/apis/dataforseo/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live) to add volume data to your keywords.

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/search_intent/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/search_intent/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/search_intent/live
