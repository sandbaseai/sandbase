# Idol API: pricing, parameters and code examples

`speridlabs/idol` · image generation model · speridlabs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 per call · **Modes:** async

Idol by Sperid Labs turns a single image of an object into a 3D Gaussian splat (PLY) with a GLB point-cloud preview.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "speridlabs/idol", "image": "https://static.sandbase.ai/examples/92b467b8-e906-4df4-a912-290fbd4a134d/input/969c0927-46b5-4d95-91ca-8568e6eed33d.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('speridlabs/idol', {'image': 'https://static.sandbase.ai/examples/92b467b8-e906-4df4-a912-290fbd4a134d/input/969c0927-46b5-4d95-91ca-8568e6eed33d.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("speridlabs/idol", {
  "image": "https://static.sandbase.ai/examples/92b467b8-e906-4df4-a912-290fbd4a134d/input/969c0927-46b5-4d95-91ca-8568e6eed33d.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "speridlabs/idol", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/92b467b8-e906-4df4-a912-290fbd4a134d/input/969c0927-46b5-4d95-91ca-8568e6eed33d.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results.  |
| `image` | string | yes | Image of a single object to convert into a 3D Gaussian splat.  |
| `image_type` | string |  | 'synthetic' for renders and generated images (tight crop), 'real' for photographs (looser crop). one of: `synthetic`, `real`; default `"synthetic"` |
| `num_gaussians` | integer |  | Target number of Gaussians in the output splat. default `262144`; range 32768–1048576 |

## Details

Idol by Sperid Labs turns a single image of an object into a 3D Gaussian splat (PLY) with a GLB point-cloud preview.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image of a single object to convert into a 3D Gaussian splat. |
| `image_type` | `synthetic` / `real` | `synthetic` | 'synthetic' for renders and generated images (tight crop), 'real' for photographs (looser crop). |
| `num_gaussians` | integer 32768–1048576 | `262144` | Target number of Gaussians in the output splat. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
- `gaussian_splat`: Additional file returned by the provider.
### Billing
$0.10 per request.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/speridlabs/idol.json`](../../../catalog/models/speridlabs/idol.json) · Store page: https://www.sandbase.ai/model/speridlabs/idol
