# Gemini Omni Flash 1.1 Edit API: pricing, parameters and code examples

`google/gemini-omni-flash/1.1/edit` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.12 per call · **Modes:** async

Gemini Omni Flash 1.1 Edit by Google applies natural-language edits to an existing video of up to ten seconds, such as changing style, lighting, or objects, at 360p to 4K output.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `Math.min(10.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05)) * 0.02 + Math.max(3.0, Math.min(10.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05))) * ((params.resolution ?? "720p") == "360p" ? 0.04 : (params.resolution ?? "720p") == "1080p" ? 0.18 : (params.resolution ?? "720p") == "4k" ? 0.36 : 0.12)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.1/edit", "prompt": "Make this video look like a watercolor painting. Keep everything else the same.", "resolution": "1080p", "video": "https://static.sandbase.ai/examples/dc14a58a-ac90-45a2-8041-931e6bafb192/input/dc716dd9-2ff4-443f-ac62-0d7c64e7381e.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.1/edit', {'prompt': 'Make this video look like a watercolor painting. Keep everything else the same.', 'resolution': '1080p', 'video': 'https://static.sandbase.ai/examples/dc14a58a-ac90-45a2-8041-931e6bafb192/input/dc716dd9-2ff4-443f-ac62-0d7c64e7381e.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.1/edit", {
  "prompt": "Make this video look like a watercolor painting. Keep everything else the same.",
  "resolution": "1080p",
  "video": "https://static.sandbase.ai/examples/dc14a58a-ac90-45a2-8041-931e6bafb192/input/dc716dd9-2ff4-443f-ac62-0d7c64e7381e.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.1/edit", sandbase.Params{
	"prompt": "Make this video look like a watercolor painting. Keep everything else the same.",
	"resolution": "1080p",
	"video": "https://static.sandbase.ai/examples/dc14a58a-ac90-45a2-8041-931e6bafb192/input/dc716dd9-2ff4-443f-ac62-0d7c64e7381e.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the video to edit.  |
| `prompt` | string | yes | A simple instruction describing the edit.  |
| `resolution` | string |  | The resolution of the edited video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |

## Details

Gemini Omni Flash 1.1 edit: change an existing clip of up to 10 seconds with an instruction, such as style, lighting, or objects, while the rest of the scene stays consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `video` | video URL, required | — | Source clip, up to 10 seconds. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |

### Billing

Billing counts the source and the output: $0.02 per source second plus the output rate ($0.04 at 360p, $0.12 at 720p, $0.18 at 1080p, $0.36 at 4K) for the same length, with a 3-second minimum on the output. The quote before submission assumes an 8-second source.

| Source clip | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s source | $0.18 | $0.42 | $0.60 | $1.14 |
| 5s source | $0.30 | $0.70 | $1.00 | $1.90 |
| 8s source | $0.48 | $1.12 | $1.60 | $3.04 |
| 10s source | $0.60 | $1.40 | $2.00 | $3.80 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay the same.

### Limits

- Source clips longer than 10 seconds are billed and processed as 10 seconds.

### Also on SandBase

Other Gemini Omni Flash 1.1 endpoints: `google/gemini-omni-flash/1.1/text-to-video`, `google/gemini-omni-flash/1.1/image-to-video`, `google/gemini-omni-flash/1.1/reference-to-video`, `google/gemini-omni-flash/edit` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.1/edit.json`](../../../../../catalog/models/google/gemini-omni-flash/1.1/edit.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.1/edit
