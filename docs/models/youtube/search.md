# YouTube Search API: pricing, parameters and code examples

`youtube/search` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0005 per call · **Modes:** sync

Search YouTube and get matching videos (title, channel, views, length, publish time) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search", "query": "how to cook rice"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search', {'query': 'how to cook rice'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search", {
  "query": "how to cook rice"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search", sandbase.Params{
	"query": "how to cook rice",
})
```

Same call via the path form: `POST /v1/api/youtube/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The YouTube search query.  |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `sortBy` | string |  | Sort order: "relevance" (default) or "popular" (most-viewed). one of: `relevance`, `popular`; default `"relevance"` |
| `uploadDate` | string |  | Filter by upload recency. Omit for any time. one of: `today`, `this_week`, `this_month`, `this_year` |
| `requireCursor` | boolean |  | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |

## Details

Returns a list of YouTube videos that match a search query. Each video includes its title, channel, view count, length, and publish time. The only required input is `query`.

### Use cases

- Find the most-viewed videos on a topic by setting `sortBy` to `popular`.
- Track new videos on a keyword by filtering with `uploadDate`.
- Build a list of channels that publish on a subject using `authorId` and `channel`.
- Collect video IDs and URLs to feed into a video details or transcript lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "how to cook rice"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The YouTube search query. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `requireCursor` | boolean | No | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit it |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |
| `sortBy` | string | No | Sort order: "relevance" (default) or "popular" (most-viewed). |
| `uploadDate` | string | No | Filter by upload recency. Omit for any time. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_O3xdVOP4GZWxFlEHd3vCHg",
    "videos": [
      {
        "authorAvatarUrl": "https://yt3.ggpht.com/IX9PJsD6nZ1sFOVOTCdnC2TrC3RIZxUv1GbENY78IywyYPbsCHdEuQcIfD…",
        "authorId": "UC7tiZxLBusti9zuLOnEkjFw",
        "channel": "Casual Cooking",
        "createdUtc": 1698997695,
        "id": "oQ4y4u6W0Bw",
        "image": "https://i.ytimg.com/vi/oQ4y4u6W0Bw/hq720.jpg",
        "lengthText": "1:02",
        "publishedTime": "3 years ago",
        "title": "How To Cook: White Rice on the Stove",
        "url": "https://www.youtube.com/watch?v=oQ4y4u6W0Bw",
        "views": 2394642
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videos[].id` | The YouTube video ID, for example `oQ4y4u6W0Bw`. |
| `data.videos[].title` | The video title. |
| `data.videos[].url` | Full watch URL for the video. |
| `data.videos[].channel / data.videos[].authorId` | The channel name and the channel ID of the uploader. The ID starts with `UC`. |
| `data.videos[].views` | View count as a number. |
| `data.videos[].lengthText` | Video length as shown on YouTube, for example `1:02`. |
| `data.videos[].publishedTime` | Relative publish time as text, for example `3 years ago`. |
| `data.videos[].createdUtc` | Publish time as a Unix timestamp in seconds. It appears to be derived from the relative `publishedTime`, so treat it as approximate. |
| `data.videos[].image / data.videos[].authorAvatarUrl` | URL of the video thumbnail and URL of the channel avatar image. |
| `data.nextCursor` | Token for the next page of results. Pass it as `cursor` in the next request. |

### Notes

- To page through results, send `nextCursor` from the response as `cursor`. Send `requireFields: ["nextCursor"]` on the first request so a source that returns `nextCursor` serves it.
- `nextCursor` may be absent when the serving source does not return it.
- `found` is `true` when the search returns results.
- For more detail on a single video, pass its `id` to [YouTube Video Details](/apis/youtube/video-detail). To list a channel's uploads, use [YouTube Channel Videos](/apis/youtube/channel-videos) with the `authorId`.

### Pricing

Billed at the actual cost of each call, about $0.0005 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/search.json`](../../../catalog/models/youtube/search.json) · Store page: https://www.sandbase.ai/model/youtube/search
