# Wan 2.7 Pro Text to Image API: pricing, parameters and code examples

`alibaba/wan/2.7/pro/text-to-image` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.075 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.7 Pro text-to-image model with enhanced quality and selectable aspect ratio.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.075 |

Formula: `0.075`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/pro/text-to-image", "prompt": "A red paper lantern hanging in a quiet bamboo forest at dusk"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/pro/text-to-image', {'prompt': 'A red paper lantern hanging in a quiet bamboo forest at dusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/pro/text-to-image", {
  "prompt": "A red paper lantern hanging in a quiet bamboo forest at dusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/pro/text-to-image", sandbase.Params{
	"prompt": "A red paper lantern hanging in a quiet bamboo forest at dusk",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The prompt to generate an image from. default `"A futuristic glass library building with organic curved walls surrounded by cherry blossom trees, blue sky with scattered clouds, architectural visualization, golden ratio composition"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`; default `"16:9"` |

## Details

Wan 2.7 Pro renders a written brief at higher fidelity than the standard tier, with sharper fine detail and more reliable text in the image. Chinese and English prompts are both supported.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | `16:9` | Output shape. |

### Billing

$0.075 per image, Alibaba's list price.

| Request | Price |
|---|---|
| One image | $0.075 |

Failed runs are not charged.

### Prompting

- Put the main subject first, then layout, materials, and lighting.
- Quote any text that must be rendered, and say where it goes.

> A glass library with organic curved walls among cherry trees, blue sky with scattered clouds, architectural visualization, golden-ratio composition.

### Limits

- One image per request.

### Also on SandBase

Other Wan 2.7 image endpoints: `alibaba/wan/2.7/text-to-image`, `alibaba/wan/2.7/image-to-image`, `alibaba/wan/2.7/pro/image-to-image`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/pro/text-to-image.json`](../../../../../../catalog/models/alibaba/wan/2.7/pro/text-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/pro/text-to-image
