# Gemini Omni Flash 1.2 Edit API: pricing, parameters and code examples

`google/gemini-omni-flash/1.2/edit` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.832 per call · **Modes:** async

Gemini Omni Flash 1.2 Edit by Google applies natural-language edits to an existing video of up to 15 seconds, such as swapping objects, backgrounds, lighting, or style, at 360p to 4K output.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `Math.min(15.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05)) * 0.02 + Math.max(3.0, Math.min(15.0, Math.ceil((usage.duration ?? media_duration(params.video) ?? 8.0) - 0.05))) * ((params.resolution ?? "720p") == "360p" ? 0.028 : (params.resolution ?? "720p") == "1080p" ? 0.126 : (params.resolution ?? "720p") == "4k" ? 0.252 : 0.084)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.2/edit", "prompt": "Make this video anime. Keep everything else the same.", "video": "https://static.sandbase.ai/examples/google/gemini-omni-flash/edit/input_video_0.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.2/edit', {'prompt': 'Make this video anime. Keep everything else the same.', 'video': 'https://static.sandbase.ai/examples/google/gemini-omni-flash/edit/input_video_0.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.2/edit", {
  "prompt": "Make this video anime. Keep everything else the same.",
  "video": "https://static.sandbase.ai/examples/google/gemini-omni-flash/edit/input_video_0.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.2/edit", sandbase.Params{
	"prompt": "Make this video anime. Keep everything else the same.",
	"video": "https://static.sandbase.ai/examples/google/gemini-omni-flash/edit/input_video_0.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the video to edit. Must be at most 15 seconds long.  |
| `prompt` | string | yes | A simple instruction describing the edit.  |
| `resolution` | string |  | The resolution of the edited video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |

## Details

Gemini Omni Flash 1.2 edit: change an existing clip of up to 15 seconds with an instruction, such as swapping a product or background, or changing lighting, weather, or style, while the rest of the scene stays consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `video` | video URL, required | — | Source clip, up to 15 seconds. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |

### Billing

Billing counts the source and the output: $0.02 per source second plus the output rate ($0.028 at 360p, $0.084 at 720p, $0.126 at 1080p, and $0.252 at 4K) for the same length, with a 3-second minimum on the output. Source length is rounded up to the next whole second. The quote before submission assumes an 8-second source.

| Source clip | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s source | $0.14 | $0.31 | $0.44 | $0.82 |
| 8s source | $0.38 | $0.83 | $1.17 | $2.18 |
| 10s source | $0.48 | $1.04 | $1.46 | $2.72 |
| 15s source | $0.72 | $1.56 | $2.19 | $4.08 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay the same.

### Limits

- Source clips longer than 15 seconds are rejected.

### Also on SandBase

Other Gemini Omni Flash 1.2 endpoints: `google/gemini-omni-flash/1.2/text-to-video`, `google/gemini-omni-flash/1.2/image-to-video`, `google/gemini-omni-flash/1.2/reference-to-video`, `google/gemini-omni-flash/1.1/edit` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.2/edit.json`](../../../../../catalog/models/google/gemini-omni-flash/1.2/edit.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.2/edit
