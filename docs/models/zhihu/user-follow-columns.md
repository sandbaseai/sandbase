# Zhihu User Follow Columns API: pricing, parameters and code examples

`zhihu/user-follow-columns` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get Zhihu columns followed by a user, with offset pagination. Use it to browse the columns associated with a known account's follow activity.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-follow-columns", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-follow-columns', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-follow-columns", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-follow-columns", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-follow-columns` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Get Zhihu columns followed by a user, with offset pagination. Use it to browse the columns associated with a known account's follow activity.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-follow-columns" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userUrlToken": "excited-vczh"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userUrlToken` | string | Yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`. |
| `offset` | integer | No | Start offset, begins with 0. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/zhihu/user-follow-columns.json`](../../../catalog/models/zhihu/user-follow-columns.json) · Store page: https://www.sandbase.ai/model/zhihu/user-follow-columns
