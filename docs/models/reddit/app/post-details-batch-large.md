# Reddit Post Details Large Batch API: pricing, parameters and code examples

`reddit/app/post-details-batch-large` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Returns details for up to 30 Reddit posts in a single request using comma-separated post IDs. Supports optional comment context and formatted output data.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-details-batch-large", "post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-details-batch-large', {'post_ids': 't3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-details-batch-large", {
  "post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-details-batch-large", sandbase.Params{
	"post_ids": "t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-details-batch-large` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_ids` | string | yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY,...", max 30 posts  |
| `comment_id` | string |  | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"  |
| `need_format` | boolean |  | Whether to clean and format the data  |
| `include_comment_id` | boolean |  | Whether to include specific comment ID, default False  |

## Details

Retrieve detailed post information for multiple Reddit submissions simultaneously by supplying post IDs in `post_ids`. Optional parameters like `include_comment_id` and `need_format` allow comment targeting and data formatting.

### Use cases

- Retrieve submission metadata for up to 30 Reddit posts simultaneously.
- Collect post context associated with a specific comment ID.
- Extract cleaned and formatted post datasets for bulk analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-details-batch-large" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_ids": "<post_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_ids` | string | Yes | Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY,...", max 30 posts |
| `comment_id` | string | No | Comment ID (used when include_comment_id is True), format like "t1_XXXXXX" |
| `need_format` | boolean | No | Whether to clean and format the data |
| `include_comment_id` | boolean | No | Whether to include specific comment ID, default False |

### Notes

- Pass a comma-separated list of up to 30 post IDs to `post_ids` using the `t3_` prefix format.
- Provide `comment_id` using the `t1_` prefix when `include_comment_id` is set to true.
- Set `need_format` to true to return cleaned and standardized data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-details-batch-large.json`](../../../../catalog/models/reddit/app/post-details-batch-large.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-details-batch-large
