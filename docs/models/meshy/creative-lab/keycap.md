# Meshy Creative Lab Keycap API: pricing, parameters and code examples

`meshy/creative-lab/keycap` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2.48 per call · **Modes:** async

Turns a photo into a full-color custom mechanical keyboard keycap (Cherry MX 1u by default).

## Pricing

- **$2.48 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/keycap", "image": "https://static.sandbase.ai/examples/6052dcf3-2984-44bb-af04-06a5ba10a3b2/input/da5f1801-1b40-4a13-8c22-ae1e7d913256.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/keycap', {'image': 'https://static.sandbase.ai/examples/6052dcf3-2984-44bb-af04-06a5ba10a3b2/input/da5f1801-1b40-4a13-8c22-ae1e7d913256.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/keycap", {
  "image": "https://static.sandbase.ai/examples/6052dcf3-2984-44bb-af04-06a5ba10a3b2/input/da5f1801-1b40-4a13-8c22-ae1e7d913256.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/keycap", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/6052dcf3-2984-44bb-af04-06a5ba10a3b2/input/da5f1801-1b40-4a13-8c22-ae1e7d913256.jpg",
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

Turns a photo into a full-color custom mechanical keyboard keycap (Cherry MX 1u by default).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
### Output
- `url`: Keycap GLB.
- `obj_zip`: OBJ package.
- `concept_image`: Design image.
### Billing
$2.48 per keycap (design + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/keycap.json`](../../../../catalog/models/meshy/creative-lab/keycap.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/keycap
