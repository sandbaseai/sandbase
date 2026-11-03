# Instagram User Tagged Posts (V1) API: pricing, parameters and code examples

`instagram/v1/user-tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts where a specific user is tagged by other accounts. Supports result limits and pagination through a cursor parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-tagged-posts", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-tagged-posts', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-tagged-posts", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-tagged-posts", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 12 default `12`; range 1–50 |
| `user_id` | string | yes | Instagram user ID  |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |

## Details

Returns posts where other accounts have tagged a given Instagram user. It needs the numeric Instagram `user_id` and returns one page of tagged posts with a cursor for the next page.

### Use cases

- Collect photos that fans and customers post with a brand account tagged.
- Show community posts that feature a creator on a campaign or press page.
- Rank tagged posts by like count to find the most visible user-generated content.
- Read the location and co-tagged accounts in photo captions to see where and with whom people tag a profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-tagged-posts" \
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
  "attempts": "71",
  "data": {
    "user": {
      "edge_user_to_photos_of_you": {
        "count": 11,
        "edges": [
          {
            "node": {
              "__typename": "GraphImage",
              "accessibility_caption": "Photo by LUCAS RAMOS MENDES ® in Florianópolis, Santa Catarina with @instagram, …",
              "comments_disabled": false,
              "dimensions": {
                "height": 1350,
                "width": 1080
              },
              "display_url": "https://instagram.fbcn2-1.fna.fbcdn.net/v/t51.82787-15/621585839_180920878669893…",
              "edge_liked_by": {
                "count": 149572
              },
              "edge_media_preview_like": {
                "count": 149572
              },
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {}
                  }
                ]
              }
            }
          }
        ],
        "page_info": {
          "end_cursor": "QVFCekpXTUFkN1FrbV9HcnY5TkdlV0xSZlg0Q2lvOW5hQWd2djl5aG1EUWlpc0RfRUpIdmZIVjA1T2pJ…",
          "has_next_page": true
        }
      }
    }
  },
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.edge_user_to_photos_of_you.count` | Total number of tagged posts reported for the user. |
| `data.user.edge_user_to_photos_of_you.edges[].node.__typename` | Media type of the post. The sample shows `GraphImage` for photo posts. |
| `data.user.edge_user_to_photos_of_you.edges[].node.accessibility_caption` | Auto-written description of the post. It often names the poster, the place, and the tagged accounts. |
| `data.user.edge_user_to_photos_of_you.edges[].node.display_url` | Link to the post image. |
| `data.user.edge_user_to_photos_of_you.edges[].node.dimensions.height / data.user.edge_user_to_photos_of_you.edges[].node.dimensions.width` | Height and width of the image. |
| `data.user.edge_user_to_photos_of_you.edges[].node.edge_liked_by.count / data.user.edge_user_to_photos_of_you.edges[].node.edge_media_preview_like.count` | Number of likes on the post. Both fields hold the same value in the sample. |
| `data.user.edge_user_to_photos_of_you.edges[].node.comments_disabled` | `true` when comments are turned off for the post. |
| `data.user.edge_user_to_photos_of_you.edges[].node.edge_media_to_caption.edges[].node.text` | Caption text written by the poster. It can be missing or empty when the post has no caption. |
| `data.user.edge_user_to_photos_of_you.page_info.end_cursor` | Cursor to pass as `end_cursor` to get the next page. |
| `data.user.edge_user_to_photos_of_you.page_info.has_next_page` | `true` when more tagged posts are available. |

### Notes

- Omit `end_cursor` on the first request. For the next page, send the `page_info.end_cursor` value from the last response and keep `has_next_page` as your stop check.
- `count` sets the page size from 1 to 50. The default is 12.
- `user_id` is the numeric Instagram ID, not the username. Use [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) to look up the ID from a username.
- To read a single tagged post in full, use [Instagram Post Details by ID](/apis/instagram/v1/post-by-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-tagged-posts.json`](../../../../catalog/models/instagram/v1/user-tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-tagged-posts
