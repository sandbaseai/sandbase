# Seedream 5.5 Edit API: pricing, parameters and code examples

`bytedance/seedream/5.5/edit` · image generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.028 to $0.043 per run, depending on parameters · **Modes:** async

Seedream 5.5 Edit by ByteDance edits images with text instructions and up to 10 reference images. It keeps unedited regions stable across many rounds of editing and can return transparent-background (RGBA) PNGs.

## Pricing

- Depends on parameters (`params.images`, `params.num_images`, `params.resolution`).

| parameters | USD |
|---|---|
| num_images=1, resolution="1K" | 0.028 |
| num_images=1, resolution="1.5K" | 0.028 |
| num_images=1, resolution="2K" | 0.043 |

Formula: `(params.num_images ?? 1) * (((params.resolution ?? "2K") == "2K" ? 0.035 : 0.02) + len(params.images ?? []) * 0.008)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.5/edit", "aspect_ratio": "16:9", "background": "opaque", "images": ["https://static.sandbase.ai/examples/49b822da-45bc-4cde-8457-340038e2e462/input/ef7b2adc-6272-4a5e-807f-5cbb86b8d6e2.png"], "prompt": "Have the person blow a round, semi-transparent pink bubblegum bubble. Preserve the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background, composition, and visual style of the person."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.5/edit', {'aspect_ratio': '16:9', 'background': 'opaque', 'images': ['https://static.sandbase.ai/examples/49b822da-45bc-4cde-8457-340038e2e462/input/ef7b2adc-6272-4a5e-807f-5cbb86b8d6e2.png'], 'prompt': 'Have the person blow a round, semi-transparent pink bubblegum bubble. Preserve the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background, composition, and visual style of the person.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.5/edit", {
  "aspect_ratio": "16:9",
  "background": "opaque",
  "images": [
    "https://static.sandbase.ai/examples/49b822da-45bc-4cde-8457-340038e2e462/input/ef7b2adc-6272-4a5e-807f-5cbb86b8d6e2.png"
  ],
  "prompt": "Have the person blow a round, semi-transparent pink bubblegum bubble. Preserve the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background, composition, and visual style of the person."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.5/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"background": "opaque",
	"images": []any{"https://static.sandbase.ai/examples/49b822da-45bc-4cde-8457-340038e2e462/input/ef7b2adc-6272-4a5e-807f-5cbb86b8d6e2.png"},
	"prompt": "Have the person blow a round, semi-transparent pink bubblegum bubble. Preserve the identity, facial features, gaze, hairstyle, pearl earrings, clothing, pose, blue background, composition, and visual style of the person.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | List of URLs of input reference images. Up to 10 images are supported; if more are sent, only the last 10 are used.  |
| `prompt` | string | yes | The text prompt used to edit the image.  |
| `background` | string |  | auto lets the model decide; transparent returns a PNG with an alpha channel (requires png output); opaque never adds transparency. one of: `auto`, `transparent`, `opaque`; default `"auto"` |
| `num_images` | integer |  | The number of edited images to generate. Currently limited to 1. default `1`; range 1–1 |
| `resolution` | string |  | Output resolution tier. 1K and 1.5K cost less; 2K is the highest quality. one of: `1K`, `1.5K`, `2K`; default `"2K"` |
| `aspect_ratio` | string |  | The aspect ratio of the edited image. Leave unset to follow the reference image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The file format of the generated image. Use png for transparent backgrounds. one of: `jpeg`, `png`; default `"png"` |

## Details

Seedream 5.5 Edit changes or combines up to 10 images with a text instruction. It keeps unedited regions stable across many rounds of editing and can return transparent-background (RGBA) PNGs.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] (≤10), required | — | Images to edit or combine, Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the input image. |
| `resolution` | `1K` / `1.5K` / `2K` | `2K` | Output resolution tier. |
| `background` | `auto` / `transparent` / `opaque` | `auto` | `transparent` returns a PNG with an alpha channel; `opaque` keeps multi-round edits most consistent. |
| `num_images` | integer 1–1 | 1 | Fixed at 1. |
| `output_format` | `png` / `jpeg` | `png` | Use `png` for transparent backgrounds. |

### Billing

$0.035 per output image at 2K ($0.02 at 1K or 1.5K), plus $0.008 for each input image.

| Inputs | 1K / 1.5K | 2K |
|---|---|---|
| 1 input image | $0.028 | $0.043 |
| 3 input images | $0.044 | $0.059 |
| 10 input images | $0.10 | $0.115 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- State what to change and list what must stay the same.
- For multi-round editing, feed the previous output back in as the next input and change one thing per round.

### Limits

- One output image per request.
- Up to 10 input images.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.5`, `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.5/edit.json`](../../../../../catalog/models/bytedance/seedream/5.5/edit.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.5/edit
