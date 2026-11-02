# HiDream O1 Dev API: pricing, parameters and code examples

`hidream-ai/hidream-o1/dev` · image generation model · HiDream · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Hidream O1 Dev by hidream-ai - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hidream-ai/hidream-o1/dev", "prompt": "<prompt>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hidream-ai/hidream-o1/dev', {'prompt': '<prompt>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hidream-ai/hidream-o1/dev", {
  "prompt": "<prompt>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hidream-ai/hidream-o1/dev", sandbase.Params{
	"prompt": "<prompt>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible generation.  |
| `images` | array |  | Optional reference images. Use none for text-to-image, one for image editing, or multiple for subject-driven personalization. default `[]` |
| `prompt` | string | yes | Text prompt for image generation, editing, or subject-driven personalization.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

HiDream O1 Dev generates images from a prompt, or edits when you pass `images`.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `images` | image URL[] | `[]` | Images to edit or combine, Image 1, Image 2, … |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.02 per image.

| Request | Price |
|---|---|
| One image | $0.02 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.

---
Machine-readable: [`catalog/models/hidream-ai/hidream-o1/dev.json`](../../../../catalog/models/hidream-ai/hidream-o1/dev.json) · Store page: https://www.sandbase.ai/model/hidream-ai/hidream-o1/dev
