# Gemini Omni Flash 1.1 Text to Video API: pricing, parameters and code examples

`google/gemini-omni-flash/1.1/text-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.09 to $3 per run, depending on parameters · **Modes:** async

Gemini Omni Flash 1.1 is Google's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="360p" | 0.09 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=3, resolution="4k" | 0.9 |
| duration=8, resolution="360p" | 0.24 |
| duration=8, resolution="720p" | 0.8 |
| duration=8, resolution="1080p" | 1.2 |
| duration=8, resolution="4k" | 2.4 |
| duration=10, resolution="360p" | 0.3 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |
| duration=10, resolution="4k" | 3 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "360p" ? 0.03 : (params.resolution ?? "720p") == "1080p" ? 0.15 : (params.resolution ?? "720p") == "4k" ? 0.30 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.1/text-to-video", "duration": 3, "prompt": "A red ball bounces once on a wooden floor, single continuous shot, no dialogue.", "resolution": "360p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.1/text-to-video', {'duration': 3, 'prompt': 'A red ball bounces once on a wooden floor, single continuous shot, no dialogue.', 'resolution': '360p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.1/text-to-video", {
  "duration": 3,
  "prompt": "A red ball bounces once on a wooden floor, single continuous shot, no dialogue.",
  "resolution": "360p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.1/text-to-video", sandbase.Params{
	"duration": 3,
	"prompt": "A red ball bounces once on a wooden floor, single continuous shot, no dialogue.",
	"resolution": "360p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt describing the video you want to generate.  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–10 |
| `resolution` | string |  | The resolution of the generated video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash 1.1 generates a 3–10 second clip with synchronized audio from a written prompt. It is Google's Gemini-native video model, built for fast turnaround and strong prompt following.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |

### Billing

You pay for output seconds: $0.03 at 360p, $0.10 at 720p, $0.15 at 1080p, and $0.30 at 4K.

| Output | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s | $0.09 | $0.30 | $0.45 | $0.90 |
| 8s (default) | $0.24 | $0.80 | $1.20 | $2.40 |
| 10s | $0.30 | $1.00 | $1.50 | $3.00 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in plain sentences.
- Quote dialogue and name the speaker.

### Limits

- 16:9 or 9:16 only.

### Also on SandBase

Other Gemini Omni Flash 1.1 endpoints: `google/gemini-omni-flash/1.1/image-to-video`, `google/gemini-omni-flash/1.1/reference-to-video`, `google/gemini-omni-flash/1.1/edit`, `google/gemini-omni-flash/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.1/text-to-video.json`](../../../../../catalog/models/google/gemini-omni-flash/1.1/text-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.1/text-to-video
