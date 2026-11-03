# YouTube Video API: pricing, parameters and code examples

`youtube/video` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

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

Returns metadata for one YouTube video or Short, including title, channel, views, likes, duration, category and keywords. Send either a full video `url` or a video `id`.

### Use cases

- Track the `views` and `likes` of a specific video over time.
- Pull the `title`, `image` and `channel` of a pasted link to build a link preview.
- Check the `category` and `keywords` of a video to sort it into a topic list.
- Resolve a video URL to its `authorId` so you can look up the channel that posted it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | YouTube video ID. A Short uses the same ID as any other video. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorAvatarUrl`, and it is served only by a source that returns ever |
| `url` | string | No | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorId": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "authorUrl": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
    "category": "Music",
    "channel": "Rick Astley",
    "comments": 0,
    "createdUtc": 1256453853,
    "description": "The official video for “Never Gonna Give You Up” by Rick Astley. \n\nNever: The Au…",
    "durationMs": 214000,
    "id": "dQw4w9WgXcQ",
    "image": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
    "keywords": [
      "rick astley"
    ],
    "likes": 19493819
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the video. |
| `data.channel / data.authorId` | Name of the channel that posted the video and its channel ID. |
| `data.authorUrl` | Link to the channel page. |
| `data.views / data.likes / data.comments` | View count, like count and comment count. In the sample response `comments` is `0`, so do not rely on it unless you request it with `requireFields`. |
| `data.durationMs` | Video length in milliseconds. |
| `data.createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.category / data.keywords` | YouTube category name and the list of keyword tags set on the video. |
| `data.description` | Video description text. |
| `data.image` | URL of the video thumbnail image. |
| `found` | `true` when the video was found. |

### Notes

- Pass either `url` or `id`. Shorts, youtu.be, live and embed URLs work in `url`, and a Short uses the same `id` as any other video.
- The `id` is the value after `v=` in a watch URL, for example `dQw4w9WgXcQ`.
- Use `requireFields` with `authorAvatarUrl`, `comments` or `description` only when you need those fields. Doing so can change the price of the call.
- To read the comments, call [YouTube Video Comments](/apis/youtube/video-comments). To get the spoken text, call [YouTube Video Transcript](/apis/youtube/video-transcript).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/video.json`](../../../catalog/models/youtube/video.json) · Store page: https://www.sandbase.ai/model/youtube/video
