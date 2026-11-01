# CoinGecko Exchanges List with Data

`coingecko/exchanges` · api · CoinGecko

Get all the supported exchanges with exchanges' data (ID, name, country, ...) that have active trading volumes on CoinGecko

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | number |  | Page through results. Default: 1  |
| `per_page` | number |  | Total results per page. Default: 100. Valid values: 1...250  |

## Details

Get all the supported exchanges with exchanges' data (ID, name, country, ...) that have active trading volumes on CoinGecko

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | number | No | Page through results. Default: 1 |
| `per_page` | number | No | Total results per page. Default: 100. Valid values: 1...250 |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/exchanges.json`](../../../catalog/models/coingecko/exchanges.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges
