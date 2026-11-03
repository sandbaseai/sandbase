# Polymarket Get supported assets API: pricing, parameters and code examples

`polymarket/supported-assets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get supported assets for deposits and withdrawals on the bridge.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/supported-assets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/supported-assets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/supported-assets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/supported-assets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/supported-assets` with the body above minus `model`.

## Details

Returns the list of chains and tokens that Polymarket supports for deposits and withdrawals on its bridge. It takes no input. Each row gives a chain, a token contract, and a minimum checkout amount in USD.

### Use cases

- Build a deposit screen that lists every chain and token a user can fund a Polymarket account with.
- Check whether a given token contract on a given chain is accepted before you send funds.
- Read the token `decimals` to convert raw on-chain amounts into display amounts.
- Show users the minimum deposit size for each asset before they start a checkout.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/supported-assets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "note": "These are the currently supported chains and assets for deposits and withdrawals…",
  "supportedAssets": [
    {
      "chainId": "1",
      "chainName": "Ethereum",
      "minCheckoutUsd": 3,
      "token": {
        "address": "0x0000000000085d4780B73119b644AE5ecd22b376",
        "decimals": 18,
        "name": "TrueUSD",
        "symbol": "TUSD"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `note` | Short text from the API that says the list shows the currently supported chains and assets for deposits and withdrawals. |
| `supportedAssets[]` | One entry per chain and token pair that the bridge supports. |
| `supportedAssets[].chainId` | ID of the chain, sent as a string. For example `1` for Ethereum. |
| `supportedAssets[].chainName` | Name of the chain, such as `Ethereum`. |
| `supportedAssets[].minCheckoutUsd` | Minimum checkout amount for this asset. The key name shows it is in USD. |
| `supportedAssets[].token.address` | Contract address of the token on that chain. |
| `supportedAssets[].token.symbol / supportedAssets[].token.name` | Ticker and full name of the token, such as `BAT` and `Basic Attention Token`. |
| `supportedAssets[].token.decimals` | Number of decimal places the token uses on-chain. |

### Notes

- Send an empty JSON object `{}` as the request body. There are no parameters and no pagination.
- The same `chainId` appears in many rows, one for each token on that chain. Group rows by `chainId` or `chainName` to list tokens per chain.
- Match tokens by `token.address` and `chainId` instead of `symbol`, since the response lists many tokens and symbols may not be unique.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/supported-assets.json`](../../../catalog/models/polymarket/supported-assets.json) · Store page: https://www.sandbase.ai/model/polymarket/supported-assets
