# YouTube Video Transcript API: pricing, parameters and code examples

`youtube/video-transcript` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Fetch the transcript/captions of a YouTube video or Short by URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-transcript"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-transcript', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-transcript", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-transcript", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/video-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | YouTube video ID. A Short uses the same ID as any other video.  |
| `url` | string |  | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work.  |

## Details

Fetch the transcript/captions of a YouTube video or Short by URL or ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | YouTube video ID. A Short uses the same ID as any other video. |
| `url` | string | No | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work. |

### Pricing

Billed at the actual cost of each call, usually $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/video-transcript.json`](../../../catalog/models/youtube/video-transcript.json) · Store page: https://www.sandbase.ai/model/youtube/video-transcript
