# Meshy Convert API: pricing, parameters and code examples

`meshy/convert` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.04 per call · **Modes:** async

Meshy Convert exports an existing 3D model to GLB, OBJ, FBX, STL, USDZ, BLEND or 3MF.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/convert", "format": "glb", "model_url": "https://static.sandbase.ai/examples/a371e5e4-7b44-4d5a-8811-528602691cf2/input/bcc4daf1-e924-42c6-99a9-2154a14aa1ab.fbx"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/convert', {'format': 'glb', 'model_url': 'https://static.sandbase.ai/examples/a371e5e4-7b44-4d5a-8811-528602691cf2/input/bcc4daf1-e924-42c6-99a9-2154a14aa1ab.fbx'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/convert", {
  "format": "glb",
  "model_url": "https://static.sandbase.ai/examples/a371e5e4-7b44-4d5a-8811-528602691cf2/input/bcc4daf1-e924-42c6-99a9-2154a14aa1ab.fbx"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/convert", sandbase.Params{
	"format": "glb",
	"model_url": "https://static.sandbase.ai/examples/a371e5e4-7b44-4d5a-8811-528602691cf2/input/bcc4daf1-e924-42c6-99a9-2154a14aa1ab.fbx",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `format` | string |  | Output file format. one of: `glb`, `obj`, `fbx`, `stl`, `usdz`, `blend`, `3mf`; default `"fbx"` |
| `model_url` | string | yes | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI.  |

## Details

Meshy Convert exports an existing 3D model to GLB, OBJ, FBX, STL, USDZ, BLEND or 3MF.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `format` | `glb` / `obj` / `fbx` / `stl` / `usdz` / `blend` / `3mf` | `"fbx"` | Output file format. |
### Output
- `url`: The converted model file.
### Billing
$0.04 per conversion.

---
Machine-readable: [`catalog/models/meshy/convert.json`](../../../catalog/models/meshy/convert.json) · Store page: https://www.sandbase.ai/model/meshy/convert
