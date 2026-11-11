# TripoSplat API: pricing, parameters and code examples

`tripo3d/triposplat` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

TripoSplat by Tripo3D turns a single image into a 3D Gaussian splat for real-time rendering. Output is a .ply or .splat file.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/triposplat", "image": "https://raw.githubusercontent.com/VAST-AI-Research/TripoSplat/36b6deb0a1613e43c6910de441cb57d50352e44a/static/example_inputs/building_stone_house.webp"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/triposplat', {'image': 'https://raw.githubusercontent.com/VAST-AI-Research/TripoSplat/36b6deb0a1613e43c6910de441cb57d50352e44a/static/example_inputs/building_stone_house.webp'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/triposplat", {
  "image": "https://raw.githubusercontent.com/VAST-AI-Research/TripoSplat/36b6deb0a1613e43c6910de441cb57d50352e44a/static/example_inputs/building_stone_house.webp"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/triposplat", sandbase.Params{
	"image": "https://raw.githubusercontent.com/VAST-AI-Research/TripoSplat/36b6deb0a1613e43c6910de441cb57d50352e44a/static/example_inputs/building_stone_house.webp",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for reproducible generation. Random when unset.  |
| `image` | string | yes | URL of the input image to convert into a 3D Gaussian splat.  |
| `num_gaussians` | integer |  | Target number of Gaussians. Higher means more detail but larger files. default `262144`; range 32768–262144 |
| `output_format` | string |  | File format of the generated Gaussian splat. one of: `ply`, `splat`; default `"ply"` |

## Details

TripoSplat by Tripo3D turns a single image into a 3D Gaussian splat for real-time rendering. Output is a .ply or .splat file.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | URL of the input image to convert into a 3D Gaussian splat. |
| `output_format` | `ply` / `splat` | `ply` | File format of the generated Gaussian splat. |
| `num_gaussians` | integer 32768–262144 | `262144` | Target number of Gaussians. Higher means more detail but larger files. |
| `seed` | integer | — | Seed for reproducible generation. Random when unset. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.05 per request.
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/triposplat.json`](../../../catalog/models/tripo3d/triposplat.json) · Store page: https://www.sandbase.ai/model/tripo3d/triposplat
