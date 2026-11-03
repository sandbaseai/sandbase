# LinkedIn Post Comments API: pricing, parameters and code examples

`linkedin/post-comments` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List comments on a LinkedIn post - full text, commenter name/URL/job title, timestamps, and engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/post-comments", "url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/post-comments', {'url': 'https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/post-comments", {
  "url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/post-comments", sandbase.Params{
	"url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ",
})
```

Same call via the path form: `POST /v1/api/linkedin/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the LinkedIn post to list comments for.  |
| `limit` | integer |  | Maximum number of comments to return. default `100`; range 1–100 |
| `postedLimit` | string |  | Only return comments posted within this window (default any). one of: `any`, `24h`, `week`, `month`, `3months`, `6months`, `year` |

## Details

Returns the comments on a LinkedIn post, including comment text, commenter details, timestamps and like and reply counts. It needs the full URL of the post in the `url` parameter.

### Use cases

- Read the public reaction to a company announcement without opening the post.
- Collect commenter names, profile URLs and job titles to see which roles engage with a post.
- Flag spam or complaint comments on a brand's posts for review.
- Build a dataset of comment text for sentiment analysis on a single post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/stripe_philip-kl%C3%B6ckner-in-conversation-with-conor-activity-7477791740645564416-tIbZ", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the LinkedIn post to list comments for. |
| `limit` | integer | No | Maximum number of comments to return. |
| `postedLimit` | string | No | Only return comments posted within this window (default any). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "actor": {
          "id": "ACoAABRFjvYBzGevlr0HJfL7UbMH7vjgln6iBRg",
          "image": "https://media.licdn.com/dms/image/v2/D4D03AQFG38rxIus6KA/profile-displayphoto-cr…",
          "linkedinUrl": "https://www.linkedin.com/in/trishalhjohnson",
          "name": "Trisha Johnson",
          "type": "profile"
        },
        "commentary": "BEWARE! SCAM ALERT! STRIPE IS FRAUDULENT!\n\nStripe allowed me to create an accoun…",
        "createdUtc": 1786569458,
        "edited": false,
        "engagement": {
          "comments": 0,
          "likes": 0
        },
        "id": "7493415427058929664",
        "pinned": false,
        "url": "https://www.linkedin.com/feed/update/urn:li:ugcPost:7477791277128765440?commentU…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].commentary` | Text of the comment. Long comments may be shortened in this view. |
| `data.items[].actor.name` | Display name of the person or page that wrote the comment. |
| `data.items[].actor.linkedinUrl` | LinkedIn profile URL of the commenter. |
| `data.items[].actor.position` | Headline or job title text of the commenter. Some commenters have no `position`. |
| `data.items[].actor.id / data.items[].actor.type` | Internal LinkedIn ID of the commenter and the kind of actor, such as `profile`. |
| `data.items[].actor.image` | URL of the commenter's profile photo. |
| `data.items[].createdUtc` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.items[].engagement.likes / data.items[].engagement.comments` | Number of likes on the comment and number of replies to it. |
| `data.items[].id` | ID of the comment. |
| `data.items[].url` | Link to the post that opens at this comment. |
| `data.items[].edited / data.items[].pinned` | Whether the comment was edited and whether it is pinned. |

### Notes

- Copy the post URL from the LinkedIn post page and pass it as `url`.
- Use `limit` to cap the number of comments (1 to 100, default 100). Use `postedLimit` to keep only recent comments, for example `24h` or `week`.
- Each comment `id` is a long numeric string. Keep it as a string.
- To see replies or likes for a comment, call [LinkedIn Comment Replies](/apis/linkedin/comment-replies) or [LinkedIn Comment Reactions](/apis/linkedin/comment-reactions).

### Pricing

Billed at the actual cost of each call, about $0.0029 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/post-comments.json`](../../../catalog/models/linkedin/post-comments.json) · Store page: https://www.sandbase.ai/model/linkedin/post-comments
