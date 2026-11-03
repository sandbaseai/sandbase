# Instagram Post Details by URL API: pricing, parameters and code examples

`instagram/v1/post-by-url` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns details and display resources for a single Instagram post. Queries the platform using a target post link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-url", "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-url', {'post_url': 'https://www.instagram.com/p/DPwhVB-jo9k/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-url", {
  "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-url", sandbase.Params{
	"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_url` | string | yes | Post URL  |

## Details

Returns details for a single Instagram post, including the owner, caption, like count, image sizes and posting time. It needs the full post link in `post_url`.

### Use cases

- Download the image of a post at several sizes from the `display_resources` list.
- Read the like count and caption of a known post to track a celebrity or brand announcement.
- Check whether a post is an ad or paid partnership before you report on it.
- Identify the account that published a post from its link, including the verified status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_url` | string | Yes | Post URL |

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
      "src": "https://instagram.fbcn8-1.fna.fbcdn.net/v/t39.30808-6/735018292_1867233894105495…"
    }
  ],
  "display_url": "https://instagram.fbcn8-1.fna.fbcdn.net/v/t51.82787-15/562815025_186013987930549…",
  "edge_media_preview_comment": {
    "count": 0,
    "edges": []
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shortcode / id` | The short code from the post URL and the numeric post ID. |
| `__typename / is_video` | The post type (here `GraphImage`) and whether the post is a video. |
| `taken_at_timestamp` | When the post was published, as a Unix timestamp in seconds. |
| `edge_media_to_caption.edges[].node.text` | The caption text of the post. |
| `edge_media_to_caption.edges[].node.created_at` | When the caption was written, as a Unix timestamp string. |
| `edge_media_preview_like.count` | The number of likes on the post. |
| `edge_media_to_parent_comment.count` | The number of top-level comments returned for the post. |
| `display_url` | The main image link for the post. |
| `display_resources[].src` | Image link for one size of the post image. Pair it with `config_width / config_height`. |
| `owner.username / owner.full_name / owner.id / owner.is_verified` | The username, display name and numeric ID of the account that posted, and whether it is verified. |
| `is_ad / is_paid_partnership / comments_disabled` | Flags that show whether the post is an ad, a paid partnership, or has comments turned off. |

### Notes

- Pass the full post link, such as `https://www.instagram.com/p/DPwhVB-jo9k/`. The `shortcode` in the response matches the code in the link.
- In this response the `owner.edge_followed_by.count` and `owner.edge_owner_to_timeline_media.count` values are `0`. Call [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) for the profile details of `owner.username`.
- Use [Instagram Post Comment List](/apis/instagram/post-comments) to read the comments, since the comment list in this response is empty.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-url.json`](../../../../catalog/models/instagram/v1/post-by-url.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-url
