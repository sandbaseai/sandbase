# Instagram Location Posts (V3) API: pricing, parameters and code examples

`instagram/v3/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns Instagram posts associated with a specific location. Supports sorting by ranked or recent media alongside pagination controls.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/location-posts", "location_id": "1016248898"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/location-posts', {'location_id': '1016248898'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/location-posts", {
  "location_id": "1016248898"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/location-posts", sandbase.Params{
	"location_id": "1016248898",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Post sort order one of: `ranked`, `recent` |
| `after` | string |  | Pagination cursor from previous response `page_info.end_cursor`  |
| `first` | integer |  | Posts per page (default 12, max 50) range 1–50 |
| `location_id` | string | yes | Location ID (numeric)  |
| `page_size_override` | integer |  | Posts per page (default 12)  |

## Details

Retrieve posts tagged with a specific place by passing a numeric `location_id`. Sort results by top or latest media using `tab`.

### Use cases

- Track recent user activity and photos tagged at a venue
- Monitor top-performing posts tied to a geographical location
- Analyze location-based social content for places of interest

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "<location_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID (numeric) |
| `tab` | string | No | Post sort order |
| `after` | string | No | Pagination cursor from previous response `page_info.end_cursor` |
| `first` | integer | No | Posts per page (default 12, max 50) |
| `page_size_override` | integer | No | Posts per page (default 12) |

### Notes

- Obtain `location_id` via place search endpoints or existing post details.
- Use `tab` to sort by `ranked` (top) or `recent` (latest) posts.
- Paginate using the cursor from `page_info.end_cursor` passed into `after`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/location-posts.json`](../../../../catalog/models/instagram/v3/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/location-posts
