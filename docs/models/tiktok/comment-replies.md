# TikTok Comment Replies API: pricing, parameters and code examples

`tiktok/comment-replies` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List the replies to a TikTok comment with cursor pagination (text, author, likes).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/comment-replies", "commentId": "7623828115408274207", "url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/comment-replies', {'commentId': '7623828115408274207', 'url': 'https://www.tiktok.com/@stoolpresidente/video/7623818255903329566'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/comment-replies", {
  "commentId": "7623828115408274207",
  "url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/comment-replies", sandbase.Params{
	"commentId": "7623828115408274207",
	"url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566",
})
```

Same call via the path form: `POST /v1/api/tiktok/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok video URL the comment belongs to.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `commentId` | string | yes | TikTok comment ID (the comment's cid from the comments endpoint).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorUserId`, and it is served only by a source that returns every…  |

## Details

List the replies to a TikTok comment with cursor pagination (text, author, likes).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@stoolpresidente/video/7623818255903329566", "commentId": "7623828115408274207"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `commentId` | string | Yes | TikTok comment ID (the comment's cid from the comments endpoint). |
| `url` | string | Yes | TikTok video URL the comment belongs to. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorUserId`, and it is served only by a source that returns every o |

### Pricing

Billed at the actual cost of each call, usually $0.0006 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/comment-replies.json`](../../../catalog/models/tiktok/comment-replies.json) · Store page: https://www.sandbase.ai/model/tiktok/comment-replies
