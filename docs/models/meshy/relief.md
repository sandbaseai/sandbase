# Meshy Relief API: pricing, parameters and code examples

`meshy/relief` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.8 per call · **Modes:** async

Meshy Relief turns a photo into a printable 3D relief (GLB and STL) with emboss or engrave carving and an optional curved bend.

## Pricing

- **$0.8 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/relief", "image": "https://static.sandbase.ai/examples/meshy/relief/input_image_0.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/relief', {'image': 'https://static.sandbase.ai/examples/meshy/relief/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/relief", {
  "image": "https://static.sandbase.ai/examples/meshy/relief/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/relief", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/meshy/relief/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Photo to turn into a relief. Works best with one clear subject on a plain background. JPG, PNG or WebP up to 20 MB.  |
| `size_mm` | number |  | Length of the photo's long side in millimeters, measured flat before any bend. default `60`; range 20–250 |
| `variant` | string |  | 'low' gives slight depth and finer detail (patterns, badges, seals); 'high' gives bold, sculptural depth (pets, portraits, characters). one of: `low`, `high`; default `"low"` |
| `bend_axis` | string |  | 'xz' curls the left and right edges, 'yz' the top and bottom. one of: `xz`, `yz`; default `"xz"` |
| `bend_mode` | string |  | Bend the relief into a convex or concave curve. one of: `off`, `convex`, `concave`; default `"off"` |
| `bend_angle` | number |  | Bend angle in degrees when bending is on. default `60`; range 0–360 |
| `remove_base` | boolean |  | Cut away the background and build no base plate. default `false` |
| `carving_mode` | string |  | 'emboss' makes nearer parts stand out; 'engrave' cuts them in. one of: `emboss`, `engrave`; default `"emboss"` |
| `mesh_resolution` | integer |  | Mesh points along the long side. At 2048 the GLB reaches about 150 MB and the STL about 300 MB. default `1024`; range 512–2048 |
| `carving_depth_mm` | number |  | Carving depth in millimeters. Defaults to 3 for 'low' and 6 for 'high'. range 0–60 |
| `base_thickness_mm` | number |  | Base plate thickness in millimeters (default 1). Not allowed with remove_base. range 0.1–10 |

## Details

Meshy Relief turns a photo into a printable 3D relief (GLB and STL) with emboss or engrave carving and an optional curved bend.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Photo to turn into a relief. Works best with one clear subject on a plain background. JPG, PNG or WebP up to 20 MB. |
| `variant` | `low` / `high` | `low` | 'low' gives slight depth and finer detail (patterns, badges, seals); 'high' gives bold, sculptural depth (pets, portraits, characters). |
| `carving_mode` | `emboss` / `engrave` | `emboss` | 'emboss' makes nearer parts stand out; 'engrave' cuts them in. |
| `size_mm` | number 20–250 | `60` | Length of the photo's long side in millimeters, measured flat before any bend. |
| `carving_depth_mm` | number 0–60 | — | Carving depth in millimeters. Defaults to 3 for 'low' and 6 for 'high'. |
| `base_thickness_mm` | number 0.1–10 | — | Base plate thickness in millimeters (default 1). Not allowed with remove_base. |
| `remove_base` | boolean | `false` | Cut away the background and build no base plate. |
| `bend_mode` | `off` / `convex` / `concave` | `off` | Bend the relief into a convex or concave curve. |
| `bend_axis` | `xz` / `yz` | `xz` | 'xz' curls the left and right edges, 'yz' the top and bottom. |
| `bend_angle` | number 0–360 | `60` | Bend angle in degrees when bending is on. |
| `mesh_resolution` | integer 512–2048 | `1024` | Mesh points along the long side. At 2048 the GLB reaches about 150 MB and the STL about 300 MB. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
- `stl`: Additional file returned by the provider.
- `depth_map`: Additional file returned by the provider.
### Billing
$0.80 per request.
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/relief.json`](../../../catalog/models/meshy/relief.json) · Store page: https://www.sandbase.ai/model/meshy/relief
