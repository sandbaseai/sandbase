# Kling V4 Video Edit API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/video-edit` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $8.46 per call · **Modes:** async

Kling V4 Video Edit by Kuaishou edits a 3-30 second source video from a text instruction and optional reference images.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `((params.resolution ?? "1080p") == "720p" ? 0.094 : 0.141) * 2.0 * Math.min(30.0, usage.duration ?? media_duration(params.video) ?? 30.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/video-edit", "prompt": "Change the time of day in @Video1 to a starry night with the boat glowing softly, keep the camera motion.", "video": "https://static.sandbase.ai/examples/c5782511-455d-4642-aed4-aee4d9a68521/input/cc801f7f-f034-4822-99db-04c72e2b9743.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/video-edit', {'prompt': 'Change the time of day in @Video1 to a starry night with the boat glowing softly, keep the camera motion.', 'video': 'https://static.sandbase.ai/examples/c5782511-455d-4642-aed4-aee4d9a68521/input/cc801f7f-f034-4822-99db-04c72e2b9743.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/video-edit", {
  "prompt": "Change the time of day in @Video1 to a starry night with the boat glowing softly, keep the camera motion.",
  "video": "https://static.sandbase.ai/examples/c5782511-455d-4642-aed4-aee4d9a68521/input/cc801f7f-f034-4822-99db-04c72e2b9743.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/video-edit", sandbase.Params{
	"prompt": "Change the time of day in @Video1 to a starry night with the boat glowing softly, keep the camera motion.",
	"video": "https://static.sandbase.ai/examples/c5782511-455d-4642-aed4-aee4d9a68521/input/cc801f7f-f034-4822-99db-04c72e2b9743.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Video to edit (3-30s, min 700x700 px, up to 300 MB). The output keeps its length.  |
| `images` | array |  | Optional reference images, referenced as @Image1, @Image2, ...  |
| `prompt` | string | yes | Edit instruction. Refer to the source video as @Video1 and reference images as @Image1, @Image2, ...  |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"1080p"` |

## Details

Kling V4 video edit changes a 3–30 second source video from a text instruction, with optional reference images. The output keeps the source length.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Edit instruction. Refer to the source as `@Video1` and images as `@Image1`, … |
| `video` | video URL, required | — | 3–30s, min 700×700 px, up to 300 MB. |
| `images` | image URL[] | — | Up to 10 reference images. |
| `resolution` | `720p` / `1080p` | `1080p` | Output resolution. |
### Billing
$0.094 (720p) or $0.141 (1080p) per second, counted on input plus output (2× the source length). Settlement uses the output length (it matches the source); the quote before submission assumes a 30 second source when the length cannot be read.
| Source | Price |
|---|---|
| 6s, 1080p | $1.692 |
| 10s, 720p | $1.88 |
| 30s, 1080p | $8.46 |
Failed runs are not charged.
### Prompting
- State what to change and what to keep, e.g. "replace the jacket in @Video1 with the coat in @Image1".
### Limits
- Source videos are 3–30 seconds.
### Also on SandBase
Other Kling V4 endpoints: `kwaivgi/kling-video/v4/text-to-video`, `kwaivgi/kling-video/v4/image-to-video`, `kwaivgi/kling-video/v4/reference-to-video`, `kwaivgi/kling-video/v4/video-edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/video-edit.json`](../../../../../catalog/models/kwaivgi/kling-video/v4/video-edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/video-edit
