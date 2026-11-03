# DataForSEO ChatGPT LLM Response API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.000724 per call · **Modes:** sync

Ask ChatGPT a prompt and get its answer with token usage, for AI visibility checks.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.000724**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_name` | string |  | Model name from the vendor's model list.  |
| `web_search` | string |  | Optional: let the model search the web (where supported).  |
| `user_prompt` | string |  | The prompt to send.  |
| `system_message` | string |  | Optional system instruction.  |
| `max_output_tokens` | integer |  | Optional cap on answer length; longer answers cost more.  |

## Details

This API sends one prompt to a ChatGPT model and returns the text answer plus token counts. It needs a `user_prompt` and a `model_name`.

### Use cases

- Check whether ChatGPT names your brand when it answers a buying question such as `best running shoes 2026`.
- Compare how different `model_name` values answer the same prompt.
- Track how many input and output tokens a prompt uses before you run it at scale.
- Test a `system_message` and see how it changes the answer wording.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "best running shoes 2026", "model_name": "gpt-4o-mini", "max_output_tokens": 200}'
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
        "model_name": "gpt-4o-mini",
        "se": "chat_gpt",
        "user_prompt": "best running shoes 2026"
      },
      "id": "11030828-2190-0612-0000-e367aba07f9e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:28:37 +00:00",
          "fan_out_queries": null,
          "input_tokens": 24,
          "items": [
            {
              "sections": [
                {
                  "annotations": null,
                  "text": "While I can't predict specific models for 2026, I can suggest key factors to con…",
                  "type": "text"
                }
              ],
              "type": "message"
            }
          ],
          "model_name": "gpt-4o-mini-2024-07-18",
          "money_spent": 0.0001236,
          "output_tokens": 200,
          "reasoning_tokens": 0
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.6708 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.6861 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].sections[].text` | The answer text from the model. The answer length is capped by `max_output_tokens`. |
| `tasks[].result[].items[].sections[].type` | The kind of content in the section. The sample shows `text`. |
| `tasks[].result[].items[].sections[].annotations` | Annotations attached to the text. It is `null` in the sample. |
| `tasks[].result[].model_name` | The exact model version that answered, such as `gpt-4o-mini-2024-07-18`. It can differ from the short name you sent. |
| `tasks[].result[].input_tokens / output_tokens / reasoning_tokens` | Token counts for the prompt, the answer, and the model's reasoning. In the sample, `output_tokens` equals the `max_output_tokens` cap of `200`. |
| `tasks[].result[].datetime` | The time the answer was generated, in the format `2026-11-03 08:28:37 +00:00`. |
| `tasks[].result[].fan_out_queries` | Fan-out queries for the answer. It is `null` in the sample. |
| `tasks[].id` | The task ID, in a UUID-like format. |
| `tasks[].status_code / tasks[].status_message` | The task status. `20000` with `Ok.` means success. |

### Notes

- Set `max_output_tokens` high enough for a full answer. In the sample, `output_tokens` reached the `200` cap.
- Read the answer at `tasks[].result[].items[]`. Each item has a `type` of `message` and a list of `sections`.
- To ask other models the same prompt, use [DataForSEO Claude LLM Response](/apis/dataforseo/v3/ai_optimization/claude/llm_responses/live), [DataForSEO Gemini LLM Response](/apis/dataforseo/v3/ai_optimization/gemini/llm_responses/live) or [DataForSEO Perplexity LLM Response](/apis/dataforseo/v3/ai_optimization/perplexity/llm_responses/live).

### Pricing

Billed at the actual cost of each call, about $0.000724 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live
