# Facebook Post Comments API: pricing, parameters and code examples

`facebook/post-comments` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get comments for a Facebook post ID with cursor pagination. Use it to review discussion associated with a known public post or continue through subsequent comment pages.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/post-comments", "postId": "2000749587967633"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/post-comments', {'postId': '2000749587967633'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/post-comments", {
  "postId": "2000749587967633"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/post-comments", sandbase.Params{
	"postId": "2000749587967633",
})
```

Same call via the path form: `POST /v1/api/facebook/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of comments.  |
| `postId` | string | yes | The unique identifier of the Facebook post.  |

## Details

Returns a page of comments for a public Facebook post. It needs a `postId` and returns each comment's text, author, timestamp, and reaction and reply counts, plus a `cursor` for the next page.

### Use cases

- Read the discussion under a known public post to review audience reactions.
- Collect commenter names and profile URLs for a post to see who engages with a page.
- Find comments that have replies by checking `replies_count`, then fetch deeper threads with the comment's `expansion_token`.
- Page through all comments of a post and store them for text analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"postId": "2000749587967633"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `postId` | string | Yes | The unique identifier of the Facebook post. |
| `cursor` | string | No | Pagination cursor for fetching the next set of comments. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "MToxNzkzNjkxMTk5OgF_bdzIR0HVjH3Q5On8BSpj0A6M9ITNje5gKscLyEb6EUwXduwaM75fK-XTgZvE…",
  "results": [
    {
      "author": {
        "gender": "MALE",
        "id": "100030071730868",
        "name": "Haritina Lvs",
        "profile_image": "https://scontent.fshd1-1.fna.fbcdn.net/v/t39.30808-1/834417995_1809401613405546_…",
        "url": "https://www.facebook.com/lovasoa.haritiana.3"
      },
      "comment_id": "Y29tbWVudDoyMDAwNzQ5NTg3OTY3NjMzXzIwMDY4MTI2NjA2OTQ2NTk=",
      "created_time": 1793691151,
      "depth": 0,
      "expansion_token": "MjoxNzkz…",
      "gif": null,
      "image": null,
      "is_gif": false,
      "is_sticker": false,
      "legacy_comment_id": "2006812660694659",
      "message": "Mbl dispo ve",
      "parent_comment_id": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Pagination token for the next page of comments. Send it back as the `cursor` request parameter. |
| `results[].message` | Text of the comment. |
| `results[].comment_id / results[].legacy_comment_id` | Identifiers for the comment. `comment_id` is an encoded string and `legacy_comment_id` is the numeric form. |
| `results[].created_time` | Time the comment was posted, as a Unix timestamp value. |
| `results[].author.name / results[].author.id / results[].author.url` | Display name, ID, and profile link of the commenter. |
| `results[].author.profile_image` | URL of the commenter's small profile picture. |
| `results[].reactions_count` | Number of reactions on the comment. It is returned as a string. |
| `results[].replies_count` | Number of replies to the comment. |
| `results[].depth / results[].parent_comment_id` | `depth` is the nesting level of the comment. `parent_comment_id` is `null` for top-level comments. |
| `results[].expansion_token` | Token tied to the comment, likely used to expand its replies. The response does not say which request accepts it. |

### Notes

- `postId` is the numeric ID of the post, for example `2000749587967633`.
- For the next page, pass the `cursor` value from the response as `cursor` with the same `postId`.
- The fields `gif`, `image`, `sticker`, and `video` are `null` unless the comment has that attachment. `is_gif` and `is_sticker` are booleans.
- To get the post itself, call [Facebook Post](/apis/facebook/post).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/post-comments.json`](../../../catalog/models/facebook/post-comments.json) · Store page: https://www.sandbase.ai/model/facebook/post-comments
