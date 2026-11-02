# Xiaohongshu Note Comments API: pricing, parameters and code examples

`xiaohongshu/note-comment` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get comments for a Xiaohongshu (RedNote) note with cursor pagination and normal, latest, or like-count sorting. Use it to support feedback review, discussion analysis, and comment moderation workflows.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/note-comment", "noteId": "6ae00b99000000001200a9f9"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/note-comment', {'noteId': '6ae00b99000000001200a9f9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/note-comment", {
  "noteId": "6ae00b99000000001200a9f9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/note-comment", sandbase.Params{
	"noteId": "6ae00b99000000001200a9f9",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/note-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort strategy for the result set. one of: `normal`, `latest`, `like_count`; default `"latest"` |
| `noteId` | string | yes | A Xiaohongshu note ID or an explore URL containing /explore/.  |
| `lastCursor` | string |  | Pagination cursor from the previous page (use the cursor value returned by the last response).  |

## Details

Get comments for a Xiaohongshu (RedNote) note with cursor pagination and normal, latest, or like-count sorting. Use it to support feedback review, discussion analysis, and comment moderation workflows.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/note-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6ae00b99000000001200a9f9"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | A Xiaohongshu note ID or an explore URL containing /explore/. |
| `lastCursor` | string | No | Pagination cursor from the previous page (use the cursor value returned by the last response). |
| `sort` | string | No | Sort strategy for the result set. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/note-comment.json`](../../../catalog/models/xiaohongshu/note-comment.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/note-comment
