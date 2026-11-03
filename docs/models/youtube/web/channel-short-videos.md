# YouTube Channel Short Videos API: pricing, parameters and code examples

`youtube/web/channel-short-videos` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of YouTube Shorts from a specified channel. Supports pagination through an optional continuation token to browse additional short videos.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/channel-short-videos", "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/channel-short-videos', {'channel_id': 'UCXuqSBlHAE6Xw-yeJA0Tunw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/channel-short-videos", {
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/channel-short-videos", sandbase.Params{
	"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
})
```

Same call via the path form: `POST /v1/api/youtube/web/channel-short-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID.  |
| `continuation_token` | string |  | Token to continue fetching channel short videos. Default is None.  |

## Details

Returns a list of YouTube Shorts for one channel. Each item has the video ID, title, view count and thumbnails. You send a `channel_id`, and you can add a `continuation_token` to get the next page.

### Use cases

- Build a list of a creator's Shorts with titles and thumbnails for a content dashboard.
- Compare `number_of_views` across Shorts to find a channel's top-performing short videos.
- Collect `video_id` values from a channel to fetch full details for each Short.
- Page through a channel's full Shorts catalog to archive titles and links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/channel-short-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID. |
| `continuation_token` | string | No | Token to continue fetching channel short videos. Default is None. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "continuation_token": "4qmFsgLB…",
  "videos": [
    {
      "author": null,
      "category": null,
      "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
      "description": null,
      "is_live_content": null,
      "keywords": [],
      "number_of_views": 156000,
      "published_time": "",
      "thumbnails": [
        {
          "height": 720,
          "url": "https://i.ytimg.com/vi/9st7OYkUHJk/sardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4…",
          "width": 405
        }
      ],
      "title": "Ep. 35 - Best Tech for a Deserted Island...",
      "type": "SHORTS",
      "video_id": "9st7OYkUHJk"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[]` | One Short from the channel. The list holds the Shorts for the current page. |
| `videos[].video_id` | YouTube video ID of the Short, for example `9st7OYkUHJk`. |
| `videos[].title` | Title of the Short. Long titles can appear cut off with `...`. |
| `videos[].number_of_views` | View count as a number, for example `156000`. |
| `videos[].type` | Kind of video. Every item here has the value `SHORTS`. |
| `videos[].channel_id` | ID of the channel that owns the Short. |
| `videos[].thumbnails[]` | Thumbnail images for the Short. Each entry has a `url`, a `width` and a `height`. |
| `continuation_token` | Token for the next page of Shorts. Send it back as `continuation_token` in the next request. |
| `videos[].author / videos[].category / videos[].description / videos[].published_time / videos[].video_length` | These fields were `null` or empty in this response. Do not rely on them for this API. |

### Notes

- Get the `channel_id` from a channel name or URL with [YouTube Channel ID Lookup](/apis/youtube/web/channel-id) or [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2).
- For the next page, copy the top-level `continuation_token` from the response into the `continuation_token` request parameter.
- Channel IDs start with `UC`. Video IDs are 11-character strings.
- Use [YouTube Channel Information](/apis/youtube/web/channel-info) to get profile details for the same channel.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/channel-short-videos.json`](../../../../catalog/models/youtube/web/channel-short-videos.json) · Store page: https://www.sandbase.ai/model/youtube/web/channel-short-videos
