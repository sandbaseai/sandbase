# Truth Social User Posts API: pricing, parameters and code examples

`truth-social/user-posts` · data API · Truth Social · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a Truth Social account's recent posts by handle - text, engagement (likes, comments, shares), and timestamps as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/user-posts", "handle": "realDonaldTrump"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/user-posts', {'handle': 'realDonaldTrump'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/user-posts", {
  "handle": "realDonaldTrump"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/user-posts", sandbase.Params{
	"handle": "realDonaldTrump",
})
```

Same call via the path form: `POST /v1/api/truth-social/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 20 posts.  |
| `handle` | string | yes | Truth Social handle without the @, e.g. "realDonaldTrump".  |

## Details

Returns a Truth Social account's recent posts as JSON. Each post includes its text, like, comment and share counts, a Unix timestamp, and a link. You send the account handle without the @.

### Use cases

- Track what a public figure posts on Truth Social and when.
- Compare `likes`, `comments` and `shares` across posts to see which ones get the most reaction.
- Build an archive of an account's posts with their post URLs and IDs.
- Feed new post text into a news or monitoring alert.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "realDonaldTrump"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Truth Social handle without the @, e.g. "realDonaldTrump". |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 20 posts. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_UN9TOUrS7RQgenR7fVK2NQ",
    "posts": [
      {
        "avatarUrl": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/avatars/10…",
        "comments": 369,
        "createdUtc": 1793686350,
        "displayName": "Donald J. Trump",
        "id": "117551028635722326",
        "likes": 2088,
        "shares": 707,
        "text": "FAKE ALASKA CANDIDATE DANIAL J. SULLIVAN, JR., IS MISSING IN ACTION! HE HAS TOTA…",
        "url": "https://truthsocial.com/@realDonaldTrump/117551028635722326",
        "username": "realDonaldTrump",
        "verified": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | Unique ID of the post, as a string. |
| `data.posts[].text` | Text of the post. In this sample it is cut with an ellipsis when long. A post that only shares a link shows that link as its text. |
| `data.posts[].url` | Direct link to the post on truthsocial.com. |
| `data.posts[].createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.posts[].likes / data.posts[].comments / data.posts[].shares` | Engagement counts for the post. |
| `data.posts[].username / data.posts[].displayName` | Handle and display name of the account that wrote the post. |
| `data.posts[].verified` | `true` if the account is shown as verified. |
| `data.posts[].avatarUrl` | Link to the account's avatar image. |
| `data.nextCursor` | Cursor to pass as `cursor` to get the next page of posts. |
| `found` | `true` when the account was found. |

### Notes

- Use the handle without the @, for example `realDonaldTrump`.
- Each page holds 20 posts. To get the next page, send the same `handle` with `cursor` set to the `data.nextCursor` value from the previous response.
- Post IDs are numeric strings, and the same ID appears at the end of each post `url`.
- For account details, call [Truth Social Profile](/apis/truth-social/profile). To fetch a single post, call [Truth Social Post](/apis/truth-social/post).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/truth-social/user-posts.json`](../../../catalog/models/truth-social/user-posts.json) · Store page: https://www.sandbase.ai/model/truth-social/user-posts
