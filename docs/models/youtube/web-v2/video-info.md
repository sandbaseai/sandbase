# YouTube Video Information API: pricing, parameters and code examples

`youtube/web-v2/video-info` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed video information and caption tracks for a specified YouTube video ID. Supports optional parameters to format output data and set language preferences.

## Pricing

- **$0.001 per call** (USD)
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

Returns metadata and caption tracks for one YouTube video. You pass the 11-character `video_id`. The response includes title, channel details, like count, publish date, thumbnails, end screen items and a list of caption tracks with their URLs.

### Use cases

- Collect caption track URLs and language codes for a video to start subtitle extraction.
- Pull the title, `keywords`, `category` and `description` of a video to build a content catalog.
- Check `is_private`, `is_unlisted`, `is_family_safe` and `playability_status` before you add a video to a playlist or feed.
- Read the channel ID and handle from a video to link it to its channel.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | **Purpose**: Video ID |
| `language_code` | string | No | **Purpose**: Set language preference |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "allow_ratings": true,
  "author": "Rick Astley",
  "available_countries": [
    "AD"
  ],
  "badge_tooltip": "音乐人官方频道",
  "captions": [
    {
      "base_url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&ei=0JHpavzwFZSY0_wPk9jD2Q0&c…",
      "is_translatable": true,
      "kind": "",
      "language_code": "de-DE",
      "language_name": "德语（德国）"
    }
  ],
  "category": "Music",
  "channel_avatar_thumbnails": [
    {
      "height": 48,
      "url": "https://yt3.ggpht.com/_ShEGOdg-t5YGJse14Ooq6FYBZqX_QSlhaTNjG06miYusm5lWm1UroLyVx…",
      "width": 48
    }
  ],
  "channel_handle": "@RickAstleyYT",
  "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
  "channel_url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
  "chapters": null,
  "comment_count": "246万"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / author / description` | Video title, channel name and the video description text. The description may be long. |
| `video_id / channel_id / channel_handle / channel_url` | IDs and links for the video and its channel. `channel_handle` is the `@` name of the channel. |
| `like_count / like_count_text` | Like count as a plain number string, and the same count as display text in the response language. |
| `comment_count / short_view_count / subscriber_count_text` | Display text for comments, views and channel subscribers. These values are localized strings such as `246万`, not plain numbers. |
| `publish_date / upload_date / date_text / relative_date_text` | Publish and upload time as an ISO 8601 timestamp with a UTC offset. `date_text` and `relative_date_text` are display text in the response language. |
| `length_seconds` | Video length in seconds, returned as a string. |
| `captions[].language_code / captions[].language_name` | Language code and display name of each caption track. |
| `captions[].base_url / captions[].is_translatable / captions[].kind` | URL of the caption track, whether the track can be translated, and the track kind. `kind` is an empty string for these tracks. |
| `endscreen[].style / endscreen[].title / endscreen[].video_id` | Items shown at the end of the video. `style` is `CHANNEL` or `VIDEO`. Video items carry a `video_id`. |
| `is_verified / is_private / is_unlisted / is_live_content / playability_status` | Flags for the channel and video state. `playability_status` is `OK` when the video can be played. |

### Notes

- `video_id` must be exactly 11 characters, for example `dQw4w9WgXcQ`.
- Text fields such as `comment_count`, `short_view_count` and `language_name` follow `language_code`, which defaults to `zh-CN`. The example response shows Chinese display text.
- Counts like `like_count` and `length_seconds` are strings. Convert them before you do math.
- To get comments for the video, call [YouTube Video Comments](/apis/youtube/web-v2/video-comments). For similar videos, call [YouTube Related Videos (Web V2)](/apis/youtube/web-v2/related-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-info.json`](../../../../catalog/models/youtube/web-v2/video-info.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-info
