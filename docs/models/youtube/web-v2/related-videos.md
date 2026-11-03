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

Returns a list of videos that YouTube shows as related to a given video. Send a `video_id` or a full `video_url`. Each item has the title, channel, thumbnails, and a link to the related video.

### Use cases

- Build a "watch next" carousel for a video in your own app.
- Map which channels and videos cluster around a seed video for content research.
- Collect related video IDs to feed into a video info or comments lookup.
- Compare the related lists of several videos in one niche to find shared recommendations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/related-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to format data (default true) |
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional, ignored if video_id is provided) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "related_videos": [
    {
      "author": "Retro Pulse",
      "author_id": "UCoDu_E2c5wI_zgfW4mdT0KQ",
      "author_url": "https://www.youtube.com/channel/UCoDu_E2c5wI_zgfW4mdT0KQ",
      "length_seconds": null,
      "length_text": null,
      "published_time_text": "3mo ago",
      "thumbnails": [
        {
          "height": 94,
          "url": "https://i.ytimg.com/vi/KLERRzVzPHI/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDgg…",
          "width": 168
        }
      ],
      "title": "Best of 80s Music Legends - Tears For Fears, Madonna, Cyndi Lauper, Modern Talki…",
      "video_id": "KLERRzVzPHI",
      "video_url": "https://www.youtube.com/watch?v=KLERRzVzPHI",
      "view_count_text": "470K"
    }
  ],
  "total_count": 20,
  "video_id": "dQw4w9WgXcQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `related_videos[]` | List of related videos for the input video. |
| `related_videos[].video_id / related_videos[].video_url` | ID of the related video and its full watch URL. |
| `related_videos[].title` | Title of the related video. |
| `related_videos[].author / related_videos[].author_id / related_videos[].author_url` | Name of the channel that posted the video, its channel ID, and its channel URL. |
| `related_videos[].view_count_text` | View count as short display text, for example `29M`. It is a string, not a number. |
| `related_videos[].published_time_text` | Relative publish age as display text, for example `3mo ago` or `6y ago`. |
| `related_videos[].thumbnails[]` | Thumbnail images, each with `url`, `width`, and `height`. |
| `related_videos[].length_seconds / related_videos[].length_text` | Video length. Both are `null` in this response, so do not rely on them. |
| `total_count` | Number of related videos returned. |
| `video_id` | The video ID the related list was built for. |

### Notes

- Send `video_id` when you have it. `video_url` is ignored if `video_id` is set.
- The `video_id` is the `v` value in a watch URL, such as `dQw4w9WgXcQ` in `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
- The request has no pagination parameter. Set `need_format` to `false` if you want the unformatted output structure.
- Pass a related `video_id` to [YouTube Video Information](/apis/youtube/web-v2/video-info) for full details, or to [YouTube Video Comments](/apis/youtube/web-v2/video-comments) for its comments.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/related-videos.json`](../../../../catalog/models/youtube/web-v2/related-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/related-videos
