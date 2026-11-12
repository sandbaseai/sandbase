# SAM 3 3D Body API: pricing, parameters and code examples

`meta/sam-3/3d-body` · image generation model · Meta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.024 per call · **Modes:** async

SAM 3D Body by Meta reconstructs the 3D shape and pose of the people in a single image and returns them as a GLB mesh.

## Pricing

- **$0.024 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/sam-3/3d-body", "image": "https://static.sandbase.ai/examples/662c1b28-14d4-42cb-a8af-1c1aa80892eb/input/f6e28db1-3eed-4390-a6ea-88f96f778324.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meta/sam-3/3d-body', {'image': 'https://static.sandbase.ai/examples/662c1b28-14d4-42cb-a8af-1c1aa80892eb/input/f6e28db1-3eed-4390-a6ea-88f96f778324.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meta/sam-3/3d-body", {
  "image": "https://static.sandbase.ai/examples/662c1b28-14d4-42cb-a8af-1c1aa80892eb/input/f6e28db1-3eed-4390-a6ea-88f96f778324.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meta/sam-3/3d-body", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/662c1b28-14d4-42cb-a8af-1c1aa80892eb/input/f6e28db1-3eed-4390-a6ea-88f96f778324.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mask` | string |  | Optional binary mask (white = person, black = background). When set, automatic person detection is skipped.  |
| `image` | string | yes | Image containing one or more people.  |
| `include_3d_keypoints` | boolean |  | Add 3D keypoint markers (spheres) to the GLB mesh. default `true` |

## Details

SAM 3D Body by Meta reconstructs the 3D shape and pose of the people in a single image and returns them as a GLB mesh.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image containing one or more people. |
| `mask` | image URL | — | Optional binary mask (white = person, black = background). When set, automatic person detection is skipped. |
| `include_3d_keypoints` | boolean | `true` | Add 3D keypoint markers (spheres) to the GLB mesh. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.024 per request.
Failed runs are not charged.
### Also on SandBase
Other Meta 3D endpoints: `meta/sam-3/3d-align`, `meta/sam-3/3d-objects`.

---
Machine-readable: [`catalog/models/meta/sam-3/3d-body.json`](../../../../catalog/models/meta/sam-3/3d-body.json) · Store page: https://www.sandbase.ai/model/meta/sam-3/3d-body
