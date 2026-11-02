# Douyin Comment Replies API: pricing, parameters and code examples

`douyin/video-sub-comment` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get replies to a top-level Douyin (TikTok China) video comment with page-based pagination. Use it to inspect threaded discussions and review feedback under a known comment.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/video-sub-comment", "commentId": "1767587367821390"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/video-sub-comment', {'commentId': '1767587367821390'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/video-sub-comment", {
  "commentId": "1767587367821390"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/video-sub-comment", sandbase.Params{
	"commentId": "1767587367821390",
})
```

Same call via the path form: `POST /v1/api/douyin/video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `commentId` | string | yes | The unique identifier of the top-level comment.  |

## Details

Get replies to a top-level Douyin (TikTok China) video comment with page-based pagination. Use it to inspect threaded discussions and review feedback under a known comment.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"commentId": "7373626964752450315"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | The unique identifier of the top-level comment. |
| `page` | integer | No | Page number (starting from 1). |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/video-sub-comment.json`](../../../catalog/models/douyin/video-sub-comment.json) · Store page: https://www.sandbase.ai/model/douyin/video-sub-comment
