# Kalshi Get Kalshi Market OrderBook API: pricing, parameters and code examples

`kalshi/markets-orderbook` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Kalshi Market OrderBook from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets-orderbook", "ticker": "KXHIGHNY-26OCT31-B60.5"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets-orderbook', {'ticker': 'KXHIGHNY-26OCT31-B60.5'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets-orderbook", {
  "ticker": "KXHIGHNY-26OCT31-B60.5"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets-orderbook", sandbase.Params{
	"ticker": "KXHIGHNY-26OCT31-B60.5",
})
```

Same call via the path form: `POST /v1/api/kalshi/markets-orderbook` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | integer |  | Depth of the orderbook to retrieve (0 or negative means all levels, 1-100 for specific depth) default `0`; range 0–100 |
| `ticker` | string | yes | Market ticker  |

## Details

Get Kalshi Market OrderBook from Kalshi. Returns the official Kalshi API response unchanged.

The response is the official Kalshi API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets-orderbook" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "KXHIGHNY-26OCT31-B60.5"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Market ticker |
| `depth` | integer | No | Depth of the orderbook to retrieve (0 or negative means all levels, 1-100 for specific depth) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets-orderbook.json`](../../../catalog/models/kalshi/markets-orderbook.json) · Store page: https://www.sandbase.ai/model/kalshi/markets-orderbook
