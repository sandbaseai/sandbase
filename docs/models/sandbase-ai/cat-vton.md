# try-on API: pricing, parameters and code examples

`sandbase-ai/cat-vton` · image generation model · sandbase-ai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00125 per call · **Modes:** async

CatVTON is a virtual try-on model. It dresses the person in a photo with a garment from a second image, with controls for the covered body area, guidance, steps, and aspect ratio.

## Pricing

- **$0.00125 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandbase-ai/cat-vton"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandbase-ai/cat-vton', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandbase-ai/cat-vton", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandbase-ai/cat-vton", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same input given to the same version of the model will output the same image every time.  |
| `cloth_type` | string |  | Type of the Cloth to be tried on. Options: upper: Upper body cloth lower: Lower body cloth overall: Full body cloth inner: Inner cloth, like T-shirt inside a jacket outer: Outer cloth, like a jacket over a T-shirt one of: `upper`, `lower`, `overall`, `inner`, `outer` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `guidance_scale` | number |  | The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `2.5`; range 0–20 |
| `human_image_url` | string |  | Url for the human image.  |
| `garment_image_url` | string |  | Url to the garment image.  |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `30`; range 1–50 |

## Details

CatVTON virtual try-on: dress the person in `human_image_url` with the garment in `garment_image_url`.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output frame shape. |
| `guidance_scale` | number 0–20 | 2.5 | How strictly to follow the garment. |
| `num_inference_steps` | integer 1–50 | 30 | More steps add detail and time. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `cloth_type` | `upper` / `lower` / `overall` / `inner` / `outer` | — | Which body area the garment covers. |
| `garment_image_url` | image URL | — | Photo of the garment. |
| `human_image_url` | image URL | — | Photo of the person. |

### Billing

$0.00125 per image.

| Request | Price |
|---|---|
| One image | $0.0013 |

Failed runs are not charged.

### Prompting

- Use a front-facing person photo and a flat garment photo.

---
Machine-readable: [`catalog/models/sandbase-ai/cat-vton.json`](../../../catalog/models/sandbase-ai/cat-vton.json) · Store page: https://www.sandbase.ai/model/sandbase-ai/cat-vton
