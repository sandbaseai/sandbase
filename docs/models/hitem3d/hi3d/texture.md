# Hitem3D Hi3D Texture API: pricing, parameters and code examples

`hitem3d/hi3d/texture` · image generation model · Hitem3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 per call · **Modes:** async

Hi3D Texture by Hitem3D adds textures to an untextured GLB model using a reference image. It uses the v1.5 texture models.

## Pricing

- **$0.2 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/texture", "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb", "image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hitem3d/hi3d/texture', {'model_url': 'https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb', 'image': 'https://storage.googleapis.com/falserverless/example_inputs/dog.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hitem3d/hi3d/texture", {
  "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
  "image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hitem3d/hi3d/texture", sandbase.Params{
	"model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
	"image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Reference image URL used to texture the model. PNG, JPEG and WebP, up to 20MB.  |
| `version` | string |  | Texture model version. one of: `hitem3dv1.5`, `scene-portraitv1.5`; default `"hitem3dv1.5"` |
| `model_url` | string | yes | URL of the GLB geometry model to texture (e.g. Hi3D image-to-3d output with texture off).  |
| `resolution` | string |  | Texture resolution. hitem3dv1.5 accepts 512, 1024, 1536, 1536pro; scene-portraitv1.5 accepts 1536. Uses the model's recommended value when unset. one of: `512`, `1024`, `1536`, `1536pro` |
| `export_format` | string |  | File format of the generated model. one of: `glb`, `obj`, `stl`, `fbx`, `usdz`; default `"glb"` |

## Details

Hi3D Texture by Hitem3D adds textures to an untextured GLB model using a reference image. It uses the v1.5 texture models.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the GLB geometry model to texture (e.g. Hi3D image-to-3d output with texture off). |
| `image` | image URL, required | — | Reference image URL used to texture the model. PNG, JPEG and WebP, up to 20MB. |
| `version` | `hitem3dv1.5` / `scene-portraitv1.5` | `hitem3dv1.5` | Texture model version. |
| `resolution` | `512` / `1024` / `1536` / `1536pro` | — | Texture resolution. hitem3dv1.5 accepts 512, 1024, 1536, 1536pro; scene-portraitv1.5 accepts 1536. Uses the model's recommended value when unset. |
| `export_format` | `glb` / `obj` / `stl` / `fbx` / `usdz` | `glb` | File format of the generated model. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.20 per request.
Failed runs are not charged.
### Also on SandBase
Other Hitem3D 3D endpoints: `hitem3d/hi3d/image-to-3d`, `hitem3d/hi3d/multi-view-to-3d`, `hitem3d/hi3d/multicolor`, `hitem3d/hi3d/split`.

---
Machine-readable: [`catalog/models/hitem3d/hi3d/texture.json`](../../../../catalog/models/hitem3d/hi3d/texture.json) · Store page: https://www.sandbase.ai/model/hitem3d/hi3d/texture
