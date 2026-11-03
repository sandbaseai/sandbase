# CoinGecko Exchanges List (ID Map) API: pricing, parameters and code examples

`coingecko/exchanges-list` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Exchanges List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status` | string |  | Filter by status of exchanges. Default: `active` one of: `active`, `inactive` |

## Details

Returns a list of CoinGecko exchanges, each with an `id` and a `name`. It takes one optional input, `status`, which filters the list to `active` or `inactive` exchanges. The default is `active`.

### Use cases

- Build a lookup table that maps exchange names to CoinGecko exchange IDs.
- Fill an exchange picker in a dashboard with names, and store the `id` for later calls.
- Check whether a given exchange `id` exists before you request its data.
- Compare the `active` and `inactive` lists to find exchanges that CoinGecko no longer tracks as active.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | Filter by status of exchanges. Default: `active` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "id": "10kswap-starknet-alpha",
    "name": "10KSwap"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].id` | CoinGecko exchange ID, for example `9inch`. Use this value as the exchange identifier in other CoinGecko APIs. |
| `[].name` | Display name of the exchange, for example `9mm V3 (Pulsechain)`. |

### Notes

- The response is a flat array of objects. This request has no pagination parameters.
- Pass `status` as `active` or `inactive`. If you leave it out, the API returns `active` exchanges.
- Pass an `id` to [CoinGecko Exchange Data by ID](/apis/coingecko/exchanges-by-id) for details on one exchange.
- Call [CoinGecko Exchanges List with Data](/apis/coingecko/exchanges) when you need more than the ID and name.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/exchanges-list.json`](../../../catalog/models/coingecko/exchanges-list.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-list
