# Meshy Creative Lab Fridge Magnet API: pricing, parameters and code examples

`meshy/creative-lab/fridge-magnet` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.44 per call · **Modes:** async

Turns a photo into a colorized relief fridge magnet ready to 3D print.

## Pricing

- **$1.44 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/fridge-magnet", "image": "https://static.sandbase.ai/examples/b5c313b5-8310-42c8-abae-8ef1738dd38f/input/81cb2e0d-2ab0-474a-b265-9b21bbb7d208.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/fridge-magnet', {'image': 'https://static.sandbase.ai/examples/b5c313b5-8310-42c8-abae-8ef1738dd38f/input/81cb2e0d-2ab0-474a-b265-9b21bbb7d208.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/fridge-magnet", {
  "image": "https://static.sandbase.ai/examples/b5c313b5-8310-42c8-abae-8ef1738dd38f/input/81cb2e0d-2ab0-474a-b265-9b21bbb7d208.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/fridge-magnet", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/b5c313b5-8310-42c8-abae-8ef1738dd38f/input/81cb2e0d-2ab0-474a-b265-9b21bbb7d208.jpg",
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
| `size_mm` | number |  | Edge of the bounding square in millimeters. default `60`; range 10–400 |
| `badge_shape` | string |  | Outline used when the subject is not traced. one of: `circle`, `rounded-rect`, `hexagon`, `shield`, `star`; default `"rounded-rect"` |

## Details

Turns a photo into a colorized relief fridge magnet ready to 3D print.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
| `badge_shape` | `circle` / `rounded-rect` / `hexagon` / `shield` / `star` | `"rounded-rect"` | Outline used when the subject is not traced. |
| `size_mm` | number 10–400 | `60` | Edge of the bounding square in millimeters. |
### Output
- `url`: Magnet GLB.
- `concept_image`: Concept image.
### Billing
$1.44 per object (concept image + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/fridge-magnet.json`](../../../../catalog/models/meshy/creative-lab/fridge-magnet.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/fridge-magnet
