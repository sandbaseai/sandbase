# Wan 2.5 Text to Image

`alibaba/wan/2.5/text-to-image` · image · Alibaba

Wan 2.5 is Alibaba's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language descriptions with exceptional detail and prompt adherence.

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
  -d '{"model": "alibaba/wan/2.5/text-to-image", "prompt": "A lone samurai standing on the edge of a cliff at twilight, overlooking a vast valley shrouded in mist. The sky burns with deep orange and purple hues from the setting sun, casting long, dramatic shadows. The samurai’s silhouette glows against the horizon, with their sword reflecting a glint of fading light. The overall style is hyper-realistic, cinematic, and moody, with dramatic contrast and atmospheric depth."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.5/text-to-image', {'prompt': 'A lone samurai standing on the edge of a cliff at twilight, overlooking a vast valley shrouded in mist. The sky burns with deep orange and purple hues from the setting sun, casting long, dramatic shadows. The samurai’s silhouette glows against the horizon, with their sword reflecting a glint of fading light. The overall style is hyper-realistic, cinematic, and moody, with dramatic contrast and atmospheric depth.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.5/text-to-image", {
  "prompt": "A lone samurai standing on the edge of a cliff at twilight, overlooking a vast valley shrouded in mist. The sky burns with deep orange and purple hues from the setting sun, casting long, dramatic shadows. The samurai’s silhouette glows against the horizon, with their sword reflecting a glint of fading light. The overall style is hyper-realistic, cinematic, and moody, with dramatic contrast and atmospheric depth."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.5/text-to-image", sandbase.Params{
	"prompt": "A lone samurai standing on the edge of a cliff at twilight, overlooking a vast valley shrouded in mist. The sky burns with deep orange and purple hues from the setting sun, casting long, dramatic shadows. The samurai’s silhouette glows against the horizon, with their sword reflecting a glint of fading light. The overall style is hyper-realistic, cinematic, and moody, with dramatic contrast and atmospheric depth.",
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
| `prompt` | string | yes | The prompt for image generation. Supports Chinese and English, max 2000 characters.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |

## Details

Wan 2.5 text-to-image: one image from a written brief in Chinese or English.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.05 per image.

| Request | Price |
|---|---|
| One image | $0.05 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light and color.

### Limits

- One image per request. Wan 2.7 is newer and cheaper.

### Also on SandBase

Other Wan 2.5 endpoints: `alibaba/wan/2.5/text-to-video`, `alibaba/wan/2.5/image-to-video`, `alibaba/wan/2.5/image-to-image`, `alibaba/wan/2.7/text-to-image` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.5/text-to-image.json`](../../../../../catalog/models/alibaba/wan/2.5/text-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.5/text-to-image
