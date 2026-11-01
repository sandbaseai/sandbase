# Instagram Hashtag Posts (V2)

`instagram/v2/hashtag-posts` · api · Instagram

Returns posts associated with a specific hashtag. Supports filtering by top posts, recent posts, or reels along with cursor-based pagination.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/hashtag-posts", "keyword": "cat"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/hashtag-posts', {'keyword': 'cat'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/hashtag-posts", {
  "keyword": "cat"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/hashtag-posts", sandbase.Params{
	"keyword": "cat",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Hashtag keyword (without #)  |
| `feed_type` | string |  | Feed type "top", "recent", or "reels", default top default `"top"` |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Query posts tagged with a specific topic using `keyword` without the leading hash symbol. Feed results can optionally be filtered by `feed_type`.

### Use cases

- Track media content and engagement around specific campaign hashtags.
- Discover trending reels and top posts within niche topics.
- Monitor user-generated content for brand or community tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "cat"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Hashtag keyword (without #) |
| `feed_type` | string | No | Feed type "top", "recent", or "reels", default top |
| `pagination_token` | string | No | Pagination token from previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "caption_text": "Some coffee? #cat #cute #coffee #viral #fyp",
        "comment_count": 4,
        "id": "4001398805562288512",
        "like_and_view_counts_disabled": false,
        "like_count": 343,
        "media_name": "reel",
        "media_type": 2,
        "play_count": 8090,
        "product_type": "clips",
        "thumbnail_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.71878-15/836759883_10889105004450…",
        "clips_metadata": {
          "audio_canonical_id": "18632259277042329",
          "audio_type": "original_sounds",
          "professional_clips_upsell_type": 0
        },
        "user": {
          "id": "25310575539",
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/816178425_18114219469847…",
          "username": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- Provide `keyword` without the leading '#' symbol.
- `feed_type` accepts "top", "recent", or "reels", defaulting to "top".
- Pass `pagination_token` from a prior response to page through additional items.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Highlight Stories](/model/instagram/v2/highlight-stories): Returns all stories contained within a specific Instagram highlight using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v2/hashtag-posts.json`](../../../../catalog/models/instagram/v2/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v2/hashtag-posts
