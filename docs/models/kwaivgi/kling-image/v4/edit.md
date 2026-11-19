# Kling Image V4 Edit API: pricing, parameters and code examples

`kwaivgi/kling-image/v4/edit` · image generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.06615 to $1.42065 per run, depending on parameters · **Modes:** async

Kling Image V4 Edit by Kuaishou edits or recomposes 1 to 10 reference images from a text instruction at native 2K, 4K or 8K resolution.

## Pricing

- Depends on parameters (`params.images`, `params.num_images`, `params.resolution`).

| parameters | USD |
|---|---|
| num_images=1, resolution="2K" | 0.06615 |
| num_images=1, resolution="4K" | 0.09765 |
| num_images=1, resolution="8K" | 0.16065 |
| num_images=9, resolution="2K" | 0.57015 |
| num_images=9, resolution="4K" | 0.85365 |
| num_images=9, resolution="8K" | 1.42065 |

Formula: `(params.num_images ?? 1) * ((params.resolution ?? "2K") == "8K" ? 0.1575 : (params.resolution ?? "2K") == "4K" ? 0.0945 : 0.063) + len(params.images ?? []) * 0.00315`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-image/v4/edit", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/af741566-8852-406d-be61-8044f265442c/input/ceb31edd-5be2-40d9-a2fa-7be80bf0160b.png"], "prompt": "Place the sneaker from @Image1 on a mossy rock beside a mountain stream at dawn, soft mist, keep the shoe design, colours and the KITO heel tab exactly."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-image/v4/edit', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/af741566-8852-406d-be61-8044f265442c/input/ceb31edd-5be2-40d9-a2fa-7be80bf0160b.png'], 'prompt': 'Place the sneaker from @Image1 on a mossy rock beside a mountain stream at dawn, soft mist, keep the shoe design, colours and the KITO heel tab exactly.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-image/v4/edit", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/af741566-8852-406d-be61-8044f265442c/input/ceb31edd-5be2-40d9-a2fa-7be80bf0160b.png"
  ],
  "prompt": "Place the sneaker from @Image1 on a mossy rock beside a mountain stream at dawn, soft mist, keep the shoe design, colours and the KITO heel tab exactly."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-image/v4/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/af741566-8852-406d-be61-8044f265442c/input/ceb31edd-5be2-40d9-a2fa-7be80bf0160b.png"},
	"prompt": "Place the sneaker from @Image1 on a mossy rock beside a mountain stream at dawn, soft mist, keep the shoe design, colours and the KITO heel tab exactly.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | 1-10 reference images (JPG/PNG, up to 30 MB, min 300 px, aspect ratio 2:5-5:2), referenced as @Image1, @Image2, ...  |
| `prompt` | string | yes | Describe the image. Refer to reference images as @Image1, @Image2, ...  |
| `num_images` | integer |  | Number of independent images to generate (1-9). default `1`; range 1–9 |
| `resolution` | string |  | Output resolution. 8K is native ultra-high resolution. one of: `2K`, `4K`, `8K`; default `"2K"` |
| `aspect_ratio` | string |  | Output frame shape. auto picks one from the prompt and references. one of: `auto`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`; default `"auto"` |

## Details

Kling Image V4 Edit edits or recomposes 1–10 reference images from a text instruction, at native 2K, 4K or 8K.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Refer to inputs as `@Image1`, `@Image2`, … |
| `images` | image URL[], required | — | 1–10 images (JPG/PNG, up to 30 MB, at least 300 px per side, aspect ratio 2:5–5:2). |
| `aspect_ratio` | `auto` / `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `3:2` / `2:3` / `21:9` | `auto` | `auto` picks a shape from the prompt and references. |
| `resolution` | `2K` / `4K` / `8K` | `2K` | Native output resolution. |
| `num_images` | 1–9 | 1 | Independent images, each billed. |
### Billing
Per output image by resolution, plus $0.00315 per reference image.
| Request | Price |
|---|---|
| 1 reference, 2K (default) | $0.06615 |
| 3 references, 4K | $0.10395 |
| 1 reference, 8K | $0.16065 |
Failed runs are not charged.
### Prompting
- Say what to change and what to keep, e.g. "put the bottle from @Image1 on the table in @Image2, keep its label".
### Also on SandBase
Other Kling Image V4 endpoints: `kwaivgi/kling-image/v4`, `kwaivgi/kling-image/v4/edit`, `kwaivgi/kling-image/v4/long-image`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-image/v4/edit.json`](../../../../../catalog/models/kwaivgi/kling-image/v4/edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-image/v4/edit
