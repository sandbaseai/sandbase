# YouTube Channel Videos API: pricing, parameters and code examples

`youtube/web-v2/channel-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos for a specified YouTube channel, including title, duration, URLs, and view counts. Supports pagination and region or language filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-videos", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "country_code": "US", "language_code": "zh-CN", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-videos', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg', 'country_code': 'US', 'language_code': 'zh-CN', 'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-videos", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "country_code": "US",
  "language_code": "zh-CN",
  "need_format": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-videos", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
	"country_code": "US",
	"language_code": "zh-CN",
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | **Purpose**: Channel ID  |
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data default `true` |
| `country_code` | string |  | **Purpose**: Set region code default `"US"` |
| `language_code` | string |  | **Purpose**: Set language preference default `"zh-CN"` |
| `continuation_token` | string |  | **Purpose**: Pagination token for next page  |

## Details

Returns a page of videos for one YouTube channel, plus basic details about the channel. It needs a `channel_id`, which starts with `UC`.

### Use cases

- List the newest uploads of a creator and show them in a feed or dashboard.
- Compare `view_count` across a channel's videos to see which uploads draw the most views.
- Collect video URLs and IDs from a channel to feed into other video lookups.
- Check which videos are live streams with the `is_live` flag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | **Purpose**: Channel ID |
| `continuation_token` | string | No | **Purpose**: Pagination token for next page |
| `country_code` | string | No | **Purpose**: Set region code |
| `language_code` | string | No | **Purpose**: Set language preference |
| `need_format` | boolean | No | **Purpose**: Whether to return cleaned simplified data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": {
    "avatar": "https://yt3.googleusercontent.com/jwfgqnpI22YpsFDz25QtgITBf5tX7mFHqXWVhHoWzbk3dd…",
    "description": "Minecraft ambience and cozy visuals for sleep, relaxing, studying, etc 🌿\n\nHi, I’…",
    "handle_url": "http://www.youtube.com/@CozyCraftYT",
    "id": "UCeu6U67OzJhV1KwBansH3Dg",
    "is_family_safe": true,
    "is_verified": true,
    "keywords": "Minecraft Ambience Rain Thunderstorm \"Relaxing Music\" C418 ASMR Sleep Study Rela…",
    "name": "CozyCraft",
    "rss_url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg",
    "url": "https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg"
  },
  "continuation_token": "4qmFsgLd…",
  "videos": [
    {
      "description": "",
      "duration": "11:00:00",
      "duration_accessibility": "11小时",
      "is_live": false,
      "is_verified": true,
      "moving_thumbnail": "https://i.ytimg.com/an_webp/eZ6TL5dtCLE/mqdefault_6s.webp?du=3000&sqp=CLGPptcG&r…",
      "playback_url": "https://rr5---sn-a5m7lnly.googlevideo.com/initplayback?source=youtube&oeis=1&c=W…",
      "published_time": "19小时前",
      "short_view_count": "3026次观看",
      "thumbnail": "https://i.ytimg.com/vi/eZ6TL5dtCLE/hq720_custom_2.jpg?sqp=CPyhptcG-oaymwEcCNAFEJ…",
      "thumbnails": [
        {
          "height": 202,
          "url": "https://i.ytimg.com/vi/eZ6TL5dtCLE/hq720_custom_2.jpg?sqp=CPyhptcG-oaymwEcCOgCEM…",
          "width": 360
        }
      ],
      "title": "you deserve a good night's sleep… (minecraft music & rain ambience)"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].video_id / videos[].url` | The video's ID and its full watch URL on YouTube. |
| `videos[].title` | The video title. |
| `videos[].duration / videos[].duration_accessibility` | Video length as `HH:MM:SS`, and a spoken-style length label such as `11小时`. |
| `videos[].view_count / videos[].short_view_count` | View count as display text, such as `3026次观看` or `1.9万次观看`. These are text strings, not numbers. |
| `videos[].published_time` | Relative publish time as display text, such as `7天前`. It is not an exact date. |
| `videos[].is_live` | `true` if the video is a live stream, `false` otherwise. |
| `videos[].thumbnail / videos[].thumbnails[]` | Main thumbnail URL, and a list of thumbnail URLs with `width` and `height`. |
| `videos[].playback_url` | A playback URL for the video. |
| `channel.name / channel.id / channel.handle_url` | The channel's name, its channel ID, and its `@handle` page URL. |
| `continuation_token` | Token to pass in the next request to get the next page of videos. |

### Notes

- Pass the returned `continuation_token` as the `continuation_token` parameter to get the next page.
- Text fields such as `view_count` and `published_time` come back in the language set by `language_code`. The example uses the default, so it returns Chinese text.
- If you only have a channel URL, call [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id) first to get the `channel_id`.
- For subscriber counts and channel totals, call [YouTube Channel Description](/apis/youtube/web-v2/channel-description).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-videos.json`](../../../../catalog/models/youtube/web-v2/channel-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-videos
