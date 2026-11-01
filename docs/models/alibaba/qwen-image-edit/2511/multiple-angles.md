# Qwen Image Edit 2511 Multiple Angles

`alibaba/qwen-image-edit/2511/multiple-angles` · image · Alibaba

Qwen Image Edit 2511 Multiple Angles by Alibaba - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.035 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen-image-edit/2511/multiple-angles"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/qwen-image-edit/2511/multiple-angles', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/qwen-image-edit/2511/multiple-angles", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/qwen-image-edit/2511/multiple-angles", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility.  |
| `zoom` | number |  | Camera zoom/distance. 0=wide shot (far away), 5=medium shot (normal), 10=close-up (very close). default `5`; range 0–10 |
| `images` | array |  | The URL of the image to adjust camera angle for.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the output image one of: `png`, `jpeg`; default `"png"` |
| `vertical_angle` | number |  | Vertical camera angle in degrees. -30°=low-angle shot (looking up), 0°=eye-level, 30°=elevated, 60°=high-angle, 90°=bird's-eye view (looking down). default `0`; range -30–90 |
| `horizontal_angle` | number |  | Horizontal rotation angle around the object in degrees. 0°=front view, 90°=right side, 180°=back view, 270°=left side, 360°=front view again. default `0`; range 0–360 |
| `additional_prompt` | string |  | Additional text to append to the automatically generated prompt.  |

## Details

Re-render a subject from a new camera angle. Set the rotation, tilt, and zoom and Qwen Image Edit 2511 infers the unseen sides while keeping shape, color, and branding consistent; useful for product turnarounds and character sheets.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[] | — | Image(s) of the subject. |
| `output_format` | `png` / `jpeg` | `png` | Output file format. |
| `vertical_angle` | number -30–90 | 0 | Camera tilt in degrees (−30 to 90). |
| `horizontal_angle` | number 0–360 | 0 | Camera rotation around the subject in degrees (0–360). |
| `zoom` | number 0–10 | 5 | 0 is far, 10 is close. |
| `additional_prompt` | string | — | Optional extra instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.035 per output image.

| Request | Price |
|---|---|
| One view | $0.035 |

Failed runs are not charged.

### Prompting

- Call once per view and keep `seed` fixed for a consistent set.
- Use a clean, well-lit input with the whole subject visible.

### Limits

- One view per request; there is no text prompt beyond `additional_prompt`.

### Also on SandBase

Related: `alibaba/qwen-image-edit`, `alibaba/qwen-image-edit/2511`.

---
Machine-readable: [`catalog/models/alibaba/qwen-image-edit/2511/multiple-angles.json`](../../../../../catalog/models/alibaba/qwen-image-edit/2511/multiple-angles.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen-image-edit/2511/multiple-angles
