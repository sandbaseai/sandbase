# Rodin 2.5 Text to 3D

`hyper3d/rodin/2.5/text-to-3d` · image · hyper3d

Rodin Gen-2.5 by Hyper3D (Deemos) generates game- and production-ready 3D assets from a text prompt.

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
  -d '{"model": "hyper3d/rodin/2.5/text-to-3d", "prompt": "<prompt>"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hyper3d/rodin/2.5/text-to-3d', {'prompt': '<prompt>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hyper3d/rodin/2.5/text-to-3d", {
  "prompt": "<prompt>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hyper3d/rodin/2.5/text-to-3d", sandbase.Params{
	"prompt": "<prompt>",
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
| `prompt` | string | yes | A textual prompt to guide model generation. Required for Text-to-3D mode.  |
| `material` | string |  | PBR, Shaded, All (both) or None. one of: `PBR`, `Shaded`, `All`, `None`; default `"All"` |
| `hd_texture` | boolean |  | Enhanced texture post-processing. default `false` |
| `quality_mesh_option` | string |  | Combined quality and mesh type selection. Quad = smooth surfaces, Triangle = detailed geometry. Maps to `mesh_mode` (Quad/Raw) and `quality_override` (face count) on the Hyper3D API. Valid face counts depend on the… one of: `Auto`, `4K Quad`, `8K Quad`, `18K Quad`, `50K Quad`, `100K Quad`, `200K Quad`, `2K Triangle`, `20K Triangle`, `50K Triangle`, `150K Triangle`, `500K Triangle` …; default `"Auto"` |
| `geometry_file_format` | string |  | Output file format. one of: `glb`, `usdz`, `fbx`, `obj`, `stl`; default `"glb"` |

## Details

Rodin Gen-2.5 by Hyper3D turns a text prompt into a production-ready 3D asset with PBR materials and quad or triangle meshes.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 1,024 characters. |
| `seed` | integer 0–65535 | random | Fix it to compare prompt changes. |
| `quality_mesh_option` | `Auto` / `4K Quad` / `8K Quad` / `18K Quad` / `50K Quad` / `100K Quad` / `200K Quad` / `2K Triangle` / `20K Triangle` / `50K Triangle` / `150K Triangle` / `500K Triangle` / `1M Triangle` / `2M Triangle` | `Auto` | Mesh density and topology. |
| `material` | `PBR` / `Shaded` / `All` / `None` | `All` | Material output. |
| `hd_texture` | boolean | false | Higher-resolution textures. |
| `geometry_file_format` | `glb` / `usdz` / `fbx` / `obj` / `stl` | `glb` | Output file format. |
| `TAPose` | boolean | false | Force a T/A-pose for characters. |
| `addons` | `HighPack` | — | `HighPack` adds high-resolution textures and denser meshes. |
| `tier` | `Gen-2.5-Minimum` / `Gen-2.5-Extreme-Low` / `Gen-2.5-Low` / `Gen-2.5-Medium` / `Gen-2.5-High` / `Gen-2.5-Extreme-High` | `Gen-2.5-High` | Quality tier. |

### Billing

$0.48 per model ($0.96 on the Extreme-High tier), plus $0.96 for the HighPack add-on.

| Request | Price |
|---|---|
| Default tier | $0.48 |
| Extreme-High tier | $0.96 |
| Default + HighPack | $1.44 |

Failed runs are not charged.

### Prompting

- Describe one object: shape, materials, and style.

### Also on SandBase

Other Rodin endpoints: `hyper3d/rodin/2.5/image-to-3d`, `hyper3d/rodin/2.5/fast/text-to-3d`, `hyper3d/rodin/2.5/fast/image-to-3d`.

---
Machine-readable: [`catalog/models/hyper3d/rodin/2.5/text-to-3d.json`](../../../../../catalog/models/hyper3d/rodin/2.5/text-to-3d.json) · Store page: https://www.sandbase.ai/model/hyper3d/rodin/2.5/text-to-3d
