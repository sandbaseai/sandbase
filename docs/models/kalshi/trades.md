# Kalshi Get Kalshi Trades

`kalshi/trades` · api · Kalshi

Get Kalshi Trades from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/trades"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/trades', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/trades", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/trades", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kalshi/trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results per page. Defaults to 100. Maximum value is 1000. default `100`; range 0–1000 |
| `cursor` | string |  | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.  |
| `max_ts` | integer |  | Filter items before this Unix timestamp  |
| `min_ts` | integer |  | Filter items after this Unix timestamp  |
| `ticker` | string |  | Filter by market ticker  |
| `is_block_trade` | boolean |  | Filter trades by whether they are block trades. Omit to return all trades. Set to `true` to return only block trades. Set to `false` to return only non-block trades.  |

## Details

Get Kalshi Trades from Kalshi. Returns the official Kalshi API response unchanged.

The response is the official Kalshi API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/trades" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. |
| `is_block_trade` | boolean | No | Filter trades by whether they are block trades. Omit to return all trades. Set to `true` to return only block trades. Set to `false` to return only non-block tr |
| `limit` | integer | No | Number of results per page. Defaults to 100. Maximum value is 1000. |
| `max_ts` | integer | No | Filter items before this Unix timestamp |
| `min_ts` | integer | No | Filter items after this Unix timestamp |
| `ticker` | string | No | Filter by market ticker |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/trades.json`](../../../catalog/models/kalshi/trades.json) · Store page: https://www.sandbase.ai/model/kalshi/trades
