# Polymarket List comments

`polymarket/comments` · api · Polymarket

List comments from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `holders_only` | boolean |  | holders_only  |
| `get_positions` | boolean |  | get_positions  |
| `parent_entity_id` | integer |  | parent_entity_id  |
| `parent_entity_type` | string |  | parent_entity_type one of: `Event`, `Series`, `market` |

## Details

List comments from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"parent_entity_type": "Event", "parent_entity_id": 2890, "limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `get_positions` | boolean | No | get_positions |
| `holders_only` | boolean | No | holders_only |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `parent_entity_id` | integer | No | parent_entity_id |
| `parent_entity_type` | string | No | parent_entity_type |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/comments.json`](../../../catalog/models/polymarket/comments.json) · Store page: https://www.sandbase.ai/model/polymarket/comments
