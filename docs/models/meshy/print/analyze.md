# Meshy Analyze Printability API: pricing, parameters and code examples

`meshy/print/analyze` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** free · **Modes:** async

Meshy Analyze Printability checks a 3D model for watertightness, holes, non-manifold edges, degenerate faces and thin walls before printing.

## Pricing

- **Free**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/print/analyze", "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/print/analyze', {'model_url': 'https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/print/analyze", {
  "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/print/analyze", sandbase.Params{
	"model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI.  |
| `printer_type` | string |  | Printer that sets the minimum wall thickness. one of: `fdm`, `sla`, `full_color` |
| `intended_print_height_mm` | number |  | Planned print height in millimeters (GLB input). range 1–1000 |
| `intended_print_longest_side_mm` | number |  | Planned print size by its longest side in millimeters (exclusive with intended_print_height_mm). range 1–1000 |

## Details

Meshy Analyze Printability checks a 3D model for watertightness, holes, non-manifold edges, degenerate faces and thin walls before printing.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `printer_type` | `fdm` / `sla` / `full_color` | — | Printer that sets the minimum wall thickness. |
| `intended_print_height_mm` | number 1–1000 | — | Planned print height in millimeters (GLB input). |
| `intended_print_longest_side_mm` | number 1–1000 | — | Planned print size by its longest side in millimeters (exclusive with intended_print_height_mm). |
### Output
- `status`: `ok`, `warning` or `error`.
- `issue_count / error_count / warning_count`: Issue counts.
- `metrics`: is_watertight, volume, holes, non_manifold_edges, degenerate_faces.
- `thin_walls`: Thin-wall check when a print size is given.
### Billing
Free (Meshy charges 0 credits).

---
Machine-readable: [`catalog/models/meshy/print/analyze.json`](../../../../catalog/models/meshy/print/analyze.json) · Store page: https://www.sandbase.ai/model/meshy/print/analyze
