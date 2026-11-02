# Ideogram 4.5 Edit API: pricing, parameters and code examples

`ideogram/4.5/edit` · image generation model · Ideogram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.008 to $0.22 per run, depending on parameters · **Modes:** async

Ideogram 4.5 edits an image from a text instruction, with an optional mask and style references, with reliable text rendering and polished graphic design output.

## Pricing

- Depends on parameters (`params.quality`).

| parameters | USD |
|---|---|
| quality="very_low" | 0.008 |
| quality="low" | 0.03 |
| quality="medium" | 0.06 |
| quality="high" | 0.22 |

Formula: `(params.quality ?? "medium") == "high" ? 0.22 : (params.quality ?? "medium") == "low" ? 0.03 : (params.quality ?? "medium") == "very_low" ? 0.008 : 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ideogram/4.5/edit", "image": "https://static.sandbase.ai/examples/c74a47c4-e59b-48f1-a093-03df5ef017cd/input/72ce2e87-7134-46b2-aedf-d0ac4e1d71de.png", "prompt": "add the word SALE in red", "quality": "very_low"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ideogram/4.5/edit', {'image': 'https://static.sandbase.ai/examples/c74a47c4-e59b-48f1-a093-03df5ef017cd/input/72ce2e87-7134-46b2-aedf-d0ac4e1d71de.png', 'prompt': 'add the word SALE in red', 'quality': 'very_low'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ideogram/4.5/edit", {
  "image": "https://static.sandbase.ai/examples/c74a47c4-e59b-48f1-a093-03df5ef017cd/input/72ce2e87-7134-46b2-aedf-d0ac4e1d71de.png",
  "prompt": "add the word SALE in red",
  "quality": "very_low"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ideogram/4.5/edit", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/c74a47c4-e59b-48f1-a093-03df5ef017cd/input/72ce2e87-7134-46b2-aedf-d0ac4e1d71de.png",
	"prompt": "add the word SALE in red",
	"quality": "very_low",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mask` | string |  | Mask matching the source dimensions. Black edits, white preserves. Must contain both regions after rounding.  |
| `seed` | integer |  | Random seed. Omit to choose automatically.  |
| `image` | string | yes | Primary source image to edit.  |
| `prompt` | string | yes | The generation or editing prompt.  |
| `quality` | string |  | Quality tier for either edit precision. Defaults to medium. one of: `very_low`, `low`, `medium`, `high`; default `"medium"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `edit_precision` | string |  | regular uses Generate; high uses Precise Edit with unchanged-pixel restoration. Both always prepare structured edit instructions. one of: `regular`, `high`; default `"regular"` |
| `reference_image_urls` | array |  | Up to four references plus the primary source, or three references plus the primary source and mask.  |

## Details

Ideogram 4.5 edit: change an image from an instruction, with an optional mask and style references.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `image` | image URL, required | — | Image to edit. JPEG, PNG, or WebP URL. |
| `mask` | image URL | — | Optional mask; white areas are edited. |
| `edit_precision` | `regular` / `high` | `regular` | `high` keeps unmasked areas closer to the original. |
| `reference_image_urls` | image URL[] | — | Optional style references. |
| `quality` | `very_low` / `low` / `medium` / `high` | `medium` | Sets the per-image rate. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

Per output image: $0.008 very low, $0.03 low, $0.06 medium, $0.22 high.

| Quality | Price |
|---|---|
| very_low | $0.008 |
| low | $0.03 |
| medium | $0.06 |
| high | $0.22 |

Failed runs are not charged.

### Prompting

- Use a mask for local edits.

### Also on SandBase

Related: `ideogram/4.5`.

---
Machine-readable: [`catalog/models/ideogram/4.5/edit.json`](../../../../catalog/models/ideogram/4.5/edit.json) · Store page: https://www.sandbase.ai/model/ideogram/4.5/edit
