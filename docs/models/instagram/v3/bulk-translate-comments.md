# Instagram Comment Bulk Translation API: pricing, parameters and code examples

`instagram/v3/bulk-translate-comments` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns bulk translations for multiple Instagram comments using a list of comment identifiers. Accepts up to 10 comma-separated IDs to translate multiple comments at once.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/bulk-translate-comments", "comment_ids": "<comment_ids>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/bulk-translate-comments', {'comment_ids': '<comment_ids>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/bulk-translate-comments", {
  "comment_ids": "<comment_ids>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/bulk-translate-comments", sandbase.Params{
	"comment_ids": "<comment_ids>",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/bulk-translate-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `comment_ids` | string | yes | Comment ID list, separated by commas, **max 10 IDs**  |

## Details

Translate multiple Instagram comments simultaneously by providing a list of IDs in `comment_ids`. This endpoint facilitates efficient cross-language comment analysis across posts.

### Use cases

- Translate foreign-language Instagram user comments for sentiment analysis.
- Review multilingual feedback across international marketing campaigns.
- Localize incoming audience interactions for customer support teams.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/bulk-translate-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_ids": "<comment_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `comment_ids` | string | Yes | Comment ID list, separated by commas, max 10 IDs |

### Notes

- Accepts a maximum of 10 IDs in `comment_ids`, separated by commas.
- Comment IDs can be obtained from post comments endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.
- [Instagram Shortcode Extractor](/model/instagram/v3/extract-shortcode): Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL.

---
Machine-readable: [`catalog/models/instagram/v3/bulk-translate-comments.json`](../../../../catalog/models/instagram/v3/bulk-translate-comments.json) · Store page: https://www.sandbase.ai/model/instagram/v3/bulk-translate-comments
