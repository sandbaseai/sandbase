# Kling Image V4 Long Image API: pricing, parameters and code examples

`kwaivgi/kling-image/v4/long-image` · image generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.235 to $0.8617 per run, depending on parameters · **Modes:** async

Kling Image V4 Long Image by Kuaishou designs one complete ultra-tall image, such as an ecommerce product detail page from 1 to 3 product photos or a full webpage visual.

## Pricing

- Depends on parameters (`params.images`, `params.length`, `params.resolution`, `params.skill`, `params.style_image`, `params.subject_image`).

| parameters | USD |
|---|---|
| length="short", resolution="1K", skill="webpage" | 0.5483 |
| length="short", resolution="1K", skill="ecommerce" | 0.235 |
| length="short", resolution="2K", skill="webpage" | 0.5953 |
| length="short", resolution="2K", skill="ecommerce" | 0.282 |
| length="medium", resolution="1K", skill="webpage" | 0.5483 |
| length="medium", resolution="1K", skill="ecommerce" | 0.47 |
| length="medium", resolution="2K", skill="webpage" | 0.5953 |
| length="medium", resolution="2K", skill="ecommerce" | 0.5483 |
| length="long", resolution="1K", skill="webpage" | 0.5483 |
| length="long", resolution="1K", skill="ecommerce" | 0.7833 |
| length="long", resolution="2K", skill="webpage" | 0.5953 |
| length="long", resolution="2K", skill="ecommerce" | 0.8617 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-image/v4/long-image", "prompt": "Design a complete website for a specialty coffee brand as one long image: hero section, product showcase, roasting philosophy, store information and footer."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-image/v4/long-image', {'prompt': 'Design a complete website for a specialty coffee brand as one long image: hero section, product showcase, roasting philosophy, store information and footer.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-image/v4/long-image", {
  "prompt": "Design a complete website for a specialty coffee brand as one long image: hero section, product showcase, roasting philosophy, store information and footer."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-image/v4/long-image", sandbase.Params{
	"prompt": "Design a complete website for a specialty coffee brand as one long image: hero section, product showcase, roasting philosophy, store information and footer.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `skill` | string |  | webpage: website design. ecommerce: product detail page, requires 1-3 product images. one of: `webpage`, `ecommerce`; default `"webpage"` |
| `images` | array |  | ecommerce only: 1-3 product images, referenced as @Image1, @Image2, ...  |
| `length` | string |  | ecommerce only: short (~2-5 sections), medium (~6-10) or long (~11-18). one of: `short`, `medium`, `long`; default `"medium"` |
| `prompt` | string | yes | Describe the page. Refer to product images as @Image1, @Image2, ...  |
| `resolution` | string |  | Output resolution. one of: `1K`, `2K`; default `"1K"` |
| `style_image` | string |  | webpage only: optional style reference for the visual and layout style.  |
| `subject_image` | string |  | webpage only: optional subject the design is built around.  |

## Details

Kling Image V4 Long Image designs one complete ultra-tall image: an ecommerce product detail page built from 1–3 product photos, or a full webpage visual.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe the page. Refer to product images as `@Image1`, … |
| `skill` | `webpage` / `ecommerce` | `webpage` | `ecommerce` requires `images`. |
| `images` | image URL[] | — | ecommerce only: 1–3 product images. |
| `style_image` | image URL | — | webpage only: visual and layout style reference. |
| `subject_image` | image URL | — | webpage only: subject to design around. |
| `length` | `short` / `medium` / `long` | `medium` | ecommerce only: about 2–5, 6–10 or 11–18 sections. |
| `resolution` | `1K` / `2K` | `1K` | Output resolution. |
### Billing
Per long image, plus $0.00315 per input image.
| Request | 1K | 2K |
|---|---|---|
| webpage | $0.5483 | $0.5953 |
| ecommerce, short | $0.235 | $0.282 |
| ecommerce, medium | $0.47 | $0.5483 |
| ecommerce, long | $0.7833 | $0.8617 |
Failed runs are not charged.
### Prompting
- For ecommerce, list only real product facts; the model builds the key visual, selling points and usage scenes.
### Also on SandBase
Other Kling Image V4 endpoints: `kwaivgi/kling-image/v4`, `kwaivgi/kling-image/v4/edit`, `kwaivgi/kling-image/v4/long-image`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-image/v4/long-image.json`](../../../../../catalog/models/kwaivgi/kling-image/v4/long-image.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-image/v4/long-image
