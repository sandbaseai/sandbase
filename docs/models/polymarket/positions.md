# Polymarket Get current positions for a user API: pricing, parameters and code examples

`polymarket/positions` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get current positions for a user from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/positions", "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/positions', {'user': '0x56687bf447db6ffa42ffe2204a05edaa20f55839'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/positions", {
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/positions", sandbase.Params{
	"user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
})
```

Same call via the path form: `POST /v1/api/polymarket/positions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | User address (required)  |
| `limit` | integer |  | limit default `100`; range 0–500 |
| `title` | string |  | title  |
| `market` | array |  | Comma-separated list of condition IDs. Mutually exclusive with eventId.  |
| `offset` | integer |  | offset default `0`; range 0–10000 |
| `sortBy` | string |  | sortBy one of: `CURRENT`, `INITIAL`, `TOKENS`, `CASHPNL`, `PERCENTPNL`, `TITLE`, `RESOLVING`, `PRICE`, `AVGPRICE`; default `"TOKENS"` |
| `eventId` | array |  | Comma-separated list of event IDs. Mutually exclusive with market.  |
| `mergeable` | boolean |  | mergeable default `false` |
| `redeemable` | boolean |  | redeemable default `false` |
| `sizeThreshold` | number |  | sizeThreshold default `1`; range 0– |
| `sortDirection` | string |  | sortDirection one of: `ASC`, `DESC`; default `"DESC"` |
| `includeArchived` | boolean |  | Include positions in archived markets that are still active. Archived positions are excluded by default. default `false` |

## Details

Get current positions for a user from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/positions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319", "limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `eventId` | array | No | Comma-separated list of event IDs. Mutually exclusive with market. |
| `includeArchived` | boolean | No | Include positions in archived markets that are still active. Archived positions are excluded by default. |
| `limit` | integer | No | limit |
| `market` | array | No | Comma-separated list of condition IDs. Mutually exclusive with eventId. |
| `mergeable` | boolean | No | mergeable |
| `offset` | integer | No | offset |
| `redeemable` | boolean | No | redeemable |
| `sizeThreshold` | number | No | sizeThreshold |
| `sortBy` | string | No | sortBy |
| `sortDirection` | string | No | sortDirection |
| `title` | string | No | title |
| `user` | string | Yes | User address (required) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/positions.json`](../../../catalog/models/polymarket/positions.json) · Store page: https://www.sandbase.ai/model/polymarket/positions
