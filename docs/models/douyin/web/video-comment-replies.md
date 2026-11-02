# Douyin Video Comment Replies (Web) API: pricing, parameters and code examples

`douyin/web/video-comment-replies` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns reply data for a specific comment on a Douyin video. Supports pagination controls through cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-comment-replies", "comment_id": "7354669356632638218", "item_id": "7354666303006723354"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-comment-replies', {'comment_id': '7354669356632638218', 'item_id': '7354666303006723354'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-comment-replies", {
  "comment_id": "7354669356632638218",
  "item_id": "7354666303006723354"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-comment-replies", sandbase.Params{
	"comment_id": "7354669356632638218",
	"item_id": "7354666303006723354",
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `cursor` | integer |  | Cursor  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Retrieves replies for a specific comment on a Douyin video using `item_id` and `comment_id`. Supports pagination via `cursor` and `count`.

### Use cases

- Read conversation threads under a specific comment on a Douyin video.
- Monitor user interactions and responses to parent comments.
- Export nested reply data for audience engagement analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "<comment_id>", "item_id": "<item_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `comment_id` | string | Yes | Comment id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor |

### Notes

- Requires both `item_id` (video ID) and `comment_id` (parent comment ID).
- Pagination is controlled using `cursor` and `count`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-comment-replies.json`](../../../../catalog/models/douyin/web/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-comment-replies
