# Tripo P2 Image to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p2/image-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.2 to $1.56 per run, depending on parameters · **Modes:** async

Tripo P2 is Tripo3D's latest flagship 3D generation model. It reconstructs a production-ready mesh with optional PBR textures from a single image.

## Pricing

- Depends on parameters (`params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| pbr=false, texture=false, texture_quality="fast" | 1.2 |
| pbr=false, texture=false, texture_quality="standard" | 1.2 |
| pbr=false, texture=false, texture_quality="detailed" | 1.2 |
| pbr=false, texture=false, texture_quality="extreme" | 1.2 |
| pbr=false, texture=true, texture_quality="fast" | 1.32 |
| pbr=false, texture=true, texture_quality="standard" | 1.32 |
| pbr=false, texture=true, texture_quality="detailed" | 1.44 |
| pbr=false, texture=true, texture_quality="extreme" | 1.56 |
| pbr=true, texture=false, texture_quality="fast" | 1.32 |
| pbr=true, texture=false, texture_quality="standard" | 1.32 |
| pbr=true, texture=false, texture_quality="detailed" | 1.44 |
| pbr=true, texture=false, texture_quality="extreme" | 1.56 |
| pbr=true, texture=true, texture_quality="fast" | 1.32 |
| pbr=true, texture=true, texture_quality="standard" | 1.32 |
| pbr=true, texture=true, texture_quality="detailed" | 1.44 |
| pbr=true, texture=true, texture_quality="extreme" | 1.56 |

Formula: `((params.texture ?? true) || (params.pbr ?? true)) ? ((params.texture_quality ?? "standard") == "extreme" ? 1.56 : (params.texture_quality ?? "standard") == "detailed" ? 1.44 : 1.32) : 1.20`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p2/image-to-3d", "image": "https://static.sandbase.ai/examples/b9c8f336-1f12-4a85-bb42-8683feabd507/input/09fd0b4f-c9ff-4db9-abca-fd94e1b44049.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p2/image-to-3d', {'image': 'https://static.sandbase.ai/examples/b9c8f336-1f12-4a85-bb42-8683feabd507/input/09fd0b4f-c9ff-4db9-abca-fd94e1b44049.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p2/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/b9c8f336-1f12-4a85-bb42-8683feabd507/input/09fd0b4f-c9ff-4db9-abca-fd94e1b44049.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p2/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/b9c8f336-1f12-4a85-bb42-8683feabd507/input/09fd0b4f-c9ff-4db9-abca-fd94e1b44049.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | Generate PBR materials (also enables texture). default `true` |
| `quad` | boolean |  | Generate quad mesh topology instead of triangles. default `false` |
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `image` | string | yes | Input image URL for 3D model creation.  |
| `texture` | boolean |  | Generate textures. Set both texture and pbr to false for an untextured model. default `true` |
| `face_limit` | integer |  | Maximum faces (quad meshes up to 25,000). range 48–50000 |
| `texture_quality` | string |  | Texture quality tier. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |

## Details

Tripo P2, Tripo's flagship 3D model, turns a single image into a production-ready mesh with optional PBR textures.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Input image URL for 3D model creation. |
| `face_limit` | integer 48–50000 | — | Maximum face count. |
| `pbr` | boolean | true | PBR materials. |
| `quad` | boolean | false | Quad mesh output. |
| `texture` | boolean | true | Generate textures. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | Texture detail; higher costs more. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$1.32 per textured model at standard texture quality, $1.44 detailed, $1.56 extreme; $1.20 untextured.

| Texture | Price |
|---|---|
| standard | $1.32 |
| detailed | $1.44 |
| extreme | $1.56 |
| Untextured | $1.20 |

Failed runs are not charged.

### Also on SandBase

Other Tripo endpoints: `tripo3d/tripo-p2/text-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-h3.1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p2/image-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p2/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p2/image-to-3d
