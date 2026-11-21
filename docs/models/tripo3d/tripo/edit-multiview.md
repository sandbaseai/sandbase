# Tripo Edit Multiview API: pricing, parameters and code examples

`tripo3d/tripo/edit-multiview` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1 per run, depending on parameters · **Modes:** async

Tripo Edit Multiview generates front, left, back and right views from one image and applies text edits to chosen views, keeping the views consistent.

## Pricing

- Depends on parameters (`params.prompts`).

| parameters | USD |
|---|---|
| defaults | 0.1 |

Formula: `0.10 + 0.05 * len(params.prompts ?? [])`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/edit-multiview", "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png", "prompts": [{"view": "front", "prompt": "make the horn bright red"}]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/edit-multiview', {'image': 'https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png', 'prompts': [{'view': 'front', 'prompt': 'make the horn bright red'}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/edit-multiview", {
  "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png",
  "prompts": [
    {
      "view": "front",
      "prompt": "make the horn bright red"
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/edit-multiview", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png",
	"prompts": []any{map[string]any{
		"view": "front",
		"prompt": "make the horn bright red",
	}},
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
| `prompts` | array | yes | 1 to 4 edits, one per view: {"view": "front\|left\|back\|right", "prompt": "..."} (prompt up to 1,024 characters).  |

## Details

Tripo Edit Multiview generates front, left, back and right views from one image and applies text edits to chosen views, keeping the views consistent.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Input image; the subject should stand out from a clean background. |
| `prompts` | array, required | — | 1 to 4 edits, one per view: {"view": "front|left|back|right", "prompt": "..."} (prompt up to 1,024 characters). |
### Output
- `url`: Front view (edited if requested).
- `left_view`: Left view.
- `back_view`: Back view.
- `right_view`: Right view.
### Billing
$0.10 for the four views plus $0.05 per edited view.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/edit-multiview.json`](../../../../catalog/models/tripo3d/tripo/edit-multiview.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/edit-multiview
