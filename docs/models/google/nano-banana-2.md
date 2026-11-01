# Nano Banana 2 Text to Image

`google/nano-banana-2` · image · Google

Nano Banana 2 is Google's new state-of-the-art fast image generation and editing model

## Pricing

- Depends on parameters (`params.enable_image_search`, `params.enable_web_search`, `params.resolution`).

| parameters | USD |
|---|---|
| enable_image_search=false, enable_web_search=false, resolution="0.5K" | 0.045 |
| enable_image_search=false, enable_web_search=false, resolution="1K" | 0.067 |
| enable_image_search=false, enable_web_search=false, resolution="2K" | 0.101 |
| enable_image_search=false, enable_web_search=false, resolution="4K" | 0.151 |
| enable_image_search=false, enable_web_search=true, resolution="0.5K" | 0.059 |
| enable_image_search=false, enable_web_search=true, resolution="1K" | 0.081 |
| enable_image_search=false, enable_web_search=true, resolution="2K" | 0.115 |
| enable_image_search=false, enable_web_search=true, resolution="4K" | 0.165 |
| enable_image_search=true, enable_web_search=false, resolution="0.5K" | 0.059 |
| enable_image_search=true, enable_web_search=false, resolution="1K" | 0.081 |
| enable_image_search=true, enable_web_search=false, resolution="2K" | 0.115 |
| enable_image_search=true, enable_web_search=false, resolution="4K" | 0.165 |
| enable_image_search=true, enable_web_search=true, resolution="0.5K" | 0.059 |
| enable_image_search=true, enable_web_search=true, resolution="1K" | 0.081 |
| enable_image_search=true, enable_web_search=true, resolution="2K" | 0.115 |
| enable_image_search=true, enable_web_search=true, resolution="4K" | 0.165 |

Formula: `((params.resolution ?? "1K") == "0.5K" ? 0.045 : (params.resolution ?? "1K") == "2K" ? 0.101 : (params.resolution ?? "1K") == "4K" ? 0.151 : 0.067) + (((params.enable_web_search ?? false) || (params.enable_image_search ?? false)) ? 0.014 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-2", "aspect_ratio": "3:4", "prompt": "A photo of a glossy magazine cover, the minimal blue cover has the large bold words Nano Banana. The text is in a serif font and fills the view. No other text. In front of the text there is a portrait of a person in a sleek and minimal dress. She is playfully holding the number 2, which is the focal point. Put the issue number and \"Feb 2026\" date in the corner along with a barcode. The magazine is on a shelf against an orange plastered wall, within a designer store."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-2', {'aspect_ratio': '3:4', 'prompt': 'A photo of a glossy magazine cover, the minimal blue cover has the large bold words Nano Banana. The text is in a serif font and fills the view. No other text. In front of the text there is a portrait of a person in a sleek and minimal dress. She is playfully holding the number 2, which is the focal point. Put the issue number and "Feb 2026" date in the corner along with a barcode. The magazine is on a shelf against an orange plastered wall, within a designer store.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-2", {
  "aspect_ratio": "3:4",
  "prompt": "A photo of a glossy magazine cover, the minimal blue cover has the large bold words Nano Banana. The text is in a serif font and fills the view. No other text. In front of the text there is a portrait of a person in a sleek and minimal dress. She is playfully holding the number 2, which is the focal point. Put the issue number and \"Feb 2026\" date in the corner along with a barcode. The magazine is on a shelf against an orange plastered wall, within a designer store."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-2", sandbase.Params{
	"aspect_ratio": "3:4",
	"prompt": "A photo of a glossy magazine cover, the minimal blue cover has the large bold words Nano Banana. The text is in a serif font and fills the view. No other text. In front of the text there is a portrait of a person in a sleek and minimal dress. She is playfully holding the number 2, which is the focal point. Put the issue number and \"Feb 2026\" date in the corner along with a barcode. The magazine is on a shelf against an orange plastered wall, within a designer store.",
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
| `resolution` | string |  | The resolution of the image to generate. one of: `0.5K`, `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `4:1`, `1:4` …; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `enable_web_search` | boolean |  | Enable Google web search grounding to provide background context for image generation. default `false` |
| `enable_image_search` | boolean |  | Enable Google image search to retrieve web images as visual background reference for generation. default `false` |

## Details

Nano Banana 2 (Gemini 3.1 Flash Image) is Google's fast image model with near-Pro quality, extreme aspect ratios up to 8:1, and optional web and image search grounding for current or factual subjects.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` / `4:1` / `1:4` / `8:1` / `1:8` | `1:1` | Output frame shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `resolution` | `0.5K` / `1K` / `2K` / `4K` | `1K` | Sets the per-image rate. |
| `enable_web_search` | boolean | false | Ground the image in Google Search results. |
| `enable_image_search` | boolean | false | Use image search results as visual references. |

### Billing

$0.045 at 0.5K, $0.067 at 1K, $0.101 at 2K, and $0.151 at 4K per image, Google's list price. Turning on `enable_web_search` or `enable_image_search` adds $0.014 per request (charged once even if both are on).

| Request | 0.5K | 1K | 2K | 4K |
|---|---|---|---|---|
| One image | $0.045 | $0.067 | $0.101 | $0.151 |

Failed runs are not charged.

### Prompting

- Turn on `enable_web_search` for real places, products, or events.
- Quote all text that must appear.

### Limits

- One image per request.

### Also on SandBase

Other Nano Banana endpoints: `google/nano-banana-pro`, `google/nano-banana-pro/edit`, `google/nano-banana-2/edit`, `google/nano-banana-2-lite`, `google/nano-banana-2-lite/edit`.

---
Machine-readable: [`catalog/models/google/nano-banana-2.json`](../../../catalog/models/google/nano-banana-2.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-2
