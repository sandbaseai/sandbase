# Instagram Post Details by ID API: pricing, parameters and code examples

`instagram/v1/post-by-id` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a single Instagram post using its unique post identifier. Use this endpoint to look up post metadata and display resources.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-id", "post_id": "3742637871112032100"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-id', {'post_id': '3742637871112032100'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-id", {
  "post_id": "3742637871112032100"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-id", sandbase.Params{
	"post_id": "3742637871112032100",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | Post ID  |

## Details

Returns metadata for a single Instagram post, including media type, image sizes, caption, like count, and owner details. It needs one input, the numeric `post_id` of the post.

### Use cases

- Fetch the caption and posting time of a known Instagram post for a content archive.
- Download the image URLs at different sizes to show a post preview in your own app.
- Read the like count and owner account of a post to track a public figure's content.
- Check whether a post is a video, an ad, or a paid partnership before you include it in a report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "3742637871112032100"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "__typename": "GraphImage",
  "accessibility_caption": null,
  "attempts": "0",
  "can_see_insights_as_brand": false,
  "caption_is_edited": false,
  "coauthor_producers": [],
  "commenting_disabled_for_viewer": true,
  "comments_disabled": false,
  "dimensions": {
    "height": 1080,
    "width": 1080
  },
  "display_resources": [
    {
      "config_height": 640,
      "config_width": 480,
      "src": "https://scontent-mad1-1.cdninstagram.com/v/t39.30808-6/735018292_186723389410549…"
    }
  ],
  "display_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-15/562815025_18601398793054…",
  "edge_media_preview_comment": {
    "count": 0,
    "edges": []
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / shortcode` | The numeric post ID and the short code used in Instagram post URLs. |
| `__typename / is_video` | The media type of the post (here `GraphImage`) and a flag that shows whether it is a video. |
| `taken_at_timestamp` | When the post was taken, as a Unix timestamp in seconds. |
| `edge_media_to_caption.edges[].node.text` | The caption text of the post. The node also has `created_at` and an `id` for the caption. |
| `edge_media_preview_like.count` | The number of likes on the post. |
| `edge_media_to_parent_comment.count` | The number of top-level comments. `page_info.has_next_page` and `page_info.end_cursor` in the same object show whether more comments exist. |
| `display_url` | The URL of the main image of the post. |
| `display_resources[].src` | The URL of one image rendition. `config_width` and `config_height` give its size. |
| `dimensions.width / dimensions.height` | The size of the original media in pixels. |
| `owner.username / owner.full_name / owner.id` | The username, display name, and numeric ID of the account that published the post. |
| `owner.is_verified` | Shows whether the owner account is verified. |
| `is_ad / is_paid_partnership / comments_disabled` | Flags that show whether the post is an ad, a paid partnership, or has comments turned off. |

### Notes

- Use the `id` value from the response as `post_id`. The ID is a long numeric string, so send it as a string.
- If you only have a post URL, call [Instagram Post Details by URL](/apis/instagram/v1/post-by-url) instead.
- To convert between the `shortcode` and the numeric ID, use [Instagram Shortcode to Media ID](/apis/instagram/v1/shortcode-to-media-id).
- In this example, `owner.edge_followed_by.count` is `0`, so use a user profile API for follower numbers.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-id.json`](../../../../catalog/models/instagram/v1/post-by-id.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-id
