# Douyin Index User ID Encryption API: pricing, parameters and code examples

`douyin/index/encrypt-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a standard numeric Douyin uid into the encrypted user_id required by Douyin Index endpoints for debugging or custom queries.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/encrypt-user-id", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/encrypt-user-id', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/encrypt-user-id", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/encrypt-user-id", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/index/encrypt-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Douyin uid, numeric string  |

## Details

Convert a numeric Douyin user identifier into an internal encrypted format by passing `uid`. This provides direct access to the encrypted identifier required by Douyin Index queries.

### Use cases

- Look up encrypted user identifiers for debugging Douyin Index integration issues.
- Convert numeric user IDs for manual queries against Douyin Index endpoints.
- Resolve internal user ID formats without calling full daren analytics endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/encrypt-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Douyin uid, numeric string |

### Notes

- The required `uid` parameter expects a numeric string representation of the Douyin account ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/encrypt-user-id.json`](../../../../catalog/models/douyin/index/encrypt-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/index/encrypt-user-id
