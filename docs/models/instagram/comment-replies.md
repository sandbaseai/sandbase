# Instagram Comment Replies API: pricing, parameters and code examples

`instagram/comment-replies` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List the replies to an Instagram comment with cursor pagination (text, author, likes).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/comment-replies", "commentId": "18126632131325044", "url": "https://www.instagram.com/p/C8rKmYvsrck/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/comment-replies', {'commentId': '18126632131325044', 'url': 'https://www.instagram.com/p/C8rKmYvsrck/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/comment-replies", {
  "commentId": "18126632131325044",
  "url": "https://www.instagram.com/p/C8rKmYvsrck/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/comment-replies", sandbase.Params{
	"commentId": "18126632131325044",
	"url": "https://www.instagram.com/p/C8rKmYvsrck/",
})
```

Same call via the path form: `POST /v1/api/instagram/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Instagram post or reel URL the comment belongs to.  |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `commentId` | string | yes | Instagram comment ID (a comment's id from the Instagram Post Comments endpoint).  |

## Details

List the replies to an Instagram comment with cursor pagination (text, author, likes).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/C8rKmYvsrck/", "commentId": "18126632131325044"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | Instagram comment ID (a comment's id from the Instagram Post Comments endpoint). |
| `url` | string | Yes | Full Instagram post or reel URL the comment belongs to. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/comment-replies.json`](../../../catalog/models/instagram/comment-replies.json) · Store page: https://www.sandbase.ai/model/instagram/comment-replies
