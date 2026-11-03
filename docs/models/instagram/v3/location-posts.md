# Instagram Location Posts (V3) API: pricing, parameters and code examples

`instagram/v3/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns Instagram posts associated with a specific location. Supports sorting by ranked or recent media alongside pagination controls.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/location-posts", "location_id": "1016248898"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/location-posts', {'location_id': '1016248898'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/location-posts", {
  "location_id": "1016248898"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/location-posts", sandbase.Params{
	"location_id": "1016248898",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Post sort order one of: `ranked`, `recent` |
| `after` | string |  | Pagination cursor from previous response `page_info.end_cursor`  |
| `first` | integer |  | Posts per page (default 12, max 50) range 1–50 |
| `location_id` | string | yes | Location ID (numeric)  |
| `page_size_override` | integer |  | Posts per page (default 12)  |

## Details

Returns Instagram posts tagged at one location. It needs a numeric `location_id` and returns caption, like and comment counts, media type and owner details for each post. You can pick the `ranked` or `recent` tab and page through results.

### Use cases

- Collect public posts tagged at a restaurant, clinic or shop to see what people post about it.
- Find the accounts that post most often at a venue by reading `owner.username` across pages.
- Compare `ranked` and `recent` posts for a place to see which content gets the most likes.
- Pull captions and hashtags from a local area to study how businesses and visitors describe a place.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "1016248898"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID (numeric) |
| `after` | string | No | Pagination cursor from previous response `page_info.end_cursor` |
| `first` | integer | No | Posts per page (default 12, max 50) |
| `page_size_override` | integer | No | Posts per page (default 12) |
| `tab` | string | No | Post sort order |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3432617742581",
  "count": 12,
  "data": {
    "location": {
      "edge_location_to_media": {
        "count": 12,
        "edges": [
          {
            "node": {
              "caption_text": "청소년여드름\n\n[자극은 최소화, 효과는 극대화!]\n압출 당일 자극 최소화는 기본!\n\n다르아크네에서는 단순한 압출로 끝나지 않아요.\n피부 자극을 …",
              "code": "DZlrTTlNgIr",
              "comment_count": 0,
              "id": "3919729493391311403_1425162018",
              "is_video": false,
              "like_count": 1,
              "media_type": 1,
              "owner": {
                "full_name": "창원여드름/피부염증흉터/피부루틴 맞춤설계 다르아크네대표",
                "is_verified": false,
                "pk": "1425162018",
                "username": "drr.acne_"
              }
            }
          }
        ],
        "page_info": {
          "end_cursor": null,
          "has_next_page": false
        }
      }
    }
  },
  "items": [
    {
      "caption_text": "청소년여드름\n\n[자극은 최소화, 효과는 극대화!]\n압출 당일 자극 최소화는 기본!\n\n다르아크네에서는 단순한 압출로 끝나지 않아요.\n피부 자극을 …",
      "code": "DZlrTTlNgIr",
      "comment_count": 0,
      "id": "3919729493391311403_1425162018",
      "is_video": false,
      "like_count": 1,
      "media_type": 1,
      "owner": {
        "full_name": "창원여드름/피부염증흉터/피부루틴 맞춤설계 다르아크네대표",
        "is_verified": false,
        "pk": "1425162018",
        "username": "drr.acne_"
      },
      "pk": "3919729493391311403",
      "shortcode": "DZlrTTlNgIr",
      "taken_at": null,
      "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/722665770_18590062972010…"
    }
  ],
  "next_max_id": null,
  "tab": "ranked"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | Flat list of posts on this page. It repeats the posts in `data.location.edge_location_to_media.edges[].node`, so you can read either one. |
| `items[].caption_text` | Caption text of the post. Long captions may be cut, and hashtags appear inside the text. |
| `items[].shortcode / items[].code` | Short code of the post, as used in Instagram post URLs. Pass it to a post details API. |
| `items[].id / items[].pk` | `id` joins the post ID and the owner ID with an underscore. `pk` is the post ID alone. |
| `items[].like_count / items[].comment_count / items[].view_count` | Engagement counts for the post. |
| `items[].media_type / items[].is_video` | `media_type` is a numeric code for the post format. In this response `1` is a single image post and `8` is a post with no thumbnail. `is_video` is a true or false flag. |
| `items[].owner.username / items[].owner.full_name / items[].owner.pk / items[].owner.is_verified` | Account that published the post: handle, display name, numeric user ID and verified flag. |
| `items[].thumbnail_url / items[].video_url` | Link to a preview image and to a video file. Either can be `null`. |
| `data.location.edge_location_to_media.page_info` | Pagination state. `has_next_page` tells you if more posts exist, and `end_cursor` holds the cursor for the next page. |
| `tab` | Sort order applied to this response. This request returned `ranked`. |

### Notes

- Pass `page_info.end_cursor` from the response as `after` to get the next page. When `has_next_page` is `false`, `end_cursor` is `null` and there are no more pages.
- Use `first` to set posts per page (1 to 50, default 12). Set `tab` to `ranked` or `recent` to change the order.
- `taken_at` was `null` in this response, so do not rely on it for post dates.
- To read one post in full, call [Instagram Post Info by Shortcode](/apis/instagram/v3/post-info-by-code) with the `shortcode`. Use [Instagram Location Details (V3)](/apis/instagram/v3/location-info) for the place itself.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/location-posts.json`](../../../../catalog/models/instagram/v3/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/location-posts
