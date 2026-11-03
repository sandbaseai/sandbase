# Instagram User Reels (V3) API: pricing, parameters and code examples

`instagram/v3/user-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of Reels for a specific Instagram user. Supports cursor-based forward and backward pagination alongside page size limits.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-reels", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-reels', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-reels", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-reels", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Reels per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Reels per page for forward pagination (default 12, max 50) default `12`; range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `data.page_info.start_cursor`  |
| `username` | string | yes | Instagram username (required)  |
| `page_size` | integer |  | Videos per page (default 12) default `12` |

## Details

Retrieves Reels associated with an account using `username`. Includes pagination controls via cursors such as `after` and `before`.

### Use cases

- Analyze engagement metrics like likes and comment counts on an account's Reels.
- Collect recent Reel media clips and captions for creator profiles.
- Browse through a creator's historical Reel catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `last` | integer | No | Reels per page for backward pagination, use with `before` |
| `after` | string | No | Forward pagination cursor, from previous response `data.page_info.end_cursor` |
| `first` | integer | No | Reels per page for forward pagination (default 12, max 50) |
| `before` | string | No | Backward pagination cursor, from previous response `data.page_info.start_cursor` |
| `page_size` | integer | No | Videos per page (default 12) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "xdt_api__v1__clips__user__connection_v2": {
      "edges": [
        {
          "node": {
            "caption_text": "DIY fish squishy 🐟⁣ ⁣ @yano4kaa.a made this squishy using stuff she already had at home l…",
            "comment_count": 18380,
            "id": "3998430248382584993_25025320",
            "like_count": 642825,
            "media_type": 2,
            "thumbnail_url": "https://scontent-hou1-1.cdninstagram.com/v/t51.82787-15/830594125_18798964129001…"
          }
        }
      ]
    }
  }
}
```

### Notes

- Set `first` up to a maximum of 50 to control forward pagination page size.
- Pass `after` using `end_cursor` or `before` using `start_cursor` from previous response page info.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-reels.json`](../../../../catalog/models/instagram/v3/user-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-reels
