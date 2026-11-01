# Instagram User Tagged Posts (V3)

`instagram/v3/user-tagged-posts` · api · Instagram

Returns a list of posts where a specified Instagram account is tagged by other users. Supports both forward and backward cursor pagination.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-tagged-posts", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-tagged-posts', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-tagged-posts", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-tagged-posts", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Posts per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `data.page_info.end_cursor`  |
| `count` | integer |  | Number of posts for first request (default 12) default `12` |
| `first` | integer |  | Posts per page for forward pagination (default 12, max 50) default `12`; range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `data.page_info.start_cursor`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve posts where a targeted account has been tagged by querying with `username`. Supports cursor pagination via parameters like `after`, `before`, `first`, and `last`.

### Use cases

- Monitor user-generated content and brand mentions across tagged media.
- Track engagement metrics like like counts and comment counts on tagged posts.
- Collect media feeds where a specific creator or brand has been tagged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-tagged-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `last` | integer | No | Posts per page for backward pagination, use with `before` |
| `after` | string | No | Forward pagination cursor, from previous response `data.page_info.end_cursor` |
| `count` | integer | No | Number of posts for first request (default 12) |
| `first` | integer | No | Posts per page for forward pagination (default 12, max 50) |
| `before` | string | No | Backward pagination cursor, from previous response `data.page_info.start_cursor` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user": {
      "edge_user_to_photos_of_you": {
        "edges": [
          {
            "node": {
              "caption_text": "Uma homenagem a rede social que contribui muito para divulgação do meu trabalho. . O Inst…",
              "comment_count": 10252,
              "id": "2251138696266127152_3021079942",
              "like_count": 149724,
              "media_type": 1,
              "thumbnail_url": "https://instagram.fpit1-1.fna.fbcdn.net/v/t51.82787-15/621585839_180920878669893…"
            }
          }
        ]
      }
    }
  }
}
```

### Notes

- `username` is required to locate the target account.
- Use `first` (maximum 50, default 12) and `after` for forward pagination, or `last` and `before` for backward pagination.
- Pagination cursors come from `data.page_info.end_cursor` and `data.page_info.start_cursor`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-tagged-posts.json`](../../../../catalog/models/instagram/v3/user-tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-tagged-posts
