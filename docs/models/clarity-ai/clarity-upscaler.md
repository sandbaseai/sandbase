# Clarity Upscaler API: pricing, parameters and code examples

`clarity-ai/clarity-upscaler` · image generation model · ClarityAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Clarity Upscaler by ClarityAI - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clarity-ai/clarity-upscaler", "prompt": "masterpiece, best quality, highres", "image": "<image>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clarity-ai/clarity-upscaler', {'prompt': 'masterpiece, best quality, highres', 'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clarity-ai/clarity-upscaler", {
  "prompt": "masterpiece, best quality, highres",
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clarity-ai/clarity-upscaler", sandbase.Params{
	"prompt": "masterpiece, best quality, highres",
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same prompt given to the same version of Stable Diffusion will output the same image every time. range 0– |
| `image` | string | yes | The URL of the image to upscale.  |
| `prompt` | string | yes | The prompt to use for generating the image. Be as descriptive as possible for best results. default `"masterpiece, best quality, highres"` |
| `creativity` | number |  | The creativity of the model. The higher the creativity, the more the model will deviate from the prompt. Refers to the denoise strength of the sampling. default `0.35`; range 0–1 |
| `resemblance` | number |  | The resemblance of the upscaled image to the original image. The higher the resemblance, the more the model will try to keep the original image. Refers to the strength of the ControlNet. default `0.6`; range 0–1 |
| `guidance_scale` | number |  | The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `4`; range 0–20 |
| `upscale_factor` | number |  | The upscale factor default `2`; range 1–4 |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `18`; range 4–50 |

## Details

Clarity Upscaler enlarges an image up to 4× while adding detail; `creativity` and `resemblance` balance new detail against faithfulness.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | `masterpiece, best quality, highres` | Describe the content to guide added detail. |
| `image` | image URL, required | — | Image to upscale. JPEG, PNG, or WebP URL. |
| `guidance_scale` | number 0–20 | 4 | How strictly to follow the prompt. |
| `num_inference_steps` | integer 4–50 | 18 | More steps add detail and time. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `upscale_factor` | number 1–4 | 2 | 1–4×. |
| `resemblance` | number 0–1 | 0.6 | Higher stays closer to the input. |
| `creativity` | number 0–1 | 0.35 | Higher adds more invented detail. |

### Billing

$0.03 per image.

| Request | Price |
|---|---|
| One image | $0.03 |

Failed runs are not charged.

### Also on SandBase

Related: `topaz/upscale/image`.

---
Machine-readable: [`catalog/models/clarity-ai/clarity-upscaler.json`](../../../catalog/models/clarity-ai/clarity-upscaler.json) · Store page: https://www.sandbase.ai/model/clarity-ai/clarity-upscaler
