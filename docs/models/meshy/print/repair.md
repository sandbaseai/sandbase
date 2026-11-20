# Meshy Print Repair API: pricing, parameters and code examples

`meshy/print/repair` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 per call · **Modes:** async

Meshy Print Repair fixes holes, non-manifold geometry and thin walls so a 3D model can be printed.

## Pricing

- **$0.4 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/print/repair", "model_url": "https://static.sandbase.ai/examples/b8eaa5e3-bc42-49aa-9326-f82581dfd780/input/b52c16ed-bd67-437f-9606-c936dfbd5762.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/print/repair', {'model_url': 'https://static.sandbase.ai/examples/b8eaa5e3-bc42-49aa-9326-f82581dfd780/input/b52c16ed-bd67-437f-9606-c936dfbd5762.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/print/repair", {
  "model_url": "https://static.sandbase.ai/examples/b8eaa5e3-bc42-49aa-9326-f82581dfd780/input/b52c16ed-bd67-437f-9606-c936dfbd5762.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/print/repair", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/b8eaa5e3-bc42-49aa-9326-f82581dfd780/input/b52c16ed-bd67-437f-9606-c936dfbd5762.glb",
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

## Details

Meshy Print Repair fixes holes, non-manifold geometry and thin walls so a 3D model can be printed.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, GLTF, FBX, OBJ or STL) as a public URL or data URI. |
| `printer_type` | `fdm` / `sla` / `full_color` | — | Printer that sets the minimum wall thickness. |
| `intended_print_height_mm` | number 1–1000 | — | Planned print height in millimeters (GLB input). |
### Output
- `url`: Repaired GLB.
- `thumbnail`: Preview image.
### Billing
$0.40 per model.

---
Machine-readable: [`catalog/models/meshy/print/repair.json`](../../../../catalog/models/meshy/print/repair.json) · Store page: https://www.sandbase.ai/model/meshy/print/repair
