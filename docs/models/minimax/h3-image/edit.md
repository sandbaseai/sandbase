# MiniMax H3 Image Edit API: pricing, parameters and code examples

`minimax/h3-image/edit` · image generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.038 to $0.098 per run, depending on parameters · **Modes:** async

MiniMax H3 Image Edit edits and composes images from 1 to 16 reference images with MiniMax's H3 image model, following the instruction while keeping subjects consistent, with 1K, 2K or 4K output.

## Pricing

- Depends on parameters (`params.images`, `params.resolution`).

| parameters | USD |
|---|---|
| resolution="1K" | 0.038 |
| resolution="2K" | 0.038 |
| resolution="4K" | 0.098 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.09 : 0.03) + 0.008 * len(params.images ?? [])`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-image/edit", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/566be149-b328-4c11-8148-f1316effb300/input/619c43c2-c319-43c9-9048-35fd58117ce7.png"], "prompt": "Put a red knitted scarf on the dog and keep everything else", "resolution": "1K"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-image/edit', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/566be149-b328-4c11-8148-f1316effb300/input/619c43c2-c319-43c9-9048-35fd58117ce7.png'], 'prompt': 'Put a red knitted scarf on the dog and keep everything else', 'resolution': '1K'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-image/edit", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/566be149-b328-4c11-8148-f1316effb300/input/619c43c2-c319-43c9-9048-35fd58117ce7.png"
  ],
  "prompt": "Put a red knitted scarf on the dog and keep everything else",
  "resolution": "1K"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-image/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/566be149-b328-4c11-8148-f1316effb300/input/619c43c2-c319-43c9-9048-35fd58117ce7.png"},
	"prompt": "Put a red knitted scarf on the dog and keep everything else",
	"resolution": "1K",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | URLs of 1 to 16 reference images to edit or combine (JPG, PNG, WEBP, HEIC or HEIF; 128 to 8192 px per side).  |
| `prompt` | string | yes | The text prompt to generate an image from. default `"Put a red knitted scarf on the dog and keep everything else"` |
| `resolution` | string |  | Output resolution tier: 1K (about 1 MP), 2K (about 4 MP) or 4K (about 16 MP). one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | Output aspect ratio. Leave empty to let the model choose based on the reference images and instruction. one of: `21:9`, `16:9`, `2:1`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `1:2`, `9:16` … |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`, `webp`; default `"png"` |

---
Machine-readable: [`catalog/models/minimax/h3-image/edit.json`](../../../../catalog/models/minimax/h3-image/edit.json) · Store page: https://www.sandbase.ai/model/minimax/h3-image/edit
