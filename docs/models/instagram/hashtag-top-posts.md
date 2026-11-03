# Instagram Hashtag Top Posts API: pricing, parameters and code examples

`instagram/hashtag-top-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Instagram's own top-ranked posts for a hashtag, read from its live hashtag feed rather than a web search index, with view, like, and comment counts. Reels-heavy and engagement-ranked, so it answers what is performing on a tag right now. For older relevance-ranked results with date and media-type filters use instagram.search_hashtag; for the chronological feed use instagram.hashtag_recent_posts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-top-posts", "hashtag": "skincare"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-top-posts', {'hashtag': 'skincare'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-top-posts", {
  "hashtag": "skincare"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-top-posts", sandbase.Params{
	"hashtag": "skincare",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-top-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `hashtag` | string | yes | Hashtag to fetch, without the leading #.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every…  |

## Details

This API returns Instagram's top-ranked posts for a hashtag, with view, like and comment counts, caption, author and media links. It needs one input: the `hashtag` without the leading #.

### Use cases

- Spot which Reels are getting the most views on a tag such as `skincare` right now.
- Find creators who post on a niche hashtag and check their `verified` status and engagement.
- Collect captions and co-hashtags from top posts to see which related tags appear with the main tag.
- Track `paidPartnership` posts and `coauthors` to see which brands and creators work together on a tag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-top-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "skincare"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to fetch, without the leading #. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_M2mp1YOlZVB0gi39vnq42Q",
    "posts": [
      {
        "audioId": null,
        "avatarUrl": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/834902873_18632884252018…",
        "caption": "⁨\tالدكتورة سلمى المنجد \n#ملتقى_بيوكسين_الاول \n‏#Skincare\n‏#Bioxcin\n#طب_الجلد #ال…",
        "coauthors": [
          {
            "avatarUrl": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/843548250_18093856043450…",
            "userId": "43522946622",
            "username": "lets_care_group"
          }
        ],
        "comments": 112,
        "createdUtc": 1793555863,
        "durationSeconds": 69.61100006103516,
        "hashtags": [
          "#ملتقى_بيوكسين_الاول"
        ],
        "id": "4020960450613865690",
        "likes": 935,
        "locationId": null,
        "locationLat": null
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
| `data.posts[].views / likes / comments` | View, like and comment counts for the post. |
| `data.posts[].caption` | Caption text of the post. The `hashtags` list holds the hashtags found in it. |
| `data.posts[].username / verified / avatarUrl` | Author's handle, whether the account is verified, and a link to a small profile picture. |
| `data.posts[].createdUtc` | Post creation time as a Unix timestamp in seconds. |
| `data.posts[].productType / durationSeconds` | Post format (for example `clips` for Reels) and the video length in seconds. |
| `data.posts[].media[].type / url / videoUrl` | Media type, a preview image link, and a video file link for video posts. |
| `data.posts[].soundTitle / soundAuthor / audioId` | Audio name, audio author and audio ID. These can be `null` when the post has no audio data. |
| `data.posts[].coauthors[].username / userId` | Accounts listed as co-authors of the post. The list is empty when there are none. |
| `data.posts[].locationName / locationLat / locationLng` | Place name and coordinates tagged on the post. All are `null` when no location is set. |

### Notes

- Pass `data.nextCursor` as `cursor` in the next request to get more posts.
- Use the `hashtag` value without the #, for example `skincare`.
- To see the newest posts instead of the top ones, call [Instagram Hashtag Recent Posts](/apis/instagram/hashtag-recent-posts).
- For stats about the tag itself, call [Instagram Hashtag Analytics](/apis/instagram/hashtag-analytics).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/hashtag-top-posts.json`](../../../catalog/models/instagram/hashtag-top-posts.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-top-posts
