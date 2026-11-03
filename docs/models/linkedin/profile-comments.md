# LinkedIn Profile Comments API: pricing, parameters and code examples

`linkedin/profile-comments` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List the comments a LinkedIn member has left on other people's posts - the comment text, its permalink and timestamp, plus the post it was left on and that post's author and engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/profile-comments", "url": "https://www.linkedin.com/in/jeffweiner08"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/profile-comments', {'url': 'https://www.linkedin.com/in/jeffweiner08'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/profile-comments", {
  "url": "https://www.linkedin.com/in/jeffweiner08"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/profile-comments", sandbase.Params{
	"url": "https://www.linkedin.com/in/jeffweiner08",
})
```

Same call via the path form: `POST /v1/api/linkedin/profile-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the LinkedIn member profile whose comments on other people's posts should be listed.  |
| `limit` | integer |  | Maximum number of comments to return. default `100`; range 1–100 |
| `postedLimit` | string |  | Only return comments posted within this window (default any). one of: `any`, `24h`, `week`, `month` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `edited` or `isAuthor`, and it is served only by a source that…  |

## Details

Returns the comments a LinkedIn member has left on other people's posts. Each item has the comment text, its link and timestamp, plus the post it was left on, that post's author and engagement counts. It needs the full profile URL in `url`.

### Use cases

- Track what a executive comments on to see which topics and people they engage with.
- Build a list of the post authors a prospect interacts with most often, for warm outreach.
- Monitor a public figure's recent public remarks on other people's announcements.
- Measure how much reaction a member's comments get by reading the comment `engagement` counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/profile-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/jeffweiner08", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the LinkedIn member profile whose comments on other people's posts should be listed. |
| `limit` | integer | No | Maximum number of comments to return. |
| `postedLimit` | string | No | Only return comments posted within this window (default any). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `edited` or `isAuthor`, and it is served only by a source that returns |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "actor": {
          "id": "ACoAAAFUu6sBhlQbcvAS0GdcPE344dA3vwutzVM",
          "image": "https://media.licdn.com/dms/image/v2/C4D03AQFM3Y2r-OEStw/profile-displayphoto-sh…",
          "linkedinUrl": "https://www.linkedin.com/in/jeffweiner08",
          "name": "Jeff Weiner",
          "position": "Founding Partner Next Play Ventures; Former CEO / Executive Chairman at LinkedIn"
        },
        "commentary": "Congrats Daniel, Ryan, and the entire content team on the incredible recognition…",
        "createdUtc": 1793468458,
        "edited": null,
        "engagement": {
          "comments": 0,
          "likes": 13
        },
        "id": "7522351927607660544",
        "isAuthor": null,
        "post": {
          "author": {
            "headline": "VP of Content | Editor in Chief | Building content-led products, media, and know…",
            "image": "https://media.licdn.com/dms/image/v2/D4E03AQFssLpG8RItRA/profile-displayphoto-sh…",
            "name": "Daniel Roth",
            "profileUrl": "https://www.linkedin.com/in/danielroth1",
            "publicIdentifier": "danielroth1"
          },
          "engagement": {
            "comments": 68,
            "reactions": 671,
            "reposts": 8
          },
          "id": "7522345650261270528",
          "postedUtc": 1793466961,
          "text": "If you'd told me early in my career that I'd be sitting in the Hollywood Palladi…",
          "url": "https://www.linkedin.com/posts/danielroth1_if-youd-told-me-early-in-my-career-th…"
        },
        "url": "https://www.linkedin.com/feed/update/urn:li:ugcPost:7522345650261270528?commentU…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | ID of the comment. |
| `data.items[].commentary` | Text of the comment. Long text may be cut. |
| `data.items[].url` | Permalink to the comment on LinkedIn, inside the post it belongs to. |
| `data.items[].createdUtc` | Time the comment was created, as a Unix timestamp in seconds. |
| `data.items[].engagement.likes / data.items[].engagement.comments` | Number of likes and replies on the comment itself. |
| `data.items[].actor.name / data.items[].actor.position / data.items[].actor.linkedinUrl` | Name, headline and profile URL of the member who wrote the comment. |
| `data.items[].post.id / data.items[].post.url` | ID and link of the post that was commented on. |
| `data.items[].post.text` | Text of the post that was commented on. Some posts have no `text` key. |
| `data.items[].post.postedUtc` | Time the post was published, as a Unix timestamp in seconds. |
| `data.items[].post.author.name / data.items[].post.author.headline / data.items[].post.author.profileUrl / data.items[].post.author.publicIdentifier` | Name, headline, profile URL and public handle of the person who wrote the post. |
| `data.items[].post.engagement.reactions / data.items[].post.engagement.comments / data.items[].post.engagement.reposts` | Counts of reactions, comments and reposts on the post. |

### Notes

- Use the full profile address as `url`, for example `https://www.linkedin.com/in/jeffweiner08`. You can find it with [LinkedIn Profile Search](/apis/linkedin/search-profiles).
- `limit` accepts 1 to 100. Use `postedLimit` with `24h`, `week` or `month` to keep only recent comments.
- `edited` and `isAuthor` came back as `null` in this response. Name them in `requireFields` if you need them, but the call may then cost more.
- To read the replies under a comment, call [LinkedIn Comment Replies](/apis/linkedin/comment-replies). For the full post, call [LinkedIn Post](/apis/linkedin/post).

### Pricing

Billed at the actual cost of each call, about $0.0029 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/profile-comments.json`](../../../catalog/models/linkedin/profile-comments.json) · Store page: https://www.sandbase.ai/model/linkedin/profile-comments
