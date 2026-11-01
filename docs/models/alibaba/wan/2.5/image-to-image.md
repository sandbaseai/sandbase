# Wan 2.5 Image to Image

`alibaba/wan/2.5/image-to-image` · image · Alibaba

Alibaba Wan 2.5 image-to-image model that edits one or more input images from a natural-language instruction, with selectable output aspect ratio.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.05 |

Formula: `0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.5/image-to-image", "images": ["https://static.sandbase.ai/examples/d92efef7-9913-4a55-bbe7-90fbfedf6e16/input/198eb29e-e2da-4e75-9519-0e9ddf903a3e.png"], "prompt": "Reimagine the scene under a raging thunderstorm at night: lightning forks across the sky, illuminating the samurai in stark flashes of white light."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.5/image-to-image', {'images': ['https://static.sandbase.ai/examples/d92efef7-9913-4a55-bbe7-90fbfedf6e16/input/198eb29e-e2da-4e75-9519-0e9ddf903a3e.png'], 'prompt': 'Reimagine the scene under a raging thunderstorm at night: lightning forks across the sky, illuminating the samurai in stark flashes of white light.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.5/image-to-image", {
  "images": [
    "https://static.sandbase.ai/examples/d92efef7-9913-4a55-bbe7-90fbfedf6e16/input/198eb29e-e2da-4e75-9519-0e9ddf903a3e.png"
  ],
  "prompt": "Reimagine the scene under a raging thunderstorm at night: lightning forks across the sky, illuminating the samurai in stark flashes of white light."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.5/image-to-image", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/d92efef7-9913-4a55-bbe7-90fbfedf6e16/input/198eb29e-e2da-4e75-9519-0e9ddf903a3e.png"},
	"prompt": "Reimagine the scene under a raging thunderstorm at night: lightning forks across the sky, illuminating the samurai in stark flashes of white light.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. If None, a random seed is chosen.  |
| `images` | array | yes | URLs of images to edit. For single-image editing, provide 1 URL. For multi-reference generation, provide up to 2 URLs. If more than 2 URLs are provided, only the first 2 will be used.  |
| `prompt` | string | yes | The text prompt describing how to edit the image. Max 2000 characters.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |

## Details

Wan 2.5 image editing: send one or more pictures and describe the change.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.05 per output image. Input images are not metered.

| Request | Price |
|---|---|
| One image | $0.05 |

Failed runs are not charged.

### Prompting

- State the change and what must stay the same.

### Limits

- One output image per request. Wan 2.7 is newer and cheaper.

### Also on SandBase

Other Wan 2.5 endpoints: `alibaba/wan/2.5/text-to-video`, `alibaba/wan/2.5/image-to-video`, `alibaba/wan/2.5/text-to-image`, `alibaba/wan/2.7/image-to-image` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.5/image-to-image.json`](../../../../../catalog/models/alibaba/wan/2.5/image-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.5/image-to-image
