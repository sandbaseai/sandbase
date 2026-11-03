# YouTube Comment Replies API: pricing, parameters and code examples

`youtube/comment-replies` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List replies to a YouTube comment using a continuation token with cursor pagination (text, author, likes, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/comment-replies", "continuationToken": "Eg0SC19fZm1EajBaSjFRGAYygwEaUBIaVWd3aXRjRk9fdmtpM0x4LUNfZDRBYUFCQWciAggAKhhVQ1g2T1EzRGtjc2JZTkU2SDh1UVF1VkEyC19fZm1EajBaSjFRQABICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3dpdGNGT192a2kzTHgtQ19kNEFhQUJBZw=="}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/comment-replies', {'continuationToken': 'Eg0SC19fZm1EajBaSjFRGAYygwEaUBIaVWd3aXRjRk9fdmtpM0x4LUNfZDRBYUFCQWciAggAKhhVQ1g2T1EzRGtjc2JZTkU2SDh1UVF1VkEyC19fZm1EajBaSjFRQABICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3dpdGNGT192a2kzTHgtQ19kNEFhQUJBZw=='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/comment-replies", {
  "continuationToken": "Eg0SC19fZm1EajBaSjFRGAYygwEaUBIaVWd3aXRjRk9fdmtpM0x4LUNfZDRBYUFCQWciAggAKhhVQ1g2T1EzRGtjc2JZTkU2SDh1UVF1VkEyC19fZm1EajBaSjFRQABICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3dpdGNGT192a2kzTHgtQ19kNEFhQUJBZw=="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/comment-replies", sandbase.Params{
	"continuationToken": "Eg0SC19fZm1EajBaSjFRGAYygwEaUBIaVWd3aXRjRk9fdmtpM0x4LUNfZDRBYUFCQWciAggAKhhVQ1g2T1EzRGtjc2JZTkU2SDh1UVF1VkEyC19fZm1EajBaSjFRQABICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3dpdGNGT192a2kzTHgtQ19kNEFhQUJBZw==",
})
```

Same call via the path form: `POST /v1/api/youtube/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `continuationToken` | string | yes | Replies continuation token from the comments endpoint, or the continuationToken from a previous replies response for further pagination.  |

## Details

Returns a page of replies to one YouTube comment. You send a `continuationToken` and get back each reply's text, author, like count and publish time, plus a cursor for the next page.

### Use cases

- Read the full reply thread under a popular comment to see how viewers respond.
- Collect reply text and `likes` for sentiment analysis on a single comment thread.
- Find which authors reply most often under a creator's top comment.
- Archive a complete reply thread by following `nextCursor` until no more pages come back.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"continuationToken": "Eg0SC19fZm1EajBaSjFRGAYygwEaUBIaVWd3aXRjRk9fdmtpM0x4LUNfZDRBYUFCQWciAggAKhhVQ1g2T1EzRGtjc2JZTkU2SDh1UVF1VkEyC19fZm1EajBaSjFRQABICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3dpdGNGT192a2kzTHgtQ19kNEFhQUJBZw=="}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuationToken` | string | Yes | Replies continuation token from the comments endpoint, or the continuationToken from a previous replies response for further pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "comments": [
      {
        "authorAvatarUrl": "https://yt3.ggpht.com/dekDIHrFk6_0BKWxKBc3uxWWG52rCE4f0rOF08qAojl-bs9kAgXb3YMdHO…",
        "authorId": "UCtobA_pDuI8NedREy2N81vA",
        "authorName": "@manojsharoff4235",
        "authorUrl": "https://youtube.com/@manojsharoff4235",
        "authorVerified": false,
        "content": "Your welcome MrBeast!!!!!",
        "createdUtc": 1783064892,
        "id": "UgwitcFO_vki3Lx-C_d4AaABAg.AY-YZeYup8QAY-ZiQHH3Nb",
        "likes": 15,
        "publishedTime": "4 months ago"
      }
    ],
    "nextCursor": "Eg0SC19fZm1EajBaSjFRGAYy2AIK0AFnZXRfY29tbWVudF93aXRoX3JlcGxpZXNfc3RyZWFtLS1DbVlJ…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].content` | Text of the reply. |
| `data.comments[].id` | ID of the reply. It starts with the parent comment ID, followed by a dot and a reply suffix. |
| `data.comments[].authorName / authorUrl` | Handle of the reply author and a link to their YouTube channel. |
| `data.comments[].authorId` | Channel ID of the reply author. |
| `data.comments[].authorVerified` | `true` if the author has a verified badge, `false` otherwise. |
| `data.comments[].authorAvatarUrl` | URL of the author's profile image. |
| `data.comments[].likes` | Number of likes on the reply. |
| `data.comments[].publishedTime` | Relative publish time as shown on YouTube, such as `4 months ago`. It adds `(edited)` when the reply was edited. |
| `data.comments[].createdUtc` | Creation time of the reply as a Unix timestamp in seconds. |
| `data.nextCursor` | Token for the next page of replies. Send it as `continuationToken` in the next request. |
| `found` | `true` when the lookup returned data. |

### Notes

- Get the first `continuationToken` from the replies entry of a comment returned by [YouTube Video Comments](/apis/youtube/video-comments).
- To paginate, pass `data.nextCursor` from the last response as `continuationToken` in the next call.
- `createdUtc` is the same for all replies in the sample response, while `publishedTime` is relative text. Use `id` to tell replies apart.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/comment-replies.json`](../../../catalog/models/youtube/comment-replies.json) · Store page: https://www.sandbase.ai/model/youtube/comment-replies
