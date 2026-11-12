# Tripo v2.5 Multiview to 3D API: pricing, parameters and code examples

`tripo3d/tripo-v2.5/multiview-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.45 per run, depending on parameters · **Modes:** async

Tripo v2.5 by Tripo3D reconstructs a textured 3D mesh from a front view plus optional left, back and right views of the same object.

## Pricing

- Depends on parameters (`params.pbr`, `params.quad`, `params.texture`).

| parameters | USD |
|---|---|
| pbr=false, quad=false, texture="no" | 0.2 |
| pbr=false, quad=false, texture="standard" | 0.3 |
| pbr=false, quad=false, texture="HD" | 0.4 |
| pbr=false, quad=true, texture="no" | 0.25 |
| pbr=false, quad=true, texture="standard" | 0.35 |
| pbr=false, quad=true, texture="HD" | 0.45 |
| pbr=true, quad=false, texture="no" | 0.3 |
| pbr=true, quad=false, texture="standard" | 0.3 |
| pbr=true, quad=false, texture="HD" | 0.4 |
| pbr=true, quad=true, texture="no" | 0.35 |
| pbr=true, quad=true, texture="standard" | 0.35 |
| pbr=true, quad=true, texture="HD" | 0.45 |

Formula: `((params.texture ?? "standard") == "HD" ? 0.40 : ((params.texture ?? "standard") == "no" && !(params.pbr ?? false)) ? 0.20 : 0.30) + ((params.quad ?? false) ? 0.05 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-v2.5/multiview-to-3d", "back_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/85d48a9b-54ca-41bb-89d6-557a1a551598.png", "image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/0d0f81a1-5f3f-4370-9588-c67939c2d60c.png", "left_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/6af06d30-3fff-4bb0-9a21-e30df6807dfa.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-v2.5/multiview-to-3d', {'back_image': 'https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/85d48a9b-54ca-41bb-89d6-557a1a551598.png', 'image': 'https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/0d0f81a1-5f3f-4370-9588-c67939c2d60c.png', 'left_image': 'https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/6af06d30-3fff-4bb0-9a21-e30df6807dfa.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-v2.5/multiview-to-3d", {
  "back_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/85d48a9b-54ca-41bb-89d6-557a1a551598.png",
  "image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/0d0f81a1-5f3f-4370-9588-c67939c2d60c.png",
  "left_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/6af06d30-3fff-4bb0-9a21-e30df6807dfa.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-v2.5/multiview-to-3d", sandbase.Params{
	"back_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/85d48a9b-54ca-41bb-89d6-557a1a551598.png",
	"image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/0d0f81a1-5f3f-4370-9588-c67939c2d60c.png",
	"left_image": "https://static.sandbase.ai/examples/63b09ac5-1238-4faa-abc7-8a23a30b586e/input/6af06d30-3fff-4bb0-9a21-e30df6807dfa.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | Generate PBR materials. default `false` |
| `quad` | boolean |  | Generate quad mesh topology (billed as an add-on). default `false` |
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `image` | string | yes | Front view image URL.  |
| `texture` | string |  | Texture quality: no (untextured), standard, or HD. one of: `no`, `standard`, `HD`; default `"standard"` |
| `back_image` | string | yes | Back view image URL. Front and back views are both required.  |
| `face_limit` | integer |  | Target face count. Adaptive when unset.  |
| `left_image` | string |  | Optional left view image URL.  |
| `orientation` | string |  | Set to align_image to rotate the model to match the input image. one of: `default`, `align_image`; default `"default"` |
| `right_image` | string |  | Optional right view image URL.  |

## Details

Tripo v2.5 by Tripo3D reconstructs a textured 3D mesh from a front view plus optional left, back and right views of the same object.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view image URL. |
| `left_image` | image URL | — | Optional left view image URL. |
| `back_image` | image URL | — | Optional back view image URL. |
| `right_image` | image URL | — | Optional right view image URL. |
| `texture` | `no` / `standard` / `HD` | `standard` | Texture quality: no (untextured), standard, or HD. |
| `pbr` | boolean | `false` | Generate PBR materials. |
| `quad` | boolean | `false` | Generate quad mesh topology (billed as an add-on). |
| `face_limit` | integer | — | Target face count. Adaptive when unset. |
| `orientation` | `default` / `align_image` | `default` | Set to align_image to rotate the model to match the input image. |
| `seed` | integer | — | Seed for reproducible geometry generation. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.30 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| pbr on | $0.30 |
| pbr off | $0.30 |
| quad on | $0.35 |
| quad off | $0.30 |
| texture = no | $0.20 |
| texture = standard | $0.30 |
| texture = HD | $0.40 |
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-v2.5/multiview-to-3d.json`](../../../../catalog/models/tripo3d/tripo-v2.5/multiview-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-v2.5/multiview-to-3d
