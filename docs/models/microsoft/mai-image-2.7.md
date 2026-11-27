# MAI Image 2.7 Text to Image API: pricing, parameters and code examples

`microsoft/mai-image-2.7` · image generation model · Microsoft · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.07 per run, depending on parameters · **Modes:** async

MAI Image 2.7 by Microsoft turns a text prompt into a high-quality image, with optional transparent background.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.07 |

Formula: `0.07`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/mai-image-2.7", "aspect_ratio": "16:9", "prompt": "A golden retriever wearing a yellow raincoat on a rainy city street, cinematic photo"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('microsoft/mai-image-2.7', {'aspect_ratio': '16:9', 'prompt': 'A golden retriever wearing a yellow raincoat on a rainy city street, cinematic photo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("microsoft/mai-image-2.7", {
  "aspect_ratio": "16:9",
  "prompt": "A golden retriever wearing a yellow raincoat on a rainy city street, cinematic photo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "microsoft/mai-image-2.7", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "A golden retriever wearing a yellow raincoat on a rainy city street, cinematic photo",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text description of the image.  |
| `background` | string |  | transparent returns an alpha channel (png or webp output). one of: `opaque`, `transparent`; default `"opaque"` |
| `aspect_ratio` | string |  | Output shape, about 1-2 megapixels. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"1:1"` |
| `output_format` | string |  | Image file format. one of: `png`, `jpeg`, `webp`; default `"png"` |

## Details

MAI Image 2.7 is Microsoft's newest image model. It turns a text prompt into a photorealistic or illustrated image, with optional transparent background.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | What to draw. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `1:1` | Output shape. |
| `background` | `opaque` / `transparent` | `opaque` | `transparent` needs png or webp. |
| `output_format` | `png` / `jpeg` / `webp` | `png` | File format. |
### Billing
$0.07 per image. Failed runs are not charged.
### Also on SandBase
Related: `microsoft/mai-image-2.7/edit`, `microsoft/mai-image-2.5/edit`.

---
Machine-readable: [`catalog/models/microsoft/mai-image-2.7.json`](../../../catalog/models/microsoft/mai-image-2.7.json) · Store page: https://www.sandbase.ai/model/microsoft/mai-image-2.7
