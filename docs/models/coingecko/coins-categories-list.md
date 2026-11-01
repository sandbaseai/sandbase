# CoinGecko Coins Categories List (ID Map)

`coingecko/coins-categories-list` · api · CoinGecko

Coins Categories List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-categories-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-categories-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-categories-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-categories-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/coins-categories-list` with the body above minus `model`.

## Details

Coins Categories List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged.

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-categories-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-categories-list.json`](../../../catalog/models/coingecko/coins-categories-list.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-categories-list
