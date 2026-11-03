# YouTube Channel Shorts API: pricing, parameters and code examples

`youtube/channel-shorts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get public Shorts from a YouTube channel ID with optional continuation-token pagination. Use it to browse a channel's short-form videos and continue through additional result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-shorts", "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-shorts', {'channelId': 'UCuAXFkgsw1L7xaCfnd5JJOw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-shorts", {
  "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-shorts", sandbase.Params{
	"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
})
```

Same call via the path form: `POST /v1/api/youtube/channel-shorts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channelId` | string | yes | The UC-prefixed unique identifier for a YouTube channel. @username handles are not supported.  |
| `continuationToken` | string |  | Pagination token returned by the previous response.  |

## Details

Returns a list of public Shorts from a YouTube channel. Each item has the title, video ID, link, thumbnail and a view count label. You send the channel's `UC` prefixed ID.

### Use cases

- Build a feed of a creator's latest Shorts for a dashboard or content archive.
- Compare view count labels across a channel's Shorts to see which topics get attention.
- Collect Short video IDs and URLs to pass to a video details or transcript API.
- Pull Short thumbnails and titles to build a link preview or media gallery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channelId": "UCuAXFkgsw1L7xaCfnd5JJOw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | Yes | The UC-prefixed unique identifier for a YouTube channel. @username handles are not supported. |
| `continuationToken` | string | No | Pagination token returned by the previous response. |

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
| `shorts[].video_id` | The ID of the Short. Use it to look up the video in other YouTube APIs. |
| `shorts[].video_url` | Direct `youtube.com/shorts/` link to the Short. |
| `shorts[].title` | Title of the Short, including any hashtags and emoji. |
| `shorts[].view_count_text` | View count as display text, for example `4.9 thousand views`. It is a rounded label, not a number. |
| `shorts[].thumbnails[].url / shorts[].thumbnails[].width / shorts[].thumbnails[].height` | Thumbnail image link and its pixel size. The sample is 1080 by 1920, a vertical frame. |
| `shorts[].accessibility_text` | Screen reader text that combines the title, the view count label and a play prompt. |
| `has_more` | `true` when more Shorts are available on a later page. |
| `continuation_token` | Token to send as `continuationToken` in the next request to get the next page. |
| `total_count` | Count value returned with the response. In the sample it is `48`. |
| `channel_id` | The channel ID the Shorts belong to. |

### Notes

- `channelId` must start with `UC`. `@username` handles are not supported. To find the ID from a channel URL, try [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id).
- For the next page, pass the `continuation_token` value from the last response as `continuationToken`. Keep `channelId` the same. Continue while `has_more` is `true`.
- To get full details for a Short, pass its `video_id` to [YouTube Video Details](/apis/youtube/video-detail).
- To list the channel's regular uploads instead, use [YouTube Channel Videos](/apis/youtube/channel-videos).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/channel-shorts.json`](../../../catalog/models/youtube/channel-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/channel-shorts
