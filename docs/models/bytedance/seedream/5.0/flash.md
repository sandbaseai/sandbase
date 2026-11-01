# Seedream 5.0 Flash Text to Image

`bytedance/seedream/5.0/flash` · image · Bytedance

Seedream 5.0 Flash is ByteDance's fast, low-cost Seedream 5.0 tier for high-volume text-to-image generation, with roughly 15–20 second turnaround and one flat price per image.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.0/flash", "aspect_ratio": "16:9", "prompt": "A minimalist poster with the text SANDBASE in bold letters"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.0/flash', {'aspect_ratio': '16:9', 'prompt': 'A minimalist poster with the text SANDBASE in bold letters'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.0/flash", {
  "aspect_ratio": "16:9",
  "prompt": "A minimalist poster with the text SANDBASE in bold letters"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.0/flash", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "A minimalist poster with the text SANDBASE in bold letters",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt to generate an image from. default `"Search for the popular elegant penguin meme, the penguin dons an all-black tactical techwear suit and narrow-frame futuristic sunglasses, riding a matte silver-black checkered manta ray flying vehicle; metal braided ropes, polar snowstorm backdrop, surreal futuristic techwear style, commercial fashion blockbuster aesthetic, high-definition with strong dynamic tension."` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Seedream 5.0 Flash: the fastest, lowest-cost Seedream 5.0 tier for high-volume generation, with roughly 15–20 second turnaround.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `1:1` | Output shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.018 per image.

| Request | Price |
|---|---|
| One image | $0.018 |

Failed runs are not charged.

### Prompting

- Write subject, layout, style, then light and color.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/4.5`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.0/flash.json`](../../../../../catalog/models/bytedance/seedream/5.0/flash.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.0/flash
