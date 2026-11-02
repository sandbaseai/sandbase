# Ideogram 3.0 Text to Image API: pricing, parameters and code examples

`ideogram-ai/ideogram-v3` · image generation model · Ideogram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.03 to $0.09 per run, depending on parameters · **Modes:** async

3.0 is Ideogram's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language descriptions with exceptional detail and prompt adherence.

## Pricing

- Depends on parameters (`params.rendering_speed`).

| parameters | USD |
|---|---|
| rendering_speed="TURBO" | 0.03 |
| rendering_speed="BALANCED" | 0.06 |
| rendering_speed="QUALITY" | 0.09 |

Formula: `(params.rendering_speed ?? "BALANCED") == "TURBO" ? 0.03 : (params.rendering_speed ?? "BALANCED") == "QUALITY" ? 0.09 : 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ideogram-ai/ideogram-v3", "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in router.ai\""}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ideogram-ai/ideogram-v3', {'prompt': 'The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes "Ideogram V3 in router.ai"'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ideogram-ai/ideogram-v3", {
  "prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in router.ai\""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ideogram-ai/ideogram-v3", sandbase.Params{
	"prompt": "The Bone Forest stretched across the horizon, its trees fashioned from the ossified remains of ancient leviathans that once swam through the sky. Shamans with antlers growing from their shoulders and eyes that revealed the true nature of any being they beheld conducted rituals to commune with the spirits that still inhabited the calcified grove. In sky writes \"Ideogram V3 in router.ai\"",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for the random number generator  |
| `images` | array |  | A set of images to use as style references (maximum total size 10MB across all style references). The images should be in JPEG, PNG or WebP format  |
| `prompt` | string | yes | Prompt  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `rendering_speed` | string |  | The rendering speed to use. one of: `TURBO`, `BALANCED`, `QUALITY`; default `"BALANCED"` |

## Details

Ideogram 3.0 text-to-image with strong typography, at three rendering speeds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Optional style references. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `rendering_speed` | `TURBO` / `BALANCED` / `QUALITY` | `BALANCED` | Sets the per-image rate. |

### Billing

Per image: $0.03 Turbo, $0.06 Balanced, $0.09 Quality.

| Speed | Price |
|---|---|
| TURBO | $0.03 |
| BALANCED | $0.06 |
| QUALITY | $0.09 |

Failed runs are not charged.

### Prompting

- Quote all text that must appear.

### Also on SandBase

Related: `ideogram/4.5` (newer).

---
Machine-readable: [`catalog/models/ideogram-ai/ideogram-v3.json`](../../../catalog/models/ideogram-ai/ideogram-v3.json) · Store page: https://www.sandbase.ai/model/ideogram-ai/ideogram-v3
