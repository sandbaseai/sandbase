# YouTube Video Information

`youtube/web-v2/video-info` · api · YouTube

Returns detailed video information and caption tracks for a specified YouTube video ID. Supports optional parameters to format output data and set language preferences.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-info", "video_id": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-info', {'video_id': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-info", {
  "video_id": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-info", sandbase.Params{
	"video_id": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string | yes | **Purpose**: Video ID  |
| `need_format` | boolean |  | Whether to clean and format the data default `true` |
| `language_code` | string |  | **Purpose**: Set language preference default `"zh-CN"` |

## Details

Retrieve video information and caption URLs for a specific video using `video_id`. You can optionally format the response with `need_format` and select language preferences with `language_code`.

### Use cases

- Retrieve caption track URLs for automated subtitle extraction.
- Inspect YouTube video metadata for media workflows.
- Filter video metadata by language preference.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | Purpose: Video ID |
| `need_format` | boolean | No | Whether to clean and format the data |
| `language_code` | string | No | Purpose: Set language preference |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "captions": [
    {
      "base_url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&ei=quvEapT4C4O0kucP77OG0Qw&c…",
      "language_name": "德语（德国）"
    }
  ]
}
```

### Notes

- Set `need_format` to true to return cleaned and formatted data.
- Use `language_code` to specify a preferred language for returned captions.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-info.json`](../../../../catalog/models/youtube/web-v2/video-info.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-info
