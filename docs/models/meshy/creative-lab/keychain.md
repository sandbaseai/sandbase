# Meshy Creative Lab Keychain API: pricing, parameters and code examples

`meshy/creative-lab/keychain` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.44 per call · **Modes:** async

Turns a photo into a 3D-printable keychain medallion, optionally with a name on its face.

## Pricing

- **$1.44 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/keychain", "image": "https://static.sandbase.ai/examples/001021be-9b89-4dd5-bdff-17cded73b67a/input/4b857cac-9de7-4134-b8c2-7f5d04d7ad30.jpg", "name_text": "Corgi"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/keychain', {'image': 'https://static.sandbase.ai/examples/001021be-9b89-4dd5-bdff-17cded73b67a/input/4b857cac-9de7-4134-b8c2-7f5d04d7ad30.jpg', 'name_text': 'Corgi'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/keychain", {
  "image": "https://static.sandbase.ai/examples/001021be-9b89-4dd5-bdff-17cded73b67a/input/4b857cac-9de7-4134-b8c2-7f5d04d7ad30.jpg",
  "name_text": "Corgi"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/keychain", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/001021be-9b89-4dd5-bdff-17cded73b67a/input/4b857cac-9de7-4134-b8c2-7f5d04d7ad30.jpg",
	"name_text": "Corgi",
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
| `size_mm` | number |  | Edge of the bounding square in millimeters. default `40`; range 10–400 |
| `name_text` | string |  | Name shown on the keychain, up to 10 characters.  |
| `badge_shape` | string |  | Outline used when the subject is not traced. one of: `circle`, `rounded-rect`, `hexagon`, `shield`, `star`; default `"circle"` |

## Details

Turns a photo into a 3D-printable keychain medallion, optionally with a name on its face.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
| `name_text` | string | — | Name shown on the keychain, up to 10 characters. |
| `badge_shape` | `circle` / `rounded-rect` / `hexagon` / `shield` / `star` | `"circle"` | Outline used when the subject is not traced. |
| `size_mm` | number 10–400 | `40` | Edge of the bounding square in millimeters. |
### Output
- `url`: Keychain GLB.
- `concept_image`: Colorized concept image.
### Billing
$1.44 per object (concept image + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/keychain.json`](../../../../catalog/models/meshy/creative-lab/keychain.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/keychain
