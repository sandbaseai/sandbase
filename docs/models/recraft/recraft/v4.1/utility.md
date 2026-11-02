# Recraft V4.1 Utility API: pricing, parameters and code examples

`recraft/recraft/v4.1/utility` · image generation model · Recraft · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.04 per run, depending on parameters · **Modes:** async

Recraft V4.1 Utility by Recraft - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.04 |

Formula: `0.04`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "recraft/recraft/v4.1/utility", "prompt": "Tilt-shift miniature effect on a real Portuguese fishing village at golden hour, colorful boats in the harbor appearing toy-like, selective focus band across the middle, saturated primary colors of blue red and yellow boats against white buildings, 90mm tilt-shift lens, the familiar made fantastical, Wes Anderson color sensibility"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('recraft/recraft/v4.1/utility', {'prompt': 'Tilt-shift miniature effect on a real Portuguese fishing village at golden hour, colorful boats in the harbor appearing toy-like, selective focus band across the middle, saturated primary colors of blue red and yellow boats against white buildings, 90mm tilt-shift lens, the familiar made fantastical, Wes Anderson color sensibility'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("recraft/recraft/v4.1/utility", {
  "prompt": "Tilt-shift miniature effect on a real Portuguese fishing village at golden hour, colorful boats in the harbor appearing toy-like, selective focus band across the middle, saturated primary colors of blue red and yellow boats against white buildings, 90mm tilt-shift lens, the familiar made fantastical, Wes Anderson color sensibility"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "recraft/recraft/v4.1/utility", sandbase.Params{
	"prompt": "Tilt-shift miniature effect on a real Portuguese fishing village at golden hour, colorful boats in the harbor appearing toy-like, selective focus band across the middle, saturated primary colors of blue red and yellow boats against white buildings, 90mm tilt-shift lens, the familiar made fantastical, Wes Anderson color sensibility",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `colors` | array |  | An array of preferable colors default `[]` |
| `prompt` | string | yes | Prompt  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `background_color` | string |  | The preferable background color of the generated images.  |

## Details

Recraft V4.1 Utility: fast, low-cost images for everyday design assets, with palette control.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `background_color` | string | — | Background color. |
| `colors` | object[] | `[]` | Preferred palette as RGB values. |

### Billing

$0.04 per image.

| Request | Price |
|---|---|
| One image | $0.04 |

Failed runs are not charged.

### Also on SandBase

Related: `recraft/recraft/v4.1`.

---
Machine-readable: [`catalog/models/recraft/recraft/v4.1/utility.json`](../../../../../catalog/models/recraft/recraft/v4.1/utility.json) · Store page: https://www.sandbase.ai/model/recraft/recraft/v4.1/utility
