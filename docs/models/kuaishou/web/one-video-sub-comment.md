# Kuaishou Video Sub Comments (Web) API: pricing, parameters and code examples

`kuaishou/web/one-video-sub-comment` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns sub-comments and replies for a specific comment on a Kuaishou video. Requires the video ID and root comment ID with optional cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-sub-comment", "photo_id": "3xgarycnydawq3g", "root_comment_id": "908850553827"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-sub-comment', {'photo_id': '3xgarycnydawq3g', 'root_comment_id': '908850553827'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-sub-comment", {
  "photo_id": "3xgarycnydawq3g",
  "root_comment_id": "908850553827"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-sub-comment", sandbase.Params{
	"photo_id": "3xgarycnydawq3g",
	"root_comment_id": "908850553827",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |
| `root_comment_id` | string | yes | 根评论ID/Root comment ID  |

## Details

Returns the replies under one root comment on a Kuaishou video. Each reply includes its text, author, like count, and post time. You send the video's `photo_id` and the `root_comment_id`.

### Use cases

- Show the full reply thread under a top comment on a Kuaishou video.
- Read the text of replies to judge how viewers react to a popular comment.
- Collect the author region and gender fields of repliers to see who joins a discussion.
- Track which replies get the most likes in a thread.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "3xgarycnydawq3g", "root_comment_id": "908850553827"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes |  |
| `root_comment_id` | string | Yes |  |
| `pcursor` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjmt-c26-kce-node638.idchb1az4.hb1.kwaidc.com",
  "pcursor": "911717572030",
  "result": 1,
  "subComments": [
    {
      "authorArea": "黑龙江",
      "authorVerified": false,
      "author_id": 3640978934,
      "author_liked": false,
      "author_name": "차은우",
      "cashTags": {},
      "commentAuthorTags": [],
      "commentBottomTags": [],
      "comment_id": 908917394015,
      "content": "好看啊",
      "headurl": "http://p5.a.yximgs.com/uhead/AB/2024/07/25/11/BMjAyNDA3MjUxMTQ2NTVfMzY0MDk3ODkzN…",
      "headurls": [
        {
          "cdn": "p5.a.yximgs.com",
          "url": "http://p5.a.yximgs.com/uhead/AB/2024/07/25/11/BMjAyNDA3MjUxMTQ2NTVfMzY0MDk3ODkzN…"
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subComments[]` | List of reply comments under the root comment. |
| `subComments[].comment_id` | ID of the reply itself. |
| `subComments[].content` | Text of the reply. It can contain @mentions. |
| `subComments[].author_name / subComments[].author_id` | Display name and numeric ID of the user who wrote the reply. |
| `subComments[].authorArea` | Region shown for the reply author, for example `黑龙江`. |
| `subComments[].likedCount` | Number of likes on the reply. |
| `subComments[].time / subComments[].timestamp` | Post time of the reply. `time` is a formatted string and `timestamp` is a number in milliseconds. |
| `subComments[].replyToUserName / subComments[].reply_to` | Name and numeric ID of the user the reply is addressed to. |
| `subComments[].headurl` | Avatar image URL of the reply author. |
| `pcursor` | Cursor value returned with the page. Pass it as `pcursor` in the next request to get more replies. |

### Notes

- `photo_id` and `root_comment_id` are both required. The root comment ID is the `comment_id` of a top-level comment, which you can get from [Kuaishou Video Comments (Web)](/apis/kuaishou/web/one-video-comment).
- For the next page, send the returned `pcursor` value as the `pcursor` request parameter.
- In replies, `photo_id` appears as a long number, while the request `photo_id` is a short string like `3xgarycnydawq3g`.
- To get the video itself, use [Kuaishou Single Video Details](/apis/kuaishou/web/one-video).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-sub-comment.json`](../../../../catalog/models/kuaishou/web/one-video-sub-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-sub-comment
