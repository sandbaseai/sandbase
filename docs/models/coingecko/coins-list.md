# CoinGecko Coins List (ID Map)

`coingecko/coins-list` · api · CoinGecko

Get all the supported coins on CoinGecko with coins ID, name and symbol

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/coins-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status` | string |  | Filter by status of coins. Default: active one of: `active`, `inactive` |
| `include_platform` | boolean |  | Include platform and token's contract addresses. Default: false  |

## Details

Get all the supported coins on CoinGecko with coins ID, name and symbol

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `include_platform` | boolean | No | Include platform and token's contract addresses. Default: false |
| `status` | string | No | Filter by status of coins. Default: active |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-list.json`](../../../catalog/models/coingecko/coins-list.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-list
