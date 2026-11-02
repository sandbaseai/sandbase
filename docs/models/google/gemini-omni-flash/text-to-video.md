# Gemini Omni Flash Text to Video API: pricing, parameters and code examples

`google/gemini-omni-flash/text-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.39 to $1.3 per run, depending on parameters · **Modes:** async

Gemini Omni Flash is Google's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.39 |
| duration=8 | 1.04 |
| duration=10 | 1.3 |

Formula: `(params.duration ?? 8) * 0.13`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/text-to-video", "duration": 3, "prompt": "A paper boat drifts down a rain-soaked gutter, single continuous shot, no dialogue"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/text-to-video', {'duration': 3, 'prompt': 'A paper boat drifts down a rain-soaked gutter, single continuous shot, no dialogue'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/text-to-video", {
  "duration": 3,
  "prompt": "A paper boat drifts down a rain-soaked gutter, single continuous shot, no dialogue"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/text-to-video", sandbase.Params{
	"duration": 3,
	"prompt": "A paper boat drifts down a rain-soaked gutter, single continuous shot, no dialogue",
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
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash generates a 3–10 second clip with synchronized audio from a written prompt. It is Google's Gemini-native video model, built for fast turnaround and strong prompt following.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |

### Billing

You pay $0.13 per output second.

| Output | Price |
|---|---|
| 3s | $0.39 |
| 8s (default) | $1.04 |
| 10s | $1.30 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in plain sentences.
- Quote dialogue and name the speaker.

### Limits

- 16:9 or 9:16 only.

### Also on SandBase

Other Gemini Omni Flash endpoints: `google/gemini-omni-flash/image-to-video`, `google/gemini-omni-flash/reference-to-video`, `google/gemini-omni-flash/edit`, `google/gemini-omni-flash/1.1/text-to-video` (newer).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/text-to-video.json`](../../../../catalog/models/google/gemini-omni-flash/text-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/text-to-video
