# Miora 3D T1 Image to 3D API: pricing, parameters and code examples

`tencent/miora-3d/t1/image-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.428571 to $0.6 per run, depending on parameters · **Modes:** async

Miora 3D T1 by Tencent Design is the fast Miora 3D model: it turns a single image into a textured or untextured 3D asset in about two minutes.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.face_count`, `params.generate_type`).

| parameters | USD |
|---|---|
| enable_pbr=false, face_count=3000, generate_type="Normal" | 0.428571 |
| enable_pbr=false, face_count=3000, generate_type="Geometry" | 0.428571 |
| enable_pbr=false, face_count=1500000, generate_type="Normal" | 0.428571 |
| enable_pbr=false, face_count=1500000, generate_type="Geometry" | 0.428571 |
| enable_pbr=true, face_count=3000, generate_type="Normal" | 0.6 |
| enable_pbr=true, face_count=3000, generate_type="Geometry" | 0.428571 |
| enable_pbr=true, face_count=1500000, generate_type="Normal" | 0.6 |
| enable_pbr=true, face_count=1500000, generate_type="Geometry" | 0.428571 |

Formula: `(15 + ((params.enable_pbr ?? false) && (params.generate_type ?? "Normal") != "Geometry" ? 10 : 0) + ((params.face_count ?? 0) > 0 ? 10 : 0)) * 0.12 / 7`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/miora-3d/t1/image-to-3d", "image": "https://static.sandbase.ai/examples/b338627d-beea-473f-bb2e-c900c95b27a4/input/f794b164-3a58-4306-a875-8dcf8c698d94.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/miora-3d/t1/image-to-3d', {'image': 'https://static.sandbase.ai/examples/b338627d-beea-473f-bb2e-c900c95b27a4/input/f794b164-3a58-4306-a875-8dcf8c698d94.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/miora-3d/t1/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/b338627d-beea-473f-bb2e-c900c95b27a4/input/f794b164-3a58-4306-a875-8dcf8c698d94.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/miora-3d/t1/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/b338627d-beea-473f-bb2e-c900c95b27a4/input/f794b164-3a58-4306-a875-8dcf8c698d94.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image URL. 128-5000 px per side, up to 10 MB, JPG/PNG/WEBP. Works best with a single object on a simple background.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count. Uses the model default when unset. range 3000–1500000 |
| `generate_type` | string |  | Normal: textured model. Geometry: untextured white model. one of: `Normal`, `Geometry`; default `"Normal"` |

## Details

Miora 3D T1 by Tencent Design is the fast Miora 3D model: it turns a single image into a textured or untextured 3D asset in about two minutes.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view image URL. 128-5000 px per side, up to 10 MB, JPG/PNG/WEBP. Works best with a single object on a simple background. |
| `generate_type` | string | "Normal" | Normal: textured model. Geometry: untextured white model. |
| `enable_pbr` | boolean | false | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. |
| `face_count` | integer | — | Target polygon face count. Uses the model default when unset. |

### Billing

| Request | Price |
|---|---|
| Default | $0.2571 |
| Geometry (untextured) | $0.2571 |
| With PBR | $0.4286 |
| With custom face count | $0.4286 |

PBR, a custom face count each add to the default price. Failed runs are not charged.

---
Machine-readable: [`catalog/models/tencent/miora-3d/t1/image-to-3d.json`](../../../../../catalog/models/tencent/miora-3d/t1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/miora-3d/t1/image-to-3d
