# LinkedIn Profile Posts (full) API: pricing, parameters and code examples

`linkedin/profile-posts-full` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Fetch recent public LinkedIn profile posts with enriched author, engagement, article, newsletter, media, annotation, repost, and social activity details.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/profile-posts-full", "url": "https://www.linkedin.com/in/williamhgates/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/profile-posts-full', {'url': 'https://www.linkedin.com/in/williamhgates/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/profile-posts-full", {
  "url": "https://www.linkedin.com/in/williamhgates/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/profile-posts-full", sandbase.Params{
	"url": "https://www.linkedin.com/in/williamhgates/",
})
```

Same call via the path form: `POST /v1/api/linkedin/profile-posts-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the public LinkedIn profile whose posts should be returned.  |
| `limit` | integer |  | Most posts to return (1-100, default 10). Ignored on sources that page: each call returns one full page of 50 posts; follow nextCursor for more. Sources that cannot page return up to `limit` posts in one call with no… default `10`; range 1–100 |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `postedLimit` | string |  | Only return posts published within this relative time window. one of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |
| `contextCountry` | string |  | Regional LinkedIn context used when retrieving posts. one of: `any`, `US`, `GB`, `DE`, `FR` |
| `includeReposts` | boolean |  | Whether to include reposts that share content without added commentary. default `true` |
| `postedLimitDate` | string |  | Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string.  |
| `includeQuotePosts` | boolean |  | Whether to include quote posts that add commentary to shared content. default `true` |

## Details

Returns recent public posts from a LinkedIn profile, including the post text, author details, engagement counts, and any shared article. It needs the full profile URL in `url`.

### Use cases

- Track what an executive posts and how much engagement each post gets.
- Collect the articles a public figure shares to see which sources and topics they favor.
- Compare reactions, comments, and reposts across posts to find which topics get the most response.
- Build a feed of a person's latest LinkedIn posts for a monitoring dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/profile-posts-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/williamhgates/", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the public LinkedIn profile whose posts should be returned. |
| `contextCountry` | string | No | Regional LinkedIn context used when retrieving posts. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `includeQuotePosts` | boolean | No | Whether to include quote posts that add commentary to shared content. |
| `includeReposts` | boolean | No | Whether to include reposts that share content without added commentary. |
| `limit` | integer | No | Most posts to return (1-100, default 10). Ignored on sources that page: each call returns one full page of 50 posts; follow nextCursor for more. Sources that cannot page return up to `limit` posts in one call with no nex |
| `postedLimit` | string | No | Only return posts published within this relative time window. |
| `postedLimitDate` | string | No | Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "articleImage": "https://media.licdn.com/dms/image/sync/v2/D4E27AQFkOX_Yu-a3fA/articleshare-shrin…",
        "articleImageHeight": 630,
        "articleImageWidth": 1200,
        "articleLinkLabel": "Open article: World Bank says ‘small AI’ could transform developing countries by…",
        "articleSubtitle": "theguardian.com",
        "articleTitle": "World Bank says ‘small AI’ could transform developing countries",
        "articleUrl": "https://www.theguardian.com/technology/2026/oct/18/world-bank-artificial-intelli…",
        "author": {
          "handle": "williamhgates",
          "headline": "Chair, Gates Foundation and Founder, Breakthrough Energy",
          "id": "ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc",
          "image": "https://media.licdn.com/dms/image/v2/D5603AQF-RYZP55jmXA/profile-displayphoto-sh…",
          "imageHeight": 800,
          "imageWidth": 800,
          "name": "Bill Gates",
          "profileUrl": "https://www.linkedin.com/in/williamhgates"
        },
        "contentAnnotations": [],
        "createdUtc": 1793575556,
        "engagement": {
          "breakdown": [
            {
              "count": 1062,
              "type": "LIKE"
            }
          ],
          "comments": 207,
          "reactions": 1181,
          "reposts": 103
        },
        "id": "7522801130767224832"
      }
    ],
    "nextCursor": "cur_c9q4lpCi36OpcamAqWR-jw"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].text` | Text of the post. Long text may be shortened. |
| `data.items[].url / data.items[].publicationUrl` | Link to the post on LinkedIn. `url` is the public posts page and `publicationUrl` is the feed update link with the share URN. |
| `data.items[].id` | ID of the post. |
| `data.items[].createdUtc` | Post creation time as a Unix timestamp in seconds. |
| `data.items[].author.name / data.items[].author.headline / data.items[].author.handle` | Name, headline, and profile handle of the person who wrote the post. |
| `data.items[].author.profileUrl` | Link to the author's LinkedIn profile. |
| `data.items[].engagement.reactions / data.items[].engagement.comments / data.items[].engagement.reposts` | Total reactions, comments, and reposts for the post. |
| `data.items[].engagement.breakdown[]` | Reaction counts split by type, as `type` and `count` pairs such as `LIKE` and `EMPATHY`. |
| `data.items[].articleTitle / data.items[].articleUrl / data.items[].articleSubtitle` | Title, link, and source domain of the article shared in the post. These appear when the post shares an article. |
| `data.nextCursor` | Cursor for the next page of posts. |

### Notes

- Pass the profile URL in the same form as the example, such as `https://www.linkedin.com/in/williamhgates/`.
- To get the next page, send `data.nextCursor` as `cursor` in the next request.
- `createdUtc` is in seconds, so multiply by 1000 before you pass it to a JavaScript `Date`.
- For a lighter response, use [LinkedIn Profile Posts (basic)](/apis/linkedin/profile-posts-thin). To read the comments on a post, use [LinkedIn Post Comments](/apis/linkedin/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.005 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/profile-posts-full.json`](../../../catalog/models/linkedin/profile-posts-full.json) · Store page: https://www.sandbase.ai/model/linkedin/profile-posts-full
