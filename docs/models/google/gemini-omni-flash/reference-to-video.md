# Gemini Omni Flash Reference to Video API: pricing, parameters and code examples

`google/gemini-omni-flash/reference-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.39 to $1.3 per run, depending on parameters · **Modes:** async

Gemini Omni Flash Reference to Video by Google generates a short video with synchronized audio that keeps subjects, products, or style consistent with up to ten reference images.

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
  -d '{"model": "google/gemini-omni-flash/reference-to-video", "duration": 3, "images": ["https://static.sandbase.ai/examples/784ab4ef-cb5b-4f97-a2a5-1d3604406ed1/input/f7a55771-75b2-4550-ae86-e08d9086fe4c.jpg"], "prompt": "A calm shoreline in the style of <IMAGE_REF_0>, slow pan, no dialogue"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/reference-to-video', {'duration': 3, 'images': ['https://static.sandbase.ai/examples/784ab4ef-cb5b-4f97-a2a5-1d3604406ed1/input/f7a55771-75b2-4550-ae86-e08d9086fe4c.jpg'], 'prompt': 'A calm shoreline in the style of <IMAGE_REF_0>, slow pan, no dialogue'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/reference-to-video", {
  "duration": 3,
  "images": [
    "https://static.sandbase.ai/examples/784ab4ef-cb5b-4f97-a2a5-1d3604406ed1/input/f7a55771-75b2-4550-ae86-e08d9086fe4c.jpg"
  ],
  "prompt": "A calm shoreline in the style of <IMAGE_REF_0>, slow pan, no dialogue"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/reference-to-video", sandbase.Params{
	"duration": 3,
	"images": []any{"https://static.sandbase.ai/examples/784ab4ef-cb5b-4f97-a2a5-1d3604406ed1/input/f7a55771-75b2-4550-ae86-e08d9086fe4c.jpg"},
	"prompt": "A calm shoreline in the style of <IMAGE_REF_0>, slow pan, no dialogue",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | URLs of the reference images to incorporate into the video.  |
| `prompt` | string | yes | The text prompt describing the video. You can bind reference images to roles inline using tags like ``<IMAGE_REF_0>`` (see the Omni Flash prompt guide).  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–10 |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash reference-to-video: up to 10 reference images keep subjects, products, or style consistent in a new clip with synchronized audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `images` | image URL[] (≤10) | — | Up to 10 reference images, Image 1, Image 2, … |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay $0.13 per output second.

| Output | Price |
|---|---|
| 3s | $0.39 |
| 8s (default) | $1.04 |
| 10s | $1.30 |

Failed runs are not charged.

### Prompting

- Give each reference a role and refer to it by number.

### Limits

- Send at least one reference.

### Also on SandBase

Other Gemini Omni Flash endpoints: `google/gemini-omni-flash/text-to-video`, `google/gemini-omni-flash/image-to-video`, `google/gemini-omni-flash/edit`, `google/gemini-omni-flash/1.1/reference-to-video` (newer).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/reference-to-video.json`](../../../../catalog/models/google/gemini-omni-flash/reference-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/reference-to-video
