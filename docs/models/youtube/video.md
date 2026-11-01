# YouTube Video

`youtube/video` · api · YouTube

Fetch a YouTube video or Short's metadata (title, channel, views, likes, duration, publish date) by URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | YouTube video ID. A Short uses the same ID as any other video.  |
| `url` | string |  | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorAvatarUrl`, and it is served only by a source that returns…  |

## Details

Fetch a YouTube video or Short's metadata (title, channel, views, likes, duration, publish date) by URL or ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | YouTube video ID. A Short uses the same ID as any other video. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorAvatarUrl`, and it is served only by a source that returns ever |
| `url` | string | No | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work. |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/video.json`](../../../catalog/models/youtube/video.json) · Store page: https://www.sandbase.ai/model/youtube/video
