# YouTube Video Information (V2) API: pricing, parameters and code examples

`youtube/web-v2/video-info-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive details for a YouTube video identified by its ID or direct URL, with an option to retrieve a cleaned payload format.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-info-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-info-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-info-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-info-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-info-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID, e.g. `"dQw4w9WgXcQ"`  |
| `video_url` | string |  | Full video URL (ignored if video_id provided)  |
| `need_format` | boolean |  | Whether to return cleaned payload. Default `True` default `true` |

## Details

Returns details for one YouTube video, including title, description, channel info, view and like counts, captions, and end screen items. The input is a `video_id` or a full `video_url`.

### Use cases

- Pull the title, description, keywords and thumbnail of a video to show in a media app or catalog.
- Check which countries a video is available in and whether it is unlisted, private or family safe.
- List the caption languages of a video before you fetch the text.
- Find the channel ID and handle behind a video link, then look up that channel.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-info-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to return cleaned payload. Default `True` |
| `video_id` | string | No | Video ID, e.g. `"dQw4w9WgXcQ"` |
| `video_url` | string | No | Full video URL (ignored if video_id provided) |

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
      "base_url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&ei=0JHpavCVKrGXsfIPlfGYkA0&c…",
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
| `title / author` | Title of the video and the name of the channel that posted it. |
| `channel_id / channel_handle / channel_url` | Identifiers and link for the channel that owns the video. |
| `description` | Video description text. Long text may be cut. |
| `publish_date` | Publish time as an ISO 8601 timestamp with a UTC offset, such as `2009-10-24T23:57:33-07:00`. |
| `length_seconds` | Video length in seconds. The value is a string. |
| `like_count / like_count_text` | Like count as a plain number string, and the same count as display text. |
| `short_view_count / comment_count / subscriber_count_text` | Display text for views, comments and channel subscribers. The text is localized and rounded, for example `18亿次观看`. |
| `captions[]` | Available caption tracks. Each row has `language_code`, `language_name`, `is_translatable` and a `base_url` for the caption file. |
| `endscreen[]` | End screen items. `style` shows whether the item is a `CHANNEL` or a `VIDEO`. Video items carry `video_id` and `title`. |
| `is_verified / is_unlisted / is_private / is_live_content / is_family_safe` | Flags for channel verification, visibility, live content and family safety. |
| `available_countries` | List of country codes where the video can be watched. |

### Notes

- Send either `video_id` or `video_url`. If you send both, `video_url` is ignored.
- The `video_id` is the value after `v=` in a watch URL, for example `dQw4w9WgXcQ`.
- Display text fields such as `comment_count` and `short_view_count` follow a localized format. Use `like_count` and `length_seconds` for numeric strings.
- To read comments, call [YouTube Video Comments](/apis/youtube/web-v2/video-comments). To get more videos like this one, call [YouTube Related Videos (Web V2)](/apis/youtube/web-v2/related-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-info-v2.json`](../../../../catalog/models/youtube/web-v2/video-info-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-info-v2
