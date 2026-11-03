# Instagram User Posts (V1, V2) API: pricing, parameters and code examples

`instagram/v1/user-posts-v2` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of media posts for a specified Instagram account. Filter by user ID with support for custom page limits and cursor-based navigation.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-posts-v2", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-posts-v2', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-posts-v2", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-posts-v2", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-posts-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `user_id` | string | yes | Instagram user ID  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Returns a page of timeline media posts for an Instagram account. It needs the numeric Instagram `user_id`. Each post includes its type, image URLs, dimensions and a like count.

### Use cases

- Pull the latest posts from a creator account to track what content types it publishes.
- Page through an account's older media to build a content archive.
- Compare like counts across posts to find the best performing videos and carousels.
- Collect display image URLs and accessibility captions for a media review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-posts-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |
| `count` | integer | No | Count per page, default 12 |
| `end_cursor` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "96",
  "data": {
    "user": {
      "edge_owner_to_timeline_media": {
        "count": null,
        "edges": [
          {
            "node": {
              "__typename": "GraphVideo",
              "coauthor_producers": [],
              "comments_disabled": false,
              "dash_info": {
                "is_dash_eligible": false,
                "number_of_qualities": 3,
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011…"
              },
              "dimensions": {
                "height": 1920,
                "width": 1080
              },
              "display_resources": [
                {
                  "config_height": 540,
                  "config_width": 360,
                  "src": "https://scontent-cdg4-1.cdninstagram.com/v/t51.82787-15/883416041_18810804649001…"
                }
              ],
              "display_url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.82787-15/883416041_18810804649001…",
              "edge_media_preview_like": {
                "count": 145687,
                "edges": []
              }
            }
          }
        ],
        "page_info": {
          "end_cursor": "4007127383642387898_25025320",
          "has_next_page": true
        }
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.edge_owner_to_timeline_media.edges[].node.__typename` | Post type. The response shows `GraphVideo` for videos and `GraphSidecar` for multi-item carousel posts. |
| `data.user.edge_owner_to_timeline_media.edges[].node.display_url` | URL of the main image for the post. For videos this is the cover image. |
| `data.user.edge_owner_to_timeline_media.edges[].node.display_resources[].src` | URL of the image at one size. Read `config_width` and `config_height` in the same row for the size. |
| `data.user.edge_owner_to_timeline_media.edges[].node.dimensions.height / data.user.edge_owner_to_timeline_media.edges[].node.dimensions.width` | Height and width of the post media. |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_preview_like.count` | Number of likes on the post. |
| `data.user.edge_owner_to_timeline_media.edges[].node.comments_disabled` | `true` when comments are turned off for the post. |
| `data.user.edge_owner_to_timeline_media.edges[].node.accessibility_caption` | Text description of the image. It appears on some posts, such as the carousel in the sample. |
| `data.user.edge_owner_to_timeline_media.edges[].node.coauthor_producers[]` | Co-authors of the post. Each entry has `full_name`, `id`, `is_verified` and `is_private`. The list is empty when the post has no co-author. |
| `data.user.edge_owner_to_timeline_media.edges[].node.dash_info.video_dash_manifest` | DASH manifest XML for video posts. Use it to find the video streams. `number_of_qualities` gives the count of quality levels. |
| `data.user.edge_owner_to_timeline_media.page_info.end_cursor / data.user.edge_owner_to_timeline_media.page_info.has_next_page` | Cursor for the next page and a flag that shows whether more posts exist. |

### Notes

- Send the cursor from `page_info.end_cursor` as `end_cursor` to get the next page. Omit `end_cursor` on the first call.
- Stop paging when `has_next_page` is `false`.
- Set `count` from 1 to 50. The default is 12.
- The `count` field under `edge_owner_to_timeline_media` was `null` in this response, so do not rely on it as a post total. To get a `user_id` from a handle, call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-posts-v2.json`](../../../../catalog/models/instagram/v1/user-posts-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-posts-v2
