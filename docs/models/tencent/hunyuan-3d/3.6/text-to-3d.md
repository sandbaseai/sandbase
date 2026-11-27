# Hunyuan 3D 3.6 Text to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.6/text-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.525 to $0.675 per run, depending on parameters · **Modes:** async

Hunyuan 3D 3.6 (Hy3D 3.6) is Tencent's newest native 3D generation model. Turn a text prompt into a detailed high-poly 3D model with PBR materials, up to 2,000,000 faces, for games, film and 3D printing.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.face_count`, `params.generate_type`).

| parameters | USD |
|---|---|
| enable_pbr=false, face_count=40000, generate_type="Normal" | 0.525 |
| enable_pbr=false, face_count=40000, generate_type="Geometry" | 0.525 |
| enable_pbr=false, face_count=2000000, generate_type="Normal" | 0.525 |
| enable_pbr=false, face_count=2000000, generate_type="Geometry" | 0.525 |
| enable_pbr=true, face_count=40000, generate_type="Normal" | 0.675 |
| enable_pbr=true, face_count=40000, generate_type="Geometry" | 0.525 |
| enable_pbr=true, face_count=2000000, generate_type="Normal" | 0.675 |
| enable_pbr=true, face_count=2000000, generate_type="Geometry" | 0.525 |

Formula: `0.375 + ((params.enable_pbr ?? false) && (params.generate_type ?? "Normal") != "Geometry" ? 0.15 : 0.0) + ((params.face_count ?? 0) > 0 ? 0.15 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.6/text-to-3d", "prompt": "A carved wooden treasure chest with brass corner guards and an iron lock"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.6/text-to-3d', {'prompt': 'A carved wooden treasure chest with brass corner guards and an iron lock'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.6/text-to-3d", {
  "prompt": "A carved wooden treasure chest with brass corner guards and an iron lock"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.6/text-to-3d", sandbase.Params{
	"prompt": "A carved wooden treasure chest with brass corner guards and an iron lock",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text description of the 3D content to generate. Max 1024 UTF-8 characters.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count, 40,000 to 2,000,000 (custom face count is billed as an add-on). range 40000–2000000 |
| `generate_type` | string |  | Normal: textured model. Geometry: geometry-only white model. one of: `Normal`, `Geometry`; default `"Normal"` |

## Details

Hunyuan 3D 3.6 (Hy3D 3.6) is Tencent's newest native 3D model, released 2026-11-27. It learns geometry, textures and materials directly from 3D assets, with cleaner surfaces, sharper hard-surface structure and higher-quality PBR textures than 3.1. It turns a text prompt into a textured or geometry-only model of up to 2,000,000 faces.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 1,024 characters. |
| `enable_pbr` | boolean | false | PBR materials. |
| `face_count` | integer 40000–2000000 | — | Target face count. |
| `generate_type` | `Normal` / `Geometry` | `Normal` | `Normal` textured or `Geometry` (untextured). |

### Billing

$0.375 per model; PBR, a custom face count, and extra views each add $0.15.

| Request | Price |
|---|---|
| Default | $0.375 |
| With PBR | $0.525 |
| With custom face count | $0.525 |

Failed runs are not charged.

### Also on SandBase
Other Hunyuan 3D endpoints: `tencent/hunyuan-3d/3.6/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.6/text-to-3d.json`](../../../../../catalog/models/tencent/hunyuan-3d/3.6/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.6/text-to-3d
