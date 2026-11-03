# Instagram Explore Section Posts API: pricing, parameters and code examples

`instagram/v1/section-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts listed under a specific Instagram explore section. Supports pagination controls and page size configuration by section ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/section-posts", "section_id": "10156104410190727"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/section-posts', {'section_id': '10156104410190727'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/section-posts", {
  "section_id": "10156104410190727"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/section-posts", sandbase.Params{
	"section_id": "10156104410190727",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/section-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 20 range 1–50 |
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `section_id` | string | yes | Section ID (from fetch_explore_sections API)  |

## Details

Returns a page of posts listed under one Instagram explore section, plus the section name and its subsections. It needs a `section_id`. You can set the page size with `count` and continue with `max_id`.

### Use cases

- Pull the posts shown in the Fashion & Beauty explore section to see which carousels get the most comments.
- Walk the `subsections` list to collect posts for narrower topics such as Beauty or Fashion.
- Save the `display_uri` images and post `code` values from an explore section for a content research board.
- Compare `comment_count` across posts in a section to find the most discussed posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/section-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"section_id": "10156104410190727"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `section_id` | string | Yes | Section ID (from fetch_explore_sections API) |
| `count` | integer | No | Count per page, default 20 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "0",
  "items": [
    {
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": [],
      "can_modify_carousel": true,
      "can_see_insights_as_brand": false,
      "can_view_more_preview_comments": false,
      "can_viewer_reshare": true,
      "can_viewer_save": true,
      "caption": {
        "bit_flags": 0,
        "content_type": "comment",
        "created_at": 1792382586,
        "created_at_utc": 1792382586,
        "did_report_as_spam": false,
        "is_covered": false,
        "is_ranked_comment": false,
        "media_id": 4011117858977833779
      },
      "caption_is_edited": true,
      "carousel_media": [
        {
          "caption": null,
          "carousel_parent_id": "4011117858977833779_23527883966",
          "commerciality_status": "not_commercial",
          "creative_config": null,
          "display_uri": "https://instagram.fsvq2-1.fna.fbcdn.net/v/t51.82787-15/852515261_181270900127879…",
          "explore_pivot_grid": false,
          "fb_user_tags": {
            "in": []
          },
          "featured_products": []
        }
      ],
      "carousel_media_count": 8
    }
  ],
  "max_id": null,
  "more_available": false,
  "section_name": "Fashion & Beauty",
  "status": "ok",
  "subsections": [
    {
      "name": "Beauty",
      "section_id": 1700128603535381
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `section_name` | Name of the explore section you requested, for example `Fashion & Beauty`. |
| `subsections[].name / subsections[].section_id` | Name and ID of each narrower section inside this one. You can pass these `section_id` values in a new request. |
| `items[].code` | Short post code. It is the part of an Instagram post URL that identifies the post. |
| `items[].caption.created_at` | Unix timestamp in seconds for the caption. The caption text itself is not in this response. |
| `items[].caption.media_id` | Numeric ID of the post the caption belongs to. |
| `items[].comment_count` | Number of comments on the post. |
| `items[].display_uri` | URL of the main image for the post. |
| `items[].carousel_media_count` | Number of slides in a carousel post. |
| `items[].carousel_media[].display_uri` | Image URL for one slide of the carousel. The list may show only the first few slides. |
| `more_available / max_id` | Pagination state. `more_available` tells you whether more pages exist, and `max_id` holds the cursor for the next page. |

### Notes

- Get `section_id` from the explore sections API. Each entry in `subsections` also gives a usable ID.
- For the next page, send the returned `max_id` as the `max_id` parameter. In this response `max_id` is `null` and `more_available` is `false`, so there was no next page.
- `count` accepts 1 to 50 and defaults to 20.
- Use [Instagram Post Details by ID](/apis/instagram/v1/post-by-id) or [Instagram Post Details by URL](/apis/instagram/v1/post-by-url) to look at a single post from the list.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/section-posts.json`](../../../../catalog/models/instagram/v1/section-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/section-posts
