# Rodin 2.5 Image to 3D API: pricing, parameters and code examples

`hyper3d/rodin/2.5/image-to-3d` · image generation model · hyper3d · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.44 to $1.92 per run, depending on parameters · **Modes:** async

Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from one to five reference images.

## Pricing

- Depends on parameters (`params.addons`, `params.tier`).

| parameters | USD |
|---|---|
| addons="HighPack", tier="Gen-2.5-Minimum" | 1.44 |
| addons="HighPack", tier="Gen-2.5-Extreme-Low" | 1.44 |
| addons="HighPack", tier="Gen-2.5-Low" | 1.44 |
| addons="HighPack", tier="Gen-2.5-Medium" | 1.44 |
| addons="HighPack", tier="Gen-2.5-High" | 1.44 |
| addons="HighPack", tier="Gen-2.5-Extreme-High" | 1.92 |

Formula: `((params.tier ?? "Gen-2.5-High") == "Gen-2.5-Extreme-High" ? 0.96 : 0.48) + ((params.addons ?? "") == "HighPack" ? 0.96 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hyper3d/rodin/2.5/image-to-3d", "images": ["<images>"]}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hyper3d/rodin/2.5/image-to-3d', {'images': ['<images>']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hyper3d/rodin/2.5/image-to-3d", {
  "images": [
    "<images>"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hyper3d/rodin/2.5/image-to-3d", sandbase.Params{
	"images": []any{"<images>"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed (0–65535). range 0–65535 |
| `tier` | string |  | Generation tier (quality / speed). one of: `Gen-2.5-Minimum`, `Gen-2.5-Extreme-Low`, `Gen-2.5-Low`, `Gen-2.5-Medium`, `Gen-2.5-High`, `Gen-2.5-Extreme-High`; default `"Gen-2.5-High"` |
| `TAPose` | boolean |  | Generate characters in T-pose or A-pose for rigging. default `false` |
| `addons` | string |  | Optional add-on. HighPack (4K textures, high-poly) is billed +$0.80. one of: `HighPack` |
| `images` | array | yes | 1 to 5 images of the object.  |
| `prompt` | string |  | Optional text prompt to guide generation.  |
| `material` | string |  | PBR, Shaded, All (both) or None. one of: `PBR`, `Shaded`, `All`, `None`; default `"All"` |
| `hd_texture` | boolean |  | Enhanced texture post-processing. default `false` |
| `quality_mesh_option` | string |  | Combined quality and mesh type selection. Quad = smooth surfaces, Triangle = detailed geometry. Maps to `mesh_mode` (Quad/Raw) and `quality_override` (face count) on the Hyper3D API. Valid face counts depend on the… one of: `Auto`, `4K Quad`, `8K Quad`, `18K Quad`, `50K Quad`, `100K Quad`, `200K Quad`, `2K Triangle`, `20K Triangle`, `50K Triangle`, `150K Triangle`, `500K Triangle` …; default `"Auto"` |
| `geometry_file_format` | string |  | Output file format. one of: `glb`, `usdz`, `fbx`, `obj`, `stl`; default `"glb"` |

## Details

Rodin Gen-2.5 by Hyper3D turns an image set of 1–5 views into a production-ready 3D asset with PBR materials and quad or triangle meshes.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Up to 1,024 characters. |
| `images` | image URL[] (≤5), required | — | 1–5 reference images of the object. |
| `geometry_file_format` | `glb` / `usdz` / `fbx` / `obj` / `stl` | `glb` | Output file format. |
| `quality_mesh_option` | `Auto` / `4K Quad` / `8K Quad` / `18K Quad` / `50K Quad` / `100K Quad` / `200K Quad` / `2K Triangle` / `20K Triangle` / `50K Triangle` / `150K Triangle` / `500K Triangle` / `1M Triangle` / `2M Triangle` | `Auto` | Mesh density and topology. |
| `addons` | `HighPack` | — | `HighPack` adds high-resolution textures and denser meshes. |
| `TAPose` | boolean | false | Force a T/A-pose for characters. |
| `hd_texture` | boolean | false | Higher-resolution textures. |
| `tier` | `Gen-2.5-Minimum` / `Gen-2.5-Extreme-Low` / `Gen-2.5-Low` / `Gen-2.5-Medium` / `Gen-2.5-High` / `Gen-2.5-Extreme-High` | `Gen-2.5-High` | Quality tier. |
| `material` | `PBR` / `Shaded` / `All` / `None` | `All` | Material output. |
| `seed` | integer 0–65535 | random | Fix it to compare prompt changes. |

### Billing

$0.48 per model ($0.96 on the Extreme-High tier), plus $0.96 for the HighPack add-on.

| Request | Price |
|---|---|
| Default tier | $0.48 |
| Extreme-High tier | $0.96 |
| Default + HighPack | $1.44 |

Failed runs are not charged.

### Prompting

- Use clean, evenly lit views on a plain background.

### Also on SandBase

Other Rodin endpoints: `hyper3d/rodin/2.5/text-to-3d`, `hyper3d/rodin/2.5/fast/text-to-3d`, `hyper3d/rodin/2.5/fast/image-to-3d`.

---
Machine-readable: [`catalog/models/hyper3d/rodin/2.5/image-to-3d.json`](../../../../../catalog/models/hyper3d/rodin/2.5/image-to-3d.json) · Store page: https://www.sandbase.ai/model/hyper3d/rodin/2.5/image-to-3d
