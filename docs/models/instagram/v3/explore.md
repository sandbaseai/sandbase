# Instagram Explore Feed API: pricing, parameters and code examples

`instagram/v3/explore` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns curated sectional items from the Instagram explore feed, including layout formats and feed types. Supports cursor-based pagination.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/explore"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/explore', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/explore", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/explore", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/explore` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |

## Details

Retrieve content items from the Instagram explore feed. Provide `max_id` to page through subsequent feed batches.

### Use cases

- Monitor trending content and clip formats on the explore grid.
- Analyze sectional layouts across recommended media.
- Inspect discovery feed items for market research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/explore" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `max_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_max_id` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sectional_items": [
    {
      "feed_type": "clips",
      "layout_type": "one_by_two_right"
    }
  ]
}
```

### Notes

- Omit `max_id` on the first request and use `data.next_max_id` from previous responses for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Shortcode Extractor](/apis/instagram/v3/extract-shortcode): Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL.

---
Machine-readable: [`catalog/models/instagram/v3/explore.json`](../../../../catalog/models/instagram/v3/explore.json) · Store page: https://www.sandbase.ai/model/instagram/v3/explore
