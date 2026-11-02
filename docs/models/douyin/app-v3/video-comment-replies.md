# Douyin Video Comment Replies (App V3) API: pricing, parameters and code examples

`douyin/app-v3/video-comment-replies` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns reply comments for a specific comment on a Douyin video based on the video ID and comment ID, with support for cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-comment-replies", "comment_id": "example", "item_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-comment-replies', {'comment_id': 'example', 'item_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-comment-replies", {
  "comment_id": "example",
  "item_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-comment-replies", sandbase.Params{
	"comment_id": "example",
	"item_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `item_id` | string | yes | Video id  |
| `comment_id` | string | yes | Comment id  |

## Details

Look up replies to a specific video comment on Douyin using `item_id` and `comment_id`. Supports iterating through reply threads with cursor pagination.

### Use cases

- Retrieve conversation threads under a specific Douyin video comment.
- Analyze audience discussions and engagement within nested comment replies.
- Monitor user responses directed at particular comment threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "<comment_id>", "item_id": "<item_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video id |
| `comment_id` | string | Yes | Comment id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Notes

- Set `cursor` to 0 for the first page, then pass the returned cursor value for subsequent pages.
- Keep `count` at its default value to prevent response issues.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-comment-replies.json`](../../../../catalog/models/douyin/app-v3/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-comment-replies
