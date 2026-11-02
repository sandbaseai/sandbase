# Xiaohongshu (RED) User Favorited Notes API: pricing, parameters and code examples

`xiaohongshu/app-v2/user-faved-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns a paginated list of notes favorited by a specified Xiaohongshu (RED) user. Supports querying by user ID or profile share link, with cursor-based pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-faved-notes", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-faved-notes', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-faved-notes", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-faved-notes", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-faved-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass last note_id from previous page for next page  |
| `user_id` | string |  | User ID, e.g. "5a8cf39111be10466d285d6b"  |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link)  |

## Details

Retrieve notes favorited by a Xiaohongshu (RED) user using `user_id` or `share_text`. Results can be paginated sequentially using the `cursor` parameter.

### Use cases

- Analyze content preferences and topics favorited by target users.
- Track saved posts to understand audience engagement patterns.
- Collect curated note references from public user profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-faved-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass last note_id from previous page for next page |
| `user_id` | string | No | User ID, e.g. "5a8cf39111be10466d285d6b" |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |

### Notes

- Leave `cursor` empty for the initial request, then pass the last note ID from the previous page for subsequent requests.
- The `share_text` parameter supports both mobile app and web sharing links.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/model/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-faved-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/user-faved-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-faved-notes
