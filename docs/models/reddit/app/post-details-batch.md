# Reddit Batch Post Details API: pricing, parameters and code examples

`reddit/app/post-details-batch` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Returns detailed post data for up to five Reddit posts specified by ID. Supports optional comment context and structured data formatting.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-details-batch", "post_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-details-batch', {'post_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-details-batch", {
  "post_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-details-batch", sandbase.Params{
	"post_ids": "example",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-details-batch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_ids` | string | yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY", max 5 posts  |
| `comment_id` | string |  | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"  |
| `need_format` | boolean |  | Whether to clean and format the data  |
| `include_comment_id` | boolean |  | Whether to include specific comment ID, default False  |

## Details

Retrieve detailed information for multiple Reddit posts using a comma-separated list in `post_ids`. You can also supply `comment_id` and formatting toggles to shape the output.

### Use cases

- Retrieve metadata and contents for several posts in one call.
- Inspect specific comment contexts alongside queried posts.
- Format raw Reddit post output for downstream analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_ids": "<post_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_ids` | string | Yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY", max 5 posts |
| `comment_id` | string | No | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX" |
| `need_format` | boolean | No | Whether to clean and format the data |
| `include_comment_id` | boolean | No | Whether to include specific comment ID, default False |

### Notes

- `post_ids` accepts up to 5 comma-separated post IDs formatted like `t3_XXXXXX`.
- `comment_id` requires IDs formatted like `t1_XXXXXX` and is used when `include_comment_id` is true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details-batch.json`](../../../../catalog/models/reddit/app/post-details-batch.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details-batch
