# Instagram Comment Replies (V3) API: pricing, parameters and code examples

`instagram/v3/comment-replies` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID. Supports pagination via cursor tokens.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/comment-replies", "comment_id": "<comment_id>", "media_id": "<media_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/comment-replies', {'comment_id': '<comment_id>', 'media_id': '<media_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/comment-replies", {
  "comment_id": "<comment_id>",
  "media_id": "<media_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/comment-replies", sandbase.Params{
	"comment_id": "<comment_id>",
	"media_id": "<media_id>",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `min_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_min_child_cursor`  |
| `media_id` | string | yes | Post media ID (numeric ID, required), can be obtained via `/shortcode_to_media_id` endpoint  |
| `comment_id` | string | yes | Parent comment ID (required, get `pk` field from get_post_comments response)  |

## Details

Retrieve threaded comment replies for an Instagram post by supplying `media_id` and `comment_id`. Additional pages can be fetched using `min_id`.

### Use cases

- Track conversational replies under popular post comments.
- Audit user engagement and discussions across comment threads.
- Analyze community sentiment within nested comment threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "<comment_id>", "media_id": "<media_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | Yes | Post media ID (numeric ID, required), can be obtained via `/shortcode_to_media_id` endpoint |
| `comment_id` | string | Yes | Parent comment ID (required, get `pk` field from get_post_comments response) |
| `min_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_min_child_cursor` |

### Notes

- Obtain `media_id` via the `/shortcode_to_media_id` endpoint.
- Obtain `comment_id` from the `pk` field of post comment results.
- Use `min_id` with `data.next_min_child_cursor` from the previous response for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.
- [Instagram Shortcode Extractor](/model/instagram/v3/extract-shortcode): Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL.

---
Machine-readable: [`catalog/models/instagram/v3/comment-replies.json`](../../../../catalog/models/instagram/v3/comment-replies.json) · Store page: https://www.sandbase.ai/model/instagram/v3/comment-replies
