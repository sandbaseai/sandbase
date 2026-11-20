# Meshy Resize API: pricing, parameters and code examples

`meshy/resize` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.04 per call · **Modes:** async

Meshy Resize scales an existing 3D model to a real-world height or longest side, or estimates the size automatically.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/resize", "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/resize', {'model_url': 'https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/resize", {
  "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/resize", sandbase.Params{
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
| `auto_size` | boolean |  | Estimate the object's real-world size and scale the model to it. default `false` |
| `model_url` | string | yes | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI.  |
| `origin_at` | string |  | Where to place the model origin. one of: `bottom`, `center`; default `"bottom"` |
| `resize_height` | number |  | Target height in meters. Send exactly one of resize_height, resize_longest_side or auto_size. range 0– |
| `resize_longest_side` | number |  | Target length of the longest side in meters. range 0– |

## Details

Meshy Resize scales an existing 3D model to a real-world height or longest side, or estimates the size automatically.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `resize_height` | number 0– | — | Target height in meters. Send exactly one of resize_height, resize_longest_side or auto_size. |
| `resize_longest_side` | number 0– | — | Target length of the longest side in meters. |
| `auto_size` | boolean | `false` | Estimate the object's real-world size and scale the model to it. |
| `origin_at` | `bottom` / `center` | `"bottom"` | Where to place the model origin. |
### Output
- `url`: Resized GLB.
### Billing
$0.04 per model.

---
Machine-readable: [`catalog/models/meshy/resize.json`](../../../catalog/models/meshy/resize.json) · Store page: https://www.sandbase.ai/model/meshy/resize
