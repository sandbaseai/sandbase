# Kuaishou Video Sub Comments (Web) API: pricing, parameters and code examples

`kuaishou/web/one-video-sub-comment` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns sub-comments and replies for a specific comment on a Kuaishou video. Requires the video ID and root comment ID with optional cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-sub-comment", "photo_id": "3xgarycnydawq3g", "root_comment_id": "908850553827"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-sub-comment', {'photo_id': '3xgarycnydawq3g', 'root_comment_id': '908850553827'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-sub-comment", {
  "photo_id": "3xgarycnydawq3g",
  "root_comment_id": "908850553827"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-sub-comment", sandbase.Params{
	"photo_id": "3xgarycnydawq3g",
	"root_comment_id": "908850553827",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |
| `root_comment_id` | string | yes | 根评论ID/Root comment ID  |

## Details

Retrieve threaded reply comments for a specific Kuaishou video comment using `photo_id` and `root_comment_id`.

### Use cases

- Display threaded comment replies under a primary video comment.
- Analyze conversational sentiment and audience interactions within comment threads.
- Extract nested user feedback and community discussions on video posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "<photo_id>", "root_comment_id": "<root_comment_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes | — |
| `root_comment_id` | string | Yes | — |
| `pcursor` | string | No | — |

### Notes

- Use `pcursor` to navigate across paginated pages of sub-comments.
- Both `photo_id` and `root_comment_id` are required to identify the target thread.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-sub-comment.json`](../../../../catalog/models/kuaishou/web/one-video-sub-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-sub-comment
