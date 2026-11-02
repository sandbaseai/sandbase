# Google AI Mode API: pricing, parameters and code examples

`google/ai-mode` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Ask Google AI Mode a prompt and receive the cited answer it generates. AI Mode composes the answer at search time, so repeat calls on one prompt can differ in wording and in which sources are cited.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ai-mode", "prompt": "What are the most useful open-source AI agent frameworks?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ai-mode', {'prompt': 'What are the most useful open-source AI agent frameworks?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ai-mode", {
  "prompt": "What are the most useful open-source AI agent frameworks?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ai-mode", sandbase.Params{
	"prompt": "What are the most useful open-source AI agent frameworks?",
})
```

Same call via the path form: `POST /v1/api/google/ai-mode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The question or prompt to answer with Google AI Mode.  |

## Details

Ask Google AI Mode a prompt and receive the cited answer it generates. AI Mode composes the answer at search time, so repeat calls on one prompt can differ in wording and in which sources are cited.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ai-mode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What are the most useful open-source AI agent frameworks?"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | The question or prompt to answer with Google AI Mode. |

### Pricing

Billed at the actual cost of each call, usually $0.002 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/google/ai-mode.json`](../../../catalog/models/google/ai-mode.json) · Store page: https://www.sandbase.ai/model/google/ai-mode
