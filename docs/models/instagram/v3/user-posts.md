# Instagram User Posts (V3) API: pricing, parameters and code examples

`instagram/v3/user-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of posts from a specific Instagram account. Supports bidirectional cursor pagination using the account username.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-posts", "username": "natgeo"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-posts', {'username': 'natgeo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-posts", {
  "username": "natgeo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-posts", sandbase.Params{
	"username": "natgeo",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Posts per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `page_info.end_cursor`  |
| `count` | integer |  | Number of posts for first request (default 12)  |
| `first` | integer |  | Posts per page for forward pagination (default 12, max 50) range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `page_info.start_cursor`  |
| `username` | string | yes | Username string (e.g. `99brasil`), **NOT numeric user_id**  |

## Details

Returns a page of recent posts from an Instagram account. Each post includes its caption, like and comment counts, media type, and owner. The only required input is the account `username`, not a numeric user ID.

### Use cases

- Pull the latest posts from a brand account to track what it publishes.
- Compare `like_count` and `comment_count` across posts to find which content gets the most engagement.
- Collect `video_url` and `thumbnail_url` links for video posts to review the media.
- Page backward and forward through an account's feed with cursors to build a post archive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "99brasil"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username string (e.g. `99brasil`), **NOT numeric user_id** |
| `after` | string | No | Forward pagination cursor, from previous response `page_info.end_cursor` |
| `before` | string | No | Backward pagination cursor, from previous response `page_info.start_cursor` |
| `count` | integer | No | Number of posts for first request (default 12) |
| `first` | integer | No | Posts per page for forward pagination (default 12, max 50) |
| `last` | integer | No | Posts per page for backward pagination, use with `before` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3b0c580e2be36",
  "count": 12,
  "data": {
    "user": {
      "edge_owner_to_timeline_media": {
        "count": 12,
        "edges": [
          {
            "node": {
              "caption_text": "publi | Uma das coisas mais incriveis que a gastronomia proporciona é a de conse…",
              "code": "DfDPgRny-X3",
              "comment_count": 756,
              "id": "4018123481186821623_189966948",
              "is_video": true,
              "like_count": 63872,
              "media_type": 2,
              "owner": {
                "full_name": "Gabriela Paveloski | Masterchef 11",
                "is_verified": true,
                "pk": "189966948",
                "username": "gabipaveloski"
              }
            }
          }
        ],
        "page_info": {
          "end_cursor": "3991279117147774438_791258468",
          "has_next_page": true,
          "has_previous_page": false,
          "start_cursor": null
        }
      }
    }
  },
  "items": [
    {
      "caption_text": "publi | Uma das coisas mais incriveis que a gastronomia proporciona é a de conse…",
      "code": "DfDPgRny-X3",
      "comment_count": 756,
      "id": "4018123481186821623_189966948",
      "is_video": true,
      "like_count": 63872,
      "media_type": 2,
      "owner": {
        "full_name": "Gabriela Paveloski | Masterchef 11",
        "is_verified": true,
        "pk": "189966948",
        "username": "gabipaveloski"
      },
      "pk": "4018123481186821623",
      "shortcode": "DfDPgRny-X3",
      "taken_at": null,
      "thumbnail_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-15/874538980_18642463201014…"
    }
  ],
  "next_max_id": "3991279117147774438_791258468"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | Flat list of posts on this page. It repeats the posts found under `data.user.edge_owner_to_timeline_media.edges[].node`. |
| `items[].code / items[].shortcode` | Short code that identifies the post. The same value appears in both fields. |
| `items[].id / items[].pk` | Post identifiers. `id` is the media ID followed by an underscore and the owner ID. `pk` is the media ID alone. |
| `items[].caption_text` | Caption of the post. Long captions appear cut off in the response. |
| `items[].like_count / items[].comment_count` | Number of likes and comments on the post. |
| `items[].view_count` | View count for the post. It is `0` for the non-video post in the sample. |
| `items[].media_type / items[].is_video` | `media_type` is a numeric type code. `is_video` is `true` for video posts. In the sample, `2` goes with video posts and `8` goes with a post where `is_video` is `false`. |
| `items[].owner.username / items[].owner.full_name / items[].owner.is_verified` | Username, display name and verified flag of the account that owns the post. The owner can differ from the `username` you requested. |
| `items[].thumbnail_url / items[].video_url` | Links to the thumbnail image and the video file. Both can be `null`, as with the non-video post in the sample. |
| `data.user.edge_owner_to_timeline_media.page_info` | Pagination state with `end_cursor`, `start_cursor`, `has_next_page` and `has_previous_page`. |

### Notes

- Pass a username such as `99brasil`. A numeric user ID does not work.
- For the next page, send `page_info.end_cursor` as `after`, and set the page size with `first` (maximum 50). The top-level `next_max_id` holds the same cursor value.
- For the previous page, send `page_info.start_cursor` as `before` and set the size with `last`. In the sample, `start_cursor` is `null` and `has_previous_page` is `false`.
- `taken_at` is `null` in the sample, so do not rely on it for post dates.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-posts.json`](../../../../catalog/models/instagram/v3/user-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-posts
