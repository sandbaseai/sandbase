# Midjourney V8.1 API: pricing, parameters and code examples

`midjourney/midjourney-v8.1` · image generation model · Midjourney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.08 to $0.12 per run, depending on parameters · **Modes:** async

Midjourney V8.1 text-to-image generation.

## Pricing

- Depends on parameters (`params.quality`, `params.speed`).

| parameters | USD |
|---|---|
| quality="standard", speed="draft" | 0.08 |
| quality="standard", speed="fast" | 0.1 |
| quality="hd", speed="draft" | 0.08 |
| quality="hd", speed="fast" | 0.12 |

Formula: `(params.speed ?? "fast") == "draft" ? 0.08 : ((params.quality ?? "standard") == "hd" ? 0.12 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "midjourney/midjourney-v8.1", "prompt": "Square flash sale poster for a pair of white running shoes on a bright yellow background. A headline that reads exactly: \"FLASH SALE\". Show the old price \"Was $129.00\" with a strikethrough line, and the new price \"Now $89.00\" larger next to it. At the bottom, a line that reads exactly: \"Ends 2026.10.03\". Render the text exactly as written, with no other text anywhere in the image."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('midjourney/midjourney-v8.1', {'prompt': 'Square flash sale poster for a pair of white running shoes on a bright yellow background. A headline that reads exactly: "FLASH SALE". Show the old price "Was $129.00" with a strikethrough line, and the new price "Now $89.00" larger next to it. At the bottom, a line that reads exactly: "Ends 2026.10.03". Render the text exactly as written, with no other text anywhere in the image.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("midjourney/midjourney-v8.1", {
  "prompt": "Square flash sale poster for a pair of white running shoes on a bright yellow background. A headline that reads exactly: \"FLASH SALE\". Show the old price \"Was $129.00\" with a strikethrough line, and the new price \"Now $89.00\" larger next to it. At the bottom, a line that reads exactly: \"Ends 2026.10.03\". Render the text exactly as written, with no other text anywhere in the image."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "midjourney/midjourney-v8.1", sandbase.Params{
	"prompt": "Square flash sale poster for a pair of white running shoes on a bright yellow background. A headline that reads exactly: \"FLASH SALE\". Show the old price \"Was $129.00\" with a strikethrough line, and the new price \"Now $89.00\" larger next to it. At the bottom, a line that reads exactly: \"Ends 2026.10.03\". Render the text exactly as written, with no other text anywhere in the image.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `speed` | string |  | Generation speed. one of: `draft`, `fast`; default `"fast"` |
| `prompt` | string | yes | Text prompt used to generate the image.  |
| `quality` | string |  | Output quality. HD is unavailable with draft speed. one of: `standard`, `hd`; default `"standard"` |

## Details

Midjourney V8.1 text-to-image: Midjourney's distinctive aesthetic, with draft and HD options.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 1,024 characters. |
| `speed` | `draft` / `fast` | `fast` | `draft` is faster and cheaper. |
| `quality` | `standard` / `hd` | `standard` | `hd` renders at higher resolution. |

### Billing

Per request: $0.08 draft, $0.10 standard, $0.12 HD.

| Mode | Price |
|---|---|
| Draft | $0.08 |
| Fast, standard | $0.10 |
| Fast, HD | $0.12 |

Failed runs are not charged.

### Prompting

- Midjourney prompt style works: subject, style, and parameters like `--ar 16:9`.

---
Machine-readable: [`catalog/models/midjourney/midjourney-v8.1.json`](../../../catalog/models/midjourney/midjourney-v8.1.json) · Store page: https://www.sandbase.ai/model/midjourney/midjourney-v8.1
