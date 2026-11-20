# Meshy Multi-Color Print API: pricing, parameters and code examples

`meshy/print/multi-color` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 per call · **Modes:** async

Meshy Multi-Color Print turns a textured 3D model into color regions and returns a 3MF ready for a multi-color slicer.

## Pricing

- **$0.4 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/print/multi-color", "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/print/multi-color', {'model_url': 'https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/print/multi-color", {
  "model_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/print/multi-color", sandbase.Params{
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
| `style` | string |  | Color-region style. one of: `realistic`, `cartoon`; default `"realistic"` |
| `max_depth` | integer |  | Color detail depth (realistic style only). default `4`; range 3–6 |
| `model_url` | string | yes | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI.  |
| `max_colors` | integer |  | Maximum number of colors. default `4`; range 1–16 |
| `printer_brand` | string |  | Slicer preset written into the 3MF. one of: `bambu`, `anycubic`, `creality`, `flashforge`, `snapmaker`, `elegoo`, `prusa`, `qidi`, `ankermake`; default `"bambu"` |

## Details

Meshy Multi-Color Print turns a textured 3D model into color regions and returns a 3MF ready for a multi-color slicer.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `style` | `realistic` / `cartoon` | `"realistic"` | Color-region style. |
| `max_colors` | integer 1–16 | `4` | Maximum number of colors. |
| `max_depth` | integer 3–6 | `4` | Color detail depth (realistic style only). |
| `printer_brand` | `bambu` / `anycubic` / `creality` / `flashforge` / `snapmaker` / `elegoo` / `prusa` / `qidi` / `ankermake` | `"bambu"` | Slicer preset written into the 3MF. |
### Output
- `url`: Multi-color 3MF.
### Billing
$0.40 per model.

---
Machine-readable: [`catalog/models/meshy/print/multi-color.json`](../../../../catalog/models/meshy/print/multi-color.json) · Store page: https://www.sandbase.ai/model/meshy/print/multi-color
