# Reddit App Comment Replies

`reddit/app/comment-replies` · api · Reddit

Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor. Supports custom sorting methods and data formatting options.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/comment-replies", "cursor": "commenttree:ex:(RjiJd", "post_id": "t3_1qmup73"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/comment-replies', {'cursor': 'commenttree:ex:(RjiJd', 'post_id': 't3_1qmup73'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/comment-replies", {
  "cursor": "commenttree:ex:(RjiJd",
  "post_id": "t3_1qmup73"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/comment-replies", sandbase.Params{
	"cursor": "commenttree:ex:(RjiJd",
	"post_id": "t3_1qmup73",
})
```

Same call via the path form: `POST /v1/api/reddit/app/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string | yes | Comment cursor from the more.cursor field in comment data, format like "commenttree:ex:(xxx)"  |
| `post_id` | string | yes | Post ID, format like "t3_XXXXXX"  |
| `sort_type` | string |  | Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Retrieve nested comment replies for a Reddit post by providing the target `post_id` and the comment node's `cursor`. It supports multiple sorting methods and optional response formatting.

### Use cases

- Retrieve nested sub-comments expanded under specific Reddit comment threads.
- Organize discussion branches by sorting responses by confidence, new, or top.
- Format Reddit app reply structures for clean downstream analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cursor": "<cursor>", "post_id": "<post_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | Yes | Comment cursor from the more.cursor field in comment data, format like "commenttree:ex:(xxx)" |
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
| `sort_type` | string | No | Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- Obtain `cursor` from the `more.cursor` field in prior comment response trees.
- `post_id` requires the Reddit prefix format such as `t3_XXXXXX`.
- `sort_type` accepts CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, or RANDOM.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.
- [Reddit Search](/model/reddit/app/dynamic-search): Search Reddit posts, communities, comments, media and users with the Reddit app search.

---
Machine-readable: [`catalog/models/reddit/app/comment-replies.json`](../../../../catalog/models/reddit/app/comment-replies.json) · Store page: https://www.sandbase.ai/model/reddit/app/comment-replies
