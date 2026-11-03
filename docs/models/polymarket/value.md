# Polymarket Portfolio Value API: pricing, parameters and code examples

`polymarket/value` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Current USD value of a wallet's open positions, optionally limited to given markets.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/value", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/value', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/value", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/value", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/value` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | The wallet whose portfolio value to return. Required.  |
| `condition` | string |  | Comma-separated `condition_id`s (at most 20 distinct values); omit for the full portfolio.  |

## Details

Returns the current USD value of a wallet's open positions on Polymarket. It needs a wallet address in `user`, and it can limit the total to specific markets with `condition`.

### Use cases

- Track the total size of a trader's open Polymarket portfolio over time.
- Rank a list of wallets by the current value of their open positions.
- Check how much of a wallet's value sits in one market by passing that market's `condition_id`.
- Show a portfolio balance next to a wallet's positions in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/value" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | The wallet whose portfolio value to return. Required. |
| `condition` | string | No | Comma-separated `condition_id`s (at most 20 distinct values); omit for the full portfolio. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "proxy_wallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
    "value": 185559.3014
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.proxy_wallet` | The wallet address the value belongs to. It matches the `user` you sent in this example. |
| `data.value` | Current USD value of the wallet's open positions. It covers the full portfolio, or only the markets listed in `condition`. |

### Notes

- `user` is a wallet address in `0x` hex format.
- `condition` takes up to 20 distinct `condition_id` values separated by commas. Leave it out to value the full portfolio.
- To see which positions make up the value, call [Polymarket Wallet Positions](/apis/polymarket/positions).
- To find `condition_id` values for markets, call [Polymarket List markets](/apis/polymarket/markets).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/value.json`](../../../catalog/models/polymarket/value.json) · Store page: https://www.sandbase.ai/model/polymarket/value
