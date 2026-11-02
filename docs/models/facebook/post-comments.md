# Facebook Post Comments API: pricing, parameters and code examples

`facebook/post-comments` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get comments for a Facebook post ID with cursor pagination. Use it to review discussion associated with a known public post or continue through subsequent comment pages.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/post-comments", "postId": "2000749587967633"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/post-comments', {'postId': '2000749587967633'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/post-comments", {
  "postId": "2000749587967633"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/post-comments", sandbase.Params{
	"postId": "2000749587967633",
})
```

Same call via the path form: `POST /v1/api/facebook/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of comments.  |
| `postId` | string | yes | The unique identifier of the Facebook post.  |

## Details

Get comments for a Facebook post ID with cursor pagination. Use it to review discussion associated with a known public post or continue through subsequent comment pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"postId": "2000749587967633"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `postId` | string | Yes | The unique identifier of the Facebook post. |
| `cursor` | string | No | Pagination cursor for fetching the next set of comments. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/facebook/post-comments.json`](../../../catalog/models/facebook/post-comments.json) · Store page: https://www.sandbase.ai/model/facebook/post-comments
