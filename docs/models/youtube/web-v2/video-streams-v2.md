# YouTube Video Streams (V2) API: pricing, parameters and code examples

`youtube/web-v2/video-streams-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Retrieves stream information and playback details for a YouTube video. Queries data using either a video ID or a full video URL.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-streams-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-streams-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-streams-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-streams-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-streams-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional, ignored if video_id is provided)  |

## Details

Look up stream details for a specific YouTube video by providing either a `video_id` or a `video_url`.

### Use cases

- Retrieve media stream information for video playback.
- Inspect available stream formats using a YouTube video identifier.
- Extract video stream details directly from a full video link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-streams-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional, ignored if video_id is provided) |

### Notes

- Providing `video_id` is recommended.
- The `video_url` parameter is ignored if `video_id` is supplied.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-streams-v2.json`](../../../../catalog/models/youtube/web-v2/video-streams-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-streams-v2
