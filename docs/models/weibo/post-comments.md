# Weibo Post Comments API: pricing, parameters and code examples

`weibo/post-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get comments for a Weibo post identified by MID, with optional maxId cursor pagination and time or hot sorting.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/post-comments", "mid": "4799069542679480"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/post-comments', {'mid': '4799069542679480'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/post-comments", {
  "mid": "4799069542679480"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/post-comments", sandbase.Params{
	"mid": "4799069542679480",
})
```

Same call via the path form: `POST /v1/api/weibo/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mid` | string | yes | Weibo post mid.  |
| `sort` | string |  | Sort order for the result set. one of: `TIME`, `HOT`; default `"TIME"` |
| `maxId` | string |  | Pagination cursor returned by the previous response.  |

## Details

Get comments for a Weibo post identified by MID, with optional maxId cursor pagination and time or hot sorting.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mid": "5359793518938198"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mid` | string | Yes | Weibo post mid. |
| `sort` | string | No | Sort order for the result set. |
| `maxId` | string | No | Pagination cursor returned by the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/weibo/post-comments.json`](../../../catalog/models/weibo/post-comments.json) · Store page: https://www.sandbase.ai/model/weibo/post-comments
