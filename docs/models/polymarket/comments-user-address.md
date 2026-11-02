# Polymarket Get comments by user address API: pricing, parameters and code examples

`polymarket/comments-user-address` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get comments by user address from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments-user-address", "user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments-user-address', {'user_address': '0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments-user-address", {
  "user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments-user-address", sandbase.Params{
	"user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6",
})
```

Same call via the path form: `POST /v1/api/polymarket/comments-user-address` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `user_address` | string | yes | user_address  |

## Details

Get comments by user address from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments-user-address" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_address` | string | Yes | user_address |
| `ascending` | boolean | No | ascending |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/comments-user-address.json`](../../../catalog/models/polymarket/comments-user-address.json) · Store page: https://www.sandbase.ai/model/polymarket/comments-user-address
