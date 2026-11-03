# YouTube Channel Videos API: pricing, parameters and code examples

`youtube/channel-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get public videos from a YouTube channel, with optional cursor-based pagination. Use it to browse a channel's uploads and continue through additional result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-videos", "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-videos', {'channelId': 'UCuAXFkgsw1L7xaCfnd5JJOw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-videos", {
  "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-videos", sandbase.Params{
	"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
})
```

Same call via the path form: `POST /v1/api/youtube/channel-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor for pagination.  |
| `channelId` | string | yes | The unique identifier for a YouTube channel.  |

## Details

Returns a list of public videos from a YouTube channel, plus basic channel details. It needs a `channelId` and accepts an optional `cursor` to fetch the next page.

### Use cases

- Build a list of a channel's recent uploads with titles, durations and links.
- Track view counts on a creator's latest videos.
- Collect `video_id` values to look up details, comments or transcripts for each video.
- Download thumbnails to show a channel's videos in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | Yes | The unique identifier for a YouTube channel. |
| `cursor` | string | No | The cursor for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": {
    "avatar": "https://yt3.googleusercontent.com/_ShEGOdg-t5YGJse14Ooq6FYBZqX_QSlhaTNjG06miYusm…",
    "description": "Rick Astley’s Swinging Christmas 2026 🎄 Dec 9th, Royal Albert Hall. SOLD OUT ❤️\n",
    "handle_url": "http://www.youtube.com/@RickAstleyYT",
    "id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "is_family_safe": true,
    "is_verified": false,
    "keywords": "Official Rick Astley \"rick astley\" \"never gonna give you up\" \"the best of me\" \"b…",
    "name": "Rick Astley",
    "rss_url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCuAXFkgsw1L7xaCfnd5JJOw",
    "url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw"
  },
  "continuation_token": "4qmFsgLZ…",
  "videos": [
    {
      "description": "",
      "duration": "3:51",
      "duration_accessibility": "3分钟51秒钟",
      "is_live": false,
      "is_verified": false,
      "moving_thumbnail": "",
      "playback_url": "https://rr6---sn-bvvbaxivnuxq5uu-q4fz.googlevideo.com/initplayback?source=youtub…",
      "published_time": "4个月前",
      "short_view_count": "11万次观看",
      "thumbnail": "https://i.ytimg.com/vi/PXC_PYeB6F8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARU…",
      "thumbnails": [
        {
          "height": 202,
          "url": "https://i.ytimg.com/vi/PXC_PYeB6F8/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARU…",
          "width": 360
        }
      ],
      "title": "Rick Astley - Angels On My Side (Live at The O2, London, April 2026)"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channel.id / channel.name` | The channel ID and display name. |
| `channel.url / channel.handle_url / channel.rss_url` | Links to the channel page, its `@handle` page and its RSS feed of uploads. |
| `channel.description / channel.keywords` | The channel's description text and keyword string. |
| `videos[].video_id / videos[].url` | The video ID and the full watch link. |
| `videos[].title` | The video title. |
| `videos[].duration` | Video length as text, for example `3:51`. |
| `videos[].view_count / videos[].short_view_count` | View count as display text, not a number. The text follows the language of the response, so parse it with care. |
| `videos[].published_time` | Relative publish time as text, for example "4个月前" (4 months ago). It is not an exact date. |
| `videos[].thumbnail / videos[].thumbnails[]` | The main thumbnail URL and a list of thumbnail URLs with `width` and `height`. |
| `continuation_token` | Token for the next page of videos. Pass it as `cursor` in the next request. |

### Notes

- Pass `continuation_token` from the response as `cursor` to get the next page.
- The `channelId` starts with `UC`, as in `UCuAXFkgsw1L7xaCfnd5JJOw`. The channel `url` in the response shows where it appears.
- Use a `video_id` from this response with [YouTube Video Details](/apis/youtube/video-detail) to get more about one video.
- For short-form uploads, call [YouTube Channel Shorts](/apis/youtube/channel-shorts). For live streams, call [YouTube Channel Live Streams](/apis/youtube/channel-lives).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/channel-videos.json`](../../../catalog/models/youtube/channel-videos.json) · Store page: https://www.sandbase.ai/model/youtube/channel-videos
