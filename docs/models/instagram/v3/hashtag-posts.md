# Instagram Hashtag Posts (V3) API: pricing, parameters and code examples

`instagram/v3/hashtag-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Retrieves public posts associated with a specified hashtag. Supports pagination cursors to browse through historical content feeds.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/hashtag-posts", "tag": "veganrecipes"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/hashtag-posts', {'tag': 'veganrecipes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/hashtag-posts", {
  "tag": "veganrecipes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/hashtag-posts", sandbase.Params{
	"tag": "veganrecipes",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/hashtag-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag` | string | yes | Hashtag keyword (without #)  |
| `max_id` | string |  | Pagination cursor from previous response, omit for first request  |

## Details

Use this endpoint to retrieve Instagram posts tagged with a specific keyword by supplying `tag`. Pass `max_id` to page through subsequent sets of results.

### Use cases

- Monitor user-generated content for branded hashtag campaigns.
- Track trending discussions and popular media around specific keywords.
- Collect feeds of public posts tagged with target topic labels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/hashtag-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag": "<tag>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag` | string | Yes | Hashtag keyword (without #) |
| `max_id` | string | No | Pagination cursor from previous response, omit for first request |

### Notes

- Provide the `tag` parameter without the '#' symbol.
- Pass `max_id` from a previous response cursor for pagination, or omit it on the initial request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/hashtag-posts.json`](../../../../catalog/models/instagram/v3/hashtag-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v3/hashtag-posts
