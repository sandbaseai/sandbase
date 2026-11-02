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

Ask Claude a prompt and get its answer with token usage, for AI visibility checks.

Request fields follow the official DataForSEO `/v3/ai_optimization/claude/llm_responses/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/ai_optimization/claude/llm_responses/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_prompt": "best running shoes 2026", "model_name": "claude-haiku-4-5", "max_output_tokens": 200}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `user_prompt` | The prompt to send. |
| `model_name` | Model name from the vendor's model list. |
| `max_output_tokens` | Optional cap on answer length; longer answers cost more. |
| `system_message` | Optional system instruction. |
| `web_search` | Optional: let the model search the web (where supported). |

### Reference

- Official docs: https://docs.dataforseo.com/v3/ai_optimization/claude/llm_responses/live/

### Pricing

Billed at the actual cost of each call, about $0.00162 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/ai_optimization/claude/llm_responses/live.json`](../../../../../../../catalog/models/dataforseo/v3/ai_optimization/claude/llm_responses/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/ai_optimization/claude/llm_responses/live
