# YouTube Channel Shorts API: pricing, parameters and code examples

`youtube/web-v2/channel-shorts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of YouTube Shorts from a specified channel. Supports lookups by channel identifier or URL, optional response formatting, and pagination tokens for next-page results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-shorts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-shorts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-shorts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-shorts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-shorts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string |  | Channel ID (recommended, e.g., UCuAXFkgsw1L7xaCfnd5JJOw)  |
| `channel_url` | string |  | Channel URL (optional, ignored if channel_id is provided)  |
| `need_format` | boolean |  | Whether to format data (default true) default `true` |
| `continuation_token` | string |  | Pagination token (optional, for next page)  |

## Details

Returns a page of YouTube Shorts for one channel, with each Short's title, video ID, URL, thumbnail and view count text. It needs a `channel_id` or a `channel_url`.

### Use cases

- Pull the latest Shorts from a creator channel to track new posts.
- Build a feed of a channel's Shorts with titles, thumbnails and links.
- Compare the view counts shown on Shorts across several channels.
- Check how many Shorts a channel has published using `total_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw", "channel_url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | No | Channel ID (recommended, e.g., UCuAXFkgsw1L7xaCfnd5JJOw) |
| `channel_url` | string | No | Channel URL (optional, ignored if channel_id is provided) |
| `continuation_token` | string | No | Pagination token (optional, for next page) |
| `need_format` | boolean | No | Whether to format data (default true) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
  "continuation_token": "4qmFsgK5…",
  "has_more": true,
  "shorts": [
    {
      "accessibility_text": "This version of Never Gonna Give You Up still gets to us 😭 #nevergonnagiveyouup,…",
      "thumbnails": [
        {
          "height": 1920,
          "url": "https://i.ytimg.com/vi/TIRgIY2nwOk/frame0.jpg",
          "width": 1080
        }
      ],
      "title": "This version of Never Gonna Give You Up still gets to us 😭 #nevergonnagiveyouup",
      "video_id": "TIRgIY2nwOk",
      "video_url": "https://www.youtube.com/shorts/TIRgIY2nwOk",
      "view_count_text": "4.9 thousand views"
    }
  ],
  "total_count": 48
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shorts[].video_id` | The ID of the Short. |
| `shorts[].video_url` | Direct link to the Short on YouTube, in the form `https://www.youtube.com/shorts/<video_id>`. |
| `shorts[].title` | Title of the Short, including any hashtags. |
| `shorts[].view_count_text` | View count as display text, for example `4.9 thousand views`. It is a rounded string, not a number. |
| `shorts[].thumbnails[].url / shorts[].thumbnails[].width / shorts[].thumbnails[].height` | Thumbnail image link and its pixel size. |
| `shorts[].accessibility_text` | Screen reader label that combines the title, the view count text and `play Short`. |
| `total_count` | Number of Shorts reported for the channel. |
| `has_more` | `true` when more Shorts are available on a next page. |
| `continuation_token` | Token to request the next page of Shorts. |
| `channel_id` | ID of the channel the Shorts belong to. |

### Notes

- Send `channel_id` when you have it. The API ignores `channel_url` if `channel_id` is present.
- To get the next page, send the `continuation_token` from the response in your next request, along with the same channel. Stop when `has_more` is `false`.
- If you only have a channel URL, use [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id) to get the `channel_id`.
- For regular uploads instead of Shorts, call [YouTube Channel Videos](/apis/youtube/web-v2/channel-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-shorts.json`](../../../../catalog/models/youtube/web-v2/channel-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-shorts
