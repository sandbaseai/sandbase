# Weibo User Published Posts API: pricing, parameters and code examples

`weibo/user-post` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get posts published by a Weibo user identified by UID, using page numbers and a required sinceId cursor after the first page. Use it to browse an account's posting history or continue through its post feed.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/user-post", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/user-post', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/user-post", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/user-post", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/user-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `page` | integer |  | Page number, starting with 1. default `1` |
| `sinceId` | string |  | Pagination cursor (since_id). Required if page > 1.  |

## Details

Get posts published by a Weibo user identified by UID, using page numbers and a required sinceId cursor after the first page. Use it to browse an account's posting history or continue through its post feed.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |
| `page` | integer | No | Page number, starting with 1. |
| `sinceId` | string | No | Pagination cursor (since_id). Required if page > 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/weibo/user-post.json`](../../../catalog/models/weibo/user-post.json) · Store page: https://www.sandbase.ai/model/weibo/user-post
