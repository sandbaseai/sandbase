# Tripo Image to Multiview API: pricing, parameters and code examples

`tripo3d/tripo/image-to-multiview` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 per call · **Modes:** async

Tripo Image to Multiview generates front, left, back and right views of an object from one image, ready for multiview-to-3D.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/image-to-multiview", "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/image-to-multiview', {'image': 'https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/image-to-multiview", {
  "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/image-to-multiview", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Input image; the subject should stand out from a clean background.  |

## Details

Tripo Image to Multiview generates front, left, back and right views of an object from one image, ready for multiview-to-3D.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Input image; the subject should stand out from a clean background. |
### Output
- `url`: Front view image.
- `left_view`: Left view image.
- `back_view`: Back view image.
- `right_view`: Right view image.
### Billing
$0.10 per request (4 views).
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/image-to-multiview.json`](../../../../catalog/models/tripo3d/tripo/image-to-multiview.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/image-to-multiview
