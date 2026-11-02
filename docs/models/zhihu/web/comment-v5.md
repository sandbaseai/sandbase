# Zhihu Answer Comments API: pricing, parameters and code examples

`zhihu/web/comment-v5` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the comments on a Zhihu answer: comment text, author, time, like and reply counts, with sorting and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/comment-v5", "answer_id": "2023560406912770519"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/comment-v5', {'answer_id': '2023560406912770519'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/comment-v5", {
  "answer_id": "2023560406912770519"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/comment-v5", sandbase.Params{
	"answer_id": "2023560406912770519",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/comment-v5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of comments per page  |
| `offset` | string |  | Offset/Page Number  |
| `order_by` | string |  | Sort  |
| `answer_id` | string | yes | Answer ID  |

## Details

Pass a Zhihu answer ID and get its comments with like and reply counts.

### Use cases

- Analyze discussion and sentiment around an answer.
- Collect user feedback on a topic.
- Monitor comments on brand content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/comment-v5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"answer_id": "2023560406912770519"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `answer_id` | string | Yes | Answer ID |
| `limit` | string | No | Number of comments per page |
| `offset` | string | No | Offset/Page Number |
| `order_by` | string | No | Sort |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "paging": {
    "is_end": false
  },
  "data": [
    {
      "id": "11454716173",
      "created_time": 1775378836,
      "like_count": 118,
      "child_comment_count": 60,
      "content": "人的理解能力也就那么回事，为啥非得高估人类呢，为啥感觉大模型不算理解呢？",
      "author": {
        "name": "<user>"
      }
    }
  ]
}
```

### Notes

- Get answer IDs from Zhihu search results or answer URLs.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Hot List](/model/zhihu/web/hot-list): Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links.
- [Get Zhihu AI Search (v2)](/model/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).

---
Machine-readable: [`catalog/models/zhihu/web/comment-v5.json`](../../../../catalog/models/zhihu/web/comment-v5.json) · Store page: https://www.sandbase.ai/model/zhihu/web/comment-v5
