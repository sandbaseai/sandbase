# TikTok Comment Replies API: pricing, parameters and code examples

`tiktok/comment-replies` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List the replies to a TikTok comment with cursor pagination (text, author, likes).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/comment-replies", "commentId": "7623828115408274207", "url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/comment-replies', {'commentId': '7623828115408274207', 'url': 'https://www.tiktok.com/@stoolpresidente/video/7623818255903329566'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/comment-replies", {
  "commentId": "7623828115408274207",
  "url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/comment-replies", sandbase.Params{
	"commentId": "7623828115408274207",
	"url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566",
})
```

Same call via the path form: `POST /v1/api/tiktok/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok video URL the comment belongs to.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `commentId` | string | yes | TikTok comment ID (the comment's cid from the comments endpoint).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorUserId`, and it is served only by a source that returns every…  |

## Details

This API returns the replies to one TikTok comment. Each reply includes its text, author, like count and creation time. It needs the video `url` and the `commentId` of the parent comment.

### Use cases

- Read the full discussion under a popular comment to see how viewers respond to it.
- Collect reply authors and their `authorUserId` values to find users who engage with a specific comment thread.
- Rank replies by `likes` to find the most liked responses in a thread.
- Export reply text for sentiment or keyword analysis of a single conversation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566", "commentId": "7623828115408274207"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | TikTok comment ID (the comment's cid from the comments endpoint). |
| `url` | string | Yes | TikTok video URL the comment belongs to. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorUserId`, and it is served only by a source that returns every o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "oakleighsinclair",
        "authorImage": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/9a76406c7ccf257…",
        "authorName": "oakleighsinclair",
        "authorUserId": "6920673278291231750",
        "createdUtc": 1775065855,
        "id": "7623849601356251917",
        "likes": 284,
        "text": "Tea by the Sea with Dave P!",
        "videoId": "7623818255903329566"
      }
    ],
    "nextCursor": "cur_B93AMaX1CCgbuw1jrVtYew"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].id` | ID of the reply. |
| `data.comments[].text` | Text of the reply. |
| `data.comments[].author` | Username of the reply author. |
| `data.comments[].authorName` | Display name of the reply author. It can differ from `author` and can contain special characters. |
| `data.comments[].authorUserId` | Numeric TikTok user ID of the reply author. |
| `data.comments[].authorImage` | URL of the author's avatar image. |
| `data.comments[].likes` | Number of likes on the reply. |
| `data.comments[].createdUtc` | Time the reply was posted, as a Unix timestamp in seconds (UTC). |
| `data.comments[].videoId` | ID of the video the reply belongs to. |
| `data.nextCursor` | Cursor for the next page of replies. Pass it as `cursor` in the next request. |

### Notes

- Get `commentId` from the `id` field of a comment returned by the TikTok comments endpoint. `url` must be the URL of the video that the comment belongs to.
- To page through replies, send the `data.nextCursor` value as `cursor` and keep the same `url` and `commentId`.
- Add `requireFields` with `authorUserId` only if you need that field guaranteed. It applies to the first page only and can raise the price of the call.
- A lookup with no result returns `found: false`.

### Pricing

Billed at the actual cost of each call, about $0.0006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/comment-replies.json`](../../../catalog/models/tiktok/comment-replies.json) · Store page: https://www.sandbase.ai/model/tiktok/comment-replies
