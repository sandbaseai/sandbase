# YouTube Related Videos (Web V2) API: pricing, parameters and code examples

`youtube/web-v2/related-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of related videos for a given YouTube video by ID or URL. Includes an option to format the returned output structure.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/related-videos", "need_format": true, "video_id": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/related-videos', {'need_format': True, 'video_id': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/related-videos", {
  "need_format": true,
  "video_id": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/related-videos", sandbase.Params{
	"need_format": true,
	"video_id": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/related-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional, ignored if video_id is provided)  |
| `need_format` | boolean |  | Whether to format data (default true) default `true` |

## Details

Retrieve related video recommendations by supplying a `video_id` or full `video_url`. You can also configure `need_format` to format the response data.

### Use cases

- Discover content recommendations related to a target video.
- Build recommendation carousels in external media apps.
- Analyze video association networks for research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/related-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional, ignored if video_id is provided) |
| `need_format` | boolean | No | Whether to format data (default true) |

### Notes

- If `video_id` is provided, `video_url` is ignored.
- `need_format` defaults to true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/related-videos.json`](../../../../catalog/models/youtube/web-v2/related-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/related-videos
