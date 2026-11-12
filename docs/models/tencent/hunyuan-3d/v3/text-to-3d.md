# Hunyuan 3D 3.0 Text to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/v3/text-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.45 to $0.9 per run, depending on parameters · **Modes:** async

Hunyuan 3D 3.0 by Tencent generates a textured, low-poly, or geometry-only 3D model from a text prompt.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.generate_type`).

| parameters | USD |
|---|---|
| enable_pbr=false, generate_type="Normal" | 0.63 |
| enable_pbr=false, generate_type="LowPoly" | 0.72 |
| enable_pbr=false, generate_type="Geometry" | 0.45 |
| enable_pbr=true, generate_type="Normal" | 0.81 |
| enable_pbr=true, generate_type="LowPoly" | 0.9 |
| enable_pbr=true, generate_type="Geometry" | 0.63 |

Formula: `((params.generate_type ?? "Normal") == "LowPoly" ? 0.72 : (params.generate_type ?? "Normal") == "Geometry" ? 0.45 : 0.63) + ((params.enable_pbr ?? false) ? 0.18 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/v3/text-to-3d", "prompt": "A vintage red rotary telephone with a coiled cord"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/v3/text-to-3d', {'prompt': 'A vintage red rotary telephone with a coiled cord'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/v3/text-to-3d", {
  "prompt": "A vintage red rotary telephone with a coiled cord"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/v3/text-to-3d", sandbase.Params{
	"prompt": "A vintage red rotary telephone with a coiled cord",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text description of the 3D object to generate. Up to 1024 characters.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal maps). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count (40,000-1,500,000). Leave empty for the default of 500,000. range 40000–1500000 |
| `polygon_type` | string |  | Polygon type. Only takes effect when Generate Type is LowPoly. one of: `triangle`, `quadrilateral`; default `"triangle"` |
| `generate_type` | string |  | Normal: textured model. LowPoly: polygon reduction. Geometry: white model without texture. one of: `Normal`, `LowPoly`, `Geometry`; default `"Normal"` |

## Details

Hunyuan 3D 3.0 by Tencent generates a textured, low-poly, or geometry-only 3D model from a text prompt.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. Up to 1024 characters. |
| `generate_type` | `Normal` / `LowPoly` / `Geometry` | `Normal` | Normal: textured model. LowPoly: polygon reduction. Geometry: white model without texture. |
| `enable_pbr` | boolean | `false` | Generate PBR materials (metallic, roughness, normal maps). Ignored for Geometry output. |
| `face_count` | integer 40000–1500000 | — | Target polygon face count (40,000-1,500,000). Leave empty for the default of 500,000. |
| `polygon_type` | `triangle` / `quadrilateral` | `triangle` | Polygon type. Only takes effect when Generate Type is LowPoly. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.63 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_pbr on | $0.81 |
| enable_pbr off | $0.63 |
| generate_type = Normal | $0.63 |
| generate_type = LowPoly | $0.72 |
| generate_type = Geometry | $0.45 |
Failed runs are not charged.
### Also on SandBase
Other Tencent 3D endpoints: `tencent/hunyuan-3d/3.0/image-to-3d`, `tencent/hunyuan-3d/3.1/part`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/v3/text-to-3d.json`](../../../../../catalog/models/tencent/hunyuan-3d/v3/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/v3/text-to-3d
