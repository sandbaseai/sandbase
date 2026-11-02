# Zhihu Pin Comments API: pricing, parameters and code examples

`zhihu/web/pin-comments` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a Zhihu pin, including author details, like counts, and reply counts. Supports sorting by score or newest timestamp.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/pin-comments", "pin_id": "2050290260991534603"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/pin-comments', {'pin_id': '2050290260991534603'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/pin-comments", {
  "pin_id": "2050290260991534603"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/pin-comments", sandbase.Params{
	"pin_id": "2050290260991534603",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/pin-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of comments per page default `"20"` |
| `offset` | string |  | Offset, take the cursor from the response for paging default `""` |
| `pin_id` | string | yes | Pin ID  |
| `order_by` | string |  | Sort, score=default, ts=newest one of: `score`, `ts`; default `"score"` |

## Details

Retrieve user comments and engagement metrics for a specific Zhihu pin by passing `pin_id`.

### Use cases

- Display discussion threads and feedback under Zhihu pins.
- Track sentiment and user engagement on specific pin posts.
- Sort community responses by popularity score or newest timestamp.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/pin-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pin_id": "2050290260991534603"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pin_id` | string | Yes | Pin ID |
| `limit` | string | No | Number of comments per page |
| `offset` | string | No | Offset, take the cursor from the response for paging |
| `order_by` | string | No | Sort, score=default, ts=newest |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "child_comment_count": 0,
      "comment_type": 0,
      "content": "看过吴恩达老师的课，挺不错的",
      "created_time": 1781864418,
      "dislike_count": 0,
      "id": "11511126051",
      "level_tag": 2,
      "like_count": 1,
      "member_id": 58471982,
      "reply_comment_id": "0",
      "author": {
        "id": "bee34cad7542c3006331794fb0e69bf6",
        "name": "AI通俗演绎",
        "type": "people",
        "url": "https://www.zhihu.com/api/v4/comment_v5/people/bee34cad7542c3006331794fb0e69bf6",
        "user_type": "people"
      }
    }
  ]
}
```

### Notes

- Set `order_by` to 'score' for default ranking or 'ts' for newest comments.
- Use `offset` cursor values from previous responses for pagination.
- Specify `limit` to control the number of comments returned per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/pin-comments.json`](../../../../catalog/models/zhihu/web/pin-comments.json) · Store page: https://www.sandbase.ai/model/zhihu/web/pin-comments
