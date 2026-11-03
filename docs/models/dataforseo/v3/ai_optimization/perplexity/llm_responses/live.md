# DataForSEO Perplexity LLM Response API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/perplexity/llm_responses/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005824 per call · **Modes:** sync

Ask Perplexity a prompt and get its answer with token usage, for AI visibility checks.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005824**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/perplexity/llm_responses/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/perplexity/llm_responses/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/perplexity/llm_responses/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/perplexity/llm_responses/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/perplexity/llm_responses/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_name` | string |  | Model name from the vendor's model list.  |
| `web_search` | string |  | Optional: let the model search the web (where supported).  |
| `user_prompt` | string |  | The prompt to send.  |
| `system_message` | string |  | Optional system instruction.  |
| `max_output_tokens` | integer |  | Optional cap on answer length; longer answers cost more.  |

## Details

This API sends one prompt to a Perplexity model and returns the answer text, the source links it cited, and token counts. It needs a `user_prompt` and a `model_name` such as `sonar`.

### Use cases

- Check whether Perplexity names your brand when someone asks for the best products in your category.
- Collect the source URLs Perplexity cites for a query to see which sites it relies on.
- Track how the answer to the same prompt changes by running it on a schedule.
- Compare answers from different Perplexity models for the same prompt.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/perplexity/llm_responses/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "best running shoes 2026", "model_name": "sonar", "max_output_tokens": 200}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `max_output_tokens` | integer | No | Optional cap on answer length; longer answers cost more. |
| `model_name` | string | No | Model name from the vendor's model list. |
| `system_message` | string | No | Optional system instruction. |
| `user_prompt` | string | No | The prompt to send. |
| `web_search` | string | No | Optional: let the model search the web (where supported). |

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
        "function": "llm_responses",
        "max_output_tokens": 200,
        "model_name": "sonar",
        "se": "perplexity",
        "user_prompt": "best running shoes 2026"
      },
      "id": "11030828-2190-0612-0000-d08f12190130",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:28:40 +00:00",
          "fan_out_queries": null,
          "input_tokens": 13,
          "items": [
            {
              "sections": [
                {
                  "annotations": [
                    {
                      "end_index": null,
                      "start_index": null,
                      "text": null,
                      "title": "The 7 Best Running Shoes of 2026",
                      "url": "https://www.rtings.com/running-shoes/reviews/best/running"
                    }
                  ],
                  "text": "The **best running shoe for most runners in 2026 is the adidas Adizero Evo SL**,…",
                  "type": "text"
                }
              ],
              "type": "message"
            }
          ],
          "model_name": "sonar",
          "money_spent": 0.005216,
          "output_tokens": 203,
          "reasoning_tokens": 0
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.4682 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.4759 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].sections[].text` | The answer text. It uses Markdown and numbered markers such as `[1]` that point to the cited sources. |
| `tasks[].result[].items[].sections[].annotations[].title / tasks[].result[].items[].sections[].annotations[].url` | Title and link of a source the answer cites. |
| `tasks[].result[].items[].sections[].annotations[].start_index / tasks[].result[].items[].sections[].annotations[].end_index / tasks[].result[].items[].sections[].annotations[].text` | Position and text of the cited span. These were `null` in this response. |
| `tasks[].result[].input_tokens / tasks[].result[].output_tokens / tasks[].result[].reasoning_tokens` | Token counts for the prompt, the answer and the model's reasoning. `reasoning_tokens` was `0` for `sonar`. |
| `tasks[].result[].model_name` | The model that produced the answer. |
| `tasks[].result[].datetime` | Time of the response, for example `2026-11-03 08:28:40 +00:00`. |
| `tasks[].result[].fan_out_queries` | Related queries the model ran for the answer. It was `null` in this response. |
| `tasks[].data.user_prompt / tasks[].data.max_output_tokens` | Echo of the request values for this task. |
| `tasks[].id` | Task ID in a UUID-like format. |

### Notes

- Set `max_output_tokens` to cap the answer length. In the example, 200 was requested and `output_tokens` came back as `203`.
- The answer is in `tasks[].result[].items[]`, which has `type` set to `message`. Each message holds `sections[]` with `type` set to `text`.
- For the same prompt on other models, see [DataForSEO ChatGPT LLM Response](/apis/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live), [DataForSEO Claude LLM Response](/apis/dataforseo/v3/ai_optimization/claude/llm_responses/live) or [DataForSEO Gemini LLM Response](/apis/dataforseo/v3/ai_optimization/gemini/llm_responses/live).

### Pricing

Billed at the actual cost of each call, about $0.005824 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/perplexity/llm_responses/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/perplexity/llm_responses/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/perplexity/llm_responses/live
