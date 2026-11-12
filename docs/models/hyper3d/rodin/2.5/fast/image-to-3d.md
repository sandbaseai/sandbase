# Rodin 2.5 Fast Image to 3D API: pricing, parameters and code examples

`hyper3d/rodin/2.5/fast/image-to-3d` · image generation model · hyper3d · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 per call · **Modes:** async

Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from one to five reference images, tuned for speed with the low tiers.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hyper3d/rodin/2.5/fast/image-to-3d", "images": ["https://static.sandbase.ai/examples/02943260-0e07-4cf1-bd63-e29d9dba4dde/input/6d5e76b7-018e-4da5-ad71-c9d354739c21.png"]}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hyper3d/rodin/2.5/fast/image-to-3d', {'images': ['https://static.sandbase.ai/examples/02943260-0e07-4cf1-bd63-e29d9dba4dde/input/6d5e76b7-018e-4da5-ad71-c9d354739c21.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hyper3d/rodin/2.5/fast/image-to-3d", {
  "images": [
    "https://static.sandbase.ai/examples/02943260-0e07-4cf1-bd63-e29d9dba4dde/input/6d5e76b7-018e-4da5-ad71-c9d354739c21.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hyper3d/rodin/2.5/fast/image-to-3d", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/02943260-0e07-4cf1-bd63-e29d9dba4dde/input/6d5e76b7-018e-4da5-ad71-c9d354739c21.png"},
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
| `tier` | string |  | Generation tier (quality / speed). one of: `Gen-2.5-Minimum`, `Gen-2.5-Extreme-Low`, `Gen-2.5-Low`; default `"Gen-2.5-Extreme-Low"` |
| `TAPose` | boolean |  | Generate characters in T-pose or A-pose for rigging. default `false` |
| `images` | array | yes | 1 to 5 images of the object.  |
| `prompt` | string |  | Optional text prompt to guide generation.  |
| `material` | string |  | PBR, Shaded, All (both) or None. one of: `PBR`, `Shaded`, `All`, `None`; default `"Shaded"` |
| `hd_texture` | boolean |  | Enhanced texture post-processing. default `false` |
| `quality_mesh_option` | string |  | Combined quality and mesh type selection. Quad = smooth surfaces, Triangle = detailed geometry. Maps to `mesh_mode` (Quad/Raw) and `quality_override` (face count) on the Hyper3D API. Valid face counts depend on the… one of: `Auto`, `1K Quad`, `4K Quad`, `8K Quad`, `18K Quad`, `20K Quad`, `2K Triangle`, `4K Triangle`, `8K Triangle`, `10K Triangle`, `20K Triangle`; default `"Auto"` |
| `geometry_file_format` | string |  | Output file format. one of: `glb`, `usdz`, `fbx`, `obj`, `stl`; default `"glb"` |

## Details

Rodin Gen-2.5 Fast by Hyper3D turns an image set of 1–5 views into a game-ready 3D asset, using the low tiers for speed.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Up to 1,024 characters. |
| `images` | image URL[] (≤5), required | — | 1–5 reference images of the object. |
| `material` | `PBR` / `Shaded` / `All` / `None` | `Shaded` | Material output. |
| `TAPose` | boolean | false | Force a T/A-pose for characters. |
| `hd_texture` | boolean | false | Higher-resolution textures. |
| `tier` | `Gen-2.5-Minimum` / `Gen-2.5-Extreme-Low` / `Gen-2.5-Low` | `Gen-2.5-Extreme-Low` | Quality tier. |
| `geometry_file_format` | `glb` / `usdz` / `fbx` / `obj` / `stl` | `glb` | Output file format. |
| `quality_mesh_option` | `Auto` / `1K Quad` / `4K Quad` / `8K Quad` / `18K Quad` / `20K Quad` / `2K Triangle` / `4K Triangle` / `8K Triangle` / `10K Triangle` / `20K Triangle` | `Auto` | Mesh density and topology. |
| `seed` | integer 0–65535 | random | Fix it to compare prompt changes. |

### Billing

$0.10 per model.

| Request | Price |
|---|---|
| One model | $0.10 |

Failed runs are not charged.

### Also on SandBase

Other Rodin endpoints: `hyper3d/rodin/2.5/text-to-3d`, `hyper3d/rodin/2.5/image-to-3d`, `hyper3d/rodin/2.5/fast/text-to-3d`.

---
Machine-readable: [`catalog/models/hyper3d/rodin/2.5/fast/image-to-3d.json`](../../../../../../catalog/models/hyper3d/rodin/2.5/fast/image-to-3d.json) · Store page: https://www.sandbase.ai/model/hyper3d/rodin/2.5/fast/image-to-3d
