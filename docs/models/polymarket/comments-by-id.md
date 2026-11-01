# Polymarket Get comments by comment id

`polymarket/comments-by-id` · api · Polymarket

Get comments by comment id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments-by-id", "id": 3305081}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments-by-id', {'id': 3305081})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments-by-id", {
  "id": 3305081
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments-by-id", sandbase.Params{
	"id": 3305081,
})
```

Same call via the path form: `POST /v1/api/polymarket/comments-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `get_positions` | boolean |  | get_positions  |

## Details

Get comments by comment id from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 3305081}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `get_positions` | boolean | No | get_positions |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/comments-by-id.json`](../../../catalog/models/polymarket/comments-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/comments-by-id
