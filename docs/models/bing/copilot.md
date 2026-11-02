# Bing Copilot Answer API: pricing, parameters and code examples

`bing/copilot` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Bing Copilot's conversational answer to a prompt, with the text blocks and cited references.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/copilot", "q": "what is the capital of france"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/copilot', {'q': 'what is the capital of france'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/copilot", {
  "q": "what is the capital of france"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/copilot", sandbase.Params{
	"q": "what is the capital of france",
})
```

Same call via the path form: `POST /v1/api/bing/copilot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | conversational prompt; param name not independently confirmed  |

## Details

Bing Copilot's conversational answer to a prompt, with the text blocks and cited references.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/copilot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "what is the capital of france"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | conversational prompt; param name not independently confirmed |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/copilot.json`](../../../catalog/models/bing/copilot.json) · Store page: https://www.sandbase.ai/model/bing/copilot
