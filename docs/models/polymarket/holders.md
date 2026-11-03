# Polymarket Market Holders API: pricing, parameters and code examples

`polymarket/holders` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Top holders of each outcome token in a market by condition ID, with balances and optional PnL.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/holders", "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/holders', {'condition': '0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/holders", {
  "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/holders", sandbase.Params{
	"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
})
```

Same call via the path form: `POST /v1/api/polymarket/holders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Rows per outcome token; defaults to 100, maximum 1000 (100 with `include_pnl=true`). range 0–1000 |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`; carries the per-token `(limit, offset)` window and overrides `limit`. Paging past the first page is cursor-only.  |
| `condition` | string | yes | Comma-separated `condition_id`s (at most 20 distinct values; exactly one with `include_pnl=true`). Required. `condition` is the unified key across v2 (same as the feeds and `/v2/oi`); `condition_id` / `conditionId` are…  |
| `include_pnl` | boolean |  | Opt into per-holder position economics (default `false`; `includePnl` is an accepted alias). Adds `avg_price`, `entry_cost_usdc`, `current_price`, `current_value`, `realized_pnl`, `unrealized_pnl` and `total_pnl` to…  |
| `min_balance` | number |  | Minimum net balance in shares (default 0), applied post-netting. With `include_pnl=true` it applies to the served per-side gross amount instead.  |

## Details

Returns the top holders of each outcome token in a Polymarket market. You pass one or more `condition` IDs (the market's condition ID), and each outcome token comes back with a list of holder wallets and their share balances.

### Use cases

- List the largest holders on the Yes and No sides of a market to see how concentrated each side is.
- Find the wallet addresses of big holders and then look up their other positions.
- Track which named traders hold a large share balance in a market you follow.
- Add `include_pnl=true` for one market to see entry cost and profit or loss for each top holder.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/holders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition` | string | Yes | Comma-separated `condition_id`s (at most 20 distinct values; exactly one with `include_pnl=true`). Required. `condition` is the unified key across v2 (same as the feeds and `/v2/oi`); `condition_id` / `conditionId` are a |
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`; carries the per-token `(limit, offset)` window and overrides `limit`. Paging past the first page is cursor-only. |
| `include_pnl` | boolean | No | Opt into per-holder position economics (default `false`; `includePnl` is an accepted alias). Adds `avg_price`, `entry_cost_usdc`, `current_price`, `current_value`, `realized_pnl`, `unrealized_pnl` and `total_pnl` to ever |
| `limit` | integer | No | Rows per outcome token; defaults to 100, maximum 1000 (100 with `include_pnl=true`). |
| `min_balance` | number | No | Minimum net balance in shares (default 0), applied post-netting. With `include_pnl=true` it applies to the served per-side gross amount instead. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "holders": [
        {
          "amount": 2895931.125,
          "bio": "",
          "display_username_public": true,
          "name": "colombiaman",
          "outcome_index": 0,
          "profile_image": "",
          "profile_image_optimized": "",
          "proxy_wallet": "0xbf546c698f650b7b1d85bc25842732a3710387c4"
        }
      ],
      "token_id": "10370414…"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJob2xkZXJzIiwicGFyYW1zIjp7ImwiOjIsIm8iOjJ9fSwic2lnIjoiMzRk…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].token_id` | ID of the outcome token. Each item in `data` is one outcome token of the market. |
| `data[].holders[]` | List of holders for that token, ordered as returned. The list length follows `limit`. |
| `data[].holders[].proxy_wallet` | Wallet address of the holder. Use it to look up that wallet in other wallet APIs. |
| `data[].holders[].amount` | Share balance the holder has in this outcome token. |
| `data[].holders[].outcome_index` | Index of the outcome this token represents, such as `0` or `1`. It matches the token in the same `data` item. |
| `data[].holders[].name` | Public username of the holder. It is an empty string when the holder has no public name. |
| `data[].holders[].display_username_public` | Whether the holder chose to show their username publicly. |
| `data[].holders[].bio / profile_image / profile_image_optimized` | Profile text and image URLs of the holder. They are empty strings when the holder has not set them. |
| `pagination.has_more / pagination.next_cursor` | `has_more` is `true` when more holders exist. `next_cursor` is the value to send back as `cursor` for the next page. |

### Notes

- Get the `condition` value from a market record. [Polymarket Get market by slug](/apis/polymarket/markets-slug) is one way to find it.
- `limit` applies per outcome token, so a request with `limit` set to `2` returns up to 2 holders for each token.
- To read the next page, pass `pagination.next_cursor` as `cursor`. The cursor holds the window and overrides `limit`.
- Use `include_pnl=true` with exactly one `condition`. Without it you can send up to 20 comma-separated values.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/holders.json`](../../../catalog/models/polymarket/holders.json) · Store page: https://www.sandbase.ai/model/polymarket/holders
