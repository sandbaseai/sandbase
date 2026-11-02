# TikTok Comment Replies API: pricing, parameters and code examples

`tiktok/post-sub-comment` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get replies to a specific comment on a TikTok post with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for a known post comment.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/post-sub-comment", "awemeId": "7701102965385383199", "commentId": "1650470666299398"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/post-sub-comment', {'awemeId': '7701102965385383199', 'commentId': '1650470666299398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/post-sub-comment", {
  "awemeId": "7701102965385383199",
  "commentId": "1650470666299398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/post-sub-comment", sandbase.Params{
	"awemeId": "7701102965385383199",
	"commentId": "1650470666299398",
})
```

Same call via the path form: `POST /v1/api/tiktok/post-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor. Start with '0'. default `"0"` |
| `awemeId` | string | yes | The unique ID of the TikTok post.  |
| `commentId` | string | yes | The unique ID of the comment to retrieve replies for.  |

## Details

Get replies to a specific comment on a TikTok post with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for a known post comment.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/post-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"awemeId": "7701102965385383199", "commentId": "1650470666299398"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `awemeId` | string | Yes | The unique ID of the TikTok post. |
| `commentId` | string | Yes | The unique ID of the comment to retrieve replies for. |
| `cursor` | string | No | Pagination cursor. Start with '0'. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tiktok/post-sub-comment.json`](../../../catalog/models/tiktok/post-sub-comment.json) · Store page: https://www.sandbase.ai/model/tiktok/post-sub-comment
