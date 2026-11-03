# LinkedIn Post Search API: pricing, parameters and code examples

`linkedin/search-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search public LinkedIn posts by keyword (text, link, publish date). Results come from search-engine matches over public LinkedIn posts and work best with English keywords.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-posts", "query": "hiring"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-posts', {'query': 'hiring'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-posts", {
  "query": "hiring"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-posts", sandbase.Params{
	"query": "hiring",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The post search query.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `datePosted` | string |  | Filter by recency. One of last-hour, last-day, last-week, last-month, last-year. one of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-year` |
| `requireCursor` | boolean |  | Deprecated. Every source for this search returns a nextCursor, so this changes nothing about the price or which source serves you; it stays accepted so callers that already send it keep working.  |

## Details

Returns public LinkedIn posts that match a keyword search. Each post includes the author, the post text, reaction and comment counts, and a link. The only required input is `query`, and you can narrow results with `datePosted`.

### Use cases

- Track how often people discuss a topic or brand on LinkedIn in the past week.
- Find recent posts from recruiters and companies that mention hiring.
- Collect high-engagement posts on a keyword to study what content gets reactions.
- Build a list of authors who post about a niche subject.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "hiring", "datePosted": "last-week"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The post search query. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `datePosted` | string | No | Filter by recency. One of last-hour, last-day, last-week, last-month, last-year. |
| `requireCursor` | boolean | No | Deprecated. Every source for this search returns a nextCursor, so this changes nothing about the price or which source serves you; it stays accepted so callers that already send it keep working. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_dD2XdS9o_TnOurpj9NGDxQ",
    "posts": [
      {
        "authorName": "Neal 🎙 Schaffer",
        "authorUrl": "https://www.linkedin.com/in/nealschaffer",
        "avatarUrl": "https://media.licdn.com/dms/image/v2/D5603AQEpvaq8manyPQ/profile-displayphoto-sh…",
        "commentCount": 6,
        "createdUtc": 1793296897,
        "id": "7521632349856522240",
        "reactionCount": 15,
        "text": "Hiring an agency isn't a mistake.\n\nHiring one because they called you first is.\n…",
        "url": "https://www.linkedin.com/posts/nealschaffer_hiring-an-agency-isnt-a-mistake-hiri…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].text` | Text of the post. The sample values end with an ellipsis, so the text can be shortened. |
| `data.posts[].url` | Link to the post on LinkedIn. |
| `data.posts[].id` | ID of the post. It is a numeric string and also appears at the end of the post `url`. |
| `data.posts[].authorName / data.posts[].authorUrl` | Display name and LinkedIn page link of the author. The link can point to a person (`/in/`) or a company (`/company/`). |
| `data.posts[].avatarUrl` | Link to the author's profile image. It can be an empty string. |
| `data.posts[].reactionCount / data.posts[].commentCount` | Number of reactions and comments on the post. |
| `data.posts[].createdUtc` | Time the post was created, as a Unix timestamp. |
| `data.nextCursor` | Cursor value to send as `cursor` to get the next page of results. |
| `found` | `true` when the search returned results. |

### Notes

- Pass `data.nextCursor` from a response as `cursor` in the next request to get more posts.
- `datePosted` accepts `last-hour`, `last-day`, `last-week`, `last-month` or `last-year`.
- `requireCursor` is deprecated and has no effect. You can leave it out.
- To get more detail about one post, call [LinkedIn Post](/apis/linkedin/post). For more post fields per result, see [LinkedIn Post Search (full)](/apis/linkedin/search-posts-full).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-posts.json`](../../../catalog/models/linkedin/search-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/search-posts
