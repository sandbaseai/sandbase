# Meshy Remesh API: pricing, parameters and code examples

`meshy/remesh` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 per call · **Modes:** async

Meshy Remesh rebuilds an existing 3D model at a target face count, as triangles or quads.

## Pricing

- **$0.2 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/remesh", "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/remesh', {'model_url': 'https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/remesh", {
  "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/remesh", sandbase.Params{
	"model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `topology` | string |  | Output face type. one of: `triangle`, `quad`; default `"triangle"` |
| `auto_size` | boolean |  | Estimate the object's real-world size and scale the model to it. default `false` |
| `model_url` | string | yes | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI.  |
| `origin_at` | string |  | Where to place the model origin. one of: `bottom`, `center` |
| `target_polycount` | integer |  | Target number of faces; the result can differ. default `30000`; range 100–300000 |

## Details

Meshy Remesh rebuilds an existing 3D model at a target face count, as triangles or quads.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `topology` | `triangle` / `quad` | `"triangle"` | Output face type. |
| `target_polycount` | integer 100–300000 | `30000` | Target number of faces; the result can differ. |
| `auto_size` | boolean | `false` | Estimate the object's real-world size and scale the model to it. |
| `origin_at` | `bottom` / `center` | — | Where to place the model origin. |
### Output
- `url`: Remeshed GLB.
- `thumbnail`: Preview image.
### Billing
$0.20 per model.

---
Machine-readable: [`catalog/models/meshy/remesh.json`](../../../catalog/models/meshy/remesh.json) · Store page: https://www.sandbase.ai/model/meshy/remesh
