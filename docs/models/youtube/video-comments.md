# YouTube Video Comments API: pricing, parameters and code examples

`youtube/video-comments` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

List the comments on a YouTube video or Short by URL with cursor pagination (text, author, likes, reply count).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-comments", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-comments', {'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-comments", {
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-comments", sandbase.Params{
	"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full YouTube video URL. Shorts (youtube.com/shorts/...) and youtu.be URLs also work.  |
| `order` | string |  | Comment order (e.g. top, newest). one of: `top`, `newest` |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `likes`, and it is served only by a source that returns every one of…  |

## Details

List the comments on a YouTube video or Short by URL with cursor pagination (text, author, likes, reply count).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full YouTube video URL. Shorts (youtube.com/shorts/...) and youtu.be URLs also work. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `order` | string | No | Comment order (e.g. top, newest). One of: `top`, `newest`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `likes`, and it is served only by a source that returns every one of t |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/video-comments.json`](../../../catalog/models/youtube/video-comments.json) · Store page: https://www.sandbase.ai/model/youtube/video-comments
