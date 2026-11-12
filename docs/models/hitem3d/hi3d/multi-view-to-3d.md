# Hitem3D Hi3D Multi-view to 3D API: pricing, parameters and code examples

`hitem3d/hi3d/multi-view-to-3d` · image generation model · Hitem3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.4 to $0.9 per run, depending on parameters · **Modes:** async

Hi3D by Hitem3D generates a 3D model from a front view plus optional back, left and right views, with a selectable model version and resolution tier.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.enable_texture`, `params.resolution`, `params.version`).

| parameters | USD |
|---|---|
| defaults | 0.9 |
| enable_pbr=false | 0.8 |
| enable_pbr=true | 0.9 |
| enable_texture=false | 0.6 |
| enable_texture=true | 0.9 |
| resolution="512" | 0.4 |
| resolution="1024" | 0.5 |
| resolution="1536" | 0.7 |
| resolution="1536pro" | 0.9 |
| resolution="1536fast" | 0.5 |
| resolution="1536profast" | 0.5 |
| version="hitem3dv1.5" | 0.8 |
| version="hitem3dv2.0" | 0.9 |
| version="hitem3dv2.1" | 0.9 |
| version="scene-portraitv1.5" | 0.6 |
| version="scene-portraitv2.0" | 0.9 |
| version="scene-portraitv2.1" | 0.9 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/multi-view-to-3d", "back_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/b28c0fdd-62e3-45d9-bf28-3cc8ab70353c.png", "image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/8e4047f8-9f6e-408d-bbc9-5fb3ce7c6b37.png", "left_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/f02bbf57-4e98-4756-afdd-c268dce95b6f.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hitem3d/hi3d/multi-view-to-3d', {'back_image': 'https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/b28c0fdd-62e3-45d9-bf28-3cc8ab70353c.png', 'image': 'https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/8e4047f8-9f6e-408d-bbc9-5fb3ce7c6b37.png', 'left_image': 'https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/f02bbf57-4e98-4756-afdd-c268dce95b6f.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hitem3d/hi3d/multi-view-to-3d", {
  "back_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/b28c0fdd-62e3-45d9-bf28-3cc8ab70353c.png",
  "image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/8e4047f8-9f6e-408d-bbc9-5fb3ce7c6b37.png",
  "left_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/f02bbf57-4e98-4756-afdd-c268dce95b6f.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hitem3d/hi3d/multi-view-to-3d", sandbase.Params{
	"back_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/b28c0fdd-62e3-45d9-bf28-3cc8ab70353c.png",
	"image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/8e4047f8-9f6e-408d-bbc9-5fb3ce7c6b37.png",
	"left_image": "https://static.sandbase.ai/examples/4492f098-3e35-40bc-b740-fab751711044/input/f02bbf57-4e98-4756-afdd-c268dce95b6f.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image URL (PNG/JPEG/WebP, up to 20MB).  |
| `version` | string |  | Model version. hitem3d* are general models; scene-portrait* are tuned for portraits and characters. one of: `hitem3dv1.5`, `hitem3dv2.0`, `hitem3dv2.1`, `scene-portraitv1.5`, `scene-portraitv2.0`, `scene-portraitv2.1`; default `"hitem3dv2.1"` |
| `back_image` | string |  | Optional back view image URL.  |
| `enable_pbr` | boolean |  | Generate PBR material maps with the texture (v2.0 and above; billed add-on). default `true` |
| `face_count` | integer |  | Target face count. Uses the recommended count for the resolution when unset. range 100000–2000000 |
| `left_image` | string |  | Optional left view image URL.  |
| `resolution` | string |  | Generation resolution; supported values depend on the model: v1.5/v2.0 accept 512, 1024, 1536, 1536pro; v2.1 accepts 1536fast, 1536pro; scene-portraitv1.5 accepts 1536; scene-portraitv2.0 accepts 1536pro;… one of: `512`, `1024`, `1536`, `1536pro`, `1536fast`, `1536profast` |
| `right_image` | string |  | Optional right view image URL.  |
| `export_format` | string |  | File format of the generated model. one of: `glb`, `obj`, `stl`, `fbx`, `usdz`; default `"glb"` |
| `enable_texture` | boolean |  | Generate textures in addition to geometry. When false, only the geometry mesh is generated (cheaper). default `true` |

## Details

Hi3D by Hitem3D generates a 3D model from a front view plus optional back, left and right views, with a selectable model version and resolution tier.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view image URL (PNG/JPEG/WebP, up to 20MB). |
| `back_image` | image URL | — | Optional back view image URL. |
| `left_image` | image URL | — | Optional left view image URL. |
| `right_image` | image URL | — | Optional right view image URL. |
| `version` | `hitem3dv1.5` / `hitem3dv2.0` / `hitem3dv2.1` / `scene-portraitv1.5` / `scene-portraitv2.0` / `scene-portraitv2.1` | `hitem3dv2.1` | Model version. hitem3d* are general models; scene-portrait* are tuned for portraits and characters. |
| `resolution` | `512` / `1024` / `1536` / `1536pro` / `1536fast` / `1536profast` | — | Generation resolution; supported values depend on the model: v1.5/v2.0 accept 512, 1024, 1536, 1536pro; v2.1 accepts 1536fast, 1536pro; scene-portraitv1.5 accepts 1536; scene-portraitv2.0 accepts 1536pro; scene-portraitv2.1 accepts 1536profast, 1536pro. Uses the model's recommended value when unset. |
| `enable_texture` | boolean | `true` | Generate textures in addition to geometry. When false, only the geometry mesh is generated (cheaper). |
| `enable_pbr` | boolean | `true` | Generate PBR material maps with the texture (v2.0 and above; billed add-on). |
| `face_count` | integer 100000–2000000 | — | Target face count. Uses the recommended count for the resolution when unset. |
| `export_format` | `glb` / `obj` / `stl` / `fbx` / `usdz` | `glb` | File format of the generated model. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.90 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_pbr on | $0.90 |
| enable_pbr off | $0.80 |
| enable_texture on | $0.90 |
| enable_texture off | $0.60 |
| resolution unset | $0.90 |
| resolution = 512 | $0.40 |
| resolution = 1024 | $0.50 |
| resolution = 1536 | $0.70 |
| resolution = 1536pro | $0.90 |
| resolution = 1536fast | $0.50 |
| resolution = 1536profast | $0.50 |
| version = hitem3dv1.5 | $0.80 |
| version = hitem3dv2.0 | $0.90 |
| version = hitem3dv2.1 | $0.90 |
| version = scene-portraitv1.5 | $0.60 |
| version = scene-portraitv2.0 | $0.90 |
| version = scene-portraitv2.1 | $0.90 |
Failed runs are not charged.
### Also on SandBase
Other Hitem3D 3D endpoints: `hitem3d/hi3d/image-to-3d`, `hitem3d/hi3d/multicolor`, `hitem3d/hi3d/split`, `hitem3d/hi3d/texture`.

---
Machine-readable: [`catalog/models/hitem3d/hi3d/multi-view-to-3d.json`](../../../../catalog/models/hitem3d/hi3d/multi-view-to-3d.json) · Store page: https://www.sandbase.ai/model/hitem3d/hi3d/multi-view-to-3d
