# MAI Image 2.7 Flash Edit API: pricing, parameters and code examples

`microsoft/mai-image-2.7-flash/edit` · image generation model · Microsoft · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.025 per run, depending on parameters · **Modes:** async

MAI Image 2.7 Flash Edit by Microsoft edits images from a text instruction, combining up to five reference images.

## Pricing

- Depends on parameters (`params.images`).

| parameters | USD |
|---|---|
| defaults | 0.025 |

Formula: `0.025 + 0.003 * (len(params.images ?? []) > 1 ? float(len(params.images ?? []) - 1) : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/mai-image-2.7-flash/edit", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/a3bf1d82-c235-4fa8-a0fc-61723ec5b8e2/input/63eb5a61-7940-4761-a2c4-4beb137844b9.png"], "prompt": "Place this figure on a wooden desk next to a cup of coffee, soft morning light."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('microsoft/mai-image-2.7-flash/edit', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/a3bf1d82-c235-4fa8-a0fc-61723ec5b8e2/input/63eb5a61-7940-4761-a2c4-4beb137844b9.png'], 'prompt': 'Place this figure on a wooden desk next to a cup of coffee, soft morning light.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("microsoft/mai-image-2.7-flash/edit", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/a3bf1d82-c235-4fa8-a0fc-61723ec5b8e2/input/63eb5a61-7940-4761-a2c4-4beb137844b9.png"
  ],
  "prompt": "Place this figure on a wooden desk next to a cup of coffee, soft morning light."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "microsoft/mai-image-2.7-flash/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/a3bf1d82-c235-4fa8-a0fc-61723ec5b8e2/input/63eb5a61-7940-4761-a2c4-4beb137844b9.png"},
	"prompt": "Place this figure on a wooden desk next to a cup of coffee, soft morning light.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | Images to edit or use as references, 1 to 5 files or URLs.  |
| `prompt` | string | yes | Instruction describing the edit.  |
| `background` | string |  | transparent returns an alpha channel (png or webp output). one of: `opaque`, `transparent`; default `"opaque"` |
| `aspect_ratio` | string |  | Output shape. Leave unset to stay close to the input image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | Image file format. one of: `png`, `jpeg`, `webp`; default `"png"` |

## Details

MAI Image 2.7 Flash Edit changes one or more input images from a text instruction. Up to five images can be combined as references.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image files or URLs, required | — | 1 to 5 images. |
| `prompt` | string, required | — | The edit to make. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Unset keeps a size close to the input. |
| `background` | `opaque` / `transparent` | `opaque` | `transparent` needs png or webp. |
| `output_format` | `png` / `jpeg` / `webp` | `png` | File format. |
### Billing
$0.025 per image with one input image, plus $0.003 for each additional input image.
| Input images | Price |
|---|---|
| 1 | $0.025 |
| 5 | $0.037 |
Failed runs are not charged.
### Also on SandBase
Related: `microsoft/mai-image-2.7-flash`, `microsoft/mai-image-2.5/edit`.

---
Machine-readable: [`catalog/models/microsoft/mai-image-2.7-flash/edit.json`](../../../../catalog/models/microsoft/mai-image-2.7-flash/edit.json) · Store page: https://www.sandbase.ai/model/microsoft/mai-image-2.7-flash/edit
