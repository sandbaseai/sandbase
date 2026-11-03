# Polymarket Get fee rate API: pricing, parameters and code examples

`polymarket/fee-rate` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Retrieves the base fee rate for a specific token ID. The fee rate can be provided either as a query parameter or as a path parameter.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/fee-rate"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/fee-rate', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/fee-rate", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/fee-rate", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/fee-rate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `token_id` | string |  | Token ID (asset ID)  |

## Details

Returns the base fee rate for one Polymarket outcome token. You pass the token ID (asset ID) as `token_id`.

### Use cases

- Check the fee rate for a token before you build an order for it.
- Compare the fee rate across several outcome tokens in a trading bot.
- Include the fee in a cost or profit estimate for a Polymarket trade.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/fee-rate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"token_id": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `token_id` | string | No | Token ID (asset ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_fee": 1000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_fee` | The base fee rate for the token ID you sent. This is the only field in the response. |
| `base_fee` | A whole number. The sample request returned `1000`. |
| `base_fee` | The response shows no unit label, so check the Polymarket documentation before you convert it to a percentage. |

### Notes

- `token_id` is a long numeric string in the sample request. Send it as a string.
- [Polymarket Get fee rate by path parameter](/apis/polymarket/fee-rate-by-token-id) returns the fee rate with the token ID in the path instead of the request body.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/fee-rate.json`](../../../catalog/models/polymarket/fee-rate.json) · Store page: https://www.sandbase.ai/model/polymarket/fee-rate
