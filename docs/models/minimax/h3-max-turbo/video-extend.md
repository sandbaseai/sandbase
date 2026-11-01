# MiniMax H3 Max Turbo Video Extend

`minimax/h3-max-turbo/video-extend` · video · MiniMax

MiniMax H3 Max Turbo, the fastest tier of the H3 family, continues an existing video with 1-15 seconds of new footage with native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480P" | 0.025 |
| duration=1, resolution="768P" | 0.04 |
| duration=1, resolution="1080P" | 0.08 |
| duration=1, resolution="2K" | 0.16 |
| duration=5, resolution="480P" | 0.125 |
| duration=5, resolution="768P" | 0.2 |
| duration=5, resolution="1080P" | 0.4 |
| duration=5, resolution="2K" | 0.8 |
| duration=15, resolution="480P" | 0.375 |
| duration=15, resolution="768P" | 0.6 |
| duration=15, resolution="1080P" | 1.2 |
| duration=15, resolution="2K" | 2.4 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768P") == "480P" ? 0.025 : (params.resolution ?? "768P") == "1080P" ? 0.08 : (params.resolution ?? "768P") == "2K" ? 0.16 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-max-turbo/video-extend", "duration": 1, "output": "continuation", "prompt": "the red panda keeps walking", "resolution": "480P", "video": "https://static.sandbase.ai/examples/b2271e8d-deb2-4284-9c26-65e71970825c/input/01a2e4dc-561e-48b4-8e31-86c1a102f2cd.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-max-turbo/video-extend', {'duration': 1, 'output': 'continuation', 'prompt': 'the red panda keeps walking', 'resolution': '480P', 'video': 'https://static.sandbase.ai/examples/b2271e8d-deb2-4284-9c26-65e71970825c/input/01a2e4dc-561e-48b4-8e31-86c1a102f2cd.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-max-turbo/video-extend", {
  "duration": 1,
  "output": "continuation",
  "prompt": "the red panda keeps walking",
  "resolution": "480P",
  "video": "https://static.sandbase.ai/examples/b2271e8d-deb2-4284-9c26-65e71970825c/input/01a2e4dc-561e-48b4-8e31-86c1a102f2cd.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-max-turbo/video-extend", sandbase.Params{
	"duration": 1,
	"output": "continuation",
	"prompt": "the red panda keeps walking",
	"resolution": "480P",
	"video": "https://static.sandbase.ai/examples/b2271e8d-deb2-4284-9c26-65e71970825c/input/01a2e4dc-561e-48b4-8e31-86c1a102f2cd.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for the continuation. Random when omitted.  |
| `video` | string | yes | URL of the video to extend. Must be 1.625 s to 60 s long, up to 50 MB, aspect ratio between 0.4 and 2.5.  |
| `output` | string |  | 'extended' returns the whole source video followed by the new footage. 'continuation' returns only the generated continuation. one of: `extended`, `continuation`; default `"extended"` |
| `prompt` | string | yes | What happens next. Describe the continuation, not the source.  |
| `duration` | integer |  | Seconds of new footage to add after the source. The actual duration may be slightly longer. default `5`; range 1–15 |
| `resolution` | string |  | Output video resolution. one of: `480P`, `768P`, `1080P`, `2K`; default `"768P"` |
| `aspect_ratio` | string |  | Output aspect ratio. Matches the source video when omitted. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `reference_audio_urls` | array |  | Optional audio references for the continuation (2–15 seconds each, 15 seconds combined). The full extended video retains its original source soundtrack, and its ending still conditions the transition. These clips guide…  |

## Details

MiniMax H3 Max Turbo video extend: continue an existing video with 1–15 seconds of new footage; return the joined clip or only the continuation.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | — | Output frame shape. |
| `video` | video URL, required | — | Clip to continue. |
| `resolution` | `480P` / `768P` / `1080P` / `2K` | `768P` | Sets the per-second rate. |
| `duration` | integer 1–15 | 5 | Seconds of new footage. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `reference_audio_urls` | audio URL[] | — | Optional reference audio for the new footage. |
| `output` | `extended` / `continuation` | `extended` | `extended` returns source + new footage; `continuation` returns only the new part. |

### Billing

You pay for new seconds: $0.025 at 480P, $0.04 at 768P, $0.08 at 1080P, $0.16 at 2K.

| Output | 480P | 768P | 1080P | 2K |
|---|---|---|---|---|
| 5s (default) | $0.125 | $0.20 | $0.40 | $0.80 |
| 10s | $0.25 | $0.40 | $0.80 | $1.60 |
| 15s | $0.375 | $0.60 | $1.20 | $2.40 |

Failed runs are not charged.

### Prompting

- Describe what happens next, not what is already in the clip.

### Also on SandBase

Other H3 Max Turbo endpoints: `minimax/h3-max-turbo/text-to-video`, `minimax/h3-max-turbo/image-to-video`, `minimax/h3-max/text-to-video` (H3 Max).

---
Machine-readable: [`catalog/models/minimax/h3-max-turbo/video-extend.json`](../../../../catalog/models/minimax/h3-max-turbo/video-extend.json) · Store page: https://www.sandbase.ai/model/minimax/h3-max-turbo/video-extend
