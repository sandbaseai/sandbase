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

Query detailed Instagram post data by supplying the post shortcode in the `code` parameter. The response returns post items including carousel elements and accessibility details.

### Use cases

- Inspect carousel items and media assets associated with an Instagram post.
- Extract post accessibility captions and metadata for analytics.
- Retrieve specific post data using known shortcodes from Instagram URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-info-by-code" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DUajw4YkorV"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (e.g., DUajw4YkorV, required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "carousel_media": [
        {
          "accessibility_caption": "Photo by Gigi on February 06, 2026.",
          "carousel_parent_id": "3826528124109228757_64352612340",
          "commerciality_status": "not_commercial",
          "id": "3826527467373490175_64352612340",
          "media_type": 1,
          "product_type": "carousel_item"
        }
      ]
    }
  ]
}
```

### Notes

- The `code` parameter accepts an Instagram post shortcode, such as DUajw4YkorV.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-info-by-code.json`](../../../../catalog/models/instagram/v3/post-info-by-code.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-info-by-code
