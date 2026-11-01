# MAI Image 2.5 Pro Edit

`microsoft/mai-image-2.5-pro/edit` · image · Microsoft

Mai Image 2.5 Pro Edit by Microsoft - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.29 |

Formula: `0.29`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "microsoft/mai-image-2.5-pro/edit", "prompt": "<prompt>", "image": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('microsoft/mai-image-2.5-pro/edit', {'prompt': '<prompt>', 'image': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("microsoft/mai-image-2.5-pro/edit", {
  "prompt": "<prompt>",
  "image": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "microsoft/mai-image-2.5-pro/edit", sandbase.Params{
	"prompt": "<prompt>",
	"image": "",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | The URL of the image to edit. Provide one http(s) or data: URL. default `""` |
| `prompt` | string | yes | The instruction describing how to edit the input image(s).  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

MAI Image 2.5 Pro edit: Microsoft's top image model for photoreal edits from an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | Image to edit. JPEG, PNG, or WebP URL. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |

### Billing

$0.29 per output image.

| Request | Price |
|---|---|
| One image | $0.29 |

Failed runs are not charged.

### Prompting

- State the change and what must stay.

### Also on SandBase

Related: `microsoft/mai-image-2.5/edit`.

---
Machine-readable: [`catalog/models/microsoft/mai-image-2.5-pro/edit.json`](../../../../catalog/models/microsoft/mai-image-2.5-pro/edit.json) · Store page: https://www.sandbase.ai/model/microsoft/mai-image-2.5-pro/edit
