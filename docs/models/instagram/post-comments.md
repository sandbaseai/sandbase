# Instagram Post Comment List API: pricing, parameters and code examples

`instagram/post-comments` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get top-level comments for an Instagram post by shortcode, with cursor pagination and popular or newest sorting. Use it to review audience feedback or analyze discussion around a known post.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/post-comments", "code": "DfAOoAXRg3L"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/post-comments', {'code': 'DfAOoAXRg3L'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/post-comments", {
  "code": "DfAOoAXRg3L"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/post-comments", sandbase.Params{
	"code": "DfAOoAXRg3L",
})
```

Same call via the path form: `POST /v1/api/instagram/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | The unique shortcode for the Instagram post.  |
| `minId` | string |  | Pagination cursor returned as next_min_id from the previous response.  |
| `sortOrder` | string |  | Sort order for the comments. one of: `popular`, `newest`; default `"newest"` |

## Details

Get top-level comments for an Instagram post by shortcode, with cursor pagination and popular or newest sorting. Use it to review audience feedback or analyze discussion around a known post.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "DfAOoAXRg3L"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | The unique shortcode for the Instagram post. |
| `minId` | string | No | Pagination cursor returned as next_min_id from the previous response. |
| `sortOrder` | string | No | Sort order for the comments. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/instagram/post-comments.json`](../../../catalog/models/instagram/post-comments.json) · Store page: https://www.sandbase.ai/model/instagram/post-comments
