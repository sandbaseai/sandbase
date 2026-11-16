# Kling V4 Flash Video Edit API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/flash/video-edit` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $2.52 per call · **Modes:** async

Kling V4 Flash Video Edit by Kuaishou edits a 3-20 second source video into a 720p result from a text instruction and optional reference images.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`).

Formula: `0.063 * 2.0 * Math.min(20.0, usage.duration ?? media_duration(params.video) ?? 20.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/flash/video-edit", "images": ["https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/b6aa6d28-155c-42b5-b034-064ed3222127.png", "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/cc34d877-819c-4495-a496-625cee4cc554.png"], "prompt": "The blocky car proxy is the KESSEL R4 rally car from @Image1 - chalk-white body with the diagonal signal-orange and charcoal band, black 27 on a white roundel on the doors, slim LED headlamps joined by a light bar, roof scoop, rear wing, red mudflaps, white six-spoke gravel wheels. The grey road ribbon is the loose ochre-grey gravel stage and the cones and cylinders are the pine and birch forest of @Image2, on a crisp autumn morning with low sun raking through the trees and hanging dust. The mannequin proxies behind the rope are rally spectators in muted outdoor jackets and beanies behind red-and-white tape. Keep the exact blocking, timing, camera position and pan of the playblast. Physically real gravel rally: the car slides through the hairpin with opposite lock, rear wheels throwing a thick fan of gravel and a rolling dust cloud that drifts across the spectators; stones rattle off the bank; the suspension works over the ruts; spectators flinch, cheer and raise phones. Sound: a turbocharged four-cylinder rally engine on anti-lag with pops and bangs, gravel spray, crowd cheering. No text other than the number 27, no sponsor logos.", "video": "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/4494b4bf-ff4e-4cc8-ac0d-9895bf65742e.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/flash/video-edit', {'images': ['https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/b6aa6d28-155c-42b5-b034-064ed3222127.png', 'https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/cc34d877-819c-4495-a496-625cee4cc554.png'], 'prompt': 'The blocky car proxy is the KESSEL R4 rally car from @Image1 - chalk-white body with the diagonal signal-orange and charcoal band, black 27 on a white roundel on the doors, slim LED headlamps joined by a light bar, roof scoop, rear wing, red mudflaps, white six-spoke gravel wheels. The grey road ribbon is the loose ochre-grey gravel stage and the cones and cylinders are the pine and birch forest of @Image2, on a crisp autumn morning with low sun raking through the trees and hanging dust. The mannequin proxies behind the rope are rally spectators in muted outdoor jackets and beanies behind red-and-white tape. Keep the exact blocking, timing, camera position and pan of the playblast. Physically real gravel rally: the car slides through the hairpin with opposite lock, rear wheels throwing a thick fan of gravel and a rolling dust cloud that drifts across the spectators; stones rattle off the bank; the suspension works over the ruts; spectators flinch, cheer and raise phones. Sound: a turbocharged four-cylinder rally engine on anti-lag with pops and bangs, gravel spray, crowd cheering. No text other than the number 27, no sponsor logos.', 'video': 'https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/4494b4bf-ff4e-4cc8-ac0d-9895bf65742e.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/flash/video-edit", {
  "images": [
    "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/b6aa6d28-155c-42b5-b034-064ed3222127.png",
    "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/cc34d877-819c-4495-a496-625cee4cc554.png"
  ],
  "prompt": "The blocky car proxy is the KESSEL R4 rally car from @Image1 - chalk-white body with the diagonal signal-orange and charcoal band, black 27 on a white roundel on the doors, slim LED headlamps joined by a light bar, roof scoop, rear wing, red mudflaps, white six-spoke gravel wheels. The grey road ribbon is the loose ochre-grey gravel stage and the cones and cylinders are the pine and birch forest of @Image2, on a crisp autumn morning with low sun raking through the trees and hanging dust. The mannequin proxies behind the rope are rally spectators in muted outdoor jackets and beanies behind red-and-white tape. Keep the exact blocking, timing, camera position and pan of the playblast. Physically real gravel rally: the car slides through the hairpin with opposite lock, rear wheels throwing a thick fan of gravel and a rolling dust cloud that drifts across the spectators; stones rattle off the bank; the suspension works over the ruts; spectators flinch, cheer and raise phones. Sound: a turbocharged four-cylinder rally engine on anti-lag with pops and bangs, gravel spray, crowd cheering. No text other than the number 27, no sponsor logos.",
  "video": "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/4494b4bf-ff4e-4cc8-ac0d-9895bf65742e.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/flash/video-edit", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/b6aa6d28-155c-42b5-b034-064ed3222127.png", "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/cc34d877-819c-4495-a496-625cee4cc554.png"},
	"prompt": "The blocky car proxy is the KESSEL R4 rally car from @Image1 - chalk-white body with the diagonal signal-orange and charcoal band, black 27 on a white roundel on the doors, slim LED headlamps joined by a light bar, roof scoop, rear wing, red mudflaps, white six-spoke gravel wheels. The grey road ribbon is the loose ochre-grey gravel stage and the cones and cylinders are the pine and birch forest of @Image2, on a crisp autumn morning with low sun raking through the trees and hanging dust. The mannequin proxies behind the rope are rally spectators in muted outdoor jackets and beanies behind red-and-white tape. Keep the exact blocking, timing, camera position and pan of the playblast. Physically real gravel rally: the car slides through the hairpin with opposite lock, rear wheels throwing a thick fan of gravel and a rolling dust cloud that drifts across the spectators; stones rattle off the bank; the suspension works over the ruts; spectators flinch, cheer and raise phones. Sound: a turbocharged four-cylinder rally engine on anti-lag with pops and bangs, gravel spray, crowd cheering. No text other than the number 27, no sponsor logos.",
	"video": "https://static.sandbase.ai/examples/e72b57c8-1fef-4fc5-93f8-0473dd8fb581/input/4494b4bf-ff4e-4cc8-ac0d-9895bf65742e.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Video to edit (3-20s, min 700x700 px, up to 300 MB). The output keeps its length.  |
| `images` | array |  | Optional reference images, referenced as @Image1, @Image2, ...  |
| `prompt` | string | yes | Edit instruction. Refer to the source video as @Video1 and reference images as @Image1, @Image2, ...  |

## Details

Kling V4 Flash video edit changes a 3–20 second source video from a text instruction, with optional reference images. The 720p output keeps the source length.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Edit instruction. Refer to the source as `@Video1` and images as `@Image1`, … |
| `video` | video URL, required | — | 3–20s, min 700×700 px, up to 300 MB. |
| `images` | image URL[] | — | Up to 10 reference images. |
### Billing
$0.063 per second, counted on input plus output (2× the source length). Settlement uses the output length (it matches the source); the quote before submission assumes a 20 second source when the length cannot be read.
| Source | Price |
|---|---|
| 5s | $0.63 |
| 10s | $1.26 |
| 20s | $2.52 |
Failed runs are not charged.
### Prompting
- State what to change and what to keep, e.g. "replace the jacket in @Video1 with the coat in @Image1".
### Limits
- Output is 720p only; source videos are 3–20 seconds.
### Also on SandBase
Other Kling V4 Flash endpoints: `kwaivgi/kling-video/v4/flash/text-to-video`, `kwaivgi/kling-video/v4/flash/image-to-video`, `kwaivgi/kling-video/v4/flash/reference-to-video`, `kwaivgi/kling-video/v4/flash/video-edit`. For 1080p or clips up to 30 seconds, use Kling V4 (`kwaivgi/kling-video/v4/text-to-video` and its siblings).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/flash/video-edit.json`](../../../../../../catalog/models/kwaivgi/kling-video/v4/flash/video-edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/flash/video-edit
