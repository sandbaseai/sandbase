# Facebook Post Search API: pricing, parameters and code examples

`facebook/search-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.03 per call · **Modes:** sync

Search public Facebook posts by keyword, optionally filtered by location, and get structured post records (text, author, engagement).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.03**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-posts", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-posts', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-posts", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-posts", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). range 1–20 |
| `query` | string | yes | Keyword or phrase to search Facebook posts for (e.g. 'product launch').  |
| `endDate` | string |  | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31).  |
| `location` | string |  | Optional place name; include both city and country for best matches (e.g. 'Paris, France'). Uses Facebook's place filter, which favors posts tagged at that place rather than every post by people who live there, and can…  |
| `startDate` | string |  | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imagesCount` or `albumPreview`, and it is served only by a source…  |

## Details

Returns public Facebook posts that match a keyword or phrase. Each record has the post text, the author, a post URL, and reaction, comment and share counts. The only required input is `query`, and you can narrow results with `location`, `startDate` and `endDate`.

### Use cases

- Track how people talk about a brand by searching its name and reading the post text.
- Compare `reactionCount`, `commentCount` and `shareCount` across posts to find the ones that got the most engagement.
- Find pages that post about a topic by collecting `authorName` and `authorUrl` from the results.
- Pull posts tagged at a city for a local campaign review by setting `location` to a value like `Paris, France`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "nike"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword or phrase to search Facebook posts for (e.g. 'product launch'). |
| `endDate` | string | No | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `location` | string | No | Optional place name; include both city and country for best matches (e.g. 'Paris, France'). Uses Facebook's place filter, which favors posts tagged at that place rather than every post by people who live there, and can s |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imagesCount` or `albumPreview`, and it is served only by a source tha |
| `startDate` | string | No | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "authorId": "100044541544829",
        "authorImage": "https://scontent.fdtw2-1.fna.fbcdn.net/v/t39.30808-1/284964043_10159903868513445…",
        "authorName": "Nike",
        "authorUrl": "https://www.facebook.com/nike",
        "commentCount": 2882,
        "createdUtc": 1509595630,
        "id": "10155532600988445",
        "image": "https://scontent.fdtw2-1.fna.fbcdn.net/v/t39.30808-6/468501570_10162044654548445…",
        "imagesCount": null,
        "reactionCount": 6019,
        "reactions": {
          "angry": 8,
          "care": 0,
          "haha": 15,
          "like": 4944,
          "love": 1015,
          "sad": 5,
          "wow": 32
        },
        "shareCount": 9413
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | ID of the post. |
| `data.items[].url` | Link to the post on Facebook. |
| `data.items[].text` | Text of the post. Long text may be cut in the response. |
| `data.items[].authorName / data.items[].authorUrl` | Display name and Facebook URL of the page or profile that wrote the post. |
| `data.items[].authorId` | ID of the author. |
| `data.items[].createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.items[].reactionCount` | Total reactions on the post. |
| `data.items[].reactions.like / reactions.love / reactions.haha / reactions.wow / reactions.sad / reactions.angry / reactions.care` | Count of each reaction type on the post. |
| `data.items[].commentCount / data.items[].shareCount` | Number of comments and shares on the post. |
| `data.items[].image` | URL of the post image. It is an empty string when the post has no image. |

### Notes

- Use `limit` to set how many posts come back, from 1 to 20. The default is 20.
- `startDate` and `endDate` use the `YYYY-MM-DD` format.
- `imagesCount` can be `null`. To require it, or `albumPreview` or `type`, list the name in `requireFields`. A dearer source may then serve the call, which can raise the price.
- To read the comments on a post, call [Facebook Post Comments](/apis/facebook/post-comments). For the full record of one post, use [Facebook Post](/apis/facebook/post).

### Pricing

Billed at the actual cost of each call, about $0.03 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/search-posts.json`](../../../catalog/models/facebook/search-posts.json) · Store page: https://www.sandbase.ai/model/facebook/search-posts
