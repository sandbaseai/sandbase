# Tripo H3.1 Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-h3.1/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.12 to $0.66 per run, depending on parameters · **Modes:** async

Tripo H3.1 is Tripo3D's text-to-3D AI model. Turn written descriptions into textured 3D objects with realistic geometry and materials.

## Pricing

- Depends on parameters (`params.geometry_quality`, `params.pbr`, `params.quad`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| geometry_quality="standard", pbr=false, quad=false, texture=false, texture_quality="standard" | 0.12 |
| geometry_quality="standard", pbr=false, quad=false, texture=false, texture_quality="detailed" | 0.12 |
| geometry_quality="standard", pbr=false, quad=false, texture=true, texture_quality="standard" | 0.24 |
| geometry_quality="standard", pbr=false, quad=false, texture=true, texture_quality="detailed" | 0.36 |
| geometry_quality="standard", pbr=false, quad=true, texture=false, texture_quality="standard" | 0.18 |
| geometry_quality="standard", pbr=false, quad=true, texture=false, texture_quality="detailed" | 0.18 |
| geometry_quality="standard", pbr=false, quad=true, texture=true, texture_quality="standard" | 0.3 |
| geometry_quality="standard", pbr=false, quad=true, texture=true, texture_quality="detailed" | 0.42 |
| geometry_quality="standard", pbr=true, quad=false, texture=false, texture_quality="standard" | 0.24 |
| geometry_quality="standard", pbr=true, quad=false, texture=false, texture_quality="detailed" | 0.36 |
| geometry_quality="standard", pbr=true, quad=false, texture=true, texture_quality="standard" | 0.24 |
| geometry_quality="standard", pbr=true, quad=false, texture=true, texture_quality="detailed" | 0.36 |
| geometry_quality="standard", pbr=true, quad=true, texture=false, texture_quality="standard" | 0.3 |
| geometry_quality="standard", pbr=true, quad=true, texture=false, texture_quality="detailed" | 0.42 |
| geometry_quality="standard", pbr=true, quad=true, texture=true, texture_quality="standard" | 0.3 |
| geometry_quality="standard", pbr=true, quad=true, texture=true, texture_quality="detailed" | 0.42 |
| geometry_quality="detailed", pbr=false, quad=false, texture=false, texture_quality="standard" | 0.36 |
| geometry_quality="detailed", pbr=false, quad=false, texture=false, texture_quality="detailed" | 0.36 |
| geometry_quality="detailed", pbr=false, quad=false, texture=true, texture_quality="standard" | 0.48 |
| geometry_quality="detailed", pbr=false, quad=false, texture=true, texture_quality="detailed" | 0.6 |
| geometry_quality="detailed", pbr=false, quad=true, texture=false, texture_quality="standard" | 0.42 |
| geometry_quality="detailed", pbr=false, quad=true, texture=false, texture_quality="detailed" | 0.42 |
| geometry_quality="detailed", pbr=false, quad=true, texture=true, texture_quality="standard" | 0.54 |
| geometry_quality="detailed", pbr=false, quad=true, texture=true, texture_quality="detailed" | 0.66 |

Formula: `(((params.texture ?? true) || (params.pbr ?? true)) ? ((params.texture_quality ?? "standard") == "detailed" ? 0.36 : 0.24) : 0.12) + ((params.geometry_quality ?? "standard") == "detailed" ? 0.24 : 0.0) + ((params.quad ?? false) ? 0.06 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.1/text-to-3d", "prompt": "A medieval wooden catapult with iron fittings and a stone in the basket"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-h3.1/text-to-3d', {'prompt': 'A medieval wooden catapult with iron fittings and a stone in the basket'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-h3.1/text-to-3d", {
  "prompt": "A medieval wooden catapult with iron fittings and a stone in the basket"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-h3.1/text-to-3d", sandbase.Params{
	"prompt": "A medieval wooden catapult with iron fittings and a stone in the basket",
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
| `prompt` | string | yes | Text description of the 3D object to generate. Maximum 1024 characters.  |
| `texture` | boolean |  | Generate textures. Set both texture and pbr to false for an untextured model. default `true` |
| `face_limit` | integer |  | Target face count. Adaptive when unset. range 1000–2000000 |
| `negative_prompt` | string |  | Features to avoid in the generated model.  |
| `texture_quality` | string |  | standard or detailed (HD) textures. one of: `standard`, `detailed`; default `"standard"` |
| `geometry_quality` | string |  | detailed geometry is billed as an add-on. one of: `standard`, `detailed`; default `"standard"` |

## Details

Tripo H3.1 turns a text prompt into a textured 3D model quickly and at low cost.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 1,024 characters. |
| `pbr` | boolean | true | PBR materials. |
| `quad` | boolean | false | Quad mesh output. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `texture` | boolean | true | Generate textures. |
| `face_limit` | integer 1000–2000000 | — | Maximum face count. |
| `negative_prompt` | string | — | What to avoid. |
| `texture_quality` | `standard` / `detailed` | `standard` | Texture detail; higher costs more. |
| `geometry_quality` | `standard` / `detailed` | `standard` | `detailed` adds mesh detail and cost. |

### Billing

$0.24 per textured model at standard quality, $0.36 detailed, $0.12 untextured; detailed geometry adds $0.24 and quad output $0.06.

| Request | Price |
|---|---|
| Standard texture | $0.24 |
| Detailed texture | $0.36 |
| Untextured | $0.12 |
| Standard + detailed geometry | $0.48 |

Failed runs are not charged.

### Also on SandBase

Other Tripo endpoints: `tripo3d/tripo-p2/text-to-3d`, `tripo3d/tripo-p2/image-to-3d`, `tripo3d/tripo-h3.1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-h3.1/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-h3.1/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-h3.1/text-to-3d
