# Tripo Segment API: pricing, parameters and code examples

`tripo3d/tripo/segment` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.48 per call · **Modes:** async

Tripo Segment splits an existing 3D model into named parts. Accepts GLB, OBJ, FBX or STL input.

## Pricing

- **$0.48 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/segment", "model_url": "https://static.sandbase.ai/examples/5d486446-c09b-4862-9387-00f6850d4373/input/992f8521-7777-4c3c-8d73-e11004b95d99.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/segment', {'model_url': 'https://static.sandbase.ai/examples/5d486446-c09b-4862-9387-00f6850d4373/input/992f8521-7777-4c3c-8d73-e11004b95d99.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/segment", {
  "model_url": "https://static.sandbase.ai/examples/5d486446-c09b-4862-9387-00f6850d4373/input/992f8521-7777-4c3c-8d73-e11004b95d99.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/segment", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/5d486446-c09b-4862-9387-00f6850d4373/input/992f8521-7777-4c3c-8d73-e11004b95d99.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of the input 3D model (GLB, OBJ, FBX or STL, max 150MB).  |

## Details

Tripo Segment splits an existing 3D model into named parts. Accepts GLB, OBJ, FBX or STL input.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, OBJ, FBX or STL, max 150MB). |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.48 per request.
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo/segment.json`](../../../../catalog/models/tripo3d/tripo/segment.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/segment
