# Nano Banana 2.1 Text to Image API: pricing, parameters and code examples

`google/nano-banana-2.1` · image generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.04 to $0.149 per run, depending on parameters · **Modes:** async

Nano Banana 2.1 is Google's latest fast image generation model, with better prompt adherence, cleaner text rendering, extreme aspect ratios and 1K to 4K output.

## Pricing

- Depends on parameters (`params.enable_image_search`, `params.enable_web_search`, `params.resolution`).

| parameters | USD |
|---|---|
| enable_image_search=false, enable_web_search=false, resolution="1K" | 0.04 |
| enable_image_search=false, enable_web_search=false, resolution="2K" | 0.06 |
| enable_image_search=false, enable_web_search=false, resolution="4K" | 0.135 |
| enable_image_search=false, enable_web_search=true, resolution="1K" | 0.054 |
| enable_image_search=false, enable_web_search=true, resolution="2K" | 0.074 |
| enable_image_search=false, enable_web_search=true, resolution="4K" | 0.149 |
| enable_image_search=true, enable_web_search=false, resolution="1K" | 0.054 |
| enable_image_search=true, enable_web_search=false, resolution="2K" | 0.074 |
| enable_image_search=true, enable_web_search=false, resolution="4K" | 0.149 |
| enable_image_search=true, enable_web_search=true, resolution="1K" | 0.054 |
| enable_image_search=true, enable_web_search=true, resolution="2K" | 0.074 |
| enable_image_search=true, enable_web_search=true, resolution="4K" | 0.149 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.135 : (params.resolution ?? "1K") == "2K" ? 0.06 : 0.04) + (((params.enable_web_search ?? false) || (params.enable_image_search ?? false)) ? 0.014 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-2.1", "aspect_ratio": "16:9", "prompt": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-2.1', {'aspect_ratio': '16:9', 'prompt': 'Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-2.1", {
  "aspect_ratio": "16:9",
  "prompt": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-2.1", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt to generate an image from. default `"A photo of a close-up portrait of an elderly Japanese ceramicist with deep, sun-etched wrinkles and a warm, knowing smile. He is carefully inspecting a freshly glazed tea bowl. The setting is his rustic, sun-drenched workshop. The scene is illuminated by soft, golden hour light streaming through a window, highlighting the fine texture of the clay. Captured with an 85mm portrait lens, resulting in a soft, blurred background (bokeh). The overall mood is serene and masterful. Vertical portrait orientation."` |
| `resolution` | string |  | The resolution of the image to generate. one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `4:1`, `1:4` …; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `enable_web_search` | boolean |  | Enable Google web search grounding to provide background context for image generation. default `false` |
| `enable_image_search` | boolean |  | Enable Google image search to retrieve web images as visual background reference for generation. default `false` |

---
Machine-readable: [`catalog/models/google/nano-banana-2.1.json`](../../../catalog/models/google/nano-banana-2.1.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-2.1
