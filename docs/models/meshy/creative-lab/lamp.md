# Meshy Creative Lab Lamp API: pricing, parameters and code examples

`meshy/creative-lab/lamp` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.44 per call · **Modes:** async

Turns a photo into a 3D-printable lithophane-style lampshade and base.

## Pricing

- **$1.44 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/lamp", "image": "https://static.sandbase.ai/examples/c9277bb5-737d-4841-ae51-081e673853b4/input/17cb6678-9426-4af9-acdb-7224fad2a3dd.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/lamp', {'image': 'https://static.sandbase.ai/examples/c9277bb5-737d-4841-ae51-081e673853b4/input/17cb6678-9426-4af9-acdb-7224fad2a3dd.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/lamp", {
  "image": "https://static.sandbase.ai/examples/c9277bb5-737d-4841-ae51-081e673853b4/input/17cb6678-9426-4af9-acdb-7224fad2a3dd.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/lamp", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/c9277bb5-737d-4841-ae51-081e673853b4/input/17cb6678-9426-4af9-acdb-7224fad2a3dd.jpg",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP).  |
| `diameter_mm` | number |  | Lampshade diameter in millimeters. default `150`; range 60–300 |
| `image_subject` | string |  | What the photo shows. one of: `character`, `landscape`; default `"character"` |

## Details

Turns a photo into a 3D-printable lithophane-style lampshade and base.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
| `image_subject` | `character` / `landscape` | `"character"` | What the photo shows. |
| `diameter_mm` | number 60–300 | `150` | Lampshade diameter in millimeters. |
### Output
- `url`: Lampshade preview GLB.
- `lamp_stl`: Lampshade STL.
- `base_stl`: Base STL.
- `thumbnail`: Preview image.
### Billing
$1.44 per object (concept image + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/lamp.json`](../../../../catalog/models/meshy/creative-lab/lamp.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/lamp
