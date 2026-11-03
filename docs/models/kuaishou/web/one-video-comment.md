# Kuaishou Video Comments (Web) API: pricing, parameters and code examples

`kuaishou/web/one-video-comment` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns root comments for a specified Kuaishou video, including author details, content, and like counts. Queries require a video ID and support cursor pagination.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-comment", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-comment', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-comment", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-comment", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Returns root comments for one Kuaishou video, including the comment text, author details, like count and post time. It needs the video's `photo_id`, and it accepts an optional `pcursor` to fetch the next page.

### Use cases

- Collect viewer comments on a Kuaishou video for sentiment analysis.
- Find which comments on a video get the most likes.
- Map where commenters live by reading the `authorArea` value on each comment.
- Export comment text and author IDs to track repeat commenters across videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes |  |
| `pcursor` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "commentCount": 3053,
  "host-name": "public-bjx-c34-kce-node3731.idchb1az1.hb1.kwaidc.com",
  "pcursor": "975590339642",
  "result": 1,
  "rootComments": [
    {
      "authorArea": "江西",
      "authorVerified": false,
      "author_id": 1727775365,
      "author_liked": false,
      "author_name": "韩柚希（七谨希）",
      "cashTags": {},
      "commentAuthorTags": [],
      "commentBottomTags": [],
      "comment_id": 1137733188081,
      "content": "回复 挽风：枕头垫高，不要醒来[呆住][呆住][呆住]。",
      "headurl": "http://p5.a.yximgs.com/uhead/AB/2025/12/19/23/BMjAyNTEyMTkyMzE4NDlfMTcyNzc3NTM2N…",
      "headurls": [
        {
          "cdn": "p5.a.yximgs.com",
          "url": "http://p5.a.yximgs.com/uhead/AB/2025/12/19/23/BMjAyNTEyMTkyMzE4NDlfMTcyNzc3NTM2N…"
        }
      ]
    }
  ],
  "subCommentsMap": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `commentCount` | Total number of comments on the video. |
| `pcursor` | Cursor for the next page of comments. Send it as the `pcursor` request parameter. |
| `rootComments[].comment_id` | ID of the comment. |
| `rootComments[].content` | Text of the comment. Replies to another user start with `回复` followed by that user's name. |
| `rootComments[].likedCount` | Number of likes on the comment. |
| `rootComments[].author_id / rootComments[].author_name` | ID and display name of the comment author. |
| `rootComments[].authorArea / rootComments[].user_sex` | Area shown for the author, and the sex code of the user (`M` or `F`). |
| `rootComments[].time / rootComments[].timestamp` | Comment time as a text date and as a numeric timestamp. |
| `rootComments[].replyToUserName / rootComments[].reply_to` | Name and ID of the user this comment replies to. |
| `rootComments[].headurl` | URL of the author's avatar image. |

### Notes

- `photo_id` is the numeric ID of the video, for example `5193494945927590140`. Use [Kuaishou Single Video Details](/apis/kuaishou/web/one-video) to check the video itself.
- To get the next page, pass the `pcursor` value from the response in your next request with the same `photo_id`.
- `subCommentsMap` was empty in this response. Use [Kuaishou Video Sub Comments (Web)](/apis/kuaishou/web/one-video-sub-comment) to read replies to a comment.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-comment.json`](../../../../catalog/models/kuaishou/web/one-video-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-comment
