# YouTube Related Videos (Web) API: pricing, parameters and code examples

`youtube/web/relate-video` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of related videos for a given YouTube video ID. Supports pagination using a continuation token to retrieve additional recommendations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/relate-video", "video_id": "LuIL5JATZsc"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/relate-video', {'video_id': 'LuIL5JATZsc'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/relate-video", {
  "video_id": "LuIL5JATZsc"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/relate-video", sandbase.Params{
	"video_id": "LuIL5JATZsc",
})
```

Same call via the path form: `POST /v1/api/youtube/web/relate-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string | yes | Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc.  |
| `continuation_token` | string |  | Token to continue fetching related videos. Default is None.  |

## Details

Retrieve recommended and related videos for a specific video using `video_id`. Pass `continuation_token` to load additional pages of related content.

### Use cases

- Build video recommendation feeds based on a currently playing item.
- Discover related content and channels in specific topic clusters.
- Extract recommended video metadata for audience interest analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/relate-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "LuIL5JATZsc"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. |
| `continuation_token` | string | No | Token to continue fetching related videos. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "videos": [
    {
      "author": "CozyCraft",
      "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
      "number_of_views": 0,
      "published_time": "5mo ago",
      "title": "just relax, everything can wait… (minecraft music & ambience)",
      "type": "NORMAL",
      "video_id": "CijACOd7jQk"
    }
  ]
}
```

### Notes

- Obtain `video_id` directly from the YouTube video URL.
- Use `continuation_token` to paginate through subsequent related videos.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/relate-video.json`](../../../../catalog/models/youtube/web/relate-video.json) · Store page: https://www.sandbase.ai/model/youtube/web/relate-video
