# Xiaohongshu (RED) User Posted Notes API: pricing, parameters and code examples

`xiaohongshu/app-v2/user-posted-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves a list of notes posted by a specific Xiaohongshu user with cursor pagination. Query by providing a user identifier or a shared post link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-posted-notes", "user_id": "6673f0820000000007005d06"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-posted-notes', {'user_id': '6673f0820000000007005d06'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-posted-notes", {
  "user_id": "6673f0820000000007005d06"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-posted-notes", sandbase.Params{
	"user_id": "6673f0820000000007005d06",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-posted-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page  |
| `user_id` | string |  | User ID, e.g. "61b46d790000000010008153"  |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link)  |

## Details

Returns notes posted by a specific user using either `user_id` or `share_text`. Supports cursor-based pagination through the `cursor` parameter.

### Use cases

- Retrieve historical posts from a targeted Xiaohongshu creator profile.
- Analyze recent content feeds shared by specific users.
- Extract note listings from shared profile links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-posted-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "61b46d790000000010008153", "share_text": "http://xhslink.com/o/8GqargIxrko"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page |
| `user_id` | string | No | User ID, e.g. "61b46d790000000010008153" |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |

### Notes

- Leave `cursor` empty for the initial request, then pass the returned cursor value for subsequent pages.
- Accepts either a `user_id` or an app/web sharing link via `share_text`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-posted-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/user-posted-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-posted-notes
