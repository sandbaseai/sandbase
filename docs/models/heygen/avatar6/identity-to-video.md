# HeyGen Avatar 6 Identity to Video API: pricing, parameters and code examples

`heygen/avatar6/identity-to-video` · video generation model · HeyGen · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.6 per call · **Modes:** async

HeyGen Avatar 6 by HeyGen creates a talking video with a public HeyGen avatar from a script or speech audio.

## Pricing

- Depends on parameters (`params.audio`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? ((params.audio ?? "") != "" ? media_duration(params.audio) : nil) ?? 5.0) * ((params.resolution ?? "1080p") == "2k" ? 0.145 : 0.12)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/avatar6/identity-to-video", "aspect_ratio": "16:9", "prompt": "Hello and welcome to this demonstration of HeyGen Avatar 6."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/avatar6/identity-to-video', {'aspect_ratio': '16:9', 'prompt': 'Hello and welcome to this demonstration of HeyGen Avatar 6.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/avatar6/identity-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "Hello and welcome to this demonstration of HeyGen Avatar 6."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/avatar6/identity-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Hello and welcome to this demonstration of HeyGen Avatar 6.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string |  | Optional speech audio, file or URL. When set, the script and voice are ignored.  |
| `voice` | string |  | Text-to-speech voice used for the script. default `"Warm Pro Narrator"` |
| `avatar` | string |  | Name of an Avatar 6-compatible public HeyGen avatar. default `"Abigail Sofa Front"` |
| `prompt` | string |  | Text the avatar will speak. Required unless audio is provided.  |
| `resolution` | string |  | Output resolution; 2k is billed at a higher per-second rate. one of: `1080p`, `2k`; default `"1080p"` |
| `aspect_ratio` | string |  | Output frame shape. one of: `16:9`, `9:16`, `1:1`, `4:5`, `5:4`; default `"16:9"` |
| `motion_prompt` | string |  | Optional direction for the avatar's motion and expression.  |
| `motion_expressiveness` | string |  | less gives fewer, smaller gestures and calmer expressions. one of: `default`, `less`; default `"default"` |

## Details

HeyGen Avatar 6 makes a talking video with one of HeyGen's public avatars, from a written script or a speech track.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Script; required unless `audio` is set. |
| `avatar` | string | `Abigail Sofa Front` | Public Avatar 6 avatar name. |
| `voice` | string | `Warm Pro Narrator` | Voice for the script. |
| `audio` | audio file or URL | — | Overrides script and voice. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:5` / `5:4` | `16:9` | Frame shape. |
| `motion_prompt` | string | — | Direction for motion and expression. |
| `motion_expressiveness` | `default` / `less` | `default` | `less` for calmer motion. |
| `resolution` | `1080p` / `2k` | `1080p` | Sets the per-second rate. |
### Billing
$0.12 per output second at 1080p, $0.145 at 2k. Length follows the audio or the spoken script; the quote before submission assumes 5 seconds.
| Output | 1080p | 2k |
|---|---|---|
| 10s | $1.20 | $1.450 |
| 60s | $7.20 | $8.70 |
Failed runs are not charged.
### Also on SandBase
Related: `heygen/avatar6/image-to-video`, `heygen/avatar6/ref-video-to-video`, `heygen/avatar5/digital-twin`.

---
Machine-readable: [`catalog/models/heygen/avatar6/identity-to-video.json`](../../../../catalog/models/heygen/avatar6/identity-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/avatar6/identity-to-video
