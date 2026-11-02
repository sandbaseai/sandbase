# Zhihu Sub Comments API: pricing, parameters and code examples

`zhihu/web/sub-comment-v5` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns replies to a specific Zhihu comment. Supports pagination through limit and offset parameters alongside custom sorting options.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/sub-comment-v5", "comment_id": "11586819658"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/sub-comment-v5', {'comment_id': '11586819658'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/sub-comment-v5", {
  "comment_id": "11586819658"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/sub-comment-v5", sandbase.Params{
	"comment_id": "11586819658",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/sub-comment-v5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of comments per page  |
| `offset` | string |  | Offset/Page Number  |
| `order_by` | string |  | Sort  |
| `comment_id` | string | yes | Comment ID  |

## Details

Fetch reply threads for a specific Zhihu comment by passing `comment_id`. You can configure sorting and pagination with `order_by`, `limit`, and `offset`.

### Use cases

- Read nested replies under a specific Zhihu comment.
- Track discussion threads within popular discussion topics.
- Collect detailed sub-comment interactions for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/sub-comment-v5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"comment_id": "<comment_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `comment_id` | string | Yes | Comment ID |
| `limit` | string | No | Number of comments per page |
| `offset` | string | No | Offset/Page Number |
| `order_by` | string | No | Sort |

### Notes

- `comment_id` is required to specify the parent comment.
- Use `limit` and `offset` to manage pagination.
- Use `order_by` to control the sort order of sub-comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/sub-comment-v5.json`](../../../../catalog/models/zhihu/web/sub-comment-v5.json) · Store page: https://www.sandbase.ai/model/zhihu/web/sub-comment-v5
