# Reddit App Post Comments API: pricing, parameters and code examples

`reddit/app/post-comments` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comment trees for a specific Reddit post by its ID. Supports comment sorting by hot, new, top, best, or controversial, with optional pagination via a cursor.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/post-comments", "after": "", "need_format": false, "post_id": "t3_1ojnvca", "sort_type": "CONFIDENCE"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/post-comments', {'after': '', 'need_format': False, 'post_id': 't3_1ojnvca', 'sort_type': 'CONFIDENCE'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/post-comments", {
  "after": "",
  "need_format": false,
  "post_id": "t3_1ojnvca",
  "sort_type": "CONFIDENCE"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/post-comments", sandbase.Params{
	"after": "",
	"need_format": false,
	"post_id": "t3_1ojnvca",
	"sort_type": "CONFIDENCE",
})
```

Same call via the path form: `POST /v1/api/reddit/app/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor default `""` |
| `post_id` | string | yes | Post ID, format like "t3_XXXXXX"  |
| `sort_type` | string |  | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL default `"CONFIDENCE"` |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Retrieve discussion comments for a Reddit submission using `post_id`. Configure comment order with `sort_type` and page through comment trees using `after`.

### Use cases

- Retrieve top discussion threads and reply trees under a Reddit submission.
- Analyze audience sentiment and reactions across community discussions.
- Extract recent community feedback by sorting comments by new.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "t3_1ojnvca"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID, format like "t3_XXXXXX" |
| `after` | string | No | Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more… |
| `sort_type` | string | No | Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL |
| `need_format` | boolean | No | Whether to clean and format the data |

### Notes

- `post_id` expects an identifier formatted like t3_XXXXXX.
- Supported `sort_type` options include HOT, NEW, TOP, BEST, and CONTROVERSIAL.
- Pagination uses the `after` cursor obtained from the last comment node in the comment forest.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Reddit Subreddit Mute Status](/model/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/model/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/model/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/post-comments.json`](../../../../catalog/models/reddit/app/post-comments.json) · Store page: https://www.sandbase.ai/model/reddit/app/post-comments
