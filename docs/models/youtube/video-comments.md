# YouTube Video Comments API: pricing, parameters and code examples

`youtube/video-comments` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

List the comments on a YouTube video or Short by URL with cursor pagination (text, author, likes, reply count).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-comments", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-comments', {'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-comments", {
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-comments", sandbase.Params{
	"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full YouTube video URL. Shorts (youtube.com/shorts/...) and youtu.be URLs also work.  |
| `order` | string |  | Comment order (e.g. top, newest). one of: `top`, `newest` |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `likes`, and it is served only by a source that returns every one of…  |

## Details

This API returns a page of comments for a YouTube video or Short. You pass the video URL, and each comment includes its text, author, like count, reply count, and a relative publish time.

### Use cases

- Pull the top comments on a product review video to see what viewers praise or complain about.
- Sort a video's comments by `newest` to watch fresh reactions after a launch or announcement.
- Collect author channel IDs from comments to find active viewers or possible collaborators.
- Rank comments by `likes` and `replies` to find the threads that drive the most discussion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full YouTube video URL. Shorts (youtube.com/shorts/...) and youtu.be URLs also work. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `order` | string | No | Comment order (e.g. top, newest). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `likes`, and it is served only by a source that returns every one of t |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "@bdr8823",
        "authorAvatarUrl": "https://yt3.ggpht.com/ytc/AIdro_kcDoQJUNDkDzTrA5kaF5ADVujN-6UcDjMP2Kydtw=s88-c-k…",
        "authorId": "UCdi6tGxvFvTRGe-7dAn7m7w",
        "authorUrl": "https://www.youtube.com/channel/UCdi6tGxvFvTRGe-7dAn7m7w",
        "id": "UgwPwTibxdgqCHZxktd4AaABAg",
        "likes": 70000,
        "publishedTime": "7 years ago",
        "replies": 664,
        "text": "My algebra teacher said that this was a link to the test answers"
      }
    ],
    "nextCursor": "cur_81djzPHe08vulMAyPdGcGQ"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].text` | The body of the comment. |
| `data.comments[].author` | The display handle of the commenter, such as `@bdr8823`. |
| `data.comments[].authorId / data.comments[].authorUrl` | The commenter's YouTube channel ID and the link to their channel page. |
| `data.comments[].authorAvatarUrl` | The link to the commenter's profile picture. |
| `data.comments[].id` | The unique ID of the comment. |
| `data.comments[].likes` | The number of likes on the comment. Large values look rounded in the sample (for example `70000`), so treat them as approximate unless you set `requireFields` to `likes`. |
| `data.comments[].replies` | The number of replies to the comment. |
| `data.comments[].publishedTime` | When the comment was posted, as relative text such as `7 years ago`, not an exact date. |
| `data.nextCursor` | The token to pass as `cursor` to get the next page of comments. |
| `found` | `true` when the video lookup returned data. |

### Notes

- Copy the `url` from the video page. Shorts URLs (youtube.com/shorts/...) and youtu.be links also work.
- To page through comments, send `data.nextCursor` from the last response as `cursor`, with the same `url` and `order`.
- Use `order` with `top` or `newest` to choose the sort.
- To read the replies under a comment, call [YouTube Comment Replies](/apis/youtube/comment-replies). For video metadata, call [YouTube Video Details](/apis/youtube/video-detail).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/video-comments.json`](../../../catalog/models/youtube/video-comments.json) · Store page: https://www.sandbase.ai/model/youtube/video-comments
