# MoGe-3 API: pricing, parameters and code examples

`microsoft/moge-3` · image generation model · Microsoft · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.075 per call · **Modes:** async

MoGe-3 by Microsoft estimates metric 3D geometry from a single image, refining depth with a sparse 3D refiner, and returns a textured GLB mesh, a PLY point cloud, and depth, normal and mask maps.

## Pricing

- **$0.075 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/moge-3", "image": "https://static.sandbase.ai/examples/7cf3a6ed-343a-423e-a24c-4b59a545886a/input/c4235e86-5291-4a00-8f71-e9bb3cdf85bc.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('microsoft/moge-3', {'image': 'https://static.sandbase.ai/examples/7cf3a6ed-343a-423e-a24c-4b59a545886a/input/c4235e86-5291-4a00-8f71-e9bb3cdf85bc.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("microsoft/moge-3", {
  "image": "https://static.sandbase.ai/examples/7cf3a6ed-343a-423e-a24c-4b59a545886a/input/c4235e86-5291-4a00-8f71-e9bb3cdf85bc.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "microsoft/moge-3", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/7cf3a6ed-343a-423e-a24c-4b59a545886a/input/c4235e86-5291-4a00-8f71-e9bb3cdf85bc.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `fov_x` | number |  | Known horizontal field of view in degrees. Estimated from the image when omitted. range 1–179 |
| `image` | string | yes | Input RGB image to reconstruct.  |
| `apply_mask` | boolean |  | Mask out invalid regions (sky, background, uncertain) in the reconstruction. default `true` |
| `resolution_level` | integer |  | Processing resolution level (0-9). Higher values give finer detail but run slower; output size always matches the input. default `9`; range 0–9 |
| `num_refinement_steps` | integer |  | Number of sparse 3D refinement passes over the predicted depth. 0 skips the refiner. default `3`; range 0–5 |

## Details

MoGe-3 by Microsoft estimates metric 3D geometry from a single image, refining depth with a sparse 3D refiner, and returns a textured GLB mesh, a PLY point cloud, and depth, normal and mask maps.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Input RGB image to reconstruct. |
| `num_refinement_steps` | integer 0–5 | `3` | Number of sparse 3D refinement passes over the predicted depth. 0 skips the refiner. |
| `resolution_level` | integer 0–9 | `9` | Processing resolution level (0-9). Higher values give finer detail but run slower; output size always matches the input. |
| `fov_x` | number 1–179 | — | Known horizontal field of view in degrees. Estimated from the image when omitted. |
| `apply_mask` | boolean | `true` | Mask out invalid regions (sky, background, uncertain) in the reconstruction. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `point_cloud`: Additional file returned by the provider.
- `depth_map`: Additional file returned by the provider.
- `normal_map`: Additional file returned by the provider.
- `mask`: Additional file returned by the provider.
### Billing
$0.075 per request.
Failed runs are not charged.
### Also on SandBase
Other Microsoft 3D endpoints: `microsoft/moge-2`.

---
Machine-readable: [`catalog/models/microsoft/moge-3.json`](../../../catalog/models/microsoft/moge-3.json) · Store page: https://www.sandbase.ai/model/microsoft/moge-3
