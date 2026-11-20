# Meshy Creative Lab Collapsible Fidget API: pricing, parameters and code examples

`meshy/creative-lab/fidget-collapsible` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.24 per call · **Modes:** async

Turns a photo into a print-in-place collapsible fidget toy.

## Pricing

- **$0.24 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/fidget-collapsible", "image": "https://static.sandbase.ai/examples/77fb5870-d8ec-471d-9362-7e17dc7dd79f/input/910b60cc-d9f0-498c-9fdc-7f53f426a1f7.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/fidget-collapsible', {'image': 'https://static.sandbase.ai/examples/77fb5870-d8ec-471d-9362-7e17dc7dd79f/input/910b60cc-d9f0-498c-9fdc-7f53f426a1f7.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/fidget-collapsible", {
  "image": "https://static.sandbase.ai/examples/77fb5870-d8ec-471d-9362-7e17dc7dd79f/input/910b60cc-d9f0-498c-9fdc-7f53f426a1f7.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/fidget-collapsible", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/77fb5870-d8ec-471d-9362-7e17dc7dd79f/input/910b60cc-d9f0-498c-9fdc-7f53f426a1f7.jpg",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP).  |

## Details

Turns a photo into a print-in-place collapsible fidget toy.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
### Output
- `url`: GLB.
- `stl`: STL for printing.
### Billing
$0.24 per toy.

---
Machine-readable: [`catalog/models/meshy/creative-lab/fidget-collapsible.json`](../../../../catalog/models/meshy/creative-lab/fidget-collapsible.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/fidget-collapsible
