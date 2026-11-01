# Polymarket Get closed positions for a user

`polymarket/closed-positions` · api · Polymarket

Get closed positions for a user from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/closed-positions", "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/closed-positions', {'user': '0x56687bf447db6ffa42ffe2204a05edaa20f55839'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/closed-positions", {
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/closed-positions", sandbase.Params{
	"user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
})
```

Same call via the path form: `POST /v1/api/polymarket/closed-positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | The address of the user in question  |
| `limit` | integer |  | The max number of positions to return default `10`; range 0–50 |
| `title` | string |  | Filter by market title  |
| `market` | array |  | The conditionId of the market in question. Supports multiple csv separated values. Cannot be used with the eventId param.  |
| `offset` | integer |  | The starting index for pagination default `0`; range 0–100000 |
| `sortBy` | string |  | The sort criteria one of: `REALIZEDPNL`, `TITLE`, `PRICE`, `AVGPRICE`, `TIMESTAMP`; default `"REALIZEDPNL"` |
| `eventId` | array |  | The event id of the event in question. Supports multiple csv separated values. Returns positions for all markets for those event ids. Cannot be used with the market param.  |
| `sortDirection` | string |  | The sort direction one of: `ASC`, `DESC`; default `"DESC"` |

## Details

Get closed positions for a user from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/closed-positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `eventId` | array | No | The event id of the event in question. Supports multiple csv separated values. Returns positions for all markets for those event ids. Cannot be used with the ma |
| `limit` | integer | No | The max number of positions to return |
| `market` | array | No | The conditionId of the market in question. Supports multiple csv separated values. Cannot be used with the eventId param. |
| `offset` | integer | No | The starting index for pagination |
| `sortBy` | string | No | The sort criteria |
| `sortDirection` | string | No | The sort direction |
| `title` | string | No | Filter by market title |
| `user` | string | Yes | The address of the user in question |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/closed-positions.json`](../../../catalog/models/polymarket/closed-positions.json) · Store page: https://www.sandbase.ai/model/polymarket/closed-positions
