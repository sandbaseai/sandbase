# Qwen Image Edit

`alibaba/qwen-image-edit` · image · Alibaba

Qwen Image Edit is Alibaba's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- **$0.045 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen-image-edit", "image": "https://static.sandbase.ai/examples/69e64dd1-c75f-49b4-a0e5-675d63145694/input/4195cebd-2577-49d0-a51c-97e0fece877c.png", "prompt": "Change bag to apple macbook"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/qwen-image-edit', {'image': 'https://static.sandbase.ai/examples/69e64dd1-c75f-49b4-a0e5-675d63145694/input/4195cebd-2577-49d0-a51c-97e0fece877c.png', 'prompt': 'Change bag to apple macbook'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/qwen-image-edit", {
  "image": "https://static.sandbase.ai/examples/69e64dd1-c75f-49b4-a0e5-675d63145694/input/4195cebd-2577-49d0-a51c-97e0fece877c.png",
  "prompt": "Change bag to apple macbook"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/qwen-image-edit", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/69e64dd1-c75f-49b4-a0e5-675d63145694/input/4195cebd-2577-49d0-a51c-97e0fece877c.png",
	"prompt": "Change bag to apple macbook",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same prompt given to the same version of the model will output the same image every time.  |
| `image` | string | yes | The URL of the image to edit.  |
| `prompt` | string | yes | The prompt to generate the image with  |
| `strength` | number |  | Strength of the image-to-image transformation. Lower values preserve more of the original image. default `0.94`; range 0.01–1 |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

The original Qwen Image Edit: change one image with an instruction, including Chinese and English text edits. `strength` controls how far the result may move from the input.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | Image to edit. JPEG, PNG, or WebP URL. |
| `strength` | number 0.01–1 | 0.94 | How much the output may differ from the input (0.01–1). |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the input image. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.045 per output image, Alibaba's list price.

| Request | Price |
|---|---|
| One image | $0.045 |

Failed runs are not charged.

### Prompting

- State the change and what must stay the same.
- Lower `strength` for subtle edits.

### Limits

- One input image per request; 2511 accepts several.

### Also on SandBase

Related: `alibaba/qwen-image-edit/2511`, `alibaba/qwen-image-edit/2511/multiple-angles`, `alibaba/qwen-image-3/edit` (newer).

---
Machine-readable: [`catalog/models/alibaba/qwen-image-edit.json`](../../../catalog/models/alibaba/qwen-image-edit.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen-image-edit
