# Instagram Hashtag Recent Posts API: pricing, parameters and code examples

`instagram/hashtag-recent-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Instagram posts published under a hashtag, newest first, read from its live chronological feed rather than a web search index. Built for monitoring: results arrive within a couple of minutes of posting, so engagement counts are usually still zero and reels do not appear (Instagram keeps those on a separate tab). For engagement-ranked results use instagram.hashtag_top_posts; for older relevance-ranked results use instagram.search_hashtag.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-recent-posts", "hashtag": "skincare"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-recent-posts', {'hashtag': 'skincare'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-recent-posts", {
  "hashtag": "skincare"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-recent-posts", sandbase.Params{
	"hashtag": "skincare",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-recent-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `hashtag` | string | yes | Hashtag to monitor, without the leading #.  |

## Details

Returns Instagram posts published under a hashtag, newest first, from the hashtag's chronological feed. You send a `hashtag` without the leading #, and each post includes caption, author, media links and counts.

### Use cases

- Monitor a brand or campaign hashtag and catch new posts within minutes of publishing.
- Spot new paid partnership posts in a niche like skincare by checking `paidPartnership`.
- Collect fresh creator accounts posting under a topic by reading `username`, `userId` and `verified`.
- Feed new post URLs into a moderation or reposting queue.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-recent-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "skincare"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to monitor, without the leading #. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_Kic15fMDA4fH3OYn2e--Sw",
    "posts": [
      {
        "avatarUrl": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/743081754_18056615780522…",
        "caption": "الليزر الكوري لتصغير الانف 🔥🔥🔥🔥#fypシ❤️💞❤️ #اكسبلورر #dubai #skincare #fforever",
        "comments": 0,
        "countsHidden": false,
        "createdUtc": 1793691103,
        "displayName": "Huda.altaaye",
        "hashtags": [
          "#fypシ❤️💞❤️"
        ],
        "height": 1760,
        "id": "4022091320108946819",
        "likes": 0,
        "media": [
          {
            "type": "photo",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/884648679_18085354025522…"
          }
        ],
        "mentions": []
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].url / data.posts[].shortcode` | Link to the post on Instagram and its short ID. The `shortcode` is the part of the URL after `/p/`. |
| `data.posts[].id` | Numeric ID of the post, returned as a string. |
| `data.posts[].caption` | Caption text of the post, including its hashtags. |
| `data.posts[].hashtags / data.posts[].mentions` | Lists of hashtags and @mentions found in the caption. Each hashtag keeps its leading `#`. |
| `data.posts[].username / data.posts[].displayName / data.posts[].userId` | Handle, display name and numeric account ID of the author. `displayName` can be an empty string. |
| `data.posts[].verified / data.posts[].private` | Whether the author account is verified and whether it is private. |
| `data.posts[].likes / data.posts[].comments` | Like and comment counts at the time of the call. They are often 0 on new posts. |
| `data.posts[].countsHidden` | `true` when the author hides the counts, so `likes` and `comments` of 0 do not mean no engagement. |
| `data.posts[].createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.posts[].media[].type / data.posts[].media[].url` | Type of each media item (such as `photo`) and its URL. Carousel posts list several items, and `carouselCount` gives the item count. |
| `data.posts[].productType / data.posts[].paidPartnership` | Post format, such as `feed` or `carousel_container`, and whether the post is marked as a paid partnership. |

### Notes

- Use `data.nextCursor` as the `cursor` parameter in the next request to get the next page of older posts.
- Send the hashtag without the leading #, for example `skincare`.
- Reels do not appear here. For engagement-ranked posts, call [Instagram Hashtag Top Posts](/apis/instagram/hashtag-top-posts).
- To get full details for one post, pass its URL or `shortcode` to [Instagram Post Details](/apis/instagram/post-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/hashtag-recent-posts.json`](../../../catalog/models/instagram/hashtag-recent-posts.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-recent-posts
