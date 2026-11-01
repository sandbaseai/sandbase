# FLUX.1 Kontext [dev]

`bfl/flux-2/kontext/dev` · image · BFL

Flux 2 Kontext Dev by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/kontext/dev", "image": "https://static.sandbase.ai/examples/d4b6c66d-af5e-4af7-9d4e-4d82e9f249ac/input/8fde3e25-c086-4505-bd6d-4b7c824136b5.webp", "prompt": "Change the setting to a day time, add a lot of people walking the sidewalk while maintaining the same style of the painting"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/kontext/dev', {'image': 'https://static.sandbase.ai/examples/d4b6c66d-af5e-4af7-9d4e-4d82e9f249ac/input/8fde3e25-c086-4505-bd6d-4b7c824136b5.webp', 'prompt': 'Change the setting to a day time, add a lot of people walking the sidewalk while maintaining the same style of the painting'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/kontext/dev", {
  "image": "https://static.sandbase.ai/examples/d4b6c66d-af5e-4af7-9d4e-4d82e9f249ac/input/8fde3e25-c086-4505-bd6d-4b7c824136b5.webp",
  "prompt": "Change the setting to a day time, add a lot of people walking the sidewalk while maintaining the same style of the painting"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/kontext/dev", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/d4b6c66d-af5e-4af7-9d4e-4d82e9f249ac/input/8fde3e25-c086-4505-bd6d-4b7c824136b5.webp",
	"prompt": "Change the setting to a day time, add a lot of people walking the sidewalk while maintaining the same style of the painting",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same prompt given to the same version of the model will output the same image every time.  |
| `image` | string | yes | The URL of the image to edit. Max width: 14142px, Max height: 14142px, Timeout: 20s  |
| `prompt` | string | yes | The prompt to edit the image.  |
| `output_format` | string |  | Output format one of: `jpeg`, `png`; default `"jpeg"` |
| `guidance_scale` | number |  | The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `2.5`; range 1–20 |
| `resolution_mode` | string |  | Determines how the output resolution is set for image editing. - `auto`: The model selects an optimal resolution from a predefined set that best matches the input image's aspect ratio. This is the recommended setting… one of: `auto`, `match_input`, `1:1`, `16:9`, `21:9`, `3:2`, `2:3`, `4:5`, `5:4`, `3:4`, `4:3`, `9:16` …; default `"match_input"` |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `28`; range 10–50 |

## Details

FLUX.1 Kontext [dev] edits a single image from an instruction: change objects, text, or style while keeping the rest consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | Image to edit. JPEG, PNG, or WebP URL. |
| `guidance_scale` | number 1–20 | 2.5 | How strictly to follow the prompt. |
| `num_inference_steps` | integer 10–50 | 28 | More steps add detail and time. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `resolution_mode` | `auto` / `match_input` / `1:1` / `16:9` / `21:9` / `3:2` / `2:3` / `4:5` / `5:4` / `3:4` / `4:3` / `9:16` / `9:21` | `match_input` | `match_input` keeps the input size; or choose a ratio. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.025 per image.

| Request | Price |
|---|---|
| One image | $0.025 |

Failed runs are not charged.

### Prompting

- State the change and what must stay the same.

### Limits

- One input image.

### Also on SandBase

Related: `bfl/flux-2/dev/edit` (FLUX.2, multi-image).

---
Machine-readable: [`catalog/models/bfl/flux-2/kontext/dev.json`](../../../../../catalog/models/bfl/flux-2/kontext/dev.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/kontext/dev
