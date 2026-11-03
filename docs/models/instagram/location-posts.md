# Instagram Location Posts API: pricing, parameters and code examples

`instagram/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List public Instagram posts tagged at a location, ranked or most recent, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/location-posts", "locationId": "103912118089363"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/location-posts', {'locationId': '103912118089363'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/location-posts", {
  "locationId": "103912118089363"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/location-posts", sandbase.Params{
	"locationId": "103912118089363",
})
```

Same call via the path form: `POST /v1/api/instagram/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Order the posts by Instagram's top ranking or by newest first. Defaults to ranked. one of: `ranked`, `recent` |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `locationId` | string | yes | Instagram location id, as returned by instagram.search_locations.  |

## Details

Returns public Instagram posts tagged at one location, either ranked by Instagram or newest first. It needs an Instagram `locationId`. Each post includes the author, caption, counts, media size, and the location name and coordinates.

### Use cases

- Monitor new posts tagged at a landmark, venue or hotel by polling with `sort` set to `recent`.
- Collect captions and hashtags from a tourist spot to see what visitors say about it.
- Find active local creators by listing the `author` of posts at a city location.
- Pull image links and post URLs from a place to build a visual feed for a travel page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "recent", "locationId": "103912118089363"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `locationId` | string | Yes | Instagram location id, as returned by instagram.search_locations. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `sort` | string | No | Order the posts by Instagram's top ranking or by newest first. Defaults to ranked. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_uju1QQCUkfS3KOLawGhzRg",
    "posts": [
      {
        "author": "honey_petals8483444",
        "authorId": "16540969846",
        "authorPrivate": false,
        "authorVerified": false,
        "avatarUrl": "https://scontent-cdg4-1.cdninstagram.com/v/t51.82787-19/883558648_18149634271545…",
        "caption": "Slow down, look up. Weekend mood 🍃",
        "captionEdited": false,
        "coauthors": [],
        "comments": 0,
        "countsHidden": false,
        "createdUtc": 1793667839,
        "hashtags": []
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id / data.posts[].shortcode` | The numeric post ID and the short code used in the post URL. |
| `data.posts[].url` | Link to the post on Instagram. |
| `data.posts[].caption` | Caption text of the post. `captionEdited` shows whether the caption was changed after posting. |
| `data.posts[].hashtags / data.posts[].mentions / data.posts[].taggedUsers / data.posts[].coauthors` | Lists of hashtags, mentioned accounts, tagged users and co-authors on the post. Each list is empty when none exist. |
| `data.posts[].author / data.posts[].authorId` | Username and numeric ID of the account that posted. |
| `data.posts[].authorVerified / data.posts[].authorPrivate` | Flags for whether the author account is verified and whether it is private. |
| `data.posts[].likes / data.posts[].comments` | Like and comment counts for the post. `countsHidden` is `true` when the author hides counts. |
| `data.posts[].createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.posts[].mediaType / data.posts[].productType / data.posts[].image` | Media type (such as `photo`), the post format (such as `feed`), and the image link. |
| `data.posts[].locationId / data.posts[].locationName / data.posts[].locationLat / data.posts[].locationLng` | The tagged location's ID, name, latitude and longitude. |
| `data.nextCursor` | Cursor for the next page of posts. |

### Notes

- Get `locationId` from [Instagram Location Search](/apis/instagram/search-locations).
- For the next page, send the `data.nextCursor` value as `cursor` with the same `locationId` and `sort`.
- `sort` accepts `ranked` (the default) or `recent`.
- To read a single post in full, pass its link or ID to [Instagram Post Details](/apis/instagram/post-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/location-posts.json`](../../../catalog/models/instagram/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/location-posts
