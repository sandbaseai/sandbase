# LinkedIn Post Search (full) API: pricing, parameters and code examples

`linkedin/search-posts-full` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.004 per call · **Modes:** sync

Search public LinkedIn posts with rich author, engagement, attachment, and poll details.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.004**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-posts-full", "query": "artificial intelligence"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-posts-full', {'query': 'artificial intelligence'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-posts-full", {
  "query": "artificial intelligence"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-posts-full", sandbase.Params{
	"query": "artificial intelligence",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-posts-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Order results by search relevance or publication date. one of: `relevance`, `date`; default `"relevance"` |
| `limit` | integer |  | Maximum number of posts to return (1-100, default 10). The upper bound is one LinkedIn search page. default `10`; range 1–100 |
| `query` | string | yes | LinkedIn post search query, including quoted terms or Boolean operators accepted by LinkedIn search.  |
| `authorUrls` | array |  | Only return posts authored by these LinkedIn profile or company URLs.  |
| `datePosted` | string |  | Only return posts published within this relative time window. Last-hour and windows beyond one month route to the provider that supports them. one of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-three-months`, `last-six-months`, `last-year`; default `"last-day"` |
| `contentType` | string |  | Only return posts carrying this content type. one of: `all`, `videos`, `images`, `jobs`, `live-videos`, `documents`, `collaborative-articles` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `attachmentType` or `pollOptions`, and it is served only by a source…  |
| `authorKeywords` | string |  | Only return posts whose author profile headline or job title contains at least one of these keywords.  |
| `authorIndustryIds` | array |  | Only return posts by authors associated with these LinkedIn industry IDs.  |
| `authorCompanyNames` | array |  | Only return posts by people associated with these company names.  |
| `mentioningMemberUrls` | array |  | Only return posts mentioning these LinkedIn member profile URLs.  |

## Details

Returns public LinkedIn posts that match a search query. Each post includes its author, text, URL, creation time and comment and reaction counts. The only required input is `query`, and filters narrow results by date, author, content type and more.

### Use cases

- Track how people on LinkedIn talk about a topic, brand or product over the past week.
- Find active authors in a niche by searching a keyword and filtering on `authorKeywords` or `authorCompanyNames`.
- Collect post URLs and IDs to feed into comment or reaction lookups for deeper engagement analysis.
- Monitor posts that mention specific members with `mentioningMemberUrls`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-posts-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "relevance", "limit": 10, "query": "artificial intelligence", "datePosted": "last-week"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | LinkedIn post search query, including quoted terms or Boolean operators accepted by LinkedIn search. |
| `authorCompanyNames` | array | No | Only return posts by people associated with these company names. |
| `authorIndustryIds` | array | No | Only return posts by authors associated with these LinkedIn industry IDs. |
| `authorKeywords` | string | No | Only return posts whose author profile headline or job title contains at least one of these keywords. |
| `authorUrls` | array | No | Only return posts authored by these LinkedIn profile or company URLs. |
| `contentType` | string | No | Only return posts carrying this content type. |
| `datePosted` | string | No | Only return posts published within this relative time window. Last-hour and windows beyond one month route to the provider that supports them. |
| `limit` | integer | No | Maximum number of posts to return (1-100, default 10). The upper bound is one LinkedIn search page. |
| `mentioningMemberUrls` | array | No | Only return posts mentioning these LinkedIn member profile URLs. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `attachmentType` or `pollOptions`, and it is served only by a source t |
| `sort` | string | No | Order results by search relevance or publication date. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "posts": [
      {
        "author": {
          "name": "Angela H.",
          "profileUrl": "https://www.linkedin.com/in/angela-h-75a45431b",
          "publicIdentifier": "angela-h-75a45431b"
        },
        "createdUtc": 1793675023,
        "engagement": {
          "comments": 1,
          "reactions": 0
        },
        "id": "7523218324076326913",
        "text": "Some of the greatest opportunities in artificial intelligence may not come from …",
        "url": "https://www.linkedin.com/posts/angela-h-75a45431b_artificialintelligence-ai-scie…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | Numeric ID of the post, returned as a string. |
| `data.posts[].url` | Public LinkedIn URL of the post. |
| `data.posts[].text` | Post text. Long posts may be shortened. |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds. |
| `data.posts[].author.name` | Display name of the author. |
| `data.posts[].author.profileUrl / data.posts[].author.publicIdentifier` | LinkedIn profile URL of the author and the identifier used in that URL. |
| `data.posts[].engagement.reactions / data.posts[].engagement.comments` | Number of reactions and number of comments on the post. |
| `found` | `true` when the search returned results. |

### Notes

- Use `sort` set to `date` to order by publication date instead of relevance. `datePosted` defaults to `last-day`.
- `limit` accepts 1 to 100 and defaults to 10. No pagination parameter exists, so one call returns one search page.
- Attachment and poll fields appear only when the serving source returns them. Name them in `requireFields` (for example `attachmentType` or `pollOptions`) to require them, which can change the price.
- Pass a post `url` to [LinkedIn Post](/apis/linkedin/post) for the full post, or use [LinkedIn Post Comments](/apis/linkedin/post-comments) to read its comments.

### Pricing

Billed at the actual cost of each call, about $0.004 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-posts-full.json`](../../../catalog/models/linkedin/search-posts-full.json) · Store page: https://www.sandbase.ai/model/linkedin/search-posts-full
