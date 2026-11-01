# Nano Banana 2 Lite Edit

`google/nano-banana-2-lite/edit` · image · Google

Nano Banana 2 Lite Edit is Google's low-latency, cost-efficient image editing model (Gemini 3.1 Flash Lite Image). Edit and combine supplied images with a text prompt; output is a 1K image.

## Pricing

- **$0.0336 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-2-lite/edit", "images": ["https://static.sandbase.ai/examples/17b5627b-8b12-4fc0-9e93-72f557c3fced/input/56496fc5-007b-4821-b507-b6b1b60e9408.png"], "prompt": "make the background light blue"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-2-lite/edit', {'images': ['https://static.sandbase.ai/examples/17b5627b-8b12-4fc0-9e93-72f557c3fced/input/56496fc5-007b-4821-b507-b6b1b60e9408.png'], 'prompt': 'make the background light blue'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-2-lite/edit", {
  "images": [
    "https://static.sandbase.ai/examples/17b5627b-8b12-4fc0-9e93-72f557c3fced/input/56496fc5-007b-4821-b507-b6b1b60e9408.png"
  ],
  "prompt": "make the background light blue"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-2-lite/edit", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/17b5627b-8b12-4fc0-9e93-72f557c3fced/input/56496fc5-007b-4821-b507-b6b1b60e9408.png"},
	"prompt": "make the background light blue",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The seed for the random number generator.  |
| `images` | array | yes | The URLs of the images to use for image-to-image generation or image editing.  |
| `prompt` | string | yes | The prompt for image editing.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. Leave empty to keep the aspect ratio of the input image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `system_prompt` | string |  | Optional system instruction that steers the model's persona and output style across the request. Leave blank to omit; when provided, it is sent as the system instruction to Gemini (or as a system message on… default `""` |
| `thinking_level` | string |  | When set, enables model thinking with the given level ('minimal' or 'high') and includes thoughts in the generation. Omit to disable. one of: `minimal`, `high` |

## Details

Nano Banana 2 Lite Edit: fast, low-cost edits and multi-image composition at 1K with Gemini 3.1 Flash Lite Image.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `system_prompt` | string | — | Optional standing instructions applied to every request. |
| `thinking_level` | `minimal` / `high` | — | `high` reasons more about the prompt before drawing; `minimal` is faster. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.0336 per 1K image, Google's list price.

| Request | Price |
|---|---|
| One image | $0.0336 |

Failed runs are not charged.

### Prompting

- Keep prompts direct; use `thinking_level: high` for complex layouts.

### Limits

- Output is 1K only.

### Also on SandBase

Other Nano Banana endpoints: `google/nano-banana-pro`, `google/nano-banana-pro/edit`, `google/nano-banana-2`, `google/nano-banana-2/edit`, `google/nano-banana-2-lite`.

---
Machine-readable: [`catalog/models/google/nano-banana-2-lite/edit.json`](../../../../catalog/models/google/nano-banana-2-lite/edit.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-2-lite/edit
