# Gemini Omni Flash Edit API: pricing, parameters and code examples

`google/gemini-omni-flash/edit` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.2 per call · **Modes:** async

Gemini Omni Flash Edit by Google applies natural-language edits to an existing short video, such as changing style, lighting, or objects, while keeping the rest of the scene consistent.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`).

Formula: `Math.min(10.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05)) * 0.02 + Math.max(3.0, Math.min(10.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05))) * 0.13`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/edit", "prompt": "Make this video look like a pencil sketch. Keep everything else the same.", "video": "https://static.sandbase.ai/examples/8858006e-f268-46ec-9472-2987d3c14ed6/input/cd37fee6-abad-43a3-b5e0-55fb785ea7fd.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/edit', {'prompt': 'Make this video look like a pencil sketch. Keep everything else the same.', 'video': 'https://static.sandbase.ai/examples/8858006e-f268-46ec-9472-2987d3c14ed6/input/cd37fee6-abad-43a3-b5e0-55fb785ea7fd.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/edit", {
  "prompt": "Make this video look like a pencil sketch. Keep everything else the same.",
  "video": "https://static.sandbase.ai/examples/8858006e-f268-46ec-9472-2987d3c14ed6/input/cd37fee6-abad-43a3-b5e0-55fb785ea7fd.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/edit", sandbase.Params{
	"prompt": "Make this video look like a pencil sketch. Keep everything else the same.",
	"video": "https://static.sandbase.ai/examples/8858006e-f268-46ec-9472-2987d3c14ed6/input/cd37fee6-abad-43a3-b5e0-55fb785ea7fd.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the video to edit. Note: editing uploaded videos is not available for users in the European Economic Area (EEA), Switzerland, and the United Kingdom.  |
| `prompt` | string | yes | A simple instruction describing the edit. Simple prompts work best; add "Keep everything else the same." to preserve the rest of the scene. Voice editing is not supported.  |

## Details

Gemini Omni Flash edit: change an existing clip of up to 10 seconds with an instruction, such as style, lighting, or objects, while the rest of the scene stays consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `video` | video URL, required | — | Source clip, up to 10 seconds. |

### Billing

Billing counts the source and the output: $0.02 per source second plus $0.13 per output second for the same length, with a 3-second minimum on the output. The quote before submission assumes an 8-second source.

| Source clip | Price |
|---|---|
| 3s source | $0.45 |
| 5s source | $0.75 |
| 8s source | $1.20 |
| 10s source | $1.50 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay the same.

### Limits

- Source clips longer than 10 seconds are billed and processed as 10 seconds.

### Also on SandBase

Other Gemini Omni Flash endpoints: `google/gemini-omni-flash/text-to-video`, `google/gemini-omni-flash/image-to-video`, `google/gemini-omni-flash/reference-to-video`, `google/gemini-omni-flash/1.1/edit` (newer).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/edit.json`](../../../../catalog/models/google/gemini-omni-flash/edit.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/edit
