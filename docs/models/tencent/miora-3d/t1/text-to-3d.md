# Miora 3D T1 Text to 3D API: pricing, parameters and code examples

`tencent/miora-3d/t1/text-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.514286 to $0.685714 per run, depending on parameters · **Modes:** async

Miora 3D T1 by Tencent Design is the fast Miora 3D model: it turns a text prompt into a textured or untextured 3D asset in about two minutes.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.face_count`, `params.generate_type`).

| parameters | USD |
|---|---|
| enable_pbr=false, face_count=3000, generate_type="Normal" | 0.514286 |
| enable_pbr=false, face_count=3000, generate_type="Geometry" | 0.514286 |
| enable_pbr=false, face_count=1500000, generate_type="Normal" | 0.514286 |
| enable_pbr=false, face_count=1500000, generate_type="Geometry" | 0.514286 |
| enable_pbr=true, face_count=3000, generate_type="Normal" | 0.685714 |
| enable_pbr=true, face_count=3000, generate_type="Geometry" | 0.514286 |
| enable_pbr=true, face_count=1500000, generate_type="Normal" | 0.685714 |
| enable_pbr=true, face_count=1500000, generate_type="Geometry" | 0.514286 |

Formula: `(15 + ((params.enable_pbr ?? false) && (params.generate_type ?? "Normal") != "Geometry" ? 10 : 0) + ((params.face_count ?? 0) > 0 ? 10 : 0) + 5) * 0.12 / 7`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/miora-3d/t1/text-to-3d", "prompt": "A medieval wooden catapult with iron fittings and a stone in the basket"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/miora-3d/t1/text-to-3d', {'prompt': 'A medieval wooden catapult with iron fittings and a stone in the basket'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/miora-3d/t1/text-to-3d", {
  "prompt": "A medieval wooden catapult with iron fittings and a stone in the basket"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/miora-3d/t1/text-to-3d", sandbase.Params{
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
| `prompt` | string | yes | Text description of the 3D object to generate.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count. Uses the model default when unset. range 3000–1500000 |
| `generate_type` | string |  | Normal: textured model. Geometry: untextured white model. one of: `Normal`, `Geometry`; default `"Normal"` |

## Details

Miora 3D T1 by Tencent Design is the fast Miora 3D model: it turns a text prompt into a textured or untextured 3D asset in about two minutes.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. |
| `generate_type` | string | "Normal" | Normal: textured model. Geometry: untextured white model. |
| `enable_pbr` | boolean | false | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. |
| `face_count` | integer | — | Target polygon face count. Uses the model default when unset. |

### Billing

| Request | Price |
|---|---|
| Default | $0.3429 |
| Geometry (untextured) | $0.3429 |
| With PBR | $0.5143 |
| With custom face count | $0.5143 |

PBR, a custom face count each add to the default price. Failed runs are not charged.

---
Machine-readable: [`catalog/models/tencent/miora-3d/t1/text-to-3d.json`](../../../../../catalog/models/tencent/miora-3d/t1/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/miora-3d/t1/text-to-3d
