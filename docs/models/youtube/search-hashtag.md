# YouTube Hashtag Search API: pricing, parameters and code examples

`youtube/search-hashtag` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search YouTube videos by hashtag with cursor pagination (title, channel, views, length, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search-hashtag", "hashtag": "funny"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search-hashtag', {'hashtag': 'funny'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search-hashtag", {
  "hashtag": "funny"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search-hashtag", sandbase.Params{
	"hashtag": "funny",
})
```

Same call via the path form: `POST /v1/api/youtube/search-hashtag` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Content filter. Only "all" is served: no source we buy returns a Shorts row with the channel and publish time this endpoint requires. one of: `all` |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `hashtag` | string | yes | Hashtag to search for (without the leading #).  |

## Details

Returns a page of YouTube videos that match a hashtag. Each video includes its title, channel, view count, length and publish time. The only required input is `hashtag`, written without the leading #.

### Use cases

- Find popular videos under a hashtag such as `funny` to see which topics get the most views.
- Collect channels that post often under a hashtag to build an outreach or creator list.
- Track which videos appear for a campaign hashtag and link back to each one with its `url`.
- Compare video lengths and view counts across a hashtag to study what formats perform well.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search-hashtag" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "funny"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to search for (without the leading #). |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `type` | string | No | Content filter. Only "all" is served: no source we buy returns a Shorts row with the channel and publish time this endpoint requires. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_eL-1ozhU5547jmeI0G5-Fg",
    "videos": [
      {
        "authorAvatarUrl": "https://yt3.ggpht.com/k1ZJ7WufFx4wSWlXXExVel17gg_Uy08MjThN2bKqUdSO4r3tOD2QwCZhfq…",
        "authorHandle": "PAW_YTP",
        "authorId": "UCHUcU1A9KhO9Sf4-8E5-ArA",
        "channelTitle": "PAW YTP",
        "createdUtc": 1783064897,
        "durationSeconds": 810,
        "id": "7IYXGdzlHDU",
        "image": "https://i.ytimg.com/vi/7IYXGdzlHDU/hq720.jpg",
        "lengthText": "13:30",
        "publishedTime": "4 months ago",
        "title": "BLUEY - TRY NOT TO LAUGH 😂 [YTP] GOOF CHAOS",
        "url": "https://www.youtube.com/watch?v=7IYXGdzlHDU"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videos[].id` | YouTube video ID. It is also the value of `v` in the video `url`. |
| `data.videos[].title` | Title of the video. |
| `data.videos[].url` | Link to the watch page for the video. |
| `data.videos[].views` | View count as a number. |
| `data.videos[].durationSeconds / data.videos[].lengthText` | Video length as a number of seconds and as display text such as `13:30`. |
| `data.videos[].publishedTime / data.videos[].createdUtc` | `publishedTime` is a relative label such as `4 months ago`. `createdUtc` is a numeric timestamp for the same event, in Unix seconds. |
| `data.videos[].channelTitle / data.videos[].authorHandle` | Display name and handle of the channel that posted the video. |
| `data.videos[].authorId` | Channel ID, starting with `UC`. Use it to look up the channel. |
| `data.videos[].image / data.videos[].authorAvatarUrl` | Thumbnail image URL of the video and avatar image URL of the channel. |
| `data.nextCursor` | Token to pass as `cursor` to get the next page of videos. |

### Notes

- Send the hashtag without the leading #. For example, use `funny`, not `#funny`.
- For the next page, repeat the request with the same `hashtag` and set `cursor` to `data.nextCursor` from the previous response.
- `type` accepts only `all`, which is the default behavior, so you can leave it out.
- To get more detail on a result, pass its video ID to [YouTube Video Details](/apis/youtube/video-detail), or pass `authorId` to [YouTube Channel Videos](/apis/youtube/channel-videos).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/search-hashtag.json`](../../../catalog/models/youtube/search-hashtag.json) · Store page: https://www.sandbase.ai/model/youtube/search-hashtag
