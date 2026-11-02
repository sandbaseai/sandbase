# Hunyuan Image 3.0 Edit API: pricing, parameters and code examples

`tencent/hunyuan-image/3.0/edit` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.45 per call · **Modes:** async

Hunyuan Image 3.0 Edit by Tencent - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.45 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-image/3.0/edit", "prompt": "Turn this artwork into a realistic image"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-image/3.0/edit', {'prompt': 'Turn this artwork into a realistic image'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-image/3.0/edit", {
  "prompt": "Turn this artwork into a realistic image"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-image/3.0/edit", sandbase.Params{
	"prompt": "Turn this artwork into a realistic image",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | The URLs of the images to use as a reference for the generation. A maximum of 3 images are supported.  |
| `prompt` | string | yes | The text prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Hunyuan Image 3.0 Instruct edit: change or combine images with an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |

### Billing

$0.45 per output image.

| Request | Price |
|---|---|
| One image | $0.45 |

Failed runs are not charged.

### Prompting

- State the change and what must stay.

### Limits

- One output image per request.

### Also on SandBase

Related: `tencent/hunyuan-image/3.0`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-image/3.0/edit.json`](../../../../../catalog/models/tencent/hunyuan-image/3.0/edit.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-image/3.0/edit
