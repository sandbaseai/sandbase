# Instagram Post Info by Shortcode API: pricing, parameters and code examples

`instagram/v3/post-info-by-code` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Retrieves detailed post information and media items for an Instagram post using its shortcode. Provides carousel media details, accessibility captions, and post identifiers.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-info-by-code", "code": "DUajw4YkorV"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-info-by-code', {'code': 'DUajw4YkorV'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-info-by-code", {
  "code": "DUajw4YkorV"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-info-by-code", sandbase.Params{
	"code": "DUajw4YkorV",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-info-by-code` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | Post shortcode (e.g., DUajw4YkorV, required)  |

## Details

Get an Instagram post or reel by its shortcode: caption, media type, like and comment counts, post time, author, images, video URLs and carousel items.

### Use cases

- Track engagement of specific posts.
- Get the media files and caption of a shared post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-info-by-code" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DUajw4YkorV"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (e.g., DUajw4YkorV, required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "items": [
    {
      "pk": "3826528124109228757",
      "code": "DUajw4YkorV",
      "taken_at": 1770377720,
      "media_type": 8,
      "product_type": "carousel_container",
      "like_count": 12296,
      "comment_count": 49,
      "carousel_media_count": 7,
      "caption": {
        "text": "breeze breeze breeze 🌀🌀🌀"
      },
      "user": {
        "pk": "64352612340",
        "username": "hiyroze",
        "full_name": "Gigi",
        "is_verified": false
      }
    }
  ],
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].pk / code` | Media ID and shortcode. |
| `items[].taken_at` | Post time, Unix seconds. |
| `items[].media_type / product_type` | 1 photo, 2 video, 8 carousel; `clips` for reels. |
| `items[].like_count / comment_count` | Engagement counts. |
| `items[].caption.text` | Caption. |
| `items[].user` | Author `username`, `full_name`, `pk`. |
| `items[].image_versions2 / video_versions` | Media URLs; signed and temporary. |

### Notes

- The shortcode is the part after `/p/` or `/reel/`; extract it with [Extract Shortcode](/apis/instagram/v3/extract-shortcode).
- An Instagram media ID and its shortcode are the same number in two encodings. The shortcode is the media ID written in base 64 with the alphabet `A-Z a-z 0-9 - _` (A = 0, _ = 63), so `DRhvwVLAHAG` and `3774507992167247878` name the same post. The media ID itself is a 64-bit snowflake: the top 41 bits are milliseconds since Instagram's epoch (2011-08-24 21:07:01.721 UTC), followed by 13 bits of shard ID and 10 bits of sequence, so `media_id >> 23` plus 1314220021721 gives the post's creation time in Unix milliseconds. Media IDs longer than 19 digits, with a `_<user_id>` suffix, are the same ID with the owner appended: drop the suffix before converting.

### Pricing

$0.008 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-info-by-code.json`](../../../../catalog/models/instagram/v3/post-info-by-code.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-info-by-code
