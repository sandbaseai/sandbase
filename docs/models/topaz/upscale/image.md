# Topaz Upscale

`topaz/upscale/image` · image · Topaz Labs

Upscale Image is Topaz Labs's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`usage.height`, `usage.width`).

Formula: `((usage.width ?? 0) * (usage.height ?? 0) / 1000000) <= 0 ? 1.36 : ((usage.width * usage.height / 1000000) <= 24 ? 0.08 : ((usage.width * usage.height / 1000000) <= 48 ? 0.16 : ((usage.width * usage.height / 1000000) <= 96 ? 0.32 : 1.36)))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "topaz/upscale/image", "crop_to_fill": false, "enhancement_model": "High Fidelity V2", "face_enhancement": false, "image": "https://static.sandbase.ai/examples/5f434c76-3c13-4430-ac6e-a044487d42b4/input/235e21e0-6bcc-4297-853b-0d3db8894545.png", "output_format": "png", "prompt": "Preserve the original panoramic composition, geometry, colors, and details while increasing resolution. Do not crop, reframe, or add new objects.", "upscale_factor": 2.844444444444445}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('topaz/upscale/image', {'crop_to_fill': False, 'enhancement_model': 'High Fidelity V2', 'face_enhancement': False, 'image': 'https://static.sandbase.ai/examples/5f434c76-3c13-4430-ac6e-a044487d42b4/input/235e21e0-6bcc-4297-853b-0d3db8894545.png', 'output_format': 'png', 'prompt': 'Preserve the original panoramic composition, geometry, colors, and details while increasing resolution. Do not crop, reframe, or add new objects.', 'upscale_factor': 2.844444444444445})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("topaz/upscale/image", {
  "crop_to_fill": false,
  "enhancement_model": "High Fidelity V2",
  "face_enhancement": false,
  "image": "https://static.sandbase.ai/examples/5f434c76-3c13-4430-ac6e-a044487d42b4/input/235e21e0-6bcc-4297-853b-0d3db8894545.png",
  "output_format": "png",
  "prompt": "Preserve the original panoramic composition, geometry, colors, and details while increasing resolution. Do not crop, reframe, or add new objects.",
  "upscale_factor": 2.844444444444445
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "topaz/upscale/image", sandbase.Params{
	"crop_to_fill": false,
	"enhancement_model": "High Fidelity V2",
	"face_enhancement": false,
	"image": "https://static.sandbase.ai/examples/5f434c76-3c13-4430-ac6e-a044487d42b4/input/235e21e0-6bcc-4297-853b-0d3db8894545.png",
	"output_format": "png",
	"prompt": "Preserve the original panoramic composition, geometry, colors, and details while increasing resolution. Do not crop, reframe, or add new objects.",
	"upscale_factor": 2.844444444444445,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Url of the image to be upscaled  |
| `detail` | number |  | Detail recovery level (0.0-1.0). Applies to Recovery V2 model only. range 0–1 |
| `prompt` | string | yes | Text prompt to guide generative upscaling (max 1024 chars). Applies to Redefine model only.  |
| `denoise` | number |  | Denoising level (0.0-1.0). Applies to Standard V2, Low Resolution V2, CGI, High Fidelity V2, Text Refine, and Redefine models. range 0–1 |
| `sharpen` | number |  | Sharpening level (0.0-1.0). Applies to Standard V2, Low Resolution V2, CGI, High Fidelity V2, Text Refine, and Redefine models. range 0–1 |
| `texture` | integer |  | Texture detail level for generative upscaling (1-5). Applies to Redefine model only. range 1–5 |
| `strength` | number |  | Enhancement strength (0.01-1.0). Applies to Text Refine model only. range 0.01–1 |
| `autoprompt` | boolean |  | Enable automatic prompt generation for generative upscaling. Applies to Redefine model only.  |
| `creativity` | integer |  | Creativity level for generative upscaling (1-6). Higher values produce more creative/hallucinated details. Applies to Redefine model only. range 1–6 |
| `crop_to_fill` | boolean |  | Crop To Fill default `false` |
| `output_format` | string |  | Output format of the upscaled image. one of: `jpeg`, `png`; default `"jpeg"` |
| `upscale_factor` | number |  | Factor to upscale the image by (e.g. 2.0 doubles width and height) default `2`; range 1–4 |
| `fix_compression` | number |  | Compression artifact removal level (0.0-1.0). Applies to Standard V2, Low Resolution V2, High Fidelity V2, and Text Refine models. range 0–1 |
| `face_enhancement` | boolean |  | Whether to apply face enhancement to the image. Applies to standard enhance and Recovery V2 models. default `true` |
| `enhancement_model` | string |  | Model to use for image enhancement. one of: `Low Resolution V2`, `Standard V2`, `CGI`, `High Fidelity V2`, `Text Refine`, `Recovery`, `Redefine`, `Recovery V2`, `Standard MAX`, `Wonder`; default `"Standard V2"` |
| `subject_detection` | string |  | Subject detection mode for the image enhancement. Applies to standard enhance and Recovery V2 models. one of: `All`, `Foreground`, `Background`; default `"All"` |
| `face_enhancement_strength` | number |  | Strength of the face enhancement. 0.0 means no enhancement, 1.0 means maximum enhancement. Ignored if face enhancement is disabled. default `0.8`; range 0–1 |
| `face_enhancement_creativity` | number |  | Creativity level for face enhancement. 0.0 means no creativity, 1.0 means maximum creativity. Ignored if face enhancement is disabled. default `0`; range 0–1 |

## Details

Topaz upscales and enhances images with model presets for low-resolution, CGI, high-fidelity, and face recovery work.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Optional description for generative models. |
| `image` | image URL, required | — | Image to upscale. JPEG, PNG, or WebP URL. |
| `strength` | number 0.01–1 | — | Enhancement strength (0.01-1.0). |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `face_enhancement_creativity` | number 0–1 | 0 | Creativity level for face enhancement. |
| `enhancement_model` | `Low Resolution V2` / `Standard V2` / `CGI` / `High Fidelity V2` / `Text Refine` / `Recovery` / `Redefine` / `Recovery V2` / `Standard MAX` / `Wonder` | `Standard V2` | Model preset. |
| `subject_detection` | `All` / `Foreground` / `Background` | `All` | Subject detection mode for the image enhancement. |
| `crop_to_fill` | boolean | false |  |
| `fix_compression` | number 0–1 | — | Compression artifact removal level (0.0-1.0). |
| `face_enhancement_strength` | number 0–1 | 0.8 | Strength of the face enhancement. |
| `detail` | number 0–1 | — | Detail recovery level (0.0-1.0). |
| `creativity` | integer 1–6 | — | Creativity level for generative upscaling (1-6). |
| `autoprompt` | boolean | — | Enable automatic prompt generation for generative upscaling. |
| `sharpen` | number 0–1 | — | Sharpening level (0.0-1.0). |
| `upscale_factor` | number 1–4 | 2 | 1–4×. |
| `texture` | integer 1–5 | — | Texture detail level for generative upscaling (1-5). |
| `denoise` | number 0–1 | — | Denoising level (0.0-1.0). |
| `face_enhancement` | boolean | true | Restore faces. |

### Billing

Billed by output size: $0.08 up to 24MP, $0.16 up to 48MP, $0.32 up to 96MP, $1.36 above. The quote before submission assumes the top tier; the final charge uses the measured output.

| Output | Price |
|---|---|
| 2× of a 4MP photo (16MP) | $0.08 |
| 4× of a 2MP photo (32MP) | $0.16 |
| 4× of a 6MP photo (96MP) | $0.32 |

Failed runs are not charged.

### Also on SandBase

Related: `clarity-ai/clarity-upscaler`, `bytedance/seedvr/upscale/image`.

---
Machine-readable: [`catalog/models/topaz/upscale/image.json`](../../../../catalog/models/topaz/upscale/image.json) · Store page: https://www.sandbase.ai/model/topaz/upscale/image
