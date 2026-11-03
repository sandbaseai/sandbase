# Instagram Comment Replies API: pricing, parameters and code examples

`instagram/comment-replies` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List the replies to an Instagram comment with cursor pagination (text, author, likes).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/comment-replies", "commentId": "18126632131325044", "url": "https://www.instagram.com/p/C8rKmYvsrck/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/comment-replies', {'commentId': '18126632131325044', 'url': 'https://www.instagram.com/p/C8rKmYvsrck/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/comment-replies", {
  "commentId": "18126632131325044",
  "url": "https://www.instagram.com/p/C8rKmYvsrck/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/comment-replies", sandbase.Params{
	"commentId": "18126632131325044",
	"url": "https://www.instagram.com/p/C8rKmYvsrck/",
})
```

Same call via the path form: `POST /v1/api/instagram/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Instagram post or reel URL the comment belongs to.  |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `commentId` | string | yes | Instagram comment ID (a comment's id from the Instagram Post Comments endpoint).  |

## Details

This API returns the replies to one Instagram comment. It needs the post or reel `url` and the `commentId` of the parent comment. Each reply includes its text, author, like count and creation time.

### Use cases

- Read the full conversation under a popular comment to see how followers respond to a creator.
- Collect reply text from a comment thread for sentiment or language analysis.
- Find which accounts reply most often under a post by counting `author` values.
- Check whether verified accounts take part in a comment thread.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/C8rKmYvsrck/", "commentId": "18126632131325044"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | Instagram comment ID (a comment's id from the Instagram Post Comments endpoint). |
| `url` | string | Yes | Full Instagram post or reel URL the comment belongs to. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "author": "frau.pom",
        "avatarUrl": "https://scontent-lax3-2.cdninstagram.com/v/t51.2885-19/106036945_317567719266309…",
        "createdUtc": 1723278872,
        "id": "18345120157141050",
        "likes": 1,
        "text": "@lektorat.schreibwege Das klingt ja toll. Wie bist du an den Job gekommen?",
        "userId": "1437336707",
        "verified": false
      }
    ],
    "nextCursor": null
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].id` | ID of the reply. |
| `data.comments[].text` | Text of the reply. It often starts with an @mention of the user being answered. |
| `data.comments[].author` | Username of the account that wrote the reply. |
| `data.comments[].userId` | Numeric ID of the author's account. |
| `data.comments[].likes` | Number of likes on the reply. |
| `data.comments[].createdUtc` | Time the reply was posted, as a Unix timestamp in seconds (UTC). |
| `data.comments[].verified` | `true` if the author has a verified badge, `false` otherwise. |
| `data.comments[].avatarUrl` | URL of the author's profile picture. |
| `data.nextCursor` | Cursor for the next page of replies. It is `null` when there are no more pages. |
| `found` | `true` when the lookup returned a result. |

### Notes

- Get `commentId` from the `id` field of a comment returned by [Instagram Post Comment List](/apis/instagram/post-comments).
- To get the next page, pass the value of `data.nextCursor` as `cursor`. A `null` value means the list is complete.
- Reply `id` values are strings. Keep them as strings in your code.
- A newer version of this endpoint exists: [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/comment-replies.json`](../../../catalog/models/instagram/comment-replies.json) · Store page: https://www.sandbase.ai/model/instagram/comment-replies
