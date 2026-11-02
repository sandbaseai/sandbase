# Instagram Recommended Reels Feed API: pricing, parameters and code examples

`instagram/v3/recommended-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns the Instagram Reels recommendation feed with media details and pagination support. Use optional pagination parameters to control page size and navigate subsequent results.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/recommended-reels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/recommended-reels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/recommended-reels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/recommended-reels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/recommended-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Number of Reels to fetch per request (default 12, max 50) default `12`; range 1–50 |

## Details

Retrieve recommended Instagram Reels posts using optional `first` to set page size and `after` for pagination cursors.

### Use cases

- Browse recommended Reels content from Instagram.
- Collect trending short-form video media URLs for content analysis.
- Paginate through continuous Reels recommendation feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/recommended-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` |
| `first` | integer | No | Number of Reels to fetch per request (default 12, max 50) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "edges": [
    {
      "node": {
        "media": {
          "image_versions2": {
            "candidates": [
              {
                "url": "https://scontent.cdninstagram.com/v/t51.82787-15/829788099_18117638282107842_802…"
              }
            ]
          }
        }
      }
    }
  ]
}
```

### Notes

- Use `first` to specify the count of items to return, with a default of 12 and a maximum of 50.
- Pass `after` with the cursor from `data.page_info.end_cursor` of a previous response to paginate.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/recommended-reels.json`](../../../../catalog/models/instagram/v3/recommended-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v3/recommended-reels
