# Instagram Post Details by URL (V2) API: pricing, parameters and code examples

`instagram/v1/post-by-url-v2` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns post details and media links for a specific Instagram post URL. Designed for faster responses when handling high-volume post lookups.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-url-v2", "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-url-v2', {'post_url': 'https://www.instagram.com/p/DPwhVB-jo9k/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-url-v2", {
  "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-url-v2", sandbase.Params{
	"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-url-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_url` | string | yes | Post URL  |

## Details

Returns details for one Instagram post: the caption, like and comment counts, the author, the post time, and direct links to the media files. It needs the full post URL in `post_url`.

### Use cases

- Download the image or video files from a post by reading the links in `data.medias[]`.
- Record the like count and comment count of a single post at the time you call.
- Show the caption and author name of a post in a link preview or a report.
- Check which posts in a list of URLs hold images and which hold other media types.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-url-v2" \
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
  "attempts": "0",
  "data": {
    "caption": "I’ll never forget how excited I was in 2006 when my first album sold 40,000 copi…",
    "comment_count": 0,
    "full_name": "Taylor Swift",
    "like_count": 3861627,
    "medias": [
      {
        "link": "https://instagram.fvcp2-1.fna.fbcdn.net/v/t51.82787-15/562815025_186013987930549…",
        "type": "image"
      }
    ],
    "taken_at_timestamp": 1760377223,
    "username": "taylorswift"
  },
  "status": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.caption` | Caption text of the post. Long captions may appear shortened. |
| `data.username / data.full_name` | Account handle and display name of the post author. |
| `data.like_count / data.comment_count` | Number of likes and number of comments on the post. |
| `data.taken_at_timestamp` | Time the post was taken, as a Unix timestamp in seconds. |
| `data.medias[].link` | Direct URL of a media file in the post. |
| `data.medias[].type` | Kind of media for that item, for example `image`. |
| `status` | `true` when the lookup succeeded. |
| `attempts` | Attempt counter returned as a string, `0` in this response. |

### Notes

- Use the full post link, such as `https://www.instagram.com/p/DPwhVB-jo9k/`, as `post_url`.
- `data.medias` is a list, so a post with several items can return several links.
- Media links are signed CDN URLs with long query strings. Store the file if you need it later.
- For other lookups by URL, see [Instagram Post Details by URL](/apis/instagram/v1/post-by-url) or [Instagram Post Details by ID](/apis/instagram/v1/post-by-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-url-v2.json`](../../../../catalog/models/instagram/v1/post-by-url-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-url-v2
