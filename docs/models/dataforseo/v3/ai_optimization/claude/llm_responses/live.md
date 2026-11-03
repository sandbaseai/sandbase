# DataForSEO Claude LLM Response API: pricing, parameters and code examples

`dataforseo/v3/ai_optimization/claude/llm_responses/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00162 per call · **Modes:** sync

Ask Claude a prompt and get its answer with token usage, for AI visibility checks.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00162**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/ai_optimization/claude/llm_responses/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/ai_optimization/claude/llm_responses/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/ai_optimization/claude/llm_responses/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/ai_optimization/claude/llm_responses/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/ai_optimization/claude/llm_responses/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_name` | string |  | Model name from the vendor's model list.  |
| `web_search` | string |  | Optional: let the model search the web (where supported).  |
| `user_prompt` | string |  | The prompt to send.  |
| `system_message` | string |  | Optional system instruction.  |
| `max_output_tokens` | integer |  | Optional cap on answer length; longer answers cost more.  |

## Details

This API sends a prompt to a Claude model and returns the text answer with input, output and reasoning token counts. It needs a `user_prompt` and a `model_name`.

### Use cases

- Check how Claude answers a buying question such as "best running shoes 2026" and see which products it names.
- Compare answers from different Claude models for the same prompt.
- Track how input and output token counts change as you adjust `system_message` or `max_output_tokens`.
- Collect Claude answers to a list of category prompts for an AI visibility report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/claude/llm_responses/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "best running shoes 2026", "model_name": "claude-haiku-4-5", "max_output_tokens": 200}'
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
        "model_name": "claude-haiku-4-5",
        "se": "claude",
        "user_prompt": "best running shoes 2026"
      },
      "id": "11030828-2190-0612-0000-6764163ac4b3",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:28:37 +00:00",
          "fan_out_queries": null,
          "input_tokens": 20,
          "items": [
            {
              "sections": [
                {
                  "annotations": null,
                  "text": "# Best Running Shoes 2026\n\nI should note that my knowledge was last updated in A…",
                  "type": "text"
                }
              ],
              "type": "message"
            }
          ],
          "model_name": "claude-haiku-4-5-20251001",
          "money_spent": 0.00102,
          "output_tokens": 200,
          "reasoning_tokens": 0
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.5708 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.5783 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].sections[].text` | The answer text from Claude. It is formatted as Markdown and the sample is cut short by `max_output_tokens`. |
| `tasks[].result[].items[].sections[].type` | The kind of section. The sample value is `text`. |
| `tasks[].result[].items[].type` | The kind of item. The sample value is `message`. |
| `tasks[].result[].items[].sections[].annotations` | Annotations attached to the text. It is `null` in the sample. |
| `tasks[].result[].model_name` | The full model version that answered, for example `claude-haiku-4-5-20251001`. It can differ from the short name you sent. |
| `tasks[].result[].input_tokens / output_tokens / reasoning_tokens` | Token counts for the prompt, the answer and the model's reasoning. |
| `tasks[].result[].fan_out_queries` | Related queries for the prompt, if any are returned. It is `null` in the sample. |
| `tasks[].result[].datetime` | The time the answer was generated, in the format `2026-11-03 08:28:37 +00:00`. |
| `tasks[].id` | The task ID, in UUID-like format. |

### Notes

- Each call runs one task, so `tasks[].result` holds one result with the answer in `items[].sections[]`.
- If `output_tokens` equals `max_output_tokens`, the answer was likely cut off. Raise `max_output_tokens` to get the full text.
- To compare Claude with other models on the same prompt, call [DataForSEO ChatGPT LLM Response](/apis/dataforseo/v3/ai_optimization/chat_gpt/llm_responses/live), [DataForSEO Gemini LLM Response](/apis/dataforseo/v3/ai_optimization/gemini/llm_responses/live) or [DataForSEO Perplexity LLM Response](/apis/dataforseo/v3/ai_optimization/perplexity/llm_responses/live).

### Pricing

Billed at the actual cost of each call, about $0.00162 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/claude/llm_responses/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/claude/llm_responses/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/claude/llm_responses/live
