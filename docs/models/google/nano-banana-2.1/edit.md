# Nano Banana 2.1 Edit

`google/nano-banana-2.1/edit` · image · Google

Nano Banana 2.1 Edit is Google's latest fast image editing model, fusing up to 14 reference images with stronger subject consistency and 1K to 4K output.

## Pricing

- Depends on parameters (`params.enable_image_search`, `params.enable_web_search`, `params.images`, `params.resolution`).

| parameters | USD |
|---|---|
| enable_image_search=false, enable_web_search=false, resolution="1K" | 0.044 |
| enable_image_search=false, enable_web_search=false, resolution="2K" | 0.064 |
| enable_image_search=false, enable_web_search=false, resolution="4K" | 0.139 |
| enable_image_search=false, enable_web_search=true, resolution="1K" | 0.058 |
| enable_image_search=false, enable_web_search=true, resolution="2K" | 0.078 |
| enable_image_search=false, enable_web_search=true, resolution="4K" | 0.153 |
| enable_image_search=true, enable_web_search=false, resolution="1K" | 0.058 |
| enable_image_search=true, enable_web_search=false, resolution="2K" | 0.078 |
| enable_image_search=true, enable_web_search=false, resolution="4K" | 0.153 |
| enable_image_search=true, enable_web_search=true, resolution="1K" | 0.058 |
| enable_image_search=true, enable_web_search=true, resolution="2K" | 0.078 |
| enable_image_search=true, enable_web_search=true, resolution="4K" | 0.153 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.135 : (params.resolution ?? "1K") == "2K" ? 0.06 : 0.04) + (((params.enable_web_search ?? false) || (params.enable_image_search ?? false)) ? 0.014 : 0.0) + 0.002 * len(params.images ?? [])`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-2.1/edit", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/88fdad83-3d16-4b09-9da0-f8ce8bdca922.png", "https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/d324832d-9607-4c10-a226-b596cf215649.png"], "prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-2.1/edit', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/88fdad83-3d16-4b09-9da0-f8ce8bdca922.png', 'https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/d324832d-9607-4c10-a226-b596cf215649.png'], 'prompt': 'Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-2.1/edit", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/88fdad83-3d16-4b09-9da0-f8ce8bdca922.png",
    "https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/d324832d-9607-4c10-a226-b596cf215649.png"
  ],
  "prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-2.1/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/88fdad83-3d16-4b09-9da0-f8ce8bdca922.png", "https://static.sandbase.ai/examples/99a6fd8e-c5a0-4107-85fe-28c24782d8a3/input/d324832d-9607-4c10-a226-b596cf215649.png"},
	"prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | The URLs of the images to use for image-to-image generation or image editing.  |
| `prompt` | string | yes | The text prompt to generate an image from. default `"Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humurous scene."` |
| `resolution` | string |  | The resolution of the image to generate. one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. Leave empty to keep the aspect ratio of the input image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `4:1`, `1:4` … |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `enable_web_search` | boolean |  | Enable Google web search grounding to provide background context for image generation. default `false` |
| `enable_image_search` | boolean |  | Enable Google image search to retrieve web images as visual background reference for generation. default `false` |

---
Machine-readable: [`catalog/models/google/nano-banana-2.1/edit.json`](../../../../catalog/models/google/nano-banana-2.1/edit.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-2.1/edit
