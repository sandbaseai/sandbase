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

Exchanges List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged.

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | Filter by status of exchanges. Default: `active` |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/exchanges-list.json`](../../../catalog/models/coingecko/exchanges-list.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-list
