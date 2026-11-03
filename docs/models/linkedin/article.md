# LinkedIn Article API: pricing, parameters and code examples

`linkedin/article` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00569 per call · **Modes:** sync

Read a public LinkedIn article or newsletter issue by URL, including its full body text, author, publication time, and engagement counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00569**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/article", "url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/article', {'url': 'https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/article", {
  "url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/article", sandbase.Params{
	"url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover",
})
```

Same call via the path form: `POST /v1/api/linkedin/article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public LinkedIn article or newsletter issue URL, e.g. https://www.linkedin.com/pulse/your-article-slug. Pair it with the attachmentUrl returned by linkedin.search_posts_full to read the article behind a post.  |

## Details

Returns the text and details of a public LinkedIn article or newsletter issue. You send the article `url` and get back the title, author, body text, cover image, reaction and comment counts, and timestamps.

### Use cases

- Pull the full text of an article that a LinkedIn post links to, so you can summarize or classify it.
- Track how many reactions and comments a newsletter issue has earned.
- Collect article titles, authors, and descriptions to build a reading list or content archive.
- Check the author's follower count and profile link when you vet who wrote a piece.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/pulse/artificial-intelligence-primer-stephen-dover"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Public LinkedIn article or newsletter issue URL, e.g. https://www.linkedin.com/pulse/your-article-slug. Pair it with the attachmentUrl returned by linkedin.search_posts_full to read the article behind a post. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "author": "Stephen Dover",
    "authorFollowers": 12348,
    "authorUrl": "https://www.linkedin.com/in/stephen-dover-2770b81",
    "body": "Suppose it’s 1794, when Eli Whitney invented the cotton gin. Or perhaps it’s 354…",
    "comments": 2,
    "createdUtc": 1690295321,
    "description": "Suppose it’s 1794, when Eli Whitney invented the cotton gin. Or perhaps it’s 354…",
    "image": "https://media.licdn.com/dms/image/v2/D5612AQGdh4YQrVvtDA/article-cover_image-shr…",
    "reactions": 52,
    "title": "Artificial intelligence: A primer",
    "type": "issue",
    "updatedUtc": 1775838296
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the article was found. A lookup that finds nothing returns `false`. |
| `data.title` | Title of the article or newsletter issue. |
| `data.body` | Body text of the article. Long articles may be returned as plain text in one string. |
| `data.description` | Short summary of the article, taken from its opening lines. |
| `data.author / data.authorUrl` | Name of the author and the link to their LinkedIn profile. |
| `data.authorFollowers` | Number of followers the author has. |
| `data.reactions / data.comments` | Count of reactions and count of comments on the article. |
| `data.createdUtc / data.updatedUtc` | Creation and last update times as Unix timestamps in seconds. |
| `data.type` | Kind of content. The sample shows `issue` for a newsletter issue. |
| `data.image` | URL of the article cover image. |

### Notes

- Pass a public URL such as `https://www.linkedin.com/pulse/your-article-slug` in `url`.
- To read the article behind a post, take the `attachmentUrl` from the post results of [LinkedIn Post Search (full)](/apis/linkedin/search-posts-full) and send it as `url`.
- The response echoes the article link in `data.url`.
- To look at the post that shared an article, try [LinkedIn Post](/apis/linkedin/post).

### Pricing

Billed at the actual cost of each call, about $0.00569 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/article.json`](../../../catalog/models/linkedin/article.json) · Store page: https://www.sandbase.ai/model/linkedin/article
