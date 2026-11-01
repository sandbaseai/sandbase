# Nano Banana Pro Text to Image

`google/nano-banana-pro` · image · Google

Nano Banana Pro is Google's new state-of-the-art image generation and editing model

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution="1K" | 0.134 |
| resolution="2K" | 0.134 |
| resolution="4K" | 0.24 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.24 : 0.134)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-pro", "aspect_ratio": "1:1", "prompt": "Present a clear, 45° top-down isometric miniature 3D cartoon scene of London, featuring its most iconic landmarks and architectural elements. Use soft, refined textures with realistic PBR materials and gentle, lifelike lighting and shadows. Integrate the current weather conditions directly into the city environment to create an immersive atmospheric mood. Use a clean, minimalistic composition with a soft, solid-colored background. At the top-center, place the title \"London\" in large bold text, a prominent weather icon beneath it, then the date (small text) and temperature (medium text). All text must be centered with consistent spacing, and may subtly overlap the tops of the buildings."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-pro', {'aspect_ratio': '1:1', 'prompt': 'Present a clear, 45° top-down isometric miniature 3D cartoon scene of London, featuring its most iconic landmarks and architectural elements. Use soft, refined textures with realistic PBR materials and gentle, lifelike lighting and shadows. Integrate the current weather conditions directly into the city environment to create an immersive atmospheric mood. Use a clean, minimalistic composition with a soft, solid-colored background. At the top-center, place the title "London" in large bold text, a prominent weather icon beneath it, then the date (small text) and temperature (medium text). All text must be centered with consistent spacing, and may subtly overlap the tops of the buildings.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-pro", {
  "aspect_ratio": "1:1",
  "prompt": "Present a clear, 45° top-down isometric miniature 3D cartoon scene of London, featuring its most iconic landmarks and architectural elements. Use soft, refined textures with realistic PBR materials and gentle, lifelike lighting and shadows. Integrate the current weather conditions directly into the city environment to create an immersive atmospheric mood. Use a clean, minimalistic composition with a soft, solid-colored background. At the top-center, place the title \"London\" in large bold text, a prominent weather icon beneath it, then the date (small text) and temperature (medium text). All text must be centered with consistent spacing, and may subtly overlap the tops of the buildings."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-pro", sandbase.Params{
	"aspect_ratio": "1:1",
	"prompt": "Present a clear, 45° top-down isometric miniature 3D cartoon scene of London, featuring its most iconic landmarks and architectural elements. Use soft, refined textures with realistic PBR materials and gentle, lifelike lighting and shadows. Integrate the current weather conditions directly into the city environment to create an immersive atmospheric mood. Use a clean, minimalistic composition with a soft, solid-colored background. At the top-center, place the title \"London\" in large bold text, a prominent weather icon beneath it, then the date (small text) and temperature (medium text). All text must be centered with consistent spacing, and may subtly overlap the tops of the buildings.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt to generate an image from. default `"a cat sitting on a windowsill, golden hour lighting, photorealistic"` |
| `resolution` | string |  | The resolution of the image to generate. one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Nano Banana Pro (Gemini 3 Pro Image) is Google's highest-quality image model: strong reasoning over the prompt, accurate multilingual text in the image, and 1K to 4K output.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `1:1` | Output frame shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `resolution` | `1K` / `2K` / `4K` | `1K` | Sets the per-image rate. |

### Billing

$0.134 per image at 1K or 2K and $0.24 at 4K, Google's list price.

| Request | 1K | 2K | 4K |
|---|---|---|---|
| One image | $0.134 | $0.134 | $0.24 |

Failed runs are not charged.

### Prompting

- Describe the image like a brief to a designer: subject, layout, style, and text.
- Quote all text that must appear.
- Use 2K or 4K for posters and print.

### Limits

- One image per request.

### Also on SandBase

Other Nano Banana endpoints: `google/nano-banana-pro/edit`, `google/nano-banana-2`, `google/nano-banana-2/edit`, `google/nano-banana-2-lite`, `google/nano-banana-2-lite/edit`.

---
Machine-readable: [`catalog/models/google/nano-banana-pro.json`](../../../catalog/models/google/nano-banana-pro.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-pro
