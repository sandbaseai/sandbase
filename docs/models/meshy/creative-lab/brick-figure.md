# Meshy Creative Lab Brick Figure API: pricing, parameters and code examples

`meshy/creative-lab/brick-figure` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.44 per call · **Modes:** async

Turns a photo into a textured brick-style minifigure.

## Pricing

- **$1.44 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/brick-figure", "image": "https://static.sandbase.ai/examples/98b0c36a-6be0-4c60-bd21-ebb66459cb92/input/e3584c72-ca99-4217-9dc7-ca77b302e8c1.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/brick-figure', {'image': 'https://static.sandbase.ai/examples/98b0c36a-6be0-4c60-bd21-ebb66459cb92/input/e3584c72-ca99-4217-9dc7-ca77b302e8c1.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/brick-figure", {
  "image": "https://static.sandbase.ai/examples/98b0c36a-6be0-4c60-bd21-ebb66459cb92/input/e3584c72-ca99-4217-9dc7-ca77b302e8c1.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/brick-figure", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/98b0c36a-6be0-4c60-bd21-ebb66459cb92/input/e3584c72-ca99-4217-9dc7-ca77b302e8c1.jpg",
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

Turns a photo into a textured brick-style minifigure.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
### Output
- `url`: Textured GLB.
- `thumbnail`: Preview image.
- `concept_image`: Concept image.
### Billing
$1.44 per object (concept image + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/brick-figure.json`](../../../../catalog/models/meshy/creative-lab/brick-figure.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/brick-figure
