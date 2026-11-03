# Instagram Tagged Posts API: pricing, parameters and code examples

`instagram/tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00188 per call · **Modes:** sync

List the posts an Instagram user is tagged in, with cursor pagination (author, caption, likes, comments).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00188**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/tagged-posts", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/tagged-posts', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/tagged-posts", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/tagged-posts", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `handle` | string | yes | Instagram username without the leading @.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `audioId`, and it is served only by a source that returns every one…  |

## Details

This API returns a page of Instagram posts that a given user is tagged in. It needs an Instagram `handle` without the leading @. Each post includes the author, caption, engagement counts, tagged users, and sound details where present.

### Use cases

- Track which creators and fans post content that tags a brand account such as `nasa`.
- Measure engagement on tagged posts by comparing `likes`, `comments`, `reshares`, and `views`.
- Find tagged posts at a physical place using `locationName`, `locationLat`, and `locationLng`.
- Collect `url` values of tagged reels and feed posts for a review or moderation queue.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/tagged-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `audioId`, and it is served only by a source that returns every one of |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_yHFk0Kv5Y5je_8NgQW11og",
    "posts": [
      {
        "audioId": "1455782958355315",
        "author": "exoplanet_emma",
        "avatarUrl": "https://scontent-ord5-1.cdninstagram.com/v/t51.2885-19/343267148_538566048451511…",
        "caption": "Still on cloud 9 from this weekend 🚀✨\n\n📁 Astrophysics aerospace rocket launch ex…",
        "comments": 8,
        "createdUtc": 1788205763,
        "durationSeconds": 10.842,
        "hashtags": [],
        "id": "3976079382136818132",
        "likes": 3,
        "mentions": [],
        "paidPartnership": false
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id / data.posts[].url` | The post's ID and its public Instagram link. |
| `data.posts[].author` | Username of the account that published the post. |
| `data.posts[].caption` | Caption text of the post. Long captions can be shortened. |
| `data.posts[].likes / comments / reshares / views` | Engagement counts for the post. `views` is missing on some feed posts. |
| `data.posts[].createdUtc` | Creation time of the post as a Unix timestamp in seconds. |
| `data.posts[].productType` | Post format, for example `clips` for reels or `feed` for standard posts. |
| `data.posts[].taggedUsers[].username / userId / displayName` | The accounts tagged in the post, with their username, numeric ID, and display name. |
| `data.posts[].hashtags / mentions` | Hashtags and @mentions found in the caption, as lists of strings. |
| `data.posts[].audioId / soundTitle / soundAuthor` | ID, title, and author of the sound used in the post. Present on posts that carry audio. |
| `data.posts[].locationName / locationLat / locationLng` | Name and coordinates of the tagged location. Only present when the post has a location. |

### Notes

- To get the next page, pass `data.nextCursor` from the response as `cursor` in the next request.
- Use `handle` without the @, for example `nasa`.
- Set `requireFields` to `audioId` or `carouselCount` only if you need that field on every post. This can route the call to a dearer source and raise the price.
- To read one post in full, call [Instagram Post Details](/apis/instagram/post-detail). For the tagged account itself, call [Instagram Profile](/apis/instagram/profile).

### Pricing

Billed at the actual cost of each call, about $0.00188 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/tagged-posts.json`](../../../catalog/models/instagram/tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/tagged-posts
