# YouTube Related Videos (Web) API: pricing, parameters and code examples

`youtube/web/relate-video` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of related videos for a given YouTube video ID. Supports pagination using a continuation token to retrieve additional recommendations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/relate-video", "video_id": "LuIL5JATZsc"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/relate-video', {'video_id': 'LuIL5JATZsc'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/relate-video", {
  "video_id": "LuIL5JATZsc"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/relate-video", sandbase.Params{
	"video_id": "LuIL5JATZsc",
})
```

Same call via the path form: `POST /v1/api/youtube/web/relate-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string | yes | Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc.  |
| `continuation_token` | string |  | Token to continue fetching related videos. Default is None.  |

## Details

Returns a list of videos that YouTube recommends next to a given video. You send a `video_id` and get back each related video's title, channel, length, publish age and thumbnails, plus a token for the next page.

### Use cases

- Build a "watch next" feed for a video you already track.
- Map which channels YouTube groups with a given video, such as channels that make similar music mixes.
- Collect titles and channel IDs of related videos to study a topic cluster.
- Walk through several pages of recommendations by repeating the call with the returned token.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/relate-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "LuIL5JATZsc"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. |
| `continuation_token` | string | No | Token to continue fetching related videos. Default is None. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "continuation_token": "CBQSKRIL…",
  "number_of_videos": 20,
  "videos": [
    {
      "author": "CozyCraft",
      "category": null,
      "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
      "description": "",
      "is_live_content": null,
      "keywords": [],
      "number_of_views": 0,
      "published_time": "6mo ago",
      "thumbnails": [
        {
          "height": 94,
          "url": "https://i.ytimg.com/vi/CijACOd7jQk/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDgg…",
          "width": 168
        }
      ],
      "title": "just relax, everything can wait… (minecraft music & ambience)",
      "type": "NORMAL",
      "video_id": "CijACOd7jQk"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].video_id` | ID of the related video. Use it as `video_id` in other YouTube calls. |
| `videos[].title` | Title of the related video. |
| `videos[].author / videos[].channel_id` | Name and channel ID of the channel that posted the related video. |
| `videos[].video_length` | Length of the video as a clock string, such as `11:00:00`. |
| `videos[].published_time` | Relative publish age as text, such as `6mo ago` or `13d ago`. It is not an exact date. |
| `videos[].number_of_views` | View count of the related video. The sample shows `0` for every item, so do not rely on it. |
| `videos[].thumbnails[]` | Thumbnail images with `url`, `width` and `height`. Each video lists two sizes. |
| `videos[].type` | Kind of item. The sample shows `NORMAL`. |
| `number_of_videos` | Count of videos returned in this page. |
| `continuation_token` | Token that loads the next page of related videos. |

### Notes

- Take `video_id` from the watch URL. In `https://www.youtube.com/watch?v=LuIL5JATZsc`, the ID is `LuIL5JATZsc`.
- For the next page, send the same `video_id` with the `continuation_token` from the previous response.
- In the sample, `category`, `is_live_content`, `description` and `keywords` are `null` or empty. Call [YouTube Video Details](/apis/youtube/video-detail) for a related video to get fuller data.
- For channel profile data, pass a `channel_id` from this response to [YouTube Channel Information](/apis/youtube/web/channel-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel ID Lookup](/apis/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/apis/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/apis/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/relate-video.json`](../../../../catalog/models/youtube/web/relate-video.json) · Store page: https://www.sandbase.ai/model/youtube/web/relate-video
